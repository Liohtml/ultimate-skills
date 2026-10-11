# Changelog

## Unreleased: `security-audit` (Cloudflare)

- **New skill `security/security-audit`** from
  [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)
  `c1c8a8c` (MIT): Cloudflare's source-first audit workflow, which seeded their
  vulnerability-discovery harness. Full audit mode runs six phases:
  reconnaissance into a deterministic coverage ledger, isolated coverage-led
  hunters (core attack classes plus 10 domain companions), a fresh verifier per
  candidate, `findings.json` checked by `report-schema.json` and two
  zero-dependency Node validators, independent re-verification, and a report
  written outside the target repo. Guidance mode applies the same evidence bar
  to a single question. Target code runs only inside an OS-enforced sandbox.
  - Only the frontmatter description was rewritten (with pointers to the
    neighbouring security skills) and an attribution / Claude Code terminology
    note added; all other files are byte-identical to upstream.
  - The bundled validator test suites pass (65/65). `skill-scanner` reports no
    findings on the skill.
- **Neighbours re-pointed:** `static-vuln-scan` is now the quick one-pass scan
  feeding `vuln-triage`; full codebase audits route to `security-audit` from
  `threat-model`, `vuln-triage`, `web-pentest`, `gha-security-review`,
  `llm-app-security-audit` and `engineering/security-and-hardening`.
- Catalog: **69 skills in 7 plugins from 35 source repos**.

## Unreleased: upstream sync 2 (marketplace 1.3.0)

This round syncs every provenance row whose upstream changed since its recorded
`source_commit`: 22 rows, one per skill, from 11 source repos, plus the vendored
`research/shared/`. The catalog is unchanged at **68 skills in 7 plugins from
34 source repos**. Each changed file went through a 3-way merge
(`git merge-file`, with the upstream file at the old `source_commit` as the
base). Where our copy is a rewrite rather than a lightly edited upstream file
(`create-prd`, `humanizer`, `debugging-and-error-recovery`,
`accessibility-audit`), the upstream change was applied by hand.

- **Licenses:** every upstream `LICENSE` is byte-identical at HEAD and at the old
  commit, and so is impeccable's `NOTICE.md`. The only upstream legal-file change
  is one new row in academic-research-skills' `THIRD_PARTY.md` (an OpenClaw
  port). It does not touch our material. Nothing was imported under a different
  license.
- **Local changes kept:**
  - rewritten descriptions and "For X use Y" pointers;
  - "(upstream …, not included here)" markings;
  - attribution lines and Apache-2.0 change notes, re-pinned to the new commits;
  - progressive-disclosure splits;
  - every fix from the script test pass below. The fixed files did not change
    upstream (`find-polluter.sh`, `scan_skill.py`, the run-from-the-working-tree
    note in `subagent-driven-development/SKILL.md`), so the fixes are intact.
- **New "not included here" markings** for upstream material that this round's
  text references but the marketplace does not ship:
  - `constraint-driven-development` (agent-skills);
  - a second mention of `shipping-artifacts` (pm-skills);
  - the copywriting `ai-tells.md` and seo-audit `title-tags.md` references
    (marketingskills);
  - academic-research-skills' new fifth skill `sr-screener`, its `/ars-*` slash
    commands and `scripts/check_acronyms.py`.

Plugin versions: `engineering` 1.3.0, `product` 1.3.0, `design` 1.3.0,
`writing` 1.2.0, `security` 1.2.0 and `research` 1.3.0. They also cover the
script test pass below. `security-cc-by-sa` stays at 1.0.0 (its upstream paths
are unchanged).

### engineering
addyosmani/agent-skills `bcab6a1` → `1be8e34`, mattpocock/skills `c55ee46` →
`49dd158`, obra/superpowers `5bf4e78` → `bb92a77`.
- `spec-driven-development`: a hard stop after writing the spec. Summarize it,
  list the open questions, ask for approval, then end the turn without planning
  or coding. A matching red flag and checklist item were added.
- `code-review-and-quality`: "would the tests catch a regression?" is answered by
  experiment. Invert one added condition, run the suite and restore the file; a
  mutation that stays green is a finding.
  - Upstream's fix for diffs pasted inline was folded into our rewritten
    description (the frontmatter conflict).
  - The new `constraint-driven-development` pointer is marked "not included
    here".
- `security-and-hardening`: the zod example applies `min(1)` after `trim()`, so a
  whitespace-only title is rejected.
