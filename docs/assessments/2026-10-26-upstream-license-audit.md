# Upstream license and package audit — 2026-10-26
Status: VERIFIED DOCUMENT REVIEW, NOT FULL CODE AUDIT

## Superpowers
Source: obra/superpowers package.json read via connected GitHub.
- version: 7.0.1 at review time
- type: module; main: .opencode/plugins/superpowers.js
- pi extension: .pi/extensions/superpowers.ts; skills directory: ./skills
- No installer or hooks executed. Runtime behavior and security NOT audited.

## VoiceStudio
Source: debpalash/VoiceStudio LICENSE-NOTICE.md read via connected GitHub.
- Application: AGPL-3.0-only; commercial and internal use permitted subject to license.
- Modified network-served application triggers corresponding source obligations as explained by upstream; binding license governs.
- Separate commercial licensing offered for proprietary embedding.
- CRITICAL: Default k2-fsa/OmniVoice pretrained model weights are described as CC-BY-NC; code Apache-2.0. Commercial application license DOES NOT clear model weights.
- audio_tokenizer has separate Boson Higgs Audio 2 and Meta Llama terms.
- Upstream explicitly says its model inventory does not establish complete commercial clearance.
- PyAV wheels bundle FFmpeg/x264/x265 with unresolved redistribution considerations.

## Mandatory no-go gates
- Do not use default OmniVoice weights for ASSY commercial outputs without separate validated commercial rights.
- Build exact engine/model/version/weights/tokenizer/codec license and attribution matrix, including output-use permissions.
- Keep third-party binaries out of proprietary distribution until license counsel review.
- No customer audio, voice cloning, network access, installation or production execution without consent/security review and CEO approval.

## Current status
Documentation review complete for two files. No model execution, network trace, dependency vulnerability scan, benchmark, test or code merge completed.
