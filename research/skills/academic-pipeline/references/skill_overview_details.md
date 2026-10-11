Moved verbatim from SKILL.md sections 'Quality Standards', 'Error Recovery', 'Agent File References', 'Reference Files' and 'Version Info' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Academic Pipeline — Skill Overview Details

## Quality Standards

| Dimension | Requirement |
|-----------|------------|
| Stage detection | Correctly identify user's current stage and available materials |
| Mode recommendation | Recommend appropriate mode based on user preferences and material status |
| Material handoff | Stage-to-stage handoff materials are complete and correctly formatted |
| State tracking | Pipeline state updated in real time; Progress Dashboard accurate |
| **Mandatory checkpoint** | **User confirmation required after each stage completion** |
| **Mandatory integrity check** | **Stage 2.5 and 4.5 always run; continuation past a non-PASS result requires an explicit, recorded user decision** |
| **Mandatory failure mode checklist** (v3.2) | **Stage 2.5 and 4.5 must run the 7-mode AI research failure checklist; suspected failures block; overrides require user reasoning** |
| No overstepping | ⚠️ IRON RULE: Orchestrator does not perform substantive research/writing/reviewing, only dispatching |
| No forcing | ⚠️ IRON RULE: User can pause or exit pipeline at any time (but cannot skip integrity checks) |
| Auditable workflow | Same declared contract and deterministic validators can be replayed; model/configuration and stochastic outputs remain visible rather than promised identical |
| **Convergence-aware stopping** | **Suggest stopping only when no P0, unresolved decision-bearing regression, substantive criterion-status change, or outstanding required action remains; user can override** |
| **Budget transparency** (v3.2; #388) | **Token cost estimate + interaction-count budget (round-trip caps + accumulated count at checkpoints, advisory) + user confirmation at pipeline start** |

## Error Recovery

| Stage | Error | Handling |
|-------|-------|---------|
| Intake | Cannot determine entry point | Ask user what materials they have and their goal |
| Stage 1 | deep-research not converging | Suggest mode switch (socratic -> full) or narrow scope |
| Stage 2 | Missing research foundation | Suggest returning to Stage 1 to supplement research |
| Stage 2.5 | Still FAIL after 3 correction rounds | List unverifiable items; user decides whether to continue |
| Stage 3 | Review result is Reject | Provide options: major restructuring (Stage 2) or abandon |
| Stage 4 | Revision incomplete on all items | List unaddressed items; ask whether to continue |
| Stage 3' | Verification still has major issues | Enter Stage 4' for final revision |
| Stage 4' | Issues remain after revision | Mark as Acknowledged Limitations; proceed to Stage 4.5 |
| Stage 4.5 | Final verification FAIL | Fix and re-verify (max 3 rounds) |
| Any | User leaves midway | Save pipeline state; can resume from breakpoint next time |
| Any | Skill execution failure | Report error; suggest retry, pause, or mode switch. Do not skip mandatory integrity or failure-mode gates |

## Agent File References

| Agent | Definition File |
|-------|----------------|
| pipeline_orchestrator_agent | `agents/pipeline_orchestrator_agent.md` |
| state_tracker_agent | `agents/state_tracker_agent.md` |
| integrity_verification_agent | `agents/integrity_verification_agent.md` |
| collaboration_depth_agent | `agents/collaboration_depth_agent.md` |
| claim_ref_alignment_audit_agent | `agents/claim_ref_alignment_audit_agent.md` |

## Reference Files

| Reference | Purpose |
|-----------|---------|
| `references/pipeline_state_machine.md` | Complete state machine definition: all legal transitions, preconditions, actions |
| `references/plagiarism_detection_protocol.md` | Phase D originality verification protocol + self-plagiarism + AI text characteristics |
| `references/mode_advisor.md` | Unified cross-skill decision tree: maps user intent to optimal skill + mode |
| `references/claim_verification_protocol.md` | Phase E claim verification protocol: claim extraction, source tracing, cross-referencing, verdict taxonomy |
| `references/claim_audit_calibration_protocol.md` | v3.8 #103 claim_ref_alignment audit calibration: gold-set shape (T-C3), threshold gates FNR<0.15 / FPR<0.10 (T-C1), per-class FNR/FPR reporting (T-C2). Re-run via `PYTHONPATH=. python3 -m unittest scripts.test_claim_audit_calibration -v`. |
| `references/ai_research_failure_modes.md` | 7-mode AI research failure checklist (Lu 2026), run at Stage 2.5 + 4.5 with blocking behaviour, reported at Stage 6 |
| `references/team_collaboration_protocol.md` | Multi-person team coordination: role definitions, handoff protocol, version control, conflict resolution |
| `references/integrity_review_protocol.md` | Stage 2.5 + 4.5 integrity verification: 5-phase protocol details |
| `references/two_stage_review_protocol.md` | Two-stage review: Stage 3 full review + Stage 3' verification review |
| `references/external_review_protocol.md` | External (human) reviewer feedback: 4-step intake/coaching/revision/verification |
| `references/process_summary_protocol.md` | Stage 6: collaboration quality evaluation + AI self-reflection report |
| `references/reproducibility_audit.md` | Standardized workflow contract, deterministic replay boundary, and audit trail format |
| `references/progress_dashboard_template.md` | ASCII progress dashboard template |
| `references/reinforcement_content.md` | Stage-specific reinforcement focus table for transitions |
| `references/changelog.md` | Full version history |
| `shared/handoff_schemas.md` | Cross-skill data contracts: 9 schemas for all inter-stage handoff artifacts |
| `shared/collaboration_depth_rubric.md` | Collaboration Depth Observer rubric (v1.0): 4 dimensions based on Wang & Zhang (2026) IJETHE 23:11 |

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 3.22.1 |
| Last Updated | 2026-09-23 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | deep-research v2.0+, academic-paper v2.0+, academic-paper-reviewer v1.1+ |
| Role | Full academic research workflow orchestrator |
