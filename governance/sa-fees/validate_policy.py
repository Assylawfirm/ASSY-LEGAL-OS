"""Fail-closed offline policy verification; no client data or network."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
REQUIRED = ("requires_licensed_lawyer", "requires_independent_legal_review",
            "requires_identity_check", "requires_conflict_check",
            "requires_client_authority_check", "requires_matter_scope",
            "requires_fee_approval", "requires_tax_decision",
            "requires_human_signature", "public_sources_only")
FORBIDDEN_TRUE = ("production_enabled", "client_data_ingestion_enabled",
                  "contract_auto_accept_enabled", "outcome_guaranteed",
                  "exceptional_appeals_default_included",
                  "enforcement_default_included")

def validate(p):
    errors = []
    if p.get("jurisdiction") != "SA": errors.append("jurisdiction")
    if p.get("status") != "REVIEW_ONLY": errors.append("status")
    for key in REQUIRED:
        if p.get(key) is not True: errors.append(key)
    for key in FORBIDDEN_TRUE:
        if p.get(key) is not False: errors.append(key)
    if p.get("fees_distribution") != [50, 25, 25]: errors.append("fees_distribution")
    if p.get("ordinary_litigation_scope") != ["first_instance", "ordinary_appeal_when_available"]:
        errors.append("ordinary_litigation_scope")
    if p.get("third_fee_trigger") != "appeal_final_judgment_or_first_instance_finality":
        errors.append("third_fee_trigger")
    if not re.fullmatch(r"[a-f0-9]{64}", p.get("document_sha256", "")):
        errors.append("document_sha256")
    return errors

def check_secret_leak(paths):
    patterns = (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
                r"\b(?:sk-proj-|ghp_|github_pat_)\S{8,}",
                r"\bpassword\s*[:=]\s*[^\s]+")
    bad = []
    for path in paths:
        t = pathlib.Path(path).read_text(encoding="utf-8")
        if any(re.search(pattern, t, re.I) for pattern in patterns):
            bad.append(str(path))
    return bad

if __name__ == "__main__":
    p = json.loads((ROOT / "template_policy.json").read_text(encoding="utf-8"))
    findings = validate(p)
    secret_hits = check_secret_leak([ROOT / "template_policy.json",
        ROOT / "APPROVAL_RECORD_2026-11-18.md"])
    print(json.dumps({"policy_errors": findings, "pattern_secret_hits": secret_hits}))
    raise SystemExit(int(bool(findings or secret_hits)))
