# Ultimate Skills

**One opinionated, deduplicated marketplace of the best Claude Code skills.** **68 skills in 7 plugins** (**engineering · product · design · writing · security · security-cc-by-sa · research**), taken from **34 community skill repos**. They were chosen from about 90 scouted repos: the first wave kept 39 of 109 skills from five repos, and the second wave added 29 skills and merged material from further sources into existing ones.

This is a *curation*, not original work. Every skill keeps its original author and license: see [`NOTICE.md`](./NOTICE.md) and [`PROVENANCE.csv`](./PROVENANCE.csv), which has one row per upstream source of every skill. Selection criteria: a checkable mechanism rather than generic advice, a verified redistributable license, little overlap with the other skills, and low token and tooling cost. Rejected candidates and the reasons are in [`docs/value-bombs.md`](./docs/value-bombs.md).

## What's inside

| Plugin | Skills | License | Focus |
|---|---:|---|---|
| [`engineering`](./engineering) | 22 | MIT + Apache-2.0 | Spec → plan → build → test → debug → verify → review → PR to green → harden → ship; Postgres, MCP servers |
| [`product`](./product) | 17 | MIT + Apache-2.0 | Discovery, positioning, strategy, prioritization, PRDs, pricing, SaaS metrics, analysis QA |
| [`design`](./design) | 13 | MIT + Apache-2.0 | Anti-slop frontend taste, product UI, image generation, motion, UI review, WCAG audits, icons, slides |
| [`writing`](./writing) | 3 | MIT + Apache-2.0 | Minto-pyramid structure, copy editing, humanizer pass |
| [`security`](./security) | 7 | MIT + Apache-2.0 | Authorized threat modeling, static scan, triage, GHA review, skill scanning, LLM-app audit, scoped web pentest |
| [`security-cc-by-sa`](./security-cc-by-sa) | 2 | **CC-BY-SA-4.0** | Supply-chain dependency risk, variant analysis |
| [`research`](./research) | 4 | **CC-BY-NC-4.0** | Deep research, academic writing, peer review |

