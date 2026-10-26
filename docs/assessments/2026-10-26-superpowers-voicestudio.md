# ASSY LEGAL OS — External Capability Assessment
Date: 2026-10-26
Status: RESEARCH ONLY — NOT APPROVED FOR INSTALLATION, INTEGRATION OR PRODUCTION
Owner/approval authority: ASSY LAW FIRM CEO

## Scope
- Superpowers (obra/superpowers): evaluate development workflow and skills, not an automatic dependency.
- VoiceStudio (debpalash/VoiceStudio): evaluate local speech processing via separately governed adapter, not embedded code.

## Evidence
- https://github.com/obra/superpowers
- https://github.com/debpalash/VoiceStudio
- Upstream claims are not substitutes for security, quality, legal or runtime testing.

## Non-negotiable gates
1. Inventory current repository architecture, existing voice services, contracts, CI, deployment and data model. No replacement before gap analysis.
2. Inventory upstream commits, transitive dependencies, install scripts, permissions, outbound requests and telemetry. Pin reviewed versions.
3. Superpowers: review hooks, instructions and tool execution privileges; disable optional telemetry where relevant; use isolated worktrees, tests and human sign-off.
4. VoiceStudio: separate AGPL-3.0 app license from individual model, tokenizer, voice and output licenses; counsel review before distribution or network service.
5. Data protection: lawful basis, explicit voice-cloning authorization, confidentiality, data residency, retention and deletion, access controls, audit trail; never send client audio to unapproved remote services.
6. Evaluate Arabic (Egyptian) and English legal terminology using consented synthetic or test samples; benchmark WER, diarization, latency, memory and GPU requirements.
7. Adapter must be disabled by default, configurable, least-privilege, with no direct access to legal case records and no production credentials.
8. Review legal provenance and preserve original audio, derived transcript, human corrections and hashes as separate records.
9. No merging, production deployment or publication without written CEO approval and recorded test evidence.

## Status ledger
- Public upstream repositories identified: COMPLETE.
- Target repository identified: COMPLETE.
- Target codebase inventory: BLOCKED/PENDING — standard root files not found; investigate tree and actual deployment sources.
- Upstream source audit: PENDING.
- License-by-model matrix: PENDING.
- Integration coding: NOT STARTED.
- Local installation: NOT STARTED.
- Tests: NOT RUN.
- CEO production approval: NOT GRANTED.

## Proposed architecture (unapproved)
ASSY LEGAL OS -> governance/consent policy -> isolated voice adapter -> approved local voice engine -> encrypted artifact storage + audit.
Superpowers is evaluated only as an engineering-process tool; it does not gain legal approval authority.

## Exit criteria
Architecture map + compatibility matrix + threat model + legal license review + reproducible benchmark + test report + CEO sign-off.
