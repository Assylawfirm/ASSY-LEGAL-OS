# Selective External Capability Adoption Policy
Date: 2026-10-26
Status: PROPOSED FOR CEO REVIEW — not merged or deployed.

## Principle
ASSY LEGAL OS remains the canonical system. Reuse existing verified internal implementations first. Adopt only the minimum lawful, secure, maintainable capability that demonstrably fills a gap. Never copy protected code, model weights, voices, marks, assets, or proprietary workflows without valid rights. Functional equivalence may be independently implemented using lawful methods and original code, without copying protected expression or evading restrictions.

## Decision classes
- REUSE_INTERNAL: verified existing capability, no duplication.
- BUILD_ORIGINAL: general idea or functionality can be independently implemented lawfully; maintain design provenance and clean-room records where warranted.
- REVIEW_OPEN_SOURCE: use only after exact license, version, dependency, distribution, attribution, security and business-use review.
- EXCLUDE_OR_DEFER: paid, unclear, noncommercial-only, restricted, permission-dependent, or otherwise unsuitable; no install, copying, reverse engineering in violation of law or contracts, or production use.

## Candidate disposition
1. Superpowers: learn from generic concepts such as explicit planning, tests, review and verification; prefer original ASSY procedures. No upstream hooks, plugins, skill text, or code copied or installed until license and runtime audit.
2. VoiceStudio: use only as an architectural reference for modular voice pipelines. No VoiceStudio application or OmniVoice default weights integrated. Upstream notice identifies CC-BY-NC default model weights and separate third-party terms; commercial clearance absent. No copying UI, brand, code or weights.
3. Existing archive: reuse only after interface verification. BackupManager.execute and RestoreManager.execute are dry-run only and cannot satisfy disaster-recovery requirements.
4. Voice capability: future original adapter may support separately cleared engines, with consent, offline-first controls, original-file integrity, review-before-legal-use and explicit CEO approval.

## Approval checklist for any third-party component
- Provenance: exact URL, revision, hash, author and source evidence.
- Rights: app, models, weights, datasets, codecs, assets, outputs and trademarks separately reviewed.
- Cost: paid, trial, quotas, renewal, hosting, GPU and vendor dependency disclosed.
- Security: dependency audit, network egress, credentials, logs, data retention, deletion and isolation.
- Compatibility: map against current source APIs, schema, tests and deployment.
- Decision: signed CEO approval before merging, deployment, customer-data use or distribution.

## Non-actions
No production modification, client-data transfer, external package installation, license circumvention, copying of protected third-party implementation, or approval inferred from this document.

## Evidence status
Targeted GitHub source review completed for archive backup_manager.py and restore_manager.py; both execute methods return dry_run. Full architecture inventory, actual backup/recovery tests, and upstream runtime audit remain pending.
