Moved verbatim from SKILL.md sections 'Opt-in Inquiry Branch Ledger (#743 alpha)', 'Tortured-phrase advisory (#660)', 'Cross-document consistency advisory (#672)', 'Cross-run Adjudication Activity (#673; opt-in advisory side channel)' and 'Collaboration Depth Observer (v3.5.0, advisory only — never blocks)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Academic Pipeline — Advisory and Opt-in Side Channels

## Opt-in Inquiry Branch Ledger (#743 alpha)

`ARS_INQUIRY_LEDGER=1` enables the bounded
`inquiry-branch-ledger/1.0` memory surface. Unset or `0` emits no ledger
artifact, pointer, prompt, or summary. Even when enabled, one linear branch
does not materialize a ledger; the second recorded branch is the first lawful
publication point.

The orchestrator owns the interaction surface and the deterministic runtime
`scripts/inquiry_branch_ledger.py` owns validation, replay, append,
profile-budget checks, pointer binding, and crash recovery. Replay receives the
exact profile file for every ledger binding; it never substitutes a current
fallback for missing historical bytes. AI facets enter `parked` and can become
author-owned only through an explicit origin-bound adoption receipt. Reopening
marks only author-recorded first-degree artifacts stale and never rewrites
them.

Render the runtime's compact summary only at the Stage 1 design-freeze
checkpoint, the Stage 2.5 and 4.5 MANDATORY checkpoints, or immediately after
a recorded reopen-condition signal. With the flag off or at most one branch,
omit the block completely. Every shown interaction offers `skip`, `off`, and
reset-to-simple-path; these hide future surfaces without deleting the ledger.
The summary is advisory state memory and never changes an integrity verdict or
checkpoint requirement. Full protocol and crash semantics:
`docs/design/2026-08-17-743-inquiry-branch-ledger-design.md`.

## Integrity Review Protocol

### Tortured-phrase advisory (#660)

After the exact Stage 4.5 pass and immediately before Stage 5 formatting, the orchestrator runs the deterministic #660 checker over the exact accepted working draft using an explicit user-supplied or synthetic-fixture snapshot and detached manifest bound to the raw snapshot SHA-256; omitted supply produces an explicit `not_checked` artifact. The path ships no native PPS content/importer/fetcher or redistributed phrase list and uses no live model, external API, human or model judge, or ambient clock; timestamps are explicit inputs. Its own-draft result is `HEURISTIC-ADVISORY` / `UNMEASURED`, never changes the Stage 4.5 PASS or Stage 5 gate, never rewrites prose, and must be re-run only after a revision has re-entered the existing integrity/screen sequence.

For the literature corpus, a non-in-place producer emits one current v1.2 advisory row per `cited_title` and `cited_abstract`; a missing abstract remains explicitly `not_checked` / `unresolved` with `ABSTRACT_MISSING`. Downstream consumers are read-only and compose every row into the one existing `Bibliographic Integrity Advisories` section. The advisory mints no marker, triggers no terminal policy, gate, finalizer promotion, ranking, citation rewrite, or replacement text, and supports no clean-draft, origin, papermill, contextual-validity, publisher-acceptance, or matcher-accuracy claim.

### Cross-document consistency advisory (#672)

The Stage-1 shell-capable dispatcher is the only consumer that may invoke
`scripts/build_cross_document_consistency_advisory.py
build-preregistration-artifact`. The non-shell research architect supplies only
the caller declaration and named companion handle. The resulting exact sidecar
and provided companion are replay-validated and carried byte-for-byte through
every handoff. Omission, silent substitution, template replacement, or digest
repair is invalid.

After the same exact Stage 4.5 PASS, the single mandatory Stage-5 entry
checkpoint runs #660 first and #672 second. Both bind the identical accepted
draft; #660 `input_binding.artifact.artifact_id/artifact_sha256` must equal #672
`input_binding.accepted_draft_artifact_id/accepted_draft_sha256`. They remain
separate carriers with separate failure semantics: preserve a schema-valid #660
degraded artifact on exit 1; a #672 contract/runtime failure writes no artifact
and records only bounded `ADVISORY_UNAVAILABLE:<CODE>`.

#672 is always `LLM-ADVISORY` / `UNMEASURED`. It has no score, pass/fail, gate,
readiness, authorization, ClaimIntent, rewrite, consent/protocol duplicate, or
clean/agreement meaning. It cannot change Stage 4.5, block or delay the existing
checkpoint, or alter Stage-5 routing after user confirmation. A manuscript
revision stales both advisories and must re-enter integrity before #660 and #672
rerun, in that order, against the new accepted bytes.

