Moved verbatim from SKILL.md section 'Review-target criteria binding (#684)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory.

# Academic Paper — Review-Target Criteria Binding (#684)

## Orchestration Workflow (8 Phases)

### Review-target criteria binding (#684)

When Phase 0 has produced an author-confirmed `ReviewTargetContext` (#683), the
orchestrator initializes one pointer-only `ReviewCriteriaBindingManifest` and
uses it unchanged across the formative, internal-evaluator, and external-panel
consumers. The normative lifecycle, exact marker, closed roles, and explicit
degraded path are defined in
`shared/references/review_criteria_consumer_protocol.md`.

- Phase 2 owns the `FORMATIVE` receipt. The Structure Architect maps selected
  criterion ids to planned sections and evidence needs; later writing phases
  reuse that receipt and do not re-resolve the target.
- Phase 6a receives the same pointer authority and Target Criteria Brief while
  remaining paper-blind; its pre-commitment artifact owns the `INTERNAL`
  receipt. Phase 6b receives that unchanged artifact, may assess applicability
  after it sees the draft, and owns any Critical/Major constructive finding
  sidecar.
- Scientific validity, venue fit, and submission readiness remain distinct.
  Criteria never authorize invented evidence, results, methods, or changes to
  the author's contribution claim.

Binding validation is a handoff-conformance check only. It never supplies an
editorial verdict, severity, checkpoint state, or author triage. If the binding
is unavailable, disclose `criteria_binding_unavailable`; do not claim venue
alignment and do not silently reconstruct a target from model memory.