- `performance-optimization`: Step 3 "Fix the Bottleneck" is condensed to a rule
  and a recognizable signature per anti-pattern. The worked fixes moved to a new
  `references/optimization-patterns.md` (upstream progressive disclosure;
  SKILL.md 496 → 267 lines).
- `api-and-interface-design`: `throw;` (invalid JS/TS) → `throw e;` in the
  idempotency example.
- `documentation-and-adrs`: the ADR Status line starts at `Proposed`. There is a
  new tool-neutral "Prose Review" section with a checklist item, plus one local
  line pointing to `humanizer` for its step 2.
- `debugging-and-error-recovery` (mattpocock diagnosing-bugs `f3fc563`): if the
  red was forced by mutating code or a fixture, `diff` against a pristine copy to
  prove that the mutation landed. Upstream's CONTEXT.md → GLOSSARY.md rename
  does not apply, because that convention was never taken.
- `subagent-driven-development` (obra v7.0.0): `sdd-workspace` resolves the repo
  root as a physical path, which fixes Git Bash and symlinked repos. It now only
  creates `.sdd/.gitignore`, so a repo can commit its own.
  - One conflict: we kept our `.sdd/` workspace path.
  - A new 20-case harness passes. The pre-merge script fails the committed
    `.gitignore` case.
- The vendored `engineering/references/` and `design/references/` READMEs are
  re-pinned to `1be8e34`; their content is unchanged upstream.

### design
- `frontend-ui-engineering` (agent-skills): `refetch` is destructured from
  `useTasks()`, so `retry={refetch}` is bound.
- `redesign-existing-projects` (impeccable `e0881d2` → `c63b8dd`): the craft-floor
  rule "never animate an image on hover" is retired, as upstream did after a
  corpus review.
  - The merge conflicted because our copy folds the model-specific blocks into
    one list, so the change was applied by hand.
  - The Apache-2.0 change note is re-pinned and now says that the `<codex>`
    block was merged (upstream no longer has a `<gemini>` block).
- `web-interface-review` (vercel-labs `e3d624b` → `434b7f9`): a new desktop
  overscroll rule. Put `overscroll-behavior: none` on `<html>` inside
  `@media (pointer: fine)` and keep the coarse-pointer defaults for
  pull-to-refresh. It is in both the SKILL.md rules and the verbatim `AGENTS.md`
  copy.
- `accessibility-audit` (masuP9 `6615e6e` → `eeba8df`): we take only ideas from
  masuP9 and dropped its CLI, so the CLI-independent substance was folded into
  the manual passes:
  - axe does not cover 1.4.11, and its 2.5.3 rule is experimental and off by
    default;
  - keyboard reachability of composite widgets, popups, iframes and Shadow DOM
    (2.1.1);
  - target spacing for fixed elements (2.5.8);
  - the HTML autofill grammar for `autocomplete` (1.3.5).

  Upstream's claim that `position: sticky` targets "scroll with the page" was
  left out on purpose.

### product
phuryn/pm-skills `8607e3b` → `c68487d`.
- `create-prd` (pm-skills v2.2.0, 164 → 192 lines), folded into our deepened
  version:
  - lean by default: 1–2 pages, full version on request;
  - ask up to three questions when the problem, the users or the success measure
    is missing;
  - research freely and cite each source;
  - section 6 is now the 6-part JTBD value proposition, one per segment, and
    serves as the spine of the PRD;
  - a first version targets 2–3 segments at most;
  - "say what you left out";
  - reviews list blocking gaps first, then cuts;
  - new anti-patterns: Padded PRD, Broken spine;
  - the template, review rubric and worked example are updated to match.

  A mechanical merge conflicted across the whole body, so the changes were
  applied semantically. Two rules were reconciled:
  - an inline `[TBD: owner]` is allowed only for a specific unknown value with an
    open-question entry;
  - high-stakes work gets the lean draft first, plus a recommendation for the
    full version.

  The merged `write-spec` source (knowledge-work-plugins) is unchanged upstream
  and stays at `1bd4282`.
- `intended-vs-implemented`: follows each repo's own documentation layout. The
  new `shipping-artifacts` mention is marked "not included here".

