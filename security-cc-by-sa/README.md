# security-cc-by-sa

## ⚠️ License — share-alike (CC-BY-SA-4.0)
This plugin is licensed **CC-BY-SA-4.0** (Creative Commons Attribution-ShareAlike 4.0 International) and is isolated from the permissive (MIT / Apache-2.0) plugins in this marketplace for that reason. Under share-alike terms you may use, adapt and redistribute this material, including commercially, **but any adapted version you distribute must itself be licensed CC-BY-SA-4.0**, with attribution to the original authors preserved. Do not copy these skills into an MIT or Apache-2.0 plugin — doing so would relicense share-alike material, which the license forbids. Keep them here, or in another CC-BY-SA-4.0 container.

The skills are adapted from [Trail of Bits' skills](https://github.com/trailofbits/skills) (CC-BY-SA-4.0). The full license text is in [`LICENSE`](./LICENSE); each skill directory also carries the upstream `LICENSE.txt` and an attribution + change note. See [`../NOTICE.md`](../NOTICE.md) and [`../PROVENANCE.csv`](../PROVENANCE.csv).

## Overview
2 skills (see also the table in the [root README](../README.md#security-cc-by-sa)). Two deterministic, share-alike security-testing skills that complement the permissive `security` plugin:

| Skill | What it does |
|---|---|
| `supply-chain-risk-auditor` | Measurement-first dependency risk report for npm / PyPI / Go: version-matched advisories for direct deps and the full lockfile tree, abandoned/archived upstreams, npm publisher concentration, install-script execution. Scripts do the measuring; unavailable data is never scored as clean. Read-only, never installs or runs anything. Needs Python 3.11+ and (for full GitHub coverage) an authenticated `gh` CLI. |
| `variant-analysis` | Find the other instances of a bug you already found: extract the root cause, write an exact-match pattern, generalize one element at a time, triage, and write up with a CI regression rule. Ships CodeQL and Semgrep starters for C/C++, Go, Java, JavaScript, Python. |

## Relationship to the `security` plugin
Use these next to the MIT/Apache-2.0 skills in the [`security`](../security/README.md) plugin, not instead of them. Discovery of new bugs → `static-vuln-scan` (`security` plugin). One bug found, hunt its siblings → `variant-analysis` (here). Weed out false positives → `vuln-triage` (`security` plugin). Dependency and package risk → `supply-chain-risk-auditor` (here). Cross-pointers in each skill's description name the neighbour.

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install security-cc-by-sa@ultimate-skills
```
