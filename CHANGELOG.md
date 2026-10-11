# Changelog

## Unreleased: wave 3 (marketplace 1.2.0)

A depth and clean-up round with no new skills: still **68 skills in 7 plugins
from 34 source repos**. Four product skills were deepened, the three research
skills over 500 lines were split for progressive disclosure, `humanizer` no
longer quotes Wikipedia, and several bundled scripts were fixed.

Plugin versions: `engineering` 1.2.0, `product` 1.2.0, `design` 1.2.0,
`writing` 1.1.0, `security` 1.1.0, `research` 1.2.0. `security-cc-by-sa` is
unchanged at 1.0.0.

### Changed: product skills deepened
- `create-prd` (SKILL.md 86 → 164 lines, 5 new references):
  - evidence-first problem framing with `[Data]` / `[Research]` / `[Assumption]` labels and "why now"; never invent data;
  - success metrics split into primary, leading and guardrail, each with baseline, target, timeframe and source, plus explicit non-goals;
  - MoSCoW requirements with testable acceptance criteria, non-functional requirements and edge cases;
  - assumptions and risks typed as value, usability, feasibility or viability, each with a validation plan;
  - a release section with a rollout or experiment plan, decision rule, kill criteria and owned open questions;
  - right-sizing (one-pager, full PRD, or discovery first), Create / Review / Update modes, a quality gate, a PRD review procedure and an anti-pattern table;
  - references: copy-ready template, requirements and acceptance criteria, metrics and rollout, PRD review rubric, and a fictional worked example.
  - Merges rewritten material from anthropics/knowledge-work-plugins `write-spec` (Apache-2.0, `LICENSE.txt` added to the skill).
- `user-personas` (69 → 137 lines, 3 new references):
  - an evidence gate that labels the result as a research, provisional or proto-persona; no personas without data;
  - behavioural-variable segmentation instead of demographics; job statements with switching forces (push, pull, anxiety, habit) and triggers;
  - confidence levels, segment sizing, a primary persona and an anti-persona; privacy rules (anonymised participant IDs, no real photos);
  - validation, a refresh cadence and an anti-pattern table; the number of personas follows the data (usually 2–4) instead of a fixed 3;
  - references: evidence and synthesis, segmentation and JTBD, persona templates with a worked example.
  - Merges rewritten material from anthropics/knowledge-work-plugins `synthesize-research` (Apache-2.0, `LICENSE.txt` added to the skill).
- `prioritization-frameworks` (75 → 199 lines, 4 new references): framing the decision, choosing a framework by situation, allocating capacity before scoring, calibrated scales with worked RICE and ICE examples and a sensitivity check, cost of delay (CD3) and WSJF, Kano and opportunity-survey mechanics, a session playbook, pitfalls and a ranked-output template. Original text.
- `value-proposition` (108 → 206 lines, 5 new references): evidence labels, switching forces with a net-force check, a canvas fit check, differentiation against real alternatives (swap test, value curve), value hypotheses with the cheapest test for each, a value statement and messaging-hierarchy handoff, and a worked example. Original text.
- All examples and numbers in the new product material are fictional and labelled as such.

### Changed: other skills
- `writing/humanizer` (377 → 453 lines):
  - All 38 before/after examples were replaced with original ones; many of the old ones were quoted from Wikipedia's CC BY-SA "Signs of AI writing" page. Each new "after" uses only facts from its "before".
  - Pattern descriptions, watch lists and voice examples were reworded. The 25-pattern taxonomy, numbering, workflow and description are unchanged.
  - A check against the current Wikipedia page and 17 revisions from June 2025 to October 2026 finds no shared run of 6 or more words (148 shared 8-word runs before). Wikipedia is now credited for the pattern categories only.
  - Fixed the Voice section's dash cross-reference (§6 → §8), and added blank lines so "After:" no longer renders inside the preceding quote.
- `research`: progressive disclosure for the three skills over 500 lines. Whole sections were moved verbatim into new `references/` files. `SKILL.md` keeps each heading with a short summary of the rules that always apply (IRON RULES, gates, routing, opt-in flags, advisory-only guarantees) and a "Read references/X.md when …" pointer. The only edit inside moved text is one link target, because the file is one folder deeper.
  - `deep-research`: 606 → 470 lines; 10 sections moved to `skill_overview_details.md`, `three_way_scan_mode.md` and `handoff_and_integration.md`.
  - `academic-paper`: 558 → 468 lines; "v3.6.6 Generator-Evaluator Contract Protocol" and "Known limitations" moved to `generator_evaluator_contract_protocol.md`.
  - `academic-pipeline`: 742 → 472 lines; 19 blocks moved to `entry_and_routing.md`, `orchestrator_workflow_details.md`, `advisory_side_channels.md` and `skill_overview_details.md`.
  - New [`research/MERGE_MAPS.md`](research/MERGE_MAPS.md): a section-by-section map from the pre-split files (commit `bd033ed`) and upstream `95929c0` to the new files, the sync procedure, and a check that no upstream line was dropped. `research/README.md` points to it.
