import hashlib
import unittest
from approval_gate import validate_approval, ApprovalError

SOURCE = b"illustrative test bytes, not a real gazette"
def sample():
    return {
        "record_id":"TEST-1", "record_type":"legislation",
        "primary_source_type":"official_gazette",
        "primary_source_url":"https://example.gov.eg/scan.pdf",
        "official_reference":"test issue 1 page 4",
        "source_sha256":hashlib.sha256(SOURCE).hexdigest(),
        "source_page":4,"exact_text":"TEST-ONLY PLACEHOLDER",
        "effective_date":"2019-10-01",
        "reviewer_id":"test-reviewer","reviewer_role":"lawyer",
        "reviewed_at":"2026-10-19","amendments_checked":True,
        "conflicts_open":False,"human_approval":True,
        "citation_approved":False
    }

class ApprovalGateTests(unittest.TestCase):
    def test_complete_illustrative_record(self):
        self.assertTrue(validate_approval(sample(), SOURCE)["citation_approved"])
    def test_missing_source_bytes(self):
        with self.assertRaises(ApprovalError): validate_approval(sample())
    def test_source_changed(self):
        with self.assertRaises(ApprovalError): validate_approval(sample(), b"altered")
    def test_conflict(self):
        rec=sample();rec["conflicts_open"]=True
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_missing_human_approval(self):
        rec=sample();rec["human_approval"]=False
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_missing_reviewer(self):
        rec=sample();rec["reviewer_id"]=""
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_missing_amendment_review(self):
        rec=sample();rec["amendments_checked"]=False
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_preapproved_input(self):
        rec=sample();rec["citation_approved"]=True
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_invalid_date(self):
        rec=sample();rec["effective_date"]="2019-02-30"
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)
    def test_no_unverified_type(self):
        rec=sample();rec["primary_source_type"]="blog"
        with self.assertRaises(ApprovalError):validate_approval(rec,SOURCE)

if __name__=="__main__":unittest.main()
