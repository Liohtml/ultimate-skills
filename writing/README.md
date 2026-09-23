# writing

## Overview
Prose craft for the text agents produce every day: memos, recommendations, status updates, landing pages, emails, READMEs and PR descriptions. Three skills, meant to be used in this order:

1. **minto-pyramid**: get the *order* right. Conclusion first, grouped reasons, evidence, with SCQA. It asks before rewriting a draft you only shared, declines timelines, runbooks and tutorials, and never adds facts. Operation 6 returns a structure audit with a Share as-is / Minor edits / Restructure verdict.
2. **copy-editing**: for marketing and conversion copy, the Seven Sweeps (clarity, voice, so-what, prove-it, specificity, emotion, zero risk), an optional expert-panel score and a content-refresh checklist. Missing proof points are flagged, not invented.
3. **humanizer**: the final pass. It removes AI-sounding patterns (not-X-but-Y, one-line closers, forced triads, dash overuse, stock AI words, bold labels, chatbot residue) and checks that no fact was added or lost.

Curated from [millwright-labs/minto-pyramid-skill](https://github.com/millwright-labs/minto-pyramid-skill) (MIT), [tyroneross/pyramid-principle](https://github.com/tyroneross/pyramid-principle) (Apache-2.0, audit reference only), [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) and [blader/humanizer](https://github.com/blader/humanizer) (MIT).

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install writing@ultimate-skills
```

## Skills
3 skills (see also the table in the [root README](../README.md#writing)):

| Skill | Use it for |
|---|---|
| `minto-pyramid` | Recommendations, proposals, exec summaries, memos, updates with an ask; buried-lede test, reason audit, so-what pass, email version, structure audit |
| `copy-editing` | Improving existing landing pages, product pages, launch/sales emails, CTAs and ads |
| `humanizer` | Making any prose read like a person wrote it, as a last pass |

Neighbours in other plugins: `create-prd`, `product-positioning` and `value-proposition` (product), `documentation-and-adrs` (engineering), `academic-paper` (research, CC BY-NC).

Skills trigger automatically on matching tasks, or invoke one by name (e.g. "use minto-pyramid on this draft").

## License
MIT, except `minto-pyramid/references/audit-report.md`, which is Apache-2.0 (license text alongside it). Copies of every upstream license used by this plugin are in [`LICENSES/`](./LICENSES/); see [`../NOTICE.md`](../NOTICE.md) for attribution and [`../PROVENANCE.csv`](../PROVENANCE.csv) for per-skill sources.
