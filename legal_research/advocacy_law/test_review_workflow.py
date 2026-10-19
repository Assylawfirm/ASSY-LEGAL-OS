import hashlib
import unittest
from review_workflow import review_decision, verify_chain

DATA=b"TEST FIXTURE: not an official legal source"
ROLES={"counsel-1":"supervising_lawyer","observer":"reader"}
def record():
    return {"record_id":"FIXTURE-1","record_type":"legislation","primary_source_type":"official_gazette",
        "primary_source_url":"https://example.gov.eg/test.pdf","official_reference":"TEST ONLY",
        "source_sha256":hashlib.sha256(DATA).hexdigest(),"source_page":1,
        "exact_text":"TEST ONLY","effective_date":"2026-10-19","reviewed_at":"2026-10-19",
        "amendments_checked":True,"conflicts_open":False,"human_approval":True,
        "citation_approved":False}

class ReviewWorkflowTest(unittest.TestCase):
    def test_authorized_prototype(self):
        events=[]
        result=review_decision(record(),DATA,"counsel-1",ROLES,events,"approve")
        self.assertTrue(result["citation_approved"])
        self.assertTrue(verify_chain(events))
        self.assertEqual(events[0]["action"],"APPROVE")
    def test_untrusted_role_denied(self):
        with self.assertRaises(PermissionError):
            review_decision(record(),DATA,"observer",ROLES,[],"approve")
    def test_unknown_actor_denied(self):
        with self.assertRaises(PermissionError):
            review_decision(record(),DATA,"ghost",ROLES,[],"approve")
    def test_bad_evidence_not_approved(self):
        events=[]
        result=review_decision(record(),b"tampered","counsel-1",ROLES,events,"approve")
        self.assertFalse(result["citation_approved"])
        self.assertEqual(events[0]["action"],"DENY")
    def test_open_conflict_blocked(self):
        events=[]; candidate=record();candidate["conflicts_open"]=True
        result=review_decision(candidate,DATA,"counsel-1",ROLES,events,"approve")
        self.assertFalse(result["citation_approved"])
    def test_explicit_reject(self):
        events=[]
        result=review_decision(record(),DATA,"counsel-1",ROLES,events,"reject")
        self.assertEqual(result["approval_state"],"REJECTED")
        self.assertEqual(events[0]["action"],"REJECT")
    def test_hash_chain_detects_edit(self):
        events=[];review_decision(record(),DATA,"counsel-1",ROLES,events,"reject")
        events[0]["action"]="APPROVE"
        self.assertFalse(verify_chain(events))
    def test_corrupted_chain_blocks_further_actions(self):
        events=[];review_decision(record(),DATA,"counsel-1",ROLES,events,"reject")
        events[0]["detail"]="modified"
        with self.assertRaises(ValueError):
            review_decision(record(),DATA,"counsel-1",ROLES,events,"approve")

if __name__=="__main__":unittest.main()
