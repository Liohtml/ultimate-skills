# security

## Overview
An authorized security auditing and pentesting toolkit for AI coding agents. Seven permissively-licensed (MIT / Apache-2.0) skills that cover the defensive security loop: model the threats, find the bugs, triage them honestly, and test the running system — all on assets you own or are explicitly authorized to assess.

Every offensive-testing skill opens with an authorization / scope / rules-of-engagement step and refuses to widen scope, weaponize findings, or touch systems the user does not control. None of these skills is for malware, evasion, credential theft, or untargeted attacks.

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install security@ultimate-skills
```

## Relationship to `engineering/security-and-hardening`
`security-and-hardening` (in the `engineering` plugin) is the **builder** side: secure-coding controls and hardening checklists for code you are writing. This plugin is the **auditor / tester** side: assessing and testing code and systems that already exist. The skills cross-point to each other.

## Skills
7 skills (see also the table in the [root README](../README.md#security)):

| Skill | What it does | License |
|---|---|---|
| `threat-model` | Code-grounded threat model in three modes (interview / bootstrap / bootstrap-then-interview). Static, read-only; writes `THREAT_MODEL.md`. | Apache-2.0 |
| `static-vuln-scan` | Read-only static vulnerability scan, scoped from the threat model, fanning subagents per focus area; writes `VULN-FINDINGS.json`. | Apache-2.0 |
| `vuln-triage` | Adversarial triage of any scanner's output (its own JSON, SARIF, markdown): N-vote verification, dedupe, exploitability re-ranking, owner routing. | Apache-2.0 |
| `gha-security-review` | Exploit-focused review of GitHub Actions workflows (pwn requests, expression injection, credential theft, supply chain) with a mandatory traced attack path. | Apache-2.0 |
| `skill-scanner` | Scans an agent skill or plugin before you install it: prompt injection, dangerous scripts, config poisoning, excessive permissions, supply-chain URLs. | Apache-2.0 |
| `llm-app-security-audit` | Defensive audit of an app's AI/LLM features for prompt injection, insecure output handling, tool/agent abuse and AI permission boundaries; maps to the OWASP LLM Top 10. | MIT |
| `web-pentest` | Scope-gated black-box / grey-box web application pentest following OWASP WSTG. A written `SCOPE.md` / rules-of-engagement is reconfirmed before every active request. | MIT |

## Typical flow
`threat-model` → `static-vuln-scan` → `vuln-triage` for a source-code assessment; `gha-security-review` for CI; `skill-scanner` before importing third-party skills; `llm-app-security-audit` for AI features; `web-pentest` for authorized testing of a running app.

## License
MIT and Apache-2.0 per skill. Each skill directory carries its upstream `LICENSE.txt`, a `> Includes material adapted from …` attribution line, and (for Apache-2.0 skills) an Apache §4(b) change note at the end of `SKILL.md`. Copies of the upstream licenses are in [`LICENSES/`](./LICENSES/); full provenance is in [`../PROVENANCE.csv`](../PROVENANCE.csv) and [`../NOTICE.md`](../NOTICE.md). Share-alike (CC-BY-SA-4.0) security-testing skills are kept out of this plugin — see the separate [`security-cc-by-sa`](../security-cc-by-sa/README.md) plugin.
