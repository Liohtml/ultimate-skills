# Research skills: merge maps for upstream syncs

Three research skills were restructured locally in wave 3 (2026-10) so that
`SKILL.md` stays under about 500 lines: whole sections were cut **verbatim**
from `SKILL.md` and pasted into new files under `references/`. Upstream
([Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/tree/95929c00fc066730b40cf268fd1250b04f00356a),
CC-BY-NC-4.0, pinned at `95929c0`) still has those sections inline, so an
upstream diff no longer applies to `SKILL.md` line for line. Use the maps below
when you merge upstream changes into these skills.

| Skill | SKILL.md before → after | New reference files |
|---|---|---|
| [`deep-research`](./skills/deep-research/SKILL.md) | 606 → 470 lines | `skill_overview_details.md`, `three_way_scan_mode.md`, `handoff_and_integration.md` |
| [`academic-paper`](./skills/academic-paper/SKILL.md) | 558 → 468 lines | `generator_evaluator_contract_protocol.md` |
| [`academic-pipeline`](./skills/academic-pipeline/SKILL.md) | 742 → 472 lines | `entry_and_routing.md`, `orchestrator_workflow_details.md`, `advisory_side_channels.md`, `skill_overview_details.md` |

`academic-paper-reviewer` was not restructured; sync it as before.

## Conventions (all three skills)

- **Baseline.** "Original lines" are line numbers in the pre-split local file,
  `git show bd033ed:research/skills/<skill>/SKILL.md`. Each skill section
  below says how those map to upstream `95929c0` line numbers (the local
  attribution block and Path notes shift them).
- **Moved text is verbatim.** Each moved block is a contiguous cut of whole
  section bodies. The only edit inside moved text is one link target in
  `academic-pipeline` (A1 below), because `references/` is one folder deeper.
