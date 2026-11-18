import unittest
from security_review import security_scan

class SecurityTests(unittest.TestCase):
    def test_no_disallowed_import_or_dynamic_execution(self):
        self.assertEqual(security_scan(), [])
    def test_is_read_only_scanner(self):
        import ast, pathlib
        p = pathlib.Path(__file__).with_name("security_review.py")
        self.assertNotIn("subprocess", {a.name.split(".")[0] for n in ast.walk(ast.parse(p.read_text())) if isinstance(n, ast.Import) for a in n.names})
    def test_policy_has_no_client_identifiers(self):
        import json, pathlib
        p=json.loads(pathlib.Path(__file__).with_name("template_policy.json").read_text())
        self.assertFalse(any(k in p for k in ("client_name","national_id","phone_number","email_address")))

if __name__ == "__main__": unittest.main()
