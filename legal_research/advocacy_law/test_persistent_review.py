import hashlib
import tempfile
import unittest
from pathlib import Path
from persistent_review import ReviewStore, ApprovalError

SOURCE=b"synthetic test data, never a real legal document"
ROLES={"u":"uploader","r":"legal_reviewer","a":"supervising_lawyer"}
def fixture():
    return {"record_id":"T-1","record_type":"legislation","primary_source_type":"official_gazette",
      "primary_source_url":"https://example.gov.eg/fixture","official_reference":"TEST DATA ONLY",
      "source_sha256":hashlib.sha256(SOURCE).hexdigest(),"source_page":1,"exact_text":"TEST",
      "effective_date":"2026-10-19","reviewed_at":"2026-10-19",
      "amendments_checked":True,"conflicts_open":False,"human_approval":True,
      "citation_approved":False}
class DurableReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.name=str(Path(self.temp.name)/"review.sqlite")
        self.store=ReviewStore(self.name)
    def tearDown(self):
        self.store.close();self.temp.cleanup()
    def test_full_sequence_persists(self):
        self.store.submit("x",fixture(),SOURCE,"u",ROLES)
        self.store.review("x","r",ROLES,True)
        result=self.store.approve("x","a",ROLES,SOURCE)
        self.assertTrue(result["citation_approved"])
        self.store.close();self.store=ReviewStore(self.name)
        self.assertTrue(self.store.verify_chain())
        self.assertEqual(self.store.db.execute("SELECT state FROM cases").fetchone()[0],"APPROVED")
    def test_reject_bad_role(self):
        with self.assertRaises(PermissionError):
            self.store.submit("x",fixture(),SOURCE,"a",ROLES)
    def test_reject_bad_bytes(self):
        with self.assertRaises(ApprovalError):
            self.store.submit("x",fixture(),b"wrong","u",ROLES)
    def test_no_direct_approval(self):
        self.store.submit("x",fixture(),SOURCE,"u",ROLES)
        with self.assertRaises(ApprovalError):
            self.store.approve("x","a",ROLES,SOURCE)
    def test_hash_tampering_detected(self):
        self.store.submit("x",fixture(),SOURCE,"u",ROLES)
        self.store.db.execute("UPDATE events SET detail='forged'");self.store.db.commit()
        self.assertFalse(self.store.verify_chain())
        with self.assertRaises(ApprovalError):
            self.store.review("x","r",ROLES,True)
    def test_open_conflict_blocks_final(self):
        obj=fixture();obj["conflicts_open"]=True
        self.store.submit("x",obj,SOURCE,"u",ROLES)
        self.store.review("x","r",ROLES,True)
        with self.assertRaises(ApprovalError):
            self.store.approve("x","a",ROLES,SOURCE)
    def test_decline(self):
        self.store.submit("x",fixture(),SOURCE,"u",ROLES)
        self.store.review("x","r",ROLES,False)
        self.assertEqual(self.store.db.execute("SELECT state FROM cases").fetchone()[0],"REJECTED")
if __name__=="__main__": unittest.main()
