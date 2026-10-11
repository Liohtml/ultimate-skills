Moved verbatim from SKILL.md sections 'Quick Start', 'Trigger Conditions' and 'Phase-by-phase Invocation Contract (v3.9.2)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Academic Pipeline — Entry and Routing Details

## Quick Start

**Full workflow (from scratch):**
```
I want to write a research paper on the impact of AI on higher education quality assurance
```
--> academic-pipeline launches, starting from Stage 1 (RESEARCH)

**Mid-entry (existing paper):**
```
I already have a paper, help me review it
```
--> academic-pipeline detects mid-entry, starting from Stage 2.5 (INTEGRITY)

**Revision mode (received reviewer feedback):**
```
I received reviewer comments, help me revise
```
--> academic-pipeline detects, starting from Stage 4 (REVISE)

**Resume from passport (cross-session context reset, opt-in):**
```
resume_from_passport=<hash> [stage=<n>] [mode=<m>]
```
--> Loads the Material Passport (Schema 9), locates the `kind: boundary` entry matching `<hash>`, and confirms it has no later `kind: resume` entry consuming it. If `pending_decision` is set, the decision prompt fires first to capture the user's branch choice for the audit ledger; the prompt is never skipped, even when the user supplies `stage=`. After the prompt (or immediately if no `pending_decision`), the next stage is determined by: (a) `stage=<n>` CLI override if provided, else (b) the matched option's `next_stage`, else (c) the `next` field recorded in the boundary entry. CLI `stage=`/`mode=` overrides win over option routing.
- **Gate (emit)**: `ARS_PASSPORT_RESET=1` must be set in the emitting session. Without the flag, no `kind: boundary` entries are written and there is nothing to resume from.
- **Gate (resume)**: No flag required. Any session can invoke `resume_from_passport=<hash>` against a passport that carries a valid boundary entry matching the hash.
- **Intent**: Invoke in a *fresh* Claude Code session. Resuming within the same session that emitted the boundary provides no token savings and may drop still-live in-session context.
- **Stage**: Any. Resumes at whatever stage the routing rules above determine.
- **Reference**: [`references/passport_as_reset_boundary.md`](passport_as_reset_boundary.md) — see §"`resume_from_passport` mode contract".

## Trigger Conditions

### Trigger Keywords

**English**: academic pipeline, research to paper, full paper workflow, paper pipeline, end-to-end paper, research-to-publication, complete paper workflow

**Español**: flujo de trabajo académico, investigación a artículo, pipeline de artículo completo, desde tema de investigación hasta artículo terminado, flujo completo de investigación-publicación

**한국어**: 학술 파이프라인, 연구부터 논문까지, 논문 전체 워크플로, 연구 주제 설정부터 논문 완성까지, 연구-논문 전 과정

### Non-Trigger Scenarios

| Scenario | Skill to Use |
|----------|-------------|
| Only need to search materials or do a literature review | `deep-research` |
| Only need to write a paper (no research phase needed) | `academic-paper` |
| Only need to review a paper | `academic-paper-reviewer` |
| Only need to check citation format | `academic-paper` (citation-check mode) |
| Only need to convert paper format | `academic-paper` (format-convert mode) |

### Trigger Exclusions

- If the user only needs a single function (just search materials, just check citations), no pipeline is needed — directly trigger the corresponding skill
- If the user is already using a specific mode of a skill, respect that entry point; the pipeline is opt-in
- The pipeline is optional, not mandatory

## Phase-by-phase Invocation Contract (v3.9.2)

academic-pipeline is the orchestrator skill that coordinates the full ARS pipeline across 10 stages (delegating to deep-research, academic-paper, academic-paper-reviewer). Two invocation modes:

**Mode A — orchestrator-driven (default):** `pipeline_orchestrator_agent` runs all stages end-to-end with state tracking via Material Passport. `state_tracker_agent`, `integrity_verification_agent`, `collaboration_depth_agent`, and `claim_ref_alignment_audit_agent` are dispatched by the orchestrator at the appropriate checkpoints.

**Mode B — phase-by-phase (cross-session resume):** User invokes one phase agent at a time across sessions, typically via `ARS_PASSPORT_RESET=1` + `resume_from_passport=<hash>` (see `references/passport_as_reset_boundary.md`).

In Mode B, **single-phase agents (Bucket A per `docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md`) in the downstream skills (deep-research, academic-paper, academic-paper-reviewer) stay strictly within their assigned phase for writes**. The 5 agents in academic-pipeline itself are all cross-phase / meta by design (Bucket C/D) — they have no fence by design:

- `pipeline_orchestrator_agent` (D — orchestrator, full pipeline visibility)
- `state_tracker_agent` (D — meta state, all phases)
- `integrity_verification_agent` (C — Stage 2.5 / 4.5 cross-skill gate)
- `collaboration_depth_agent` (C — FULL/SLIM checkpoints + Stage 6 record compilation, advisory-only)
- `claim_ref_alignment_audit_agent` (C — opt-in claim audit, phase-orthogonal)

Routing into Mode B requires explicit user signal — `/ars-<mode>` slash command or `[direct-mode]` prefix. Ambiguous cross-phase input defaults to clarification per the routing core near the top of `SKILL.md` (Step 2) + `shared/references/intent_clarification_protocol.md`. **Critically:** if `pipeline_orchestrator_agent` is dispatched on ambiguous cross-phase materials, the orchestrator itself currently cannot reconcile (this is the v3.10 conductor #134 work) — v3.9.2 routes such cases to clarification BEFORE the orchestrator runs.

**Enforcement (v3.9.2):** Phase Boundary blocks on downstream Bucket A agents + advisory verifier (`scripts/check_pipeline_integrity.py`) + a deterministic PreToolUse write-scope guard in hook-enabled runtimes (#134 rescope, PR #294). Multi-phase envelope + orchestrator structured intake remain forward-scope (#134 Slices 3-5).
