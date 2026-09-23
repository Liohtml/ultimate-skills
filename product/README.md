# product

## Overview
Product-management craft for the whole arc: **continuous discovery, positioning, strategy building and red-teaming, prioritization, PRDs, competitor analysis, pricing, SaaS unit economics, A/B analysis, analysis QA, and metrics**. The thin one-shot generators and near-duplicate variants from the source sets were cut; these are the high-depth, repeat-use skills.

Curated from [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (MIT), [wondelai/skills](https://github.com/wondelai/skills) (MIT: `product-positioning`, `strategy-kernel`), [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (MIT: `saas-metrics-coach`), [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0: `validate-data`) and [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) (MIT: evidence and verification rules merged into `competitor-analysis`).

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install product@ultimate-skills
```

## Skills
17 skills (see also the table in the [root README](../README.md#product)):

| Area | Skills |
|---|---|
| Strategy | `strategy-kernel` (build it: diagnosis, guiding policy, coherent actions), `strategy-red-team` (attack its assumptions), `pre-mortem` (launch risk) |
| Positioning and market | `product-positioning`, `value-proposition`, `competitor-analysis`, `pricing-strategy` |
| Discovery | `opportunity-solution-tree`, `interview-script`, `user-personas` |
| Planning and specs | `prioritization-frameworks`, `create-prd`, `intended-vs-implemented` |
| Metrics and analysis | `north-star-metric`, `saas-metrics-coach`, `ab-test-analysis`, `validate-data` |

Skills trigger automatically on matching tasks, or invoke one by name (e.g. "use strategy-red-team on this roadmap"). For writing the results up, see the [writing](../writing/README.md) plugin (`minto-pyramid`, `copy-editing`, `humanizer`).

`saas-metrics-coach` ships three small Python 3 scripts (standard library only, no network, no environment variables).

## License
MIT, except `validate-data`, which is Apache-2.0 (license text in its folder, modifications marked). Copies of every upstream license used by this plugin are in [`LICENSES/`](./LICENSES/); see [`../NOTICE.md`](../NOTICE.md) for attribution and [`../PROVENANCE.csv`](../PROVENANCE.csv) for per-skill sources.
