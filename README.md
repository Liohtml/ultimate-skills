# Ultimate Skills

**One opinionated, deduplicated marketplace of the best Claude Code skills** — distilled from five community skill repos (**109 skills → 39 keepers**) and regrouped into four discipline plugins: **engineering · product · design · research**.

This is a *curation*, not original work. Every skill keeps its original author and license — see [`NOTICE.md`](./NOTICE.md) and [`PROVENANCE.csv`](./PROVENANCE.csv). It was assembled by a small team of specialist reviewers (engineer, product/marketing, UX, repo expert) with a devil's-advocate pass to cut redundancy.

## What's inside

| Plugin | Skills | License | Focus |
|---|---:|---|---|
| [`engineering`](./engineering) | 16 | MIT | Spec → plan → build → test → debug → review → harden → ship |
| [`product`](./product) | 13 | MIT | Discovery, strategy, prioritization, PRDs, pricing, metrics |
| [`design`](./design) | 6 | MIT | Anti-slop frontend taste, image-to-code, redesign, UI engineering |
| [`research`](./research) | 4 | **CC-BY-NC-4.0** | Deep research, academic writing, peer review |

> ⚠️ **Mixed licensing.** `engineering`, `product`, and `design` are MIT (commercial use OK). `research` is **CC-BY-NC-4.0 — non-commercial only**, isolated in its own plugin so it can be dropped cleanly. See [`NOTICE.md`](./NOTICE.md).

## Install

```bash
# Add this marketplace (from GitHub)
/plugin marketplace add Liohtml/ultimate-skills

# …or from a local clone
/plugin marketplace add /path/to/ultimate-skills

# Then install the plugins you want
/plugin install engineering@ultimate-skills
/plugin install product@ultimate-skills
/plugin install design@ultimate-skills
/plugin install research@ultimate-skills   # CC-BY-NC — non-commercial
```

Each skill activates automatically when its trigger matches your task; you can also name it explicitly (e.g. "use the strategy-red-team skill on this PRD").

## Skill catalog

### engineering (MIT)
| Skill | What it does |
|---|---|
| `spec-driven-development` | Write a spec before coding when requirements are unclear or work is significant. |
| `planning-and-task-breakdown` | Break a spec into ordered, independently verifiable tasks. |
| `incremental-implementation` | Ship multi-file changes as small, safe vertical slices. |
| `test-driven-development` | Drive logic and bug-fixes with tests; prove code works. |
| `debugging-and-error-recovery` | Systematic root-cause debugging when things break. |
| `code-review-and-quality` | Multi-axis review with severity labels before merge. |
| `code-simplification` | Refactor for clarity without changing behavior. |
| `security-and-hardening` | Harden input handling, auth, storage, and integrations (incl. LLM). |
| `performance-optimization` | Measure-first optimization, budgets, Core Web Vitals. |
| `api-and-interface-design` | Stable, contract-first API and module-boundary design. |
| `git-workflow-and-versioning` | Commits, branching, conflicts, bisect-driven debugging. |
| `ci-cd-and-automation` | Quality-gated build/deploy pipelines and rollout/rollback. |
| `doubt-driven-development` | In-flight fresh-context adversarial review of key decisions. |
| `documentation-and-adrs` | ADRs, READMEs, and changelogs that record context. |
| `browser-testing-with-devtools` | Verify behavior in a real browser via Chrome DevTools MCP. |
| `karpathy-guidelines` | Lightweight behavioral rules to avoid common LLM-coding mistakes. |

### product (MIT)
| Skill | What it does |
|---|---|
| `strategy-red-team` | Steelman then attack a PRD/roadmap's load-bearing assumptions. |
| `opportunity-solution-tree` | Torres-style discovery: outcome → opportunities → solutions → experiments. |
| `prioritization-frameworks` | 9 frameworks (RICE, ICE, Kano, MoSCoW…) with formulas and when-to-use. |
| `pre-mortem` | Imagine the launch failed; triage Tigers / Paper Tigers / Elephants. |
| `create-prd` | 8-section Product Requirements Document. |
| `pricing-strategy` | Pricing models, value metric, Van Westendorp, experiments. |
| `ab-test-analysis` | Significance, sample size, SRM, guardrails → ship/extend/stop. |
| `north-star-metric` | Define the NSM + input-metric constellation by business game. |
| `value-proposition` | 6-part JTBD value-proposition design. |
| `competitor-analysis` | Research-driven competitive landscape and differentiation. |
| `interview-script` | Mom-Test / JTBD customer-discovery interview script. |
| `user-personas` | Research-grounded personas with JTBD, pains, gains. |
| `intended-vs-implemented` | Audit the gap between intended behavior and shipped code. |

### design (MIT)
| Skill | What it does |
|---|---|
| `design-taste-frontend` | Brief-aware, anti-slop design direction for greenfield UIs. |
| `redesign-existing-projects` | Audit an existing UI, strip generic AI patterns, upgrade to premium. |
| `image-to-code` | Generate a design image first, analyze it, then implement to match. |
| `imagegen-frontend-web` | Produce premium, conversion-aware website design-reference images. |
| `industrial-brutalist-ui` | A distinct Swiss-terminal / brutalist aesthetic system. |
| `frontend-ui-engineering` | Production UI: components, state, layout, WCAG-AA accessibility. |

### research (CC-BY-NC-4.0 — non-commercial)
| Skill | What it does |
|---|---|
| `deep-research` | Universal multi-agent deep-research pipeline (7 modes). |
| `academic-paper` | 12-agent academic paper-writing pipeline (10 modes). |
| `academic-paper-reviewer` | 5-reviewer peer-review simulation. |
| `academic-pipeline` | Orchestrator: research → write → integrity → review → revise. |

## Attribution & licensing

Curated from: [agent-skills](https://github.com/addyosmani/agent-skills) (Addy Osmani),
[pm-skills](https://github.com/phuryn/pm-skills) (Paweł Huryn),
[taste-skill](https://github.com/Leonxlnx/taste-skill) (Leonxlnx),
[andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (forrestchang / multica-ai),
and [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu).

Full per-skill provenance: [`PROVENANCE.csv`](./PROVENANCE.csv) · Licenses: [`LICENSES/`](./LICENSES/) · Details: [`NOTICE.md`](./NOTICE.md).

The curation, manifests, and docs are MIT. The `research/` plugin is CC-BY-NC-4.0 and may not be used commercially.
