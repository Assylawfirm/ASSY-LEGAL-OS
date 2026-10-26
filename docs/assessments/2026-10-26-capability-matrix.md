# Capability Compatibility Matrix — 2026-10-26
Status: DOCUMENTED CANDIDATE DESIGN; no code integration or test executed.

## Verified baseline
Private repository Assylawfirm/ASSY_Sovereign_Archive_Organizer:
- assy_archive/__init__.py declares backup_manager, classifier, database, document_reader, document_dna, duplicate_detector, file_scanner, keyword_indexer, knowledge_engine, knowledge_statistics, legal_document_analyzer, legal_query_engine, operation_logger, reports, restore_manager, search_engine, settings, integrity_checker.
- requirements-test.txt pins pytest==8.4.1 and documents CPython 3.12.
- .gitignore excludes .env*, *.pem, *.key, *.db, *.sqlite*, *.log, local /data/, agent state directories. Ignore rules are not proof of no leaked secrets.
- Implementations of the declared modules have NOT been inspected; names are not proof of API availability.

| Existing declared capability | VoiceStudio candidate | Superpowers candidate | Integration decision |
| --- | --- | --- | --- |
| file_scanner / document_reader | import consented audio/transcripts | test plan | Adapter reads copies only; no archive source mutations |
| document_dna / integrity_checker | hash originals and derived outputs | verification gates | Confirm implementation and algorithm before reuse |
| keyword_indexer / search_engine | index human-verified transcript | test-driven indexing | Do not index confidential data into public services |
| legal_query_engine / knowledge_engine | retrieve approved transcript excerpts | review workflow | No automatic legal authority or final advice |
| operation_logger / reports | provenance, consent, processing logs | review artifacts | Restrict logs from storing raw audio or secrets |
| backup_manager / restore_manager | recover original and derived media | recovery tests | Require retention/deletion policies |
| classifier / database | typed media records and status | schema review | No schema changes until current contracts mapped |

## Suggested minimum contract (not implemented)
Input: opaque case_id, asset_id, consent_record_id, requested_operation, engine_id, model_revision, policy_version.
Output: immutable artifact_id, original_sha256, derived_sha256, engine/model provenance, review_status=UNVERIFIED, timestamps, errors without PII.
Policy: deny by default; no network; no auto-publish; human verification before legal use.

## Acceptance tests to design
- reject missing/withdrawn consent; reject model without commercial clearance
- no outbound network by default; enforce storage isolation
- preserve original hash, store derivation lineage and prevent silent overwrite
- verify Arabic legal names, numbers and negation by human reviewer
- fail closed on timeout or engine failure; scrub logs
- run existing Python 3.12 pytest suite before and after changes

## Remaining evidence gaps
Full module source, actual interfaces, CI status, dependency inventory, voice service inventory, runtime benchmarks and security scanning. No assertion of test pass.
