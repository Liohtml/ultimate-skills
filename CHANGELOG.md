# Changelog

## Unreleased

Second curation wave: **39 → 68 skills, 4 → 7 plugins, 5 → 34 source repos**. The
marketplace is now version 1.1.0.

### Added: plugins
- `writing` (1.0.0, MIT + Apache-2.0): `minto-pyramid`, `copy-editing`, `humanizer`.
- `security` (1.0.0, MIT + Apache-2.0, authorized use only): `threat-model`,
  `static-vuln-scan`, `vuln-triage`, `gha-security-review`, `skill-scanner`,
  `llm-app-security-audit`, `web-pentest`.
- `security-cc-by-sa` (1.0.0, **CC-BY-SA-4.0**, isolated share-alike plugin):
  `supply-chain-risk-auditor`, `variant-analysis` (Trail of Bits).

### Added: skills in existing plugins
- `engineering` 1.1.0 (16 → 22 skills):
  - `verification-before-completion` (obra/superpowers)
  - `mcp-builder` (anthropics/skills, Apache-2.0)
  - `iterate-pr` (getsentry/skills, Apache-2.0, with obra's receiving-code-review merged in)
  - `subagent-driven-development` (obra/superpowers, decoupled from the other superpowers skills)
  - `postgres-best-practices` (supabase/agent-skills, plus Neon operations references under Apache-2.0)
  - `long-horizon-prompting` (muratcankoylan)
- `product` 1.1.0 (13 → 17 skills):
  - `product-positioning` (wondelai obviously-awesome)
  - `strategy-kernel` (wondelai good-strategy-bad-strategy)
  - `validate-data` (anthropics/knowledge-work-plugins, Apache-2.0)
  - `saas-metrics-coach` (alirezarezvani)
- `design` 1.1.0 (6 → 13 skills):
  - `web-interface-review` (vercel-labs, rules pinned rather than fetched at runtime)
  - `motion-craft` (emilkowalski)
  - `interface-design` (Dammyjay93)
  - `accessibility-audit` (84emllc + masuP9)
  - `image-generation` (openai/skills base under Apache-2.0, plus jezweb, wuyoscar and replicate material; bundled OpenAI and Gemini scripts)
  - `icon-set-generator` (jezweb)
  - `frontend-slides` (zarazhangrui)

### Changed
- Merged into existing skills:
  - `debugging-and-error-recovery`: mattpocock diagnosing-bugs, which adds a red feedback loop before any hypothesis, ranked hypotheses and tagged logs, plus `hitl-loop.template.sh` and obra's `find-polluter.sh`.
  - `competitor-analysis`: ferdinandobons evidence labels and a verification pass.
  - `redesign-existing-projects`: impeccable's craft floor and heuristic critique (Apache-2.0).
  - `minto-pyramid`: tyroneross pyramid-audit, as `references/audit-report.md` (Apache-2.0).
- "For X use Y" cross-pointers were added to the descriptions of neighbouring skills across all plugins.
  - `security-and-hardening` (builder side) and the `security` plugin (auditor side) point at each other.
- Split three oversized design skills into `SKILL.md` plus `references/`:
  - `design-taste-frontend`: 1206 → 367 lines
  - `image-to-code`: 1233 → 216 lines
  - `imagegen-frontend-web`: 991 → 222 lines
- Upstream sync: all 19 changed engineering, product, design and research skills were 3-way-merged with upstream HEAD. Local edits were kept.
  - Upstream plugin-level checklists were vendored into `engineering/references/` and `design/references/`, and 60 more files into `research/shared/`.
  - `research` is now 1.1.0.
- `PROVENANCE.csv`:
  - New `role` column (`base` / `merged`), with one row per upstream source of each skill. A skill with merged material has one `base` row and one `merged` row per extra source.
  - `source_path` may list several `;`-separated upstream paths (directories or single files).
  - `upstream_status` was recomputed against the recorded commits. Several first-wave rows had been marked `identical-to-head` although our copy was modified.
- `scripts/check_upstream.py`:
  - supports any `owner/repo`, with clones stored as `<owner>__<repo>` so repos that share a name no longer collide;
  - checks several paths per row, including single files and the repo root;
  - adds a `--repo` filter;
  - labels merged rows and reports unknown commits.
- `scripts/validate.py` now also validates `PROVENANCE.csv`:
  - exactly one `base` row per skill;
  - full SHAs;
  - known status and role values;
  - each row's license must be part of its plugin's license. This keeps CC-BY-SA and CC-BY-NC material out of the permissive plugins.
- CI validates every plugin directory rather than a hard-coded list.
- Licensing:
  - 29 upstream license files were added to `LICENSES/`, plus `impeccable.NOTICE.md` for reference.
  - Each permissive plugin now carries copies of its sources' licenses in `<plugin>/LICENSES/`, and `security-cc-by-sa/LICENSE` was added, so an installed plugin keeps its notices on its own.
  - `NOTICE.md` has a new source table and sections on Apache-2.0 §4 compliance, excluded third-party material and mixed licensing.
  - The root `LICENSE` preamble was updated for the new plugins.
- `docs/value-bombs.md`: every candidate now has an integration status (integrated, merged or rejected) and a reason.

### Not integrated (see `docs/value-bombs.md`)
- trailofbits property-based-testing, differential-review and fp-check: CC-BY-SA, and they overlap `vuln-triage`.
- writing-skills and skill-creator: skill-creator is already built into Claude Code.
- getsentry security-review: its references are CC-BY-SA and 7 of the files it references are missing upstream.
- Unlicensed or unclear repos, for example robonuggets, devonjones, op7418, rknall, SonOfBytes and indi256s.
- Candidates whose content another skill already covers.

### Fixed (wave-1 polish)
- `research`: vendored the 81 upstream `shared/` files the skills reference into
  `research/shared/` (upstream `Imbad0202/academic-research-skills@95929c0`), fixed
  all broken relative links, and noted that upstream `scripts/` and `docs/design/`
  are optional and not included. Removed generic triggers ("research",
  "help me think through", …) from `deep-research`.
- `design`: `image-to-code` and `imagegen-frontend-web` are no longer Codex-specific,
  document the image-generation prerequisite, fall back to `design-taste-frontend`
  without one, and are delimited from each other.
- Trigger collisions: `pre-mortem` ↔ `strategy-red-team`,
  `design-taste-frontend` ↔ `redesign-existing-projects`; narrowed the
  "any change" triggers of `git-workflow-and-versioning`, `test-driven-development`,
  `incremental-implementation` and `code-review-and-quality`; added disambiguators
  between overlapping engineering skills.
- Marked dead references to upstream-only skills (`context-engineering`,
  `deprecation-and-migration`, `source-driven-development`).

### Added (tooling)
- `scripts/validate.py` (frontmatter, manifests, relative links, SKILL.md size warnings)
  and `.github/workflows/validate.yml` (also runs `claude plugin validate --strict`).
- `scripts/check_upstream.py` to report upstream changes since the recorded commit.
- `PROVENANCE.csv`: `source_commit` and `upstream_status` columns.
- `docs/value-bombs.md`: ranked candidates from other skill repositories for future waves.

## 1.0.0
- Initial curated release: 39 skills in 4 plugins.