- **Ultimate-skills text, not upstream text:**
  - in each new reference file, the first line ("Moved verbatim from SKILL.md
    section(s) '…' by ultimate-skills (progressive disclosure)."), the Path note
    blockquote and the H1 title; the original section headings are repeated
    above their blocks;
  - in `SKILL.md`, the 1–3 line summary under each kept heading, ending in a
    "Read references/X.md when …" pointer. Summaries restate the rules that
    must stay in context on every run (IRON RULES, gates, routing, opt-in flags,
    "advisory only / never blocks" guarantees).

## Sync procedure

1. Run `python3 scripts/check_upstream.py --skill <skill> --diff` to see the
   upstream commits and the `SKILL.md` diff since `95929c0`.
2. 3-way merge the upstream `SKILL.md` change against the previous upstream base
   as usual. For every hunk, convert its upstream line numbers to original local
   lines (offsets below) and look it up in the skill's table:
   - **inside a moved range:** apply the hunk verbatim to the listed reference
     file, then re-read the summary left in `SKILL.md` and update it if a rule it
     restates changed;
   - **anywhere else:** merge it into `SKILL.md` normally.
3. **New upstream sections** stay in `SKILL.md` unless that pushes it past 500
   lines; then move them the same way and add a row to the table here.
4. If upstream renames or splits a heading that stays in `SKILL.md` as a stub,
   rename the stub too: other files cite these headings by name (see the
   `academic-paper` notes).
5. Check that nothing was dropped. Every non-blank line of the pre-split file
   must still appear in `SKILL.md` or the reference files (the only expected
   miss is the A1 link line in `academic-pipeline`). After a sync, compare
   against the new merged text instead of `bd033ed`.

   ```bash
   skill=deep-research   # or academic-paper, academic-pipeline
   git show "bd033ed:research/skills/$skill/SKILL.md" | python3 -c '
   import collections, pathlib, sys
   need = collections.Counter(l for l in sys.stdin.read().splitlines() if l.strip())
   have = collections.Counter()
   for f in sys.argv[1:]:
       have.update(l for l in pathlib.Path(f).read_text(encoding="utf-8").splitlines() if l.strip())
   missing = need - have
   print(f"{sum(need.values())} non-blank lines, {sum(missing.values())} missing")
   for line in missing.elements():
       print("MISSING:", line[:140])
   ' "research/skills/$skill/SKILL.md" research/skills/$skill/references/*.md
   ```

   Expected today: `deep-research` 472 lines / 0 missing, `academic-paper`
   395 / 0, `academic-pipeline` 537 / 1 (the A1 link line).
6. Run `python3 scripts/validate.py` (relative links, 500-line warning).

## deep-research

Upstream line = original local line − 2 for local lines 19–282, and − 4 for
local lines 285 and later (local attribution block at 17–18, local Path note at
283–284). No link targets inside the moved text needed changing; it contains only
code-span paths, which are relative to the skill root (each new file's Path note
says so).

| # | Heading kept in SKILL.md | Original local lines | Upstream lines (95929c0) | New file | Summary lines in new SKILL.md |
|---|---|---|---|---|---|
| 1 | Trigger Conditions → Trigger Keywords | 55–61 (7) | 53–59 | `references/skill_overview_details.md` | 55–56 |
| 2 | Three-Way Scan Mode (WHY / HOW / WHAT) | 340–371 (32) | 336–367 | `references/three_way_scan_mode.md` | 335–336 |
| 3 | Handoff Protocol: deep-research → academic-paper | 404–432 (29) | 400–428 | `references/handoff_and_integration.md` | 369–371 |
| 4 | Agent File References | 444–458 (15) | 440–454 | `references/skill_overview_details.md` | 383–384 |
| 5 | Reference Files | 464–497 (34) | 460–493 | `references/skill_overview_details.md` | 390–391 |
| 6 | Templates | 503–510 (8) | 499–506 | `references/skill_overview_details.md` | 397–398 |
| 7 | Examples | 516–525 (10) | 512–521 | `references/skill_overview_details.md` | 404–405 |
| 8 | Integration with Other Skills | 569–578 (10) | 565–574 | `references/handoff_and_integration.md` | 449–450 |
| 9 | Model Tiering (#517, optional) | 584–589 (6) | 580–585 | `references/handoff_and_integration.md` | 456–457 |
| 10 | Version Info | 595–600 (6) | 591–596 | `references/skill_overview_details.md` | 463–464 |

In each reference file the original heading is repeated above its block; Trigger
Keywords also repeats its parent `## Trigger Conditions`.

Summaries to re-check when upstream changes a moved range: the Handoff Protocol
summary (it restates the preregistration-sidecar rule: exactly one
`preregistration-artifact/1.0` sidecar, created or updated only by
`build-preregistration-artifact`, carried byte for byte) and the Model Tiering
summary (unset or unknown `ARS_MODEL_TIERING` means every agent inherits the
session model), the Reference Files summary (the IRB decision tree is navigation
only, never an authority; the authority protocol is fail-closed; full file list) and
the Templates summary (all six template files).

Kept in `SKILL.md` unchanged: frontmatter and attribution block, v2.4
report-compiler notes, routing discipline, Quick Start, Socratic Mode activation,
Does NOT Trigger, Quick Mode Selection Guide, Agent Team, Mode Selection Guide
flowchart, the 6-phase Orchestration Workflow with its Checkpoint Rules (IRON
RULES), Phase-by-phase Invocation Contract (with the local Path note), Socratic
Mode, Systematic Review Mode, Operational Modes table, Failure Paths table,
Literature Monitoring, Full Academic Pipeline, Output Language, Anti-Patterns,
Quality Standards, Cross-Agent Quality Alignment and the Version History pointer.

## academic-paper

Upstream line = original local line − 2 for local lines 20–186, and − 4 for
local lines 189 and later (local attribution block at 18–19, local Path note at
187–188).

| # | Heading (original) | Original local lines | Upstream lines (95929c0) | New file | Lines in new file |
|---|---|---|---|---|---|
| 1 | `## v3.6.6 Generator-Evaluator Contract Protocol` with its H3s: Overview, Four-call structure, System prompt vs user content discipline, Schema field name vs runtime emission distinction, Phase 4a / 6a output lint, Phase 4b / 6b output lint, Single-agent generator unusable handling, Cross-session resume scope | 195–288, plus blank line 289 | 191–285 | `references/generator_evaluator_contract_protocol.md` | 7–101 |
| 2 | `## Known limitations` | 290–294 | 286–290 | same file | 102–106 |

- New `SKILL.md` lines 195–200 keep the `## v3.6.6 Generator-Evaluator
  Contract Protocol` heading with a summary of the rules that always apply:
  `full` mode only; 4a, 4b, 6a and 6b run as separate calls; the contract is
  re-sent each call and no dynamic output goes into the system prompt; a lint
  failure is retried once, then `[GENERATOR-PHASE-ABORTED: ...]`; an abort cannot
  enter Stage 3, only a 6b F0/F4/F5 decision can; a round must finish within one
  session. Lines 202–204 keep `## Known limitations` with a one-line summary.
- Everything else is unchanged: original lines 1–194 are new lines 1–194, and
  original lines 295–558 are new lines 205–468 (offset −90).
- Both H2s moved together, so the cross-references inside the moved text
  (`§ "Phase 4a / 6a output lint" below`, `§ "Known limitations" below`, …)
  still resolve within the reference file.
- Other files cite `academic-paper/SKILL.md § "v3.6.6 Generator-Evaluator
  Contract Protocol"`: `agents/draft_writer_agent.md`,
  `agents/peer_reviewer_agent.md`,
  `academic-paper-reviewer/references/sprint_contract_protocol.md` and
  `shared/contracts/README.md`. The stub keeps that heading and forwards to the
  reference file; if upstream renames it, rename the stub too.

## academic-pipeline

Upstream line = original local line − 2 for local lines 21–329, and − 4 for
local lines 332 and later (local attribution block at 19–20, and the local Path
note at 330–331 inside the Phase-by-phase Invocation Contract, which stays in
`SKILL.md`).

| # | Heading kept in SKILL.md | Original local lines | New file | Summary lines in new SKILL.md | Notes |
|---|---|---|---|---|---|
| A1 | Quick Start | 39–66 (28) | `references/entry_and_routing.md` | 39–40 | examples and the `resume_from_passport` contract; link target `references/passport_as_reset_boundary.md` → `passport_as_reset_boundary.md`; the "Execution flow" list (68–73) stays |
| A2 | Trigger Conditions | 79–101 (23) | `references/entry_and_routing.md` | 53–54 | |
| B1 | Pipeline Stages (10 Stages) | 120–125 (6) | `references/orchestrator_workflow_details.md` | 73–74 | parallelization paragraph only; the stage table stays |
| B2 | Decision Dashboard (shown at FULL checkpoints) | 160–180 (21) | `references/orchestrator_workflow_details.md` | 109–110 | |
| B5 | Mid-Conversation Reinforcement Protocol | 300–316 (17) | `references/orchestrator_workflow_details.md` | 230–231 | |
| A3a | Phase-by-phase Invocation Contract (v3.9.2) | 322–328 (7) | `references/entry_and_routing.md` | 237–238 | lines 329–331 (a blank line and the local Path note) stay in SKILL.md |
| A3b | Phase-by-phase Invocation Contract, continued | 332–340 (9) | `references/entry_and_routing.md` | — | continues A3a after the Path note; blank line 341 dropped |
| C1 | Opt-in Inquiry Branch Ledger (#743 alpha) | 346–368 (23) | `references/advisory_side_channels.md` | 246–247 | |
| C2 | Tortured-phrase advisory (#660) | 387–389 (3) | `references/advisory_side_channels.md` | 266–267 | |
| C3 | Cross-document consistency advisory (#672) | 393–414 (22) | `references/advisory_side_channels.md` | 271–273 | |
| C4 | Cross-run Adjudication Activity (#673; opt-in advisory side channel) | 481–509 (29) | `references/advisory_side_channels.md` | 340–341 | |
| C5 | Collaboration Depth Observer (v3.5.0, advisory only — never blocks) | 533–555 (23) | `references/advisory_side_channels.md` | 365–366 | |
| D1 | Quality Standards | 578–591 (14) | `references/skill_overview_details.md` | 389–390 | |
| D2 | Error Recovery | 597–609 (13) | `references/skill_overview_details.md` | 396–397 | |
| D3 | Agent File References | 615–621 (7) | `references/skill_overview_details.md` | 403–404 | |
| D4 | Reference Files | 627–645 (19) | `references/skill_overview_details.md` | 410–411 | |
| B6 | Integration with Other Skills | 674–703 (30) | `references/orchestrator_workflow_details.md` | 440–442 | |
| B7 | Model Tiering (#517, optional) | 719–724 (6) | `references/orchestrator_workflow_details.md` | 458–459 | |
| D5 | Version Info | 730–736 (7) | `references/skill_overview_details.md` | 465–466 | |

In the reference files, parent headings are repeated where a moved block was a
subsection (for example `## Adaptive Checkpoint System` above `### Decision
Dashboard …`, `## Orchestrator Workflow` above `### Mid-Conversation
Reinforcement Protocol`, `## Integrity Review Protocol` above `### Tortured-phrase
advisory (#660)`).

Summaries to re-check when upstream changes a moved range: the opt-in flags
(`ARS_INQUIRY_LEDGER`, `ARS_MODEL_TIERING`, `ARS_PASSPORT_RESET`),
`resume_from_passport` and Mode A/B routing, the Stage-5 entry advisories (#660
runs before #672 on the same accepted draft; both advisory only, never a gate),
the #673 guarantee (its data never enters the passport or any gate), the
collaboration observer's never-blocks guarantee, "never skip gates on
errors", the Quality Standards summary (continuing past a non-PASS result at Stage
2.5/4.5 needs an explicit, recorded user decision; user confirmation after every
stage), the Error Recovery summary (every row of the moved table) and the Reference
Files summary (includes literature_corpus_consumers.md, adapters/overview.md,
score_trajectory_protocol.md).

Kept in `SKILL.md` unchanged: frontmatter and attribution block (lines 1–36),
Orchestrator Workflow Steps 1–4 with the handoff contents for each transition,
State Machine, checkpoint types, adaptive rules, checkpoint rules and self-check,
the integrity IRON RULES, Two-Stage Review, Mid-Entry, Revision Loop and its
budget, Stage 6, Anti-Patterns, Templates, Examples, Related Skills and
Changelog.

Known upstream gaps, left as they are: the Examples table omits
`examples/integrity_failure_recovery.md`, and the Reference Files index omits
`literature_corpus_consumers.md`, `score_trajectory_protocol.md` and
`adapters/`.
