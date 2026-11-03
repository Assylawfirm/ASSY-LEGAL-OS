# Harvey — outbound-path security review (automated inventory triage)

Date: 2026-11-03
Status: **HUMAN SECURITY REVIEW REQUIRED / NO PRODUCTION AUTHORIZATION**
Scope: isolated GitHub Actions pilot on `proposal/harvey-outreach-dry-run-20261103`.
Evidence: workflow run 41588572137 (successful AST inventory); run 41588572118 (successful pip-audit); run 41588572077 (Windows install smoke); run 41588572126 (configuration safety checks).

## Inventory observations

The AST inventory produced **454 potential outbound-related references** (imports and calls). This is a *keyword-based triage count*, not 454 verified network operations or vulnerabilities. Selected high-priority files (reference counts):

| File | References | Review priority |
| --- | ---: | --- |
| `harvey/integrations/email_finder.py` | 49 | High: lead enrichment and external lookups |
| `harvey/dashboard.py` | 47 | High: dashboard exposure and actions |
| `harvey/agents/sender.py` | 37 | Critical: message delivery |
| `harvey/integrations/gmail.py` | 37 | Critical: OAuth/mail provider |
| `harvey/integrations/microsoft.py` | 27 | Critical: Microsoft mail integration |
| `harvey/agents/scout.py` | 25 | High: discovery, LinkedIn automation |
| `harvey/config.py` | 23 | Critical: configuration precedence and defaults |
| `harvey/integrations/smtp_mail.py` | 17 | Critical: SMTP transport |
| `harvey/agents/handler.py` | 12 | Critical: reply/approval handling |
| `harvey/integrations/linkedin.py` | 6 | High: platform automation |

Other paths, including `harvey/main.py`, `harvey/cli.py`, `harvey/public_http.py`, and `harvey/integrations/instantly.py`, require review.

## Verified versus unverified

- **Verified in CI**: isolated Windows installation/import; dependency audit of installed environment (no findings in successful run); offline pilot configuration checks; AST inventory creation.
- **NOT verified**: absence of unauthorized network activity during agent runtime, end-to-end enforcement of zero-send across Gmail/SMTP/Microsoft/Instantly, dashboard authentication, data retention, handling of third-party prospect data, actual mail-provider mocking, source-code vulnerability review, and supply-chain integrity.
- The upstream clone currently tracks a moving branch. Before approval, pin a reviewed commit SHA and record checksums/SBOM.
- No real credentials, leads, customer records, outbound mail, LinkedIn sessions, DNS, production deployment, or PR merge are authorized.

## Required next gates

1. Review sender, handler, provider adapters and config precedence for every send entry point.
2. Add network-denied end-to-end tests using synthetic prospects and fake providers; fail on any attempted outbound connection.
3. Pin upstream SHA and review license, provenance and dependency inventory.
4. Review dashboard access control and data lifecycle.
5. Obtain explicit human legal/security approval before any real-world operation.

**Decision: HOLD.** This document does not approve outreach or production use.
