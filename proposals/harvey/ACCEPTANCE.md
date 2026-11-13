# Acceptance and installation plan — PR #3

## Execution status
- GitHub source/docs review: partial, not a full security audit.
- Local GitHub clone attempt from execution environment: failed (DNS/network unavailable).
- Application installed/running: NO.
- Real mailboxes authenticated: NO.
- Sending enabled: NO.
- Production integration: NO.

## Staged operator workflow
1. On an authorized local macOS/Linux/Windows host, inspect pinned upstream commit, dependencies, and executable code.
2. Clone upstream into an isolated checkout; create Python 3.11+ venv, install reviewed dependencies.
3. Choose Claude Code login, or Codex where upstream supports OS/CLI version; verify provider access without publishing tokens.
4. Copy the pilot YAML into Harvey's effective configuration; set Gmail credentials EMPTY.
5. Run `python verify_sending_disabled.py /path/to/harvey` using this pilot's verification script.
6. If training is approved, run `harvey train https://assylawfirm.com`, then REAPPLY safe values to `harvey.local.yaml` and rerun verification.
7. Use synthetic prospect data for drafts; confirm Arabic and English quality, website claim provenance, no legal advice by unsolicited email.
8. Start dashboard only after code audit, loopback-only, private unlock token. Do not run the heartbeat or live discovery before legal and privacy signoff.
9. Validate send paths with mocked email provider; the static verifier alone is insufficient.

## Go/no-go matrix
| Gate | Pass criteria | Current |
|---|---|---|
| Source integrity | pinned commit, security review, dependency scan | NOT TESTED |
| Config | email disabled; manual approval; zero sends; no local override | TEMPLATE ONLY |
| Credentials | none committed; auth kept on authorized host | NOT CONFIGURED |
| Local install | CLI and tests run on authorized host | BLOCKED |
| Dashboard | loopback bind and auth verified | NOT TESTED |
| Outreach compliance | Egyptian data/privacy/professional advertising review | OPEN |
| Sending | separately authorized; each recipient+final message approved | NOT AUTHORIZED |

## Important
The upstream code's YAML config is not the same as generic dotenv keys. Do not use invented `AUTO_SEND` or `DRY_RUN` variables as a substitute for documented channel settings. Even if approval is on, `channels.email.enabled: false` and no credentials are essential to this pilot.
