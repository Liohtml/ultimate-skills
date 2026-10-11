# Research skills: merge maps for upstream syncs

All four research skills are restructured locally so that `SKILL.md` stays
under 500 lines: whole sections were cut **verbatim** from `SKILL.md` and pasted
into files under `references/`. `deep-research`, `academic-paper` and
`academic-pipeline` were split in wave 3 (2026-10). Upstream sync 2 moved more
sections, because upstream grew, and split `academic-paper-reviewer` for the
first time. Upstream
([Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/tree/ebc21bf2429643fe4c2495aa99e1bbacd926772b),
CC-BY-NC-4.0, pinned at `ebc21bf`, v3.23.0) still has those sections inline, so
an upstream diff no longer applies to `SKILL.md` line for line. Use the maps
below when you merge upstream changes into these skills.

| Skill | Upstream `ebc21bf` SKILL.md | Local SKILL.md | Reference files holding moved sections |
|---|---:|---:|---|
| [`deep-research`](./skills/deep-research/SKILL.md) | 729 lines | 480 lines | `skill_overview_details.md`, `three_way_scan_mode.md`, `handoff_and_integration.md`, `workflow_details.md` (sync 2) |
| [`academic-paper`](./skills/academic-paper/SKILL.md) | 662 | 464 | `generator_evaluator_contract_protocol.md`, `skill_overview_details.md` (sync 2), `review_target_criteria_binding.md` (sync 2) |
| [`academic-paper-reviewer`](./skills/academic-paper-reviewer/SKILL.md) | 538 | 486 | `skill_overview_details.md` (sync 2) |
| [`academic-pipeline`](./skills/academic-pipeline/SKILL.md) | 777 | 478 | `entry_and_routing.md`, `orchestrator_workflow_details.md`, `advisory_side_channels.md`, `skill_overview_details.md` |

