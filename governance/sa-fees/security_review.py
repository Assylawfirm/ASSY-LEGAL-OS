"""Read-only, fail-closed, narrow security review for the Saudi fee template.
Does NOT certify broader ASSY LEGAL OS security.
"""
import ast
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parents[1]
FILES = [ROOT / "validate_policy.py", ROOT / "test_policy.py"]
DANGEROUS_IMPORTS = {"subprocess", "socket", "requests", "urllib", "http", "ftplib", "paramiko"}
DANGEROUS_BUILTINS = {"eval", "exec", "compile", "__import__"}
DANGEROUS_NAMES = {"os.system", "os.popen", "subprocess.run", "subprocess.Popen",
                   "subprocess.call", "subprocess.check_output"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:sk-proj-|ghp_|github_pat_)\S{8,}"),
]
def security_scan():
    findings = []
    for path in FILES:
        body = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(body, filename=str(path))
        except SyntaxError as e:
            findings.append(f"Syntax error: {path.name}: {e}")
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for item in node.names:
                    if item.name.split(".")[0] in DANGEROUS_IMPORTS:
                        findings.append(f"Disallowed import {item.name} in {path.name}")
            if isinstance(node, ast.ImportFrom) and node.module:
                if node.module.split(".")[0] in DANGEROUS_IMPORTS:
                    findings.append(f"Disallowed import {node.module} in {path.name}")
            if isinstance(node, ast.Call):
                name = None
                if isinstance(node.func, ast.Name): name = node.func.id
                elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    name = f"{node.func.value.id}.{node.func.attr}"
                if name in DANGEROUS_BUILTINS | DANGEROUS_NAMES:
                    findings.append(f"Forbidden dynamic execution {name} in {path.name}")
        for rx in SECRET_PATTERNS:
            if rx.search(body): findings.append(f"Possible secret in {path.name}")
    wf = (PROJECT / ".github/workflows/sa-fees-review.yml").read_text(encoding="utf-8")
    if "contents: read" not in wf: findings.append("Review workflow token is not read-only")
    if re.search(r"\b(pull_request_target|push):", wf): findings.append("Unsafe workflow trigger")
    if "workflow_dispatch" not in wf: findings.append("Expected manual validation entrypoint absent")
    policy = json.loads((ROOT / "template_policy.json").read_text(encoding="utf-8"))
    if any(policy.get(k) is not False for k in ("production_enabled",
                                              "client_data_ingestion_enabled",
                                              "contract_auto_accept_enabled")):
        findings.append("Production/data/auto-accept gate is not fail-closed")
    # Verify that exported policy contains neither customer-level fields nor example names.
    public = json.dumps(policy, ensure_ascii=False)
    for term in ("client_name", "national_id", "phone_number", "email_address", "case_facts"):
        if term in public: findings.append(f"Client-data field detected: {term}")
    return findings

if __name__ == "__main__":
    findings = security_scan()
    print(json.dumps({"scope":"sa-fees-review-only","findings":findings}, ensure_ascii=False))
    sys.exit(1 if findings else 0)