> ⚠️ **Mixed licensing.** `engineering`, `product`, `design`, `writing` and `security` are permissive: each skill is MIT or Apache-2.0, and commercial use is allowed. Apache-2.0 skills carry their `LICENSE.txt` and a modification notice. `security-cc-by-sa` is **share-alike**: commercial use is allowed, but adapted versions you distribute must stay CC-BY-SA-4.0. `research` is **non-commercial only** (CC-BY-NC-4.0). Both are isolated in their own plugins so you can drop them cleanly. See [`NOTICE.md`](./NOTICE.md).

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
/plugin install writing@ultimate-skills
/plugin install security@ultimate-skills
/plugin install security-cc-by-sa@ultimate-skills   # CC-BY-SA: share-alike
/plugin install research@ultimate-skills            # CC-BY-NC: non-commercial
```

Each skill activates automatically when its trigger matches your task. You can also name it explicitly (e.g. "use the strategy-red-team skill on this PRD"). Neighbouring skills point to each other in their descriptions ("For X use Y"), so the agent can hand off to the right one.

A few skills bundle helper scripts or need external tools or API keys. The plugin READMEs list them: `iterate-pr` (`gh`), `mcp-builder` (`ANTHROPIC_API_KEY` for evals), `image-generation` (`OPENAI_API_KEY` or `GEMINI_API_KEY`), `frontend-slides` (Node for PDF export), `supply-chain-risk-auditor` (Python 3.11+, `gh`).

## Skill catalog

### engineering
MIT + Apache-2.0 · [plugin README](./engineering/README.md)

| Skill | What it does |
|---|---|
| `spec-driven-development` | Write a spec before coding when requirements are unclear or the work is significant. |
| `planning-and-task-breakdown` | Break a spec into ordered, independently verifiable tasks. |
| `api-and-interface-design` | Stable, contract-first API and module-boundary design, including idempotency. |
| `incremental-implementation` | Ship multi-file changes as thin, verifiable vertical slices. |
| `subagent-driven-development` | Run a plan with one implementer subagent per task and a review after each, tracked in a ledger that survives compaction. |
| `test-driven-development` | Drive logic and bug fixes with tests; prove the code works. |
| `karpathy-guidelines` | Lightweight behavioral rules against common LLM coding mistakes. |
| `doubt-driven-development` | Fresh-context adversarial review of key decisions while the work is in progress. |
| `debugging-and-error-recovery` | Root-cause debugging that starts from a red, deterministic feedback loop and ranked, falsifiable hypotheses. |
| `verification-before-completion` | Evidence gate: run the proving command fresh and read its output before claiming "done", "fixed" or "green". |
| `browser-testing-with-devtools` | Verify behavior in a real browser via Chrome DevTools MCP. |
| `code-review-and-quality` | Multi-axis review with severity labels before merge. |
| `code-simplification` | Refactor for clarity without changing behavior. |
| `iterate-pr` | Drive an open PR to green: fix CI, evaluate and address review feedback, re-check until only human gates remain. |
| `git-workflow-and-versioning` | Commits, branching, conflicts, releases, bisect-driven debugging. |
| `ci-cd-and-automation` | Quality-gated build and deploy pipelines, rollout and rollback. |
| `documentation-and-adrs` | ADRs, READMEs and changelogs that record the context behind decisions. |
| `security-and-hardening` | Builder-side hardening: input handling, auth, secrets, storage, integrations (incl. LLM). |
| `performance-optimization` | Measure-first optimization, budgets, Core Web Vitals, backend and database hot paths. |
| `postgres-best-practices` | Postgres rules with incorrect-vs-correct SQL, plus safe migrations, backup/restore and upgrades. |
| `mcp-builder` | Build MCP servers LLMs can actually use, then measure that with a QA-pair evaluation. |
| `long-horizon-prompting` | Write the launch brief for long autonomous or multi-agent runs: success predicate, non-outcomes, gated persistence. |

### product
MIT + Apache-2.0 · [plugin README](./product/README.md)

| Skill | What it does |
|---|---|
| `strategy-kernel` | Build or audit a strategy with Rumelt's kernel: diagnosis, guiding policy, coherent actions. |
| `strategy-red-team` | Steelman, then attack a PRD's or roadmap's load-bearing assumptions. |
| `pre-mortem` | Imagine the launch failed; triage Tigers / Paper Tigers / Elephants. |
| `product-positioning` | April Dunford's 5-step positioning, with a canvas and a 0–10 score. |
| `value-proposition` | 6-part JTBD value-proposition design. |
| `competitor-analysis` | Competitive landscape with evidence labels, threat ratings and a verification pass. |
| `pricing-strategy` | Pricing models, value metric, Van Westendorp, experiments. |
| `opportunity-solution-tree` | Torres-style discovery: outcome → opportunities → solutions → experiments. |
| `interview-script` | Mom-Test / JTBD customer-discovery interview script. |
| `user-personas` | Research-grounded personas with JTBD, pains and gains. |
| `prioritization-frameworks` | 9 frameworks (RICE, ICE, Kano, MoSCoW…) with formulas and when to use each. |
| `create-prd` | 8-section Product Requirements Document. |
| `intended-vs-implemented` | Audit the gap between intended behavior and shipped code. |
| `north-star-metric` | Define the NSM and its input-metric constellation by business game. |
| `saas-metrics-coach` | ARR, churn, CAC, LTV, NRR and payback from raw numbers with scripts; benchmarked health check. |
| `ab-test-analysis` | Significance, sample size, SRM, guardrails → ship / extend / stop. |
| `validate-data` | QA gate for an analysis before sharing: pitfall catalog, recomputation, chart integrity, verdict. |

### design
MIT + Apache-2.0 · [plugin README](./design/README.md)

| Skill | What it does |
|---|---|
| `design-taste-frontend` | Brief-aware, anti-slop design direction for new marketing pages and sites. |
| `interface-design` | Craft rules for product UI: dashboards, admin, SaaS apps, settings, data tables. |
| `redesign-existing-projects` | Audit an existing UI with heuristic scoring, strip generic AI patterns, and upgrade it. |
| `industrial-brutalist-ui` | A distinct Swiss-terminal / brutalist aesthetic system. |
| `image-generation` | Generate or edit images with OpenAI GPT Image, Gemini or any session image tool, with cost consent and pixel review. |
| `imagegen-frontend-web` | Premium website design-concept images, one per section (no code). |
| `image-to-code` | Generate a design image first, analyze it, then implement to match. |
| `motion-craft` | Decidable animation rules in two modes: Build, and a strict Review. |
| `web-interface-review` | Lint-style `file:line` review of UI code against ~100 checkable rules. |
| `accessibility-audit` | WCAG 2.2 A/AA audit (axe, keyboard, contrast, screen reader) as an issue review or a conformance table. |
| `frontend-ui-engineering` | Production UI: components, state, layout, accessibility. |
| `icon-set-generator` | Cohesive custom SVG icon set from a frozen style spec, with a preview page. |
| `frontend-slides` | Animation-rich single-file HTML slide decks on a 1920×1080 stage (or PPTX → web). |

### writing
MIT + Apache-2.0 · [plugin README](./writing/README.md)

| Skill | What it does |
|---|---|
| `minto-pyramid` | Conclusion-first structure (SCQA) for decision documents, plus a structure audit with a verdict. |
| `copy-editing` | Seven Sweeps edit of marketing and conversion copy; missing proof is flagged, never invented. |
| `humanizer` | Final pass that removes AI-sounding patterns without adding or losing facts. |

### security
MIT + Apache-2.0 · authorized use only · [plugin README](./security/README.md)

| Skill | What it does |
|---|---|
| `threat-model` | Code-grounded, read-only threat model (interview or bootstrap from the repo). |
| `static-vuln-scan` | Read-only static vulnerability scan scoped from the threat model. |
| `vuln-triage` | Adversarial N-vote verification, dedupe and re-ranking of any scanner's findings (incl. SARIF). |
| `gha-security-review` | Exploit-focused review of GitHub Actions workflows with a traced attack path. |
| `skill-scanner` | Scan an agent skill or plugin for injection, dangerous scripts and excess permissions before installing it. |
| `llm-app-security-audit` | Defensive audit of an app's LLM features: prompt injection, output handling, tool and permission boundaries. |
| `web-pentest` | Scope-gated OWASP-WSTG web pentest with written rules of engagement reconfirmed before every active request. |

### security-cc-by-sa
**CC-BY-SA-4.0: share-alike** · [plugin README](./security-cc-by-sa/README.md)

| Skill | What it does |
|---|---|
| `supply-chain-risk-auditor` | Measurement-first dependency risk report for npm / PyPI / Go; read-only, never installs anything. |
| `variant-analysis` | Find the other instances of a known bug, with CodeQL and Semgrep starters. |

### research
**CC-BY-NC-4.0: non-commercial** · [plugin README](./research/README.md)

| Skill | What it does |
|---|---|
| `deep-research` | Universal multi-agent deep-research pipeline. |
| `academic-paper` | Multi-agent academic paper-writing pipeline. |
| `academic-paper-reviewer` | 5-reviewer peer-review simulation. |
| `academic-pipeline` | Orchestrator: research → write → integrity → review → revise. |

## Attribution & licensing

Curated from these repositories (details, licenses and what was taken: [`NOTICE.md`](./NOTICE.md)):

- **engineering:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (Addy Osmani), [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (forrestchang / multica-ai), [mattpocock/skills](https://github.com/mattpocock/skills) (Matt Pocock), [obra/superpowers](https://github.com/obra/superpowers) (Jesse Vincent), [anthropics/skills](https://github.com/anthropics/skills) (Anthropic), [getsentry/skills](https://github.com/getsentry/skills) (Sentry), [supabase/agent-skills](https://github.com/supabase/agent-skills) (Supabase), [neondatabase/postgres-skills](https://github.com/neondatabase/postgres-skills) (Neon), [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) (Context Engineering Agent Skills Contributors)
- **product:** [phuryn/pm-skills](https://github.com/phuryn/pm-skills) (Paweł Huryn), [wondelai/skills](https://github.com/wondelai/skills) (Wondel.ai), [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Anthropic), [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (Alireza Rezvani; skill author Abbas Mir), [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) (Ferdinando Bons)
- **design:** [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (Leonxlnx), [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) (Vercel Labs), [emilkowalski/skills](https://github.com/emilkowalski/skills) (Emil Kowalski), [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) (Damola Akinleye), [84emllc/claude-wcag-skill](https://github.com/84emllc/claude-wcag-skill) (84EM), [masuP9/a11y-specialist-skills](https://github.com/masuP9/a11y-specialist-skills) (masuP9), [openai/skills](https://github.com/openai/skills) (OpenAI), [jezweb/claude-skills](https://github.com/jezweb/claude-skills) (Jeremy Dawes), [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) (Wuyoscar), [replicate/skills](https://github.com/replicate/skills) (Replicate), [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (Zara Zhang), [pbakaus/impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus)
- **writing:** [millwright-labs/minto-pyramid-skill](https://github.com/millwright-labs/minto-pyramid-skill) (Millwright Labs), [tyroneross/pyramid-principle](https://github.com/tyroneross/pyramid-principle) (Tyrone Ross), [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (Corey Haines), [blader/humanizer](https://github.com/blader/humanizer) (Siqi Chen)
- **security:** [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) (Anthropic), [getsentry/skills](https://github.com/getsentry/skills) (Sentry), [briiirussell/cybersecurity-skills](https://github.com/briiirussell/cybersecurity-skills) (Bri Russell)
- **security-cc-by-sa:** [trailofbits/skills](https://github.com/trailofbits/skills) (Trail of Bits)
- **research:** [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu)

Full per-skill provenance: [`PROVENANCE.csv`](./PROVENANCE.csv) · Licenses: [`LICENSES/`](./LICENSES/) · Details: [`NOTICE.md`](./NOTICE.md) · Changes: [`CHANGELOG.md`](./CHANGELOG.md).

The curation, manifests and docs are MIT. Each skill stays under its upstream license: MIT or Apache-2.0 in the permissive plugins, CC-BY-SA-4.0 in `security-cc-by-sa/`, and CC-BY-NC-4.0 in `research/`, which may not be used commercially.

## Maintenance

- `python3 scripts/validate.py` checks frontmatter (name = directory, description ≤ 1024 chars), manifests, relative links, `PROVENANCE.csv` (one base row per skill, and each license must fit its plugin's license) and SKILL.md length. CI also runs `claude plugin validate --strict` on the marketplace and every plugin.
- `python3 scripts/check_upstream.py [--skill NAME] [--repo OWNER/REPO]` reports every provenance row whose upstream paths changed since the recorded commit.
