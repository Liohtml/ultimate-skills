Moved verbatim from SKILL.md sections 'Pipeline Stages (10 Stages)', 'Decision Dashboard (shown at FULL checkpoints)', 'Orchestrator Workflow' (Steps 1–3), 'Mid-Conversation Reinforcement Protocol', 'Integration with Other Skills' and 'Model Tiering (#517, optional)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Academic Pipeline — Orchestrator Workflow Details

## Pipeline Stages (10 Stages)

**Parallelization opportunity (v3.3)**: Within Stage 2, the `academic-paper` skill's Phase 1 (literature_strategist_agent) and the `visualization_agent` can operate in parallel after Phase 2 (structure_architect_agent) completes the outline. Specifically:
- Once the outline includes a visualization plan, `visualization_agent` can begin figure generation
- Simultaneously, `argument_builder_agent` can build CER chains
- `draft_writer_agent` waits for both to complete before beginning Phase 4

This mirrors PaperOrchestra's parallel execution of Plot Generation (Step 2) and Literature Review (Step 3) after Outline (Step 1), which reduces overall pipeline latency. The parallelization is optional — sequential execution remains the default for simplicity.

## Adaptive Checkpoint System

### Decision Dashboard (shown at FULL checkpoints)

```
━━━ Stage [X] [Name] Complete ━━━

Metrics:
- Word count: [N] (target: [T] +/-10%; ceiling: [C] if set)    [OK/OVER/UNDER — OVER whenever N > C]
- References: [N] (min: [M])              [OK/LOW]
- Coverage: [N]/[T] sections drafted       [COMPLETE/PARTIAL]
- Criterion status: [named criterion + evidence-anchored categorical judgement, or `NOT_COMPARABLE`]

Deliverables:
- [Material 1]
- [Material 2]

Flagged: [any issues detected, or "None"]

Ready to proceed to Stage [Y]? You can also:
1. View progress (say "status")
2. Adjust settings
3. Pause pipeline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Orchestrator Workflow

### Step 1: INTAKE & DETECTION

```
pipeline_orchestrator_agent analyzes the user's input:

1. What materials does the user have?
   - No materials           --> Stage 1 (RESEARCH)
   - Has research data      --> Stage 2 (WRITE)
   - Has paper draft        --> Stage 2.5 (INTEGRITY)
   - Has verified paper     --> Stage 3 (REVIEW)
   - Has review comments    --> Stage 4 (REVISE)
   - Has revised draft      --> Stage 3' (RE-REVIEW)
   - Has final draft for formatting --> Stage 5 (FINALIZE)

2. What is the user's goal?
   - Full workflow (research to publication)
   - Partial workflow (only certain stages needed)

3. Determine entry point, confirm with user
```

### Step 2: MODE RECOMMENDATION

```
Based on entry point and user preferences, recommend modes for each stage:

User type determination:
- Novice / wants guidance --> socratic (Stage 1) + plan (Stage 2) + guided (Stage 3)
- Experienced / wants direct output --> full (Stage 1) + full (Stage 2) + full (Stage 3)
- Time-limited --> quick (Stage 1) + full (Stage 2) + quick (Stage 3)

Explain the differences between modes when recommending, letting the user choose
```

### Step 3: STAGE EXECUTION

```
Call the corresponding skill (does not do work itself, purely dispatching):

1. Inform the user which Stage is about to begin
2. Load the corresponding skill's SKILL.md
3. Launch the skill with the recommended mode
4. Monitor stage completion status

After completion:
1. Compile deliverables list
2. Update pipeline state (call state_tracker_agent)
3. [MANDATORY] Proactively prompt checkpoint, wait for user confirmation
```

### Mid-Conversation Reinforcement Protocol

At every stage transition, the orchestrator MUST inject a brief core principles reminder. This prevents context rot in long conversations.

**Template** (adapt to the upcoming stage):

````
--- STAGE TRANSITION: [Current] → [Next] ---

🔄 Core Principles Reinforcement:
1. [Most relevant IRON RULE for the next stage]
2. [Most relevant Anti-Pattern to avoid in the next stage]
3. Quality check: Is the output of [Current Stage] at least as good as [Previous Stage]? If not, PAUSE.

Checkpoint: [MANDATORY/ADVISORY] — [What user needs to confirm]
---
````

**Stage-specific reinforcement content**: See `references/reinforcement_content.md` for the full transition → reinforcement focus table.

## Integration with Other Skills

```
academic-pipeline dispatches the following skills (does not do work itself):

Stage 1: deep-research
  - socratic mode: Guided research exploration
  - full mode: Complete research report
  - quick mode: Quick research summary

Stage 2: academic-paper
  - plan mode: Socratic chapter-by-chapter guidance
  - full mode: Complete paper writing, stopping after Phase 6 (Phase 7 formatting runs at Stage 5)

Stage 2.5: integrity_verification_agent (Mode 1: pre-review)
Stage 4.5: integrity_verification_agent (Mode 2: final-check)

Stage 3: academic-paper-reviewer
  - full mode: Complete 5-person review (Journal-Fit Reviewer + R1/R2/R3 + Devil's Advocate)

Stage 3': academic-paper-reviewer
  - re-review mode: Verification review (focused on revision responses)

Stage 4/4': academic-paper (revision mode)
Stage 5: academic-paper (format-convert mode)
  - Step 1: Consume the citation-style decision recorded at the Stage 5 entry gate; ask which academic formatting style (APA 7.0 / Chicago / IEEE, etc.) only when no gate decision exists (direct format-convert / mid-entry invocation)
  - Then the Stage 5 output process in `agents/pipeline_orchestrator_agent.md`: MD, only the files the user wants (a DOCX via Pandoc when available; a PDF compiled from LaTeX generated from the MD, using the corresponding document class, e.g., apa7 for APA 7.0; the .tex source only when asked for), content confirmation, PDF; if tectonic is unavailable, say so instead of substituting another route
  - Fonts: Times New Roman (English) + Source Han Serif TC VF (Chinese) + Courier New (monospace)
  - ⚠️ IRON RULE: PDF must be compiled from LaTeX (HTML-to-PDF is prohibited)
```

## Model Tiering (#517, optional)

When `ARS_MODEL_TIERING` is set, the dispatching session routes this skill's agents per `shared/model_tiering.md` (canonical: the full 43-agent judgment/execution table + rules). Compact rule:

- **Unset (default):** every agent inherits the session model — byte-equivalent pre-#517 behavior.
- **`economy`** (frontier-tier session): execution-type agents dispatch ONE tier below the session model — floor Opus-class, never lower; judgment-type agents stay on the session model. No-op at or below the floor (announce once).
- **`quality-boost`** (below-frontier session): judgment-type agents at the checkpoint surfaces (Stage 2.5/4.5 gates; the opt-in Stage 4→5 claim–ref audit; final review) jump UP to the frontier tier (however many tiers away — not a single increment); nothing is ever downgraded. No-op at the frontier (announce once).
- Unknown values → warn once, behave as unset. Tiers are relative positions, never hard-pinned model ids. When a direction is active, route repeated same-stage calls to the SAME worker so its prompt cache accumulates, where the protocol permits (never merging seats that must stay blind; `shared/model_tiering.md`); unset means dispatch shapes stay byte-equivalent too.
