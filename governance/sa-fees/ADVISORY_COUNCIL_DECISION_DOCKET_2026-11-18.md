# ASSY Advisory Council — Final Decision Docket (not yet resolved)

Document ID: ASSY-AC-SA-FEES-2026-11-18-001
Related PR: https://github.com/Assylawfirm/ASSY-LEGAL-OS/pull/6
Template policy: ASSY-SA-FEE-PROPOSAL-MASTER-2026-001 v1.0
Date: 2026-11-18
Authority: Owner authorized expanded security and repository protection review, NOT production merging or deployment.
Status: SUBMITTED_FOR_REVIEW / NO-GO / NO COUNCIL VOTE RECORDED

## What is approved
- Institutional policy baseline for legal fees offers: ordinary first instance and appeal (where applicable); 50/25/25 schedule; no promised results; lawyer-led review and client authorization gates.
- Preparation of verification package and security evidence on isolated review branch.
- Previous limited policy CI run 44209030674 succeeded.

## Verified technical facts
- Repository `Assylawfirm/ASSY-LEGAL-OS` is **public**.
- `main` branch reported `protected:false`; no active repository rulesets were returned when checked. **Critical governance risk.**
- Draft PR #6 is open and not merged. Do not use mergeable:true as authorization.
- Only de-identified policy metadata and tests are committed; the uploaded Word source itself is not embedded in this repository.
- Workflow uses read-only GITHUB_TOKEN contents permission.
- Expanded security workflow initially failed due to scanner matching its own signature literal: false positive. A corrective commit was added; new CI evidence to be obtained before clearance.
- The review module is not an integrated live application, so integration tests only cover *policy logic*, not end-to-end user workflows, payments, privilege enforcement or persistence.

## Required security evidence
1. Enable main branch protection/ruleset: require PR, ≥2 approvals including human legal owner and security reviewer, dismiss stale approvals, require current checks, resolve discussions, block force-push/deletion, no bypass, no auto-merge.
2. Run and record GitHub Actions: policy and static security checks against exact commit.
3. SAST (Bandit and preferably Semgrep), secret scanning (gitleaks or equivalent), dependency scanning, plus verified scope limitations.
4. Validate role-based access, tenant/case isolation, audit trail, backups/restore and no client-data exposure using the actual application environment (not provided in this branch).
5. Lock review sources to exact publication references and obtain signed independent Saudi-licensed legal opinion.
6. Confirm professional license/authority, VAT wording, early termination and settlement authorization, finality trigger, whether execution is included; validate against official law.
7. Obtain separate council signatures/decision and explicit owner authorization for merge. Production activation must require its own separate authorization and deployment checks.

## Risk matrix
| Risk | Severity | Status |
| --- | --- | --- |
| Unprotected main / no rulesets | CRITICAL | OPEN, not remediated by draft PR |
| Independent Saudi lawyer review missing | HIGH | OPEN |
| No full-system RBAC/client privacy test | HIGH | OPEN |
| No full repository SAST/dependency/secret review | HIGH | OPEN |
| Policy tests pass but not real integration | MEDIUM | LIMITATION |
| Tax / termination and execution scope variation | MEDIUM | HUMAN REVIEW |

## Council decision form (UNSIGNED)
- Saudi independent reviewer (name, license verification, signature, date): PENDING
- Security reviewer (identity, evidence, date): PENDING
- Data protection reviewer: PENDING
- Advisory council resolution: PENDING
- Owner explicit merge approval: NOT GRANTED
- Owner production authorization: NOT GRANTED

Recommended outcome: ACCEPT evidence dossier for examination, **DEFER MERGE (NO-GO)** pending above gates. No meeting, decision or vote is asserted.