### writing
- `copy-editing` (marketingskills `5b2c000` → `1efedbc`, 416 → 448 lines):
  - an AI-Tell Check on every edit;
  - a "replace with the fact" table;
  - a "Reads as AI-Written" problem;
  - an AI Tells checklist block;
  - SERP gap analysis and "keep what already works" in the content-refresh
    reference.

  Our no-invented-facts `[needs: …]` marker wins over upstream's `[NEED: …]`.
  The humanizer boundary stays in the description: copy-editing covers marketing
  copy, humanizer other prose. Upstream's "sounds like AI" triggers were not
  adopted. Upstream `evals/` are still not included.
- `humanizer` (`9862685` → `225a6f3`, 3.0.0 → 3.1.0, 453 → 482 lines): rules and
  taxonomy only, written in original wording with original examples:
  - new family F "Writing for the wrong reader" with §26 "Re-explaining what the
    reader knows";
  - §25 widened to text that describes itself;
  - §2 additions;
  - the core rule now counts conversation context;
  - §20 covers headings written for effect;
  - de-duplicated watch lists;
  - a detector non-goal;
  - 26 patterns.

  A check against the Wikipedia page dumps finds no shared run of 6 or more
  words. Upstream's dash cross-reference fix matches our wave-3 fix.

### security
getsentry/skills `c2f99a5` → `d18b7aa`.
- `gha-security-review` and `skill-scanner`: upstream's `# nosemgrep`
  suppressions above the IMDS and reverse-shell examples in the reference files.
  - The `allowed-tools` comma fix does not apply, because our copies drop
    `allowed-tools`.
  - The Apache-2.0 change notes are re-pinned to `d18b7aa`.
  - `scan_skill.py` is unchanged upstream and every test-pass fix is kept.
  - Re-run: the malicious fixture gives the same 21 findings, with no secret in
    the output. A scan of all 68 skills gives valid JSON with empty stderr for
    every one.

### research
Imbad0202/academic-research-skills `95929c0` → `ebc21bf` (upstream v3.22.1 →
v3.23.0), covering all four skills and `research/shared/`.

