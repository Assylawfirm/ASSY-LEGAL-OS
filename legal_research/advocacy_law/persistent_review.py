"""SQLite persistent review queue with role separation; research prototype only.
Identity is supplied by a trusted calling service, NEVER from client JSON.
"""
import sqlite3
import hashlib
import json
from datetime import datetime,timezone
from approval_gate import validate_approval, ApprovalError

def utc(): return datetime.now(timezone.utc).isoformat()
def canonical(obj): return json.dumps(obj,sort_keys=True,ensure_ascii=False,separators=(",",":"))

class ReviewStore:
    def __init__(self,filename):
        self.db=sqlite3.connect(filename)
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS cases(
          id TEXT PRIMARY KEY, submitted_by TEXT NOT NULL, reviewer TEXT,
          approver TEXT, payload TEXT NOT NULL, state TEXT NOT NULL,
          source_sha256 TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS events(
          seq INTEGER PRIMARY KEY AUTOINCREMENT, case_id TEXT NOT NULL,
          actor TEXT NOT NULL, action TEXT NOT NULL, created_at TEXT NOT NULL,
          prev_hash TEXT NOT NULL, hash TEXT NOT NULL, detail TEXT NOT NULL);
        """)
        self.db.commit()
    def _append(self,case_id,actor,action,detail):
        last=self.db.execute("SELECT hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        prev=last[0] if last else "0"*64
        e={"case_id":case_id,"actor":actor,"action":action,"created_at":utc(),
           "prev_hash":prev,"detail":detail}
        digest=hashlib.sha256(canonical(e).encode()).hexdigest()
        self.db.execute("INSERT INTO events(case_id,actor,action,created_at,prev_hash,hash,detail) VALUES (?,?,?,?,?,?,?)",
                        (case_id,actor,action,e["created_at"],prev,digest,detail))
    def verify_chain(self):
        prev="0"*64
        for case_id,actor,action,created_at,prev_hash,digest,detail in self.db.execute(
                "SELECT case_id,actor,action,created_at,prev_hash,hash,detail FROM events ORDER BY seq"):
            e={"case_id":case_id,"actor":actor,"action":action,"created_at":created_at,
               "prev_hash":prev_hash,"detail":detail}
            if prev_hash!=prev or hashlib.sha256(canonical(e).encode()).hexdigest()!=digest:
                return False
            prev=digest
        return True
    def _role(self,actor,roles,allowed):
        if roles.get(actor) not in allowed:
            raise PermissionError("Insufficient trusted role")
        if not self.verify_chain():
            raise ApprovalError("Audit chain integrity violation")
    def submit(self,case_id,record,source_bytes,actor,roles):
        self._role(actor,roles,{"uploader"})
        if not isinstance(source_bytes,bytes) or not source_bytes:
            raise ApprovalError("Original bytes required")
        digest=hashlib.sha256(source_bytes).hexdigest()
        if record.get("source_sha256")!=digest:
            raise ApprovalError("Source hash mismatch")
        with self.db:
            self.db.execute("INSERT INTO cases VALUES(?,?,?,?,?,?,?)",
                            (case_id,actor,None,None,canonical(record),"SUBMITTED",digest))
            self._append(case_id,actor,"SUBMIT","Source received")
    def review(self,case_id,actor,roles,accept):
        self._role(actor,roles,{"legal_reviewer"})
        row=self.db.execute("SELECT submitted_by,state FROM cases WHERE id=?",(case_id,)).fetchone()
        if not row or row[1]!="SUBMITTED" or row[0]==actor:
            raise ApprovalError("Invalid reviewer/state")
        with self.db:
            self.db.execute("UPDATE cases SET reviewer=?,state=? WHERE id=?",
                            (actor,"REVIEWED" if accept else "REJECTED",case_id))
            self._append(case_id,actor,"REVIEW_ACCEPT" if accept else "REVIEW_REJECT","Review decision")
    def approve(self,case_id,actor,roles,source_bytes):
        self._role(actor,roles,{"supervising_lawyer"})
        row=self.db.execute("SELECT submitted_by,reviewer,payload,state FROM cases WHERE id=?",(case_id,)).fetchone()
        if not row or row[3]!="REVIEWED" or actor in (row[0],row[1]):
            raise ApprovalError("Separation of duties or invalid review state")
        record=json.loads(row[2])
        candidate={**record,"reviewer_id":row[1],"reviewer_role":"legal_reviewer"}
        approved=validate_approval(candidate,source_bytes)
        with self.db:
            self.db.execute("UPDATE cases SET approver=?,state='APPROVED' WHERE id=?",(actor,case_id))
            self._append(case_id,actor,"APPROVE",approved["source_sha256"])
        return approved
    def close(self): self.db.close()
