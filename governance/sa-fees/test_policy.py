"""Regression checks for pre-production Saudi legal fee proposal policy."""
import copy
import json
import pathlib
import unittest
from validate_policy import validate, check_secret_leak
ROOT = pathlib.Path(__file__).resolve().parent
BASELINE = json.loads((ROOT / "template_policy.json").read_text(encoding="utf-8"))

class FeesPolicyTests(unittest.TestCase):
    def assert_rejected(self, field, value):
        p = copy.deepcopy(BASELINE)
        p[field] = value
        self.assertTrue(validate(p), field)

    def test_valid_baseline(self): self.assertEqual(validate(BASELINE), [])
    def test_no_production(self): self.assert_rejected("production_enabled", True)
    def test_no_client_data_ingestion(self): self.assert_rejected("client_data_ingestion_enabled", True)
    def test_no_auto_accept(self): self.assert_rejected("contract_auto_accept_enabled", True)
    def test_no_guaranteed_outcomes(self): self.assert_rejected("outcome_guaranteed", True)
    def test_independent_legal_review_gate(self): self.assert_rejected("requires_independent_legal_review", False)
    def test_conflicts_gate(self): self.assert_rejected("requires_conflict_check", False)
    def test_fee_schedule(self): self.assert_rejected("fees_distribution", [50, 50])
    def test_finality_fallback(self): self.assert_rejected("third_fee_trigger", "appeal_only")
    def test_enforcement_excluded(self): self.assert_rejected("enforcement_default_included", True)
    def test_extraordinary_appeals_excluded(self): self.assert_rejected("exceptional_appeals_default_included", True)
    def test_licensed_lawyer_required(self): self.assert_rejected("requires_licensed_lawyer", False)
    def test_tax_decision_required(self): self.assert_rejected("requires_tax_decision", False)
    def test_manual_signoff_required(self): self.assert_rejected("requires_human_signature", False)
    def test_secret_pattern_scan(self):
        self.assertEqual(check_secret_leak([ROOT / "template_policy.json",
                        ROOT / "APPROVAL_RECORD_2026-11-18.md"]), [])

if __name__ == "__main__": unittest.main()
