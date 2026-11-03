# Windows installation runbook — ASSY LAW FIRM

**Status:** Ready for operator execution, NOT installed on user's Windows PC. The GitHub connector cannot execute commands on a Windows machine. No external code has been run.

## 1. Prerequisites
- Windows 10/11, Git for Windows, Python >=3.11 (`py -3 --version`), PowerShell.
- Choose Claude Code on Windows; upstream currently documents Codex provider as macOS/Linux only. Do not set Codex provider on native Windows. WSL2/Linux is a separate supported path, pending review.
- Avoid administrator shell and never paste authentication secrets into chat or GitHub.
- Before executing scripts, inspect source, scripts, dependencies, and review the exact upstream commit.

## 2. Stage source (safe subset)
In PowerShell, download or copy the reviewed `bootstrap-windows.ps1` from this PR to a local folder and inspect it. Execute from a normal user shell:
```powershell
powershell -NoProfile -File .\bootstrap-windows.ps1
```
This clones the upstream and creates a venv, but does not install third-party dependencies or start Harvey. It leaves the .env file unpopulated.

## 3. Dependency review and install (human gate)
Review `pyproject.toml`, `requirements.txt`, `CLAUDE.md`, entrypoints, and Python import side effects. If approved:
```powershell
cd "$HOME\ASSY-Harvey-Pilot"
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m pip check
```
Run the repository's documented offline test suite with fake providers before any live operation. Do not install Playwright browsers or authenticate until required and approved.

## 4. Fail-closed config
Use `harvey.pilot.yaml` as a template for the effective Harvey config, not as a command-line flag. The project uses `harvey.yaml` and possibly `harvey.local.yaml`, with the local config taking priority after training.
Mandatory settings:
```yaml
channels:
  email:
    enabled: false
    provider: gmail
    max_daily_sends: 0
    require_approval: true
  linkedin:
    enabled: false
```
Leave Gmail OAuth/SMTP/IMAP/Instantly secrets blank. Verify configuration before any CLI command that may load it:
```powershell
.\.venv\Scripts\python.exe -m pip show pyyaml
.\.venv\Scripts\python.exe path\to\verify_sending_disabled.py .
```
**Important:** Copy the verifier from this PR, and verify the *effective* config. After `harvey train`, re-check `harvey.local.yaml` and rerun verifier. The static check is not a runtime send-path proof.

## 5. Testing and dashboard
- Execute unit tests using synthetic prospects and fake providers only.
- Validate Windows CLI compatibility and dashboard loopback binding before launching.
- If safe, run `harvey dashboard` from the venv and open the private localhost unlock URL locally. Never paste the dashboard token in chat.
- Do NOT run `harvey run`, live discovery, or mail authentication in this stage.

## 6. Gates before live pilot
- Code/security/dependency audit, Windows runtime tests, mocked send-path tests, Egyptian data protection and legal marketing review, and owner approval.
- The firm's official mailbox is a contact identity, not authorized for cold-email sending.
- PR #3 remains Draft, no merge, no deployment, no sending.
