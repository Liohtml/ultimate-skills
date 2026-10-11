Moved verbatim from SKILL.md sections 'Trigger Keywords', 'Integration', 'Agent File References', 'Reference Files', 'Templates', 'Examples' and 'Version Info' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`, `templates/...`, `examples/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Academic Paper Reviewer — Skill Overview Details

## Trigger Conditions

### Trigger Keywords

**English**: review paper, peer review, manuscript review, referee report, review my paper, critique paper, simulate review, editorial review, calibrate reviewer, reviewer calibration, measure reviewer accuracy

**Español**: revisar artículo, revisión entre pares, revisión de manuscrito, informe de árbitro, revisión simulada, evaluar desde perspectiva de revisor, calibración de revisor, medir precisión del revisor

**한국어**: 논문 심사, 동료 심사, 모의 심사, 원고 심사, 심사 보고서, 심사자 관점에서 평가, 심사자 보정, 심사 정확도 측정

**繁體中文**: 審查論文, 論文審查, 模擬審查, 同儕審查, 幫我審這篇, 以審查人角度評估, 審查者校準

---

## Integration

### Upstream/Downstream Relationships

```
deep-research --> academic-paper --> [integrity check] --> academic-paper-reviewer --> academic-paper (revision) --> academic-paper-reviewer (re-review) --> [final integrity] --> finalize
   (research)       (writing)         (integrity audit)      (review)                    (revision)                    (verification review)                (final verification)   (finalization)
```

### Specific Integration Methods

| Integration Direction | Description |
|----------------------|-------------|
| **Upstream: academic-paper -> reviewer** | Receives the complete paper output from `academic-paper` full mode, directly enters Phase 0 |
| **Upstream: integrity check -> reviewer** | In the Pipeline, the paper must pass integrity check before entering reviewer |
| **Downstream: reviewer -> academic-paper** | `revision-roadmap/1.0` remains immutable; revision mode additionally requires the exact claim-surface manifest and complete explicit `author-adjudication/1.0` sidecar |
| **Downstream: reviewer (re-review) -> integrity** | After re-review completes, proceeds to final integrity verification |

The upstream handoff also carries the exact #684 context/manifest/brief when a
criteria-aware target review is active. Re-review preserves that authority by
pointer; a changed target starts a new, explicitly non-comparable review id.

### Pipeline Usage Example

> See `references/integration_guide.md` for a complete 9-step pipeline usage example.

---

## Agent File References

| Agent | Definition File |
|-------|----------------|
| field_analyst_agent | `agents/field_analyst_agent.md` |
| eic_agent | `agents/eic_agent.md` |
| methodology_reviewer_agent | `agents/methodology_reviewer_agent.md` |
| domain_reviewer_agent | `agents/domain_reviewer_agent.md` |
| perspective_reviewer_agent | `agents/perspective_reviewer_agent.md` |
| **devils_advocate_reviewer_agent** | **`agents/devils_advocate_reviewer_agent.md`** |
| editorial_synthesizer_agent | `agents/editorial_synthesizer_agent.md` |

---

## Reference Files

| Reference | Purpose | Used By |
|-----------|---------|---------|
| `references/review_criteria_framework.md` | Structured review criteria framework (differentiated by paper type) | all reviewers |
| `references/top_journals_by_field.md` | Top journal lists for major academic fields (Journal-Fit Reviewer role calibration) | field_analyst, eic |
| `references/editorial_decision_standards.md` | Accept/Minor/Major/Reject criteria and decision matrix | eic, editorial_synthesizer |
| `references/statistical_reporting_standards.md` | Statistical reporting standards + APA 7.0 format quick reference + red flag list | methodology_reviewer |
| `references/quality_rubrics.md` | Criterion-bound narrative judgement for 7 review dimensions; every current live seat and Schema 6 package remains `NOT_CALIBRATED` because candidate-profile application is not wired | all reviewers |
| `references/review_quality_thinking.md` | Cognitive framework for review quality: three lenses (internal validity, external validity, contribution), common reviewer traps, calibration questions | all reviewers |
| `references/re_review_mode_protocol.md` | Full re-review verification logic (three-gate contract), R&R traceability output format, Socratic guidance after re-review | orchestrating layer; routed-seat Phase 1/2A calls; Phase 2B integration call |
| `references/guided_mode_protocol.md` | Guided mode dialogue flow, progressive revelation sequence, dialogue rules | all reviewers |
| `references/calibration_mode_protocol.md` | Calibration mode: explicit 3-paper directional tier plus the default 5-20-paper full measurement tier, Minor/Major boundary matrix, and tier-scoped session disclosure | all reviewers |
| `references/review_panel_provenance_protocol.md` | Closed six-axis execution-provenance semantics, correlated-error disclosure, and deterministic build/replay rules; no binary independence reduction | dispatcher, editorial_synthesizer, re-review consumer |
| `references/reviewer_sprint_prompt_source.md` | Canonical marked source for the five inline sprint-reviewer Phase 1/2 prompt fragments and the synthesizer protocol; runtime mirrors stay inline for bare dispatch and are exact-sync linted | five panel reviewers, editorial_synthesizer |
| `references/integration_guide.md` | Complete 9-step pipeline usage example | — |
| `references/changelog.md` | Full version history | — |

---

## Templates

| Template | Purpose |
|----------|---------|
| `templates/peer_review_report_template.md` | Review report template used by each reviewer |
| `templates/editorial_decision_template.md` | Editorial Decision Letter template (produced by `editorial_synthesizer_agent` in Phase 2 — not by the Journal-Fit Reviewer, #574 C2) |
| `templates/revision_response_template.md` | Revision response template for authors (R->A->C format) |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/hei_paper_review_example.md` | Full review example: "Impact of Declining Birth Rates on Management Strategies of Taiwan's Private Universities" |
| `examples/interdisciplinary_review_example.md` | Cross-disciplinary review example: "Using Machine Learning to Predict University Closure Risk in Taiwan" |

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 1.11.1 |
| Last Updated | 2026-08-15 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | academic-paper v1.0+ (upstream/downstream integration) |
| Role | Multi-perspective academic paper review simulator |
