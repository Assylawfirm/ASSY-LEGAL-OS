# Harvey outreach pilot — isolated proposal (2026-11-03)

Status: **Proposal / DRY RUN ONLY**. Not deployed, not integrated, not approved for outbound email.

## Provenance
Upstream: https://github.com/ethanplusai/harvey (main, inspected 2026-11-03)
Read: README.md, CLAUDE.md, pyproject.toml, requirements.txt, harvey.yaml, .env.example, CONTRIBUTING.md, harvey/cli.py.
Upstream version in pyproject: 0.3.0; Python >=3.11, MIT.
This folder contains **instructions, not a vendored copy** of third-party source code.

## Firm profile
- ASSY LAW FIRM — مكتب عاصي للمحاماة
- https://assylawfirm.com
- Contact identity: info@assylawfirm.com
- From name: Hussein Fahmy Assy
- Location: Hurghada, Red Sea, Egypt
- Targeting: SMEs (2-50 employees), developers, hospitality businesses, startups, foreign investors in Red Sea/Cairo/Egypt.
- Services: corporate formation, contracts, intellectual property, real estate legal due diligence, litigation.
- Goal: optional 15-minute introductory call, no hard sell; Arabic/English by verified recipient business language.

## Non-negotiable policy
1. Do not enable email transport. **channels.email.enabled = false**; **channels.email.require_approval = true** in the effective config, including harvey.local.yaml after training. Do not set credentials.
2. All testing uses **synthetic people / domains**; no prospect email, real outbound mail, real client records, or public contact exports.
3. No changes to DNS, Workspace, firm website, production ASSY LEGAL OS, existing repositories beyond this proposal branch, or secrets.
4. After train, diff effective config: harvey.local.yaml takes priority; verify approval and disabled email again.
5. For eventual sending require separately approved legal/privacy review, mailbox/deliverability review (SPF/DKIM/DMARC), and individually approved content/recipients. Main domain is a contact identity, **not authorized cold-outreach sending infrastructure**.
6. Never interpret absence of Terms/Privacy as proof of a legal violation. Verify claims against URLs and timestamps.
7. Verify provider subscription access and compatibility locally. Upstream README says Codex requires selected CLI version and macOS/Linux, Claude needs --safe-mode; usage limits still apply.
8. Keep private dashboard on 127.0.0.1 and never publish its token.
9. Never merge, deploy, enable autopilot, or send without a separate explicit decision.
10. Escalate concerns about Egyptian Personal Data Protection Law 151/2020, legal advertising rules, cross-border data transfers and website terms to human legal reviewer.

## Operator procedure (after source/dependency audit)
```bash
git clone https://github.com/ethanplusai/harvey.git
cd harvey
python3 --version    # >=3.11
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -e .
cp .env.example .env  # leave all mail credentials blank
# Configure the actual documented harvey.yaml schema with email.enabled=false,
# email.require_approval=true; business + ICP settings; then verify effective config.
# Run the documented offline tests before discovery or training.
harvey train https://assylawfirm.com
# TRAIN may generate harvey.local.yaml: inspect and re-disable email there.
harvey signals
harvey discover --providers
harvey discover --estimate
harvey dashboard
# Do not run live discovery or 'harvey run' until review of settings and privacy.
```

## Acceptance tests (no external sends)
- Python dependency isolation and CLI import smoke test
- Confirm training-generated local config cannot override disabled sending
- Confirm no message leaves without manual approval, and no messages leave when transport disabled
- No live addresses in tests; mock provider records only
- Arabic and English short drafts, one verified site-specific fact, opt-out and no false legal assertions
- Confirm OSM attribution/use, website robots and acceptable request rates
- Confirm dashboard loopback binding/token control
- Confirm no secrets in Git, dry-run logs only

### Remaining blockers
- No local environment or Claude/Codex login inspected via GitHub.
- No full security audit of the executable source and dependencies yet.
- No installation or dashboard running on the user's device.
- No email provider credentials or sending infrastructure authorized.

Owner approval required before any live prospect processing or email sending.