- `engineering/security-and-hardening` (216 → 226 lines): scope narrowed to code being built. The description now says that auditing or testing an existing system belongs to the `security` plugin, and names `supply-chain-risk-auditor (security-cc-by-sa)`. A "Scope:" line and one-line pointers at the top of four sections were added (Threat Model First → `threat-model`, dependencies → `supply-chain-risk-auditor`, AI/LLM features → `llm-app-security-audit`, Review Checklist → `static-vuln-scan` / `web-pentest`). Nothing was removed.

### Fixed: bundled scripts and paths
- `design/frontend-slides` `scripts/export-pdf.sh` (418 → 530 lines):
  - Playwright is pinned to 1.63.0; `SLIDES_PLAYWRIGHT_VERSION` overrides it with an exact version only. An installed Playwright that can launch Chromium is reused first; otherwise the pinned version goes into a temp dir with `npm install --no-save --ignore-scripts`. `SLIDES_CHROMIUM_PATH` uses an existing Chrome or Chromium and skips the download.
  - Security: the local server listened on all interfaces and served files outside the deck folder via `..%2F`. It now binds to 127.0.0.1, returns 403 outside the deck folder and 400 for malformed URLs; URLs with a query string load.
  - A relative output path such as `out.pdf` was written into the temp dir and then deleted; it now resolves against the caller's directory. Temp files are always cleaned up, running without arguments works on macOS bash 3.2, and a failing `open` / `xdg-open` no longer turns a successful export into an error.
  - New `--help` and `--no-open`; unknown options are rejected.
  - `SKILL.md` runs both scripts via `${CLAUDE_SKILL_DIR}` (the extract script used to need the skill folder as working directory) and describes the Playwright and browser-cache behaviour correctly.
- `security/skill-scanner` `scripts/scan_skill.py`: argparse `--help` and argument handling (invalid arguments exit 2), and a JSON error instead of a traceback when PyYAML is missing; Apache-2.0 §4(b) notice added to the file header. Scan logic and output are unchanged (byte-identical to upstream on 9 skills).
- `${CLAUDE_SKILL_DIR}`: Claude Code expands it in `SKILL.md` text and `allowed-tools` only, not in `references/*.md` and not in older versions. The fallback notes in the `threat-model` and `vuln-triage` SKILL.md files now say so and name the plugin-install path (`${CLAUDE_PLUGIN_ROOT}/skills/<name>`). The reference files that use the variable (`threat-model`: `bootstrap.md`, `interview.md`, `schema.md`; `vuln-triage`: `checkpointing.md`, `output-format.md`) carry a "Paths:" note near the top: replace it with the skill directory before running a command.

### Changed: provenance, notices and tooling
- `PROVENANCE.csv`: two `merged` rows for anthropics/knowledge-work-plugins @ `1bd4282` (Apache-2.0): `write-spec` → `create-prd`, `synthesize-research` → `user-personas`. Every row stays `modified-locally`.
- `NOTICE.md`: the knowledge-work-plugins row and the Apache-2.0 material list now include `create-prd` and `user-personas`; the `humanizer` caveat about quoted Wikipedia examples was replaced, because no CC BY-SA text remains in the MIT `writing` plugin; the wave-3 modifications are listed. No new license file was needed: upstream `product-management/LICENSE` is byte-identical to the `data/LICENSE` already shipped as `knowledge-work-plugins.LICENSE`.
- `scripts/check_upstream.py`: prints a `note:` under CHANGED rows for skills that diverge from upstream on purpose. The three split research skills point to `research/MERGE_MAPS.md`; `humanizer` must not re-import upstream examples.
- `docs/value-bombs.md`: wave-3 status; the open item about the unpinned Playwright install is closed.
- Read but not adapted: alirezarezvani `ux-researcher-designer` and coreyhaines31 `customer-research` (MIT). deanpeters/Product-Manager-Skills (CC-BY-NC-SA) was not used.

## Unreleased: wave 2 (marketplace 1.1.0)

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