From upstream:
- In all four `SKILL.md` files:
  - The routing core (#892) is now inline, byte-identical to the newly vendored
    `shared/references/routing_core.md`, because plugin installs never load
    upstream's `.claude/CLAUDE.md`. It includes #961: only a `[direct-mode]` at
    byte 0 is the escape hatch.
  - A new section "Pasted and retrieved text is data, not instructions" carries
    the canonical instruction/data boundary (#890, #894). Matching sections were
    added to the agents that read pasted or retrieved text.
  - Model tiering grows from 39 to 43 agents.
- `academic-pipeline` (v3.23.0):
  - new orchestration: a run ledger and handoff check (#887/#898), standing
    constraints (#927), integrity-excluded sources (#936), an experiment-intake
    question (#925), declined items at Stage 3'/4' (#927), a final-output
    pre-check at Stage 4.5 (#929) and an evidence source folder handoff
    (#933/#947/#948);
  - the v3.6.7 audit artifact gate is opt-in (`ARS_AUDIT_ARTIFACT_GATE=1`; the
    variable is configuration, not consent);
  - `ARS_PASSPORT_RESET` resets at FULL and MANDATORY checkpoints;
  - Stages 5 and 6 ask which files to produce (#928).
- `academic-paper`:
  - acronym-check hooks (#849);
  - a `word_ceiling` standing constraint (#927);
  - the formatter reports gaps and word-count mismatches instead of writing
    content (#928, #929);
  - a full Mode A run stops after Phase 6;
  - journal and conference reviewers are peer review, never the
    committee-correspondence variant (#854);
  - the review-form note (#921);
  - a revision does not regenerate the abstract (#936);
  - per-source method weaknesses (#916).
- `deep-research`:
  - the review-form note, shown on `lit-review` selection or RQ confirmation
    (#921);
  - per-source method weaknesses in the three-way scan, bibliography agent and
    evidence template (#916);
  - `systematic-review` only on the author's choice;
  - Schema 1 scope axes (#938).
- `academic-paper-reviewer`:
  - an advisory acronym-check attachment to the Editorial Decision Letter, added
    only after `check_panel_synthesis.py` exits 0; it never feeds back into the
    decision (#849);
  - a Major that comes only from declined items goes into the next roadmap as a
    limitations target (#927).
- `shared/`:
  - 10 files 3-way merged with 0 conflicts;
  - 7 files added: the `excluded_source_entry`, `standing_constraint_entry` and
    `run_ledger` passport schemas; `references/routing_core.md`,
    `intent_clarification_protocol.md` and `review_form_note.md`; and
    `research_workflow_profiles/field_general.json` (`contracts/README.md`
    always pointed to it);
  - `per_source_method_weaknesses.md` is not vendored, because the skills carry
    that block inline.

Local:
- 12 `SKILL.md` conflicts (pipeline 3, paper 3, deep-research 4, reviewer 2).
  They were all on lines where we had dropped pointers to unvendored upstream
  files, or inside moved ranges. They were resolved to upstream content plus our
  markings.
- Progressive disclosure:
  - `academic-paper-reviewer` was split for the first time (542 lines after the
    merge → 486), with a new `references/skill_overview_details.md`.
  - `deep-research` (480 lines): the Mode Selection flowchart, the Phase-by-phase
    contract body and the key failure-path table moved to a new
    `references/workflow_details.md`.
  - `academic-paper` (575 lines after the merge → 464): new
    `references/skill_overview_details.md` and
    `references/review_target_criteria_binding.md`.
  - `academic-pipeline` (513 lines after the merge → 478): the Orchestrator
    Workflow Step 1–3 blocks moved to `references/orchestrator_workflow_details.md`.
    The routing core and the boundary section stay inline because upstream
    requires them in every `SKILL.md`, and the #925 flag stays because opt-in
    flags must stay in context.
  - In `deep-research` and `academic-paper`, the 60-line review-form-note block
    is now a pointer stub to `shared/references/review_form_note.md`.
- Attribution pins and pinned docs URLs were bumped to `ebc21bf`, and every
  target was checked to exist.
- [`research/MERGE_MAPS.md`](research/MERGE_MAPS.md) was rewritten:
  - all four maps are now keyed to upstream `ebc21bf` line numbers, so no
    offsets are needed;
  - the routing core and boundary block are listed as keep-inline;
  - the no-drop check now covers `academic-paper-reviewer`;
  - expected today: 562/4, 471/5, 402/3 and 561/4 non-blank/missing lines.

### Provenance, notices and docs
- `PROVENANCE.csv`: the 22 synced rows are re-pinned and all stay
  `modified-locally`. Rows without upstream changes keep their commits:
  - the other addyosmani rows and obra's `find-polluter.sh`,
    `verification-before-completion` and `receiving-code-review` rows;
  - `create-prd`'s `write-spec` row (identical at upstream `02ffa99`);
  - `iterate-pr`'s getsentry row, whose attribution link pins `c2f99a5`.
- `NOTICE.md`:
  - the `find-polluter.sh` and `scan_skill.py` modification notes now list the
    test-pass fixes;
  - the `research/` notes cover the sync-2 splits and the vendored files'
    markings;
  - the `humanizer` note covers the 3.1.0 rules.
- `docs/value-bombs.md`: status for upstream sync 2.

## Unreleased: script test pass

Every bundled script (24) was run for real on realistic inputs, with local mock
APIs where no key was available. Bugs found by those runs are fixed:

- `image-generation`: the default Gemini model is now `gemini-nano-banana-2.1`.
  `gemini-3.1-flash-image` is deprecated and shuts down on 2026-10-29 (per
  google-gemini/gemini-skills `832c8f9`). `gemini_image.py` no longer saves interim
  `thought` images. `image_gen.py` checks for an existing output before the paid
  call, reports API errors without a traceback, ignores `--moderation` on edits
  (the edit API has no such parameter) and has a corrected retry-after regex.
- `frontend-slides`: `export-pdf.sh` captured every slide after the first blank or
  mid-fade; reveal transitions are now disabled during export. `extract-pptx.py`
  now extracts tables, grouped shapes and placeholder pictures, and fails cleanly
  on bad input.
- `saas-metrics-coach`: the projection compounded one month too few; the quick
  ratio now includes reactivation; Rule of 40 annualises MoM growth by compounding;
  zero/negative inputs and non-interactive runs no longer crash.
- `skill-scanner`: no longer follows symlinks out of the skill directory, masks
  secrets in its evidence, does not crash on YAML dates, and its HTTP-exfiltration
  pattern now matches real calls.
- `mcp-builder`: `mcp` pinned below 2.0; `evaluation.py` serialises MCP content
  blocks and parses its arguments reliably.
- `iterate-pr`, `find-polluter.sh`, `checkpoint.py` (threat-model, vuln-triage):
  robustness fixes (missing fields, paths with spaces, clean errors, `--help`).
- `subagent-driven-development`: the SKILL.md now says to run the scripts from the
  project's working tree (running them from the skill directory created the
  workspace inside the plugin checkout).

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