In `deep-research` and `academic-paper`, the upstream review-form-note block
(#921) is not inline either. It lives once, in
[`shared/references/review_form_note.md`](./shared/references/review_form_note.md),
and `SKILL.md` keeps a pointer stub (see Conventions).

The wave-3 maps were keyed to the pre-split local files (`bd033ed`) and upstream
`95929c0`. They are in git history: `git show 0387255:research/MERGE_MAPS.md`.

## Conventions (all four skills)

- **Baseline.** Every line number in the tables below is a line of upstream
  `ebc21bf` `SKILL.md`, i.e. `git -C <clone> show ebc21bf:<skill>/SKILL.md`.
  `scripts/check_upstream.py --diff` diffs from the recorded `source_commit`
  (`ebc21bf`), so the old-side line numbers of each hunk can be looked up
  directly. No offsets are needed.
- **Moved text is verbatim**, with three one-line exceptions:
  - `academic-pipeline` A1: link target `references/passport_as_reset_boundary.md`
    → `passport_as_reset_boundary.md`, because `references/` is one folder deeper;
  - `academic-pipeline` A3b and `deep-research` row 12: the Mode B routing line
    says "near the top of `SKILL.md`" instead of "near the top of this file",
    because that line now lives in `references/`.
- **Ultimate-skills text, not upstream text:**
  - in each reference file, the first line ("Moved verbatim from SKILL.md
    section(s) '…' by ultimate-skills (progressive disclosure)."), the Path note
    blockquote and the H1 title; the original section headings are repeated
    above their blocks;
  - in `SKILL.md`, the rewritten frontmatter `description`, the attribution
    block, the Path notes, the routing-discipline note where it was adapted, and
    the 1–3 line summary under each kept heading, ending in a "Read
    references/X.md when …" pointer. Summaries restate the rules that must stay
    in context on every run (IRON RULES, gates, routing, opt-in flags, "advisory
    only / never blocks" guarantees).
- **Kept inline, byte-identical to `shared/`.** Never move these into
  `references/`. Upstream requires them in every `SKILL.md`: upstream CI checks
  the routing core byte for byte, and §2A of `shared/ground_truth_isolation_pattern.md`
  requires the boundary block.
  - The routing core between `<!-- routing-core:begin -->` and
    `<!-- routing-core:end -->` equals `shared/references/routing_core.md` (#892).
  - The canonical instruction/data boundary block under "Pasted and retrieved
    text is data, not instructions" equals the block in
    `shared/ground_truth_isolation_pattern.md` (#890, #894).
  - Markings for upstream-only material (the `sr-screener` skill, the `/ars-*`
    slash commands) go **outside** these blocks: in the routing-discipline note
    (`deep-research`, `academic-paper`, `academic-paper-reviewer`) or in a Path
    note just above the core (`academic-pipeline`).
- **Pointer stub.** In `deep-research` and `academic-paper`, the
  `### Review-form note (#921)` heading stays (other files cite
  "§ Review-form note") with a short summary and a link to
  `../../shared/references/review_form_note.md`, whose marker block is
  byte-identical to upstream's inline copies. Both stub summaries must keep the
  #921 rule that the note is shown at no other point and never depends on the
  topic, the wording or the kind of research question. Upstream's sentence "The canonical
  copy of the block below is `shared/references/review_form_note.md`; …" is
  dropped, because no copy follows it here.

## Sync procedure

1. Run `python3 scripts/check_upstream.py --skill <skill> --diff` to see the
   upstream commits and the `SKILL.md` diff since `ebc21bf`.
2. 3-way merge the upstream `SKILL.md` change (`git merge-file`) as usual. For
   every hunk, look up its old-side `ebc21bf` line numbers in the skill's table:
   - **inside a moved range:** apply the hunk verbatim to the listed reference
     file (a 3-way merge of that file works, since its block equals the base
     range), then re-read the summary left in `SKILL.md` and update it if a rule
     it restates changed;
   - **inside the review-form-note block:** sync
     `shared/references/review_form_note.md`, then re-check both stub summaries;
   - **inside the routing core or the boundary block:** sync the `shared/` copy
     first, then copy the block byte for byte into all four `SKILL.md` files;
   - **anywhere else:** merge it into `SKILL.md` normally.
3. **New upstream sections** stay in `SKILL.md` unless that pushes it past 500
   lines. Then move lookup-style material (keyword lists, file indexes, version
   tables, procedure blocks) the same way and add a row here. Do not move the
   routing core, the boundary section, IRON RULES, gates, opt-in flags or
   headings that other files cite by name.
4. If upstream renames or splits a heading that stays in `SKILL.md` as a stub,
   rename the stub too: other files cite these headings by name (see the notes
   per skill).
5. Check that nothing was dropped. Every non-blank line of upstream `SKILL.md`
   must still appear in `SKILL.md`, the reference files or the shared
   review-form note, except the deliberate local edits listed per skill. After a
   sync, run it against the new upstream commit and update the expected numbers.

   ```bash
   skill=deep-research   # or academic-paper, academic-paper-reviewer, academic-pipeline
   clone=<clone-dir>/Imbad0202__academic-research-skills   # from check_upstream.py --clone-dir
   git -C "$clone" show "ebc21bf:$skill/SKILL.md" | python3 -c '
   import collections, pathlib, sys
   need = collections.Counter(l for l in sys.stdin.read().splitlines() if l.strip())
   have = collections.Counter()
   for f in sys.argv[1:]:
       have.update(l for l in pathlib.Path(f).read_text(encoding="utf-8").splitlines() if l.strip())
   missing = need - have
   print(f"{sum(need.values())} non-blank lines, {sum(missing.values())} missing")
   for line in missing.elements():
       print("MISSING:", line[:140])
   ' "research/skills/$skill/SKILL.md" research/skills/$skill/references/*.md \
     research/shared/references/review_form_note.md
   ```

   Expected today (all misses are deliberate local edits, listed per skill):
   `deep-research` 562 non-blank lines / 4 missing, `academic-paper` 471 / 5,
   `academic-paper-reviewer` 402 / 3, `academic-pipeline` 561 / 4.
6. Run `python3 scripts/validate.py` (relative links, 500-line warning).

## deep-research

Local-only lines in `SKILL.md`: the description, the attribution block (17), the
adapted routing-discipline note (25: "the upstream repository's
`.claude/CLAUDE.md`", plus the `sr-screener` and `/ars-*` markings, including
`/ars-mark-read`) and the Path note in the Phase-by-phase contract (300).

| # | Heading kept in SKILL.md | Upstream lines (`ebc21bf`) | New file | Summary lines in SKILL.md |
|---|---|---|---|---|
| 1 | Trigger Conditions → Trigger Keywords | 92–98 | `references/skill_overview_details.md` | 94–95 |
| 2 | Three-Way Scan Mode (WHY / HOW / WHAT) | 440–494 | `references/three_way_scan_mode.md` | 355–356 |
| 3 | Handoff Protocol: deep-research → academic-paper | 527–555 | `references/handoff_and_integration.md` | 379–381 |
| 4 | Agent File References | 567–581 | `references/skill_overview_details.md` | 393–394 |
| 5 | Reference Files | 587–620 | `references/skill_overview_details.md` | 400–401 |
| 6 | Templates | 626–633 | `references/skill_overview_details.md` | 407–408 |
| 7 | Examples | 639–648 | `references/skill_overview_details.md` | 414–415 |
| 8 | Integration with Other Skills | 692–701 | `references/handoff_and_integration.md` | 459–460 |
| 9 | Model Tiering (#517, optional) | 707–712 | `references/handoff_and_integration.md` | 466–467 |
| 10 | Version Info | 718–723 | `references/skill_overview_details.md` | 473–474 |
| 11 | Mode Selection Guide: the decision flowchart only (the "See `references/mode_selection_guide.md`" line stays) | 168–187 | `references/workflow_details.md` | 165–166 |
| 12 | Phase-by-phase Invocation Contract (v3.9.2): the body (the local Path note stays) | 375–385 | `references/workflow_details.md` | 297–298 |
| 13 | Failure Paths: "Key failure path summary:" and its table (the pointer to `references/failure_paths.md` stays) | 502–513 | `references/workflow_details.md` | 364–365 |

Pointer stub: `### Review-form note (#921)` at `SKILL.md` 168–171 replaces
upstream 189 (canonical-copy sentence) and 191–249 (marker block). The routing
core is upstream 25–44 → `SKILL.md` 27–46; the boundary section is upstream
70–84 → `SKILL.md` 72–86.

In each reference file the original heading is repeated above its block; Trigger
Keywords also repeats its parent `## Trigger Conditions`.

Step-5 misses (4): the description; the routing-discipline note; the
canonical-copy sentence; the row-12 Mode B routing line ("this file" →
`SKILL.md`).

Summaries to re-check when upstream changes a moved range or the shared block:
- Handoff Protocol: exactly one `preregistration-artifact/1.0` sidecar, created
  or updated only by `build-preregistration-artifact`, carried byte for byte.
- Model Tiering: unset or unknown `ARS_MODEL_TIERING` means every agent inherits
  the session model.
- Reference Files: the IRB decision tree is navigation only, never an authority;
  the authority protocol is fail-closed; full file list.
- Templates: all six template files.
- Three-Way Scan: escalate to `lit-review`; `systematic-review` only on the
  author's choice; method weaknesses are information only.
- Review-form stub: show points (selecting `lit-review`, or confirming the RQ),
  verbatim text, no recommendation, skip conditions, only the author enters
  `systematic-review`.
- Phase-by-phase: Mode B needs an explicit signal; Bucket A write scope.
- Failure Paths: a Devil's Advocate CRITICAL stops the run; Ethics
  confirm-once; Socratic non-generation.

Kept in `SKILL.md` unchanged: frontmatter and attribution block, v2.4
report-compiler notes, the routing core, the boundary section, Quick Start,
Socratic Mode activation, Does NOT Trigger, Quick Mode Selection Guide, Agent
Team, the 6-phase Orchestration Workflow with its Checkpoint Rules (IRON RULES),
the Phase-by-phase Path note, Socratic Mode, Systematic Review Mode, Operational
Modes table, the Failure Paths pointer, Literature Monitoring, Full Academic
Pipeline, Output Language, Anti-Patterns, Quality Standards, Cross-Agent Quality
Alignment and the Version History pointer.

## academic-paper

Local-only lines in `SKILL.md`: the description, the attribution block (18),
the adapted routing-discipline note (26, with the `sr-screener` marking), the
Path note (201), the "(upstream script, not included here: …)" marking
appended to the "Acronym check (#849)" line (240), and the Output Language link
(`../shared/` → `../../shared/`).

| # | Heading (upstream) | Upstream lines (`ebc21bf`) | New file | Summary lines in SKILL.md |
|---|---|---|---|---|
| 1 | `## v3.6.6 Generator-Evaluator Contract Protocol` with its H3s: Overview, Four-call structure, System prompt vs user content discipline, Schema field name vs runtime emission distinction, Phase 4a / 6a output lint, Phase 4b / 6b output lint, Single-agent generator unusable handling, Cross-session resume scope | 230–325 | `references/generator_evaluator_contract_protocol.md` (lines 7–102) | 211–214 |
| 2 | `## Known limitations` | 326–330 | same file (lines 103–107) | 218 |
| 3 | Trigger Conditions → Trigger Keywords | 92–98 | `references/skill_overview_details.md` | 94–95 |
| 4 | Orchestration Workflow → Review-target criteria binding (#684) | 178–200 | `references/review_target_criteria_binding.md` | 175–177 |
| 5 | File Structure | 548–565 | `references/skill_overview_details.md` | 379–380 |
| 6 | Integration with Other Skills | 628–634 | `references/skill_overview_details.md` | 443–444 |
| 7 | Model Tiering (#517, optional) | 640–645 | `references/skill_overview_details.md` | 450–451 |
| 8 | Version Info | 651–656 | `references/skill_overview_details.md` | 457–458 |

Pointer stub: `### Review-form note (#921)` at `SKILL.md` 271–274 replaces
upstream 383 (canonical-copy sentence) and 385–443 (marker block). The routing
core is `SKILL.md` 28–47.

- Rows 1 and 2 moved together, so the cross-references inside the moved text
  (`§ "Phase 4a / 6a output lint" below`, `§ "Known limitations" below`, …)
  still resolve within the reference file.
- Other files cite `academic-paper/SKILL.md § "v3.6.6 Generator-Evaluator
  Contract Protocol"`: `agents/draft_writer_agent.md`,
  `agents/peer_reviewer_agent.md`,
  `academic-paper-reviewer/references/sprint_contract_protocol.md` and
  `shared/contracts/README.md`. The stub keeps that heading and forwards to the
  reference file; if upstream renames it, rename the stub too.

Step-5 misses (5): the description; the routing-discipline note; the Acronym
check line (marking appended); the canonical-copy sentence; the Output Language
line (link fix).

Summaries to re-check when upstream changes a moved range or the shared block:
- Generator-Evaluator stub: `full` mode only; 4a, 4b, 6a and 6b run as separate
  calls; the contract is re-sent each call and no dynamic output goes into the
  system prompt; a lint failure is retried once, then
  `[GENERATOR-PHASE-ABORTED: ...]`; an abort cannot enter Stage 3, only a 6b
  F0/F4/F5 decision can; a round must finish within one session; the #849
  acronym report goes only to the next 4b call, never into 6a/6b.
- Review-target criteria binding: FORMATIVE/INTERNAL receipt ownership;
  validity, venue fit and readiness stay distinct; no invented evidence;
  conformance check only; `criteria_binding_unavailable`.
- Review-form stub: shown when the author selects `lit-review`; verbatim EN or
  zh-TW text; no recommendation; wait for the reply; skip rules;
  `systematic-review` only on the author's explicit choice.
- Model Tiering: unset or unknown means every agent inherits the session model.

Known upstream gaps, left as they are (now in
`references/skill_overview_details.md`): File Structure says "28 files in
references/" and "9 files in examples/" (`commitment_ledger_example.md` is not
listed). `agents/intake_agent.md` cites the stale line `academic-paper/SKILL.md:139`;
the quoted text is still accurate.

## academic-paper-reviewer

First split in upstream sync 2 (merged file 542 → 486 lines). Local-only lines
in `SKILL.md`: the description, the attribution block (17), the adapted
routing-discipline note (26, with the `sr-screener` and `/ars-*` markings), the
"(upstream script, not included here: …)" marking appended to the Acronym check
attachment paragraph (229) and the Path note in the Phase-by-phase contract
(276).

| # | Heading kept in SKILL.md | Upstream lines (`ebc21bf`) | New file | Summary lines in SKILL.md |
|---|---|---|---|---|
| 1 | Trigger Conditions → Trigger Keywords | 86–92 | `references/skill_overview_details.md` | 88–89 |
| 2 | Integration (H3s Upstream/Downstream Relationships, Specific Integration Methods, Pipeline Usage Example) | 376–396 | `references/skill_overview_details.md` | 373–374 |
| 3 | Agent File References | 402–410 | `references/skill_overview_details.md` | 380–381 |
| 4 | Reference Files | 416–430 | `references/skill_overview_details.md` | 387–388 |
| 5 | Templates | 436–440 | `references/skill_overview_details.md` | 394–395 |
| 6 | Examples | 446–449 | `references/skill_overview_details.md` | 401–402 |
| 7 | Version Info | 526–532 | `references/skill_overview_details.md` | 479–480 |

Kept inline (do not move): the routing core (`SKILL.md` 28–47), the boundary
section (from 66), Checkpoint Rules and the IRON RULES,
`### Acronym check attachment (#849)` (227; cited by name by
`references/sprint_contract_protocol.md`, `templates/editorial_decision_template.md`
and `academic-paper/references/writing_quality_check.md`), Re-Review Mode and
the Phase 2.5 list (cited by `academic-pipeline` files), and the Phase-by-phase
contract with its Path note.

Step-5 misses (3): the description; the routing-discipline note; the Acronym
check attachment paragraph (marking appended).

Summaries to re-check: Integration (pipeline position; the immutable
`revision-roadmap/1.0` and `author-adjudication/1.0` requirement; the #684
pointer rule) and Reference Files (all 13 files; the NOT_CALIBRATED note).

## academic-pipeline

Local-only lines in `SKILL.md`: the description, the attribution block (19), a
Path note just above the routing core (25: `sr-screener` and the `/ars-*`
commands marked "not included here", with the fallback signal), the link in the
"#925 (opt-in)" line (`../shared/` → `../../shared/`) and the Path note in the
Phase-by-phase contract (246). The routing-discipline note itself is upstream's.

| # | Heading kept in SKILL.md | Upstream lines (`ebc21bf`) | New file | Summary lines in SKILL.md | Notes |
|---|---|---|---|---|---|
| A1 | Quick Start | 60–87 | `references/entry_and_routing.md` | 64–65 | examples and the `resume_from_passport` contract; link-target edit (see Conventions); the "Execution flow" list stays |
| A2 | Trigger Conditions | 118–140 | `references/entry_and_routing.md` | 96–97 | |
| B1 | Pipeline Stages (10 Stages) | 159–164 | `references/orchestrator_workflow_details.md` | 116–117 | parallelization paragraph only; the stage table stays |
| B2 | Decision Dashboard (shown at FULL checkpoints) | 199–219 | `references/orchestrator_workflow_details.md` | 152–153 | |
| B0 | Orchestrator Workflow → Step 1: INTAKE & DETECTION, Step 2: MODE RECOMMENDATION, Step 3: STAGE EXECUTION | 266–315 | `references/orchestrator_workflow_details.md` | 202, 206, 210–211 | sync 2; the three H3s stay in `SKILL.md` with a one-line summary each; Step 4 TRANSITION stays |
| B5 | Mid-Conversation Reinforcement Protocol | 339–355 | `references/orchestrator_workflow_details.md` | 236–237 | |
| A3a | Phase-by-phase Invocation Contract (v3.9.2) | 361–367 | `references/entry_and_routing.md` | 243–244 | the local Path note (246) stays in `SKILL.md` |
| A3b | Phase-by-phase Invocation Contract, continued | 369–377 | `references/entry_and_routing.md` | — | continues A3a after the Path note; Mode B line edited (see Conventions) |
| C1 | Opt-in Inquiry Branch Ledger (#743 alpha) | 383–405 | `references/advisory_side_channels.md` | 252–253 | |
| C2 | Tortured-phrase advisory (#660) | 424–426 | `references/advisory_side_channels.md` | 272–273 | |
| C3 | Cross-document consistency advisory (#672) | 430–451 | `references/advisory_side_channels.md` | 277–279 | |
| C4 | Cross-run Adjudication Activity (#673; opt-in advisory side channel) | 518–546 | `references/advisory_side_channels.md` | 346–347 | |
| C5 | Collaboration Depth Observer (v3.5.0, advisory only — never blocks) | 570–592 | `references/advisory_side_channels.md` | 371–372 | |
| D1 | Quality Standards | 615–628 | `references/skill_overview_details.md` | 395–396 | |
| D2 | Error Recovery | 634–646 | `references/skill_overview_details.md` | 402–403 | |
| D3 | Agent File References | 652–658 | `references/skill_overview_details.md` | 409–410 | |
| D4 | Reference Files | 664–682 | `references/skill_overview_details.md` | 416–417 | |
| B6 | Integration with Other Skills | 711–738 | `references/orchestrator_workflow_details.md` | 446–448 | |
| B7 | Model Tiering (#517, optional) | 754–759 | `references/orchestrator_workflow_details.md` | 464–465 | |
| D5 | Version Info | 765–771 | `references/skill_overview_details.md` | 471–472 | |

In the reference files, parent headings are repeated where a moved block was a
subsection (for example `## Adaptive Checkpoint System` above `### Decision
Dashboard …`, `## Orchestrator Workflow` above the Step 1–3 blocks and above
`### Mid-Conversation Reinforcement Protocol`, `## Integrity Review Protocol`
above `### Tortured-phrase advisory (#660)`).

B0 was moved in sync 2 instead of the new upstream sections (routing core,
boundary section, #925 flag), which must stay in context; without the move
`SKILL.md` would have been 513 lines.

Step-5 misses (4): the description; the "#925 (opt-in)" line (link fix); the A1
link line; the A3b Mode B routing line.

Summaries to re-check when upstream changes a moved range: the opt-in flags
(`ARS_INQUIRY_LEDGER`, `ARS_MODEL_TIERING`, `ARS_PASSPORT_RESET`,
`ARS_AUDIT_ARTIFACT_GATE`), `resume_from_passport` and Mode A/B routing, the
Step 1–3 summaries (entry-stage map, user-type mode table, dispatch only plus the
MANDATORY checkpoint), the Decision Dashboard summary (word-count ceiling), the
Stage-5 entry advisories (#660 runs before #672 on the same accepted draft; both
advisory only, never a gate), the #673 guarantee (its data never enters the
passport or any gate), the collaboration observer's never-blocks guarantee,
"never skip gates on errors", the Quality Standards summary (continuing past a
non-PASS result at Stage 2.5/4.5 needs an explicit, recorded user decision; user
confirmation after every stage), the Error Recovery summary (every row of the
moved table), the Reference Files summary (includes
`literature_corpus_consumers.md`, `adapters/overview.md`,
`score_trajectory_protocol.md`) and the Integration summary (Stage 2 full mode
stops after Phase 6; Stage 5 asks which files to produce; say so when `tectonic`
is unavailable).

Kept in `SKILL.md` unchanged: frontmatter and attribution block, the
routing-discipline note and routing core, the boundary section, the #925 flag,
Orchestrator Workflow Step 4 TRANSITION with the handoff contents for each
transition (Steps 1–3 summarized), State Machine, checkpoint types, adaptive
rules, checkpoint rules and self-check, the integrity IRON RULES, Two-Stage
Review, Mid-Entry, Revision Loop and its budget, Stage 6, Anti-Patterns,
Templates, Examples, Related Skills and Changelog.

Known upstream gaps, left as they are: the Examples table omits
`examples/integrity_failure_recovery.md`, and the Reference Files index omits
`literature_corpus_consumers.md`, `score_trajectory_protocol.md` and
`adapters/`.