## Cross-run Adjudication Activity (#673; opt-in advisory side channel)

The state tracker section "Adjudication-activity metadata" is the single
producer/state authority. Each run receives one stable explicit `run_id`.
Structured handlers first durably apply their existing author-choice,
compliance-override, explicit-request, or MANDATORY-checkpoint routing/state
effect and only then best-effort append a data-minimized binding to the
five-row `pending_adjudication_activity_bindings[]` inventory. A refused
MANDATORY skip leaves state unchanged before the optional receipt stores
`skip_refused`. Author groups use `artifact_group_stage` and may preserve both
Stage 3 and Stage 3-prime; receipt stages use the complete Stage 1-through-6
closed enum, with no Stage 0. Compliance permits a plain report-only
captured-zero group and requires the paired action receipt only for a fully
qualifying override.

Terminal behavior is unchanged and runs first. After the completed/aborted
state is durable, and only for a user-selected local store, the orchestrator
passes explicit state/artifact-root paths and the explicit pending five rows to
`seal_terminal_inventory(state_path, artifact_root, pending_bindings)`, then
best-effort runs sealed-inventory `build-input`, idempotent `append-run`, and
optional `render`. The helper computes hashes; it does not read pending state,
accept caller hashes, infer sources, or scan. Root `run_id` plus sealed root
`adjudication_activity_sources` are exact authority. Any activity failure is an
advisory diagnostic and cannot affect the already-durable terminal outcome.

Activity data never enters a Material Passport, handoff, Process Record,
reviewer/model/observer/compliance input, gate, verdict, checkpoint input, or
stage transition. No live model, judge, eval, network/API, ambient clock,
directory scan, or glob participates. Full details and frozen receipt schemas
remain in `docs/design/2026-08-10-673-cross-run-adjudication-activity-spec.md`
and `shared/contracts/activity/`.

## Collaboration Depth Observer (v3.5.0, advisory only — never blocks)

The `collaboration_depth_agent` observes the user's collaboration pattern with the pipeline. It is **advisory only** and **never blocks** progression at any checkpoint. It is `non-blocking` by design and carries `blocking: false` in its frontmatter as a structural guarantee.

**When invoked**: every FULL checkpoint, every SLIM checkpoint, and during Stage 6 record compilation (the whole-pipeline pass runs before the Process Record is generated and delivered, so its output can be a chapter of the record the user acknowledges). MANDATORY checkpoints (Stages 2.5 / 4.5 integrity gates) **do not** invoke the observer — those are integrity concerns and must not be diluted.

**What it does**: reads the dialogue range for the just-completed stage (at checkpoints) or the whole pipeline (during Stage 6 record compilation), scores the pattern against the canonical rubric at `shared/collaboration_depth_rubric.md`, and emits an advisory block/chapter. Dimensions: Delegation Intensity, Cognitive Vigilance, Cognitive Reallocation, Zone Classification (Zone 1 / Zone 2 / Zone 3). Rubric is based on Wang & Zhang (2026) IJETHE 23:11 (DOI 10.1186/s41239-026-00585-x).

**Distinction from existing mechanisms**:

| Mechanism | What it evaluates | Blocking? |
|---|---|---|
| `integrity_verification_agent` (Stages 2.5 / 4.5) | Paper content — references, citations, data | Yes (blocking gate) |
| Stage 6 Collaboration Quality Evaluation (6 dims, 1–100) | The user's collaboration as the AI assessed it (the AI Self-Reflection Report covers the AI's own behaviour) | No, but produced once only |
| `collaboration_depth_agent` (this observer) | The **user's** collaboration pattern (delegation intensity, vigilance, reallocation) | **No — never blocks. Advisory only.** |

**Non-blocking guarantees**:
- Observer output never appears on the "Flagged" line of any checkpoint.
- The `Ready to proceed?` prompt is unchanged by observer output.
- `blocked_by: collaboration_depth_agent` is never a legal state in `state_tracker`.
- If observer frontmatter ever asserts `blocking: true`, the orchestrator must refuse to dispatch it.

**Cross-model**: when `ARS_CROSS_MODEL` is set, the observer runs on both models and flags any dimension divergence > 2 points. Scores are never silently averaged across models.

> See `agents/collaboration_depth_agent.md` for full scoring procedure and anti-sycophancy discipline; `shared/collaboration_depth_rubric.md` for the canonical 4-dimension rubric.
