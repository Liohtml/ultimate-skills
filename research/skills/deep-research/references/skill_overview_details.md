Moved verbatim from SKILL.md sections 'Trigger Keywords', 'Agent File References', 'Reference Files', 'Templates', 'Examples' and 'Version Info' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`, `templates/...`, `examples/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Deep Research — Skill Overview Details

## Trigger Conditions

### Trigger Keywords

**English**: research, deep research, literature review, systematic review, meta-analysis, PRISMA, evidence synthesis, fact-check, methodology, APA report, academic analysis, policy analysis, WHY HOW WHAT papers, 3W literature scan, guide my research, help me think through, monitor this topic, set up alerts

**Español**: investigación profunda, revisión de literatura, revisión sistemática, metaanálisis, síntesis de evidencia, verificación de datos, informe APA, comparación de artículos WHY HOW WHAT, escaneo de tres vías, guía mi investigación, ayúdame a razonar, monitorear este tema, configurar alertas

**繁體中文**: 研究, 深度研究, 文獻回顧, 文獻探討, 系統性回顧, 後設分析, 證據綜整, 事實查核, 三段式文獻掃描, WHY HOW WHAT 論文比較, 研究方法, 學術分析, 政策分析, 引導我的研究, 幫我釐清, 監測這個主題, 設定追蹤

**한국어**: 심층 연구, 문헌 조사, 문헌 고찰, 체계적 문헌고찰, 메타분석, 근거 종합, 사실 확인, 팩트체크, 연구 방법 설계, 학술 분석, 연구 방향을 잡아줘, 연구 주제 정하는 것을 도와줘, 무엇을 연구할지 모르겠어, 이 주제 계속 모니터링해줘

---

## Agent File References

| Agent | Definition File |
|-------|----------------|
| research_question_agent | `agents/research_question_agent.md` |
| research_architect_agent | `agents/research_architect_agent.md` |
| bibliography_agent | `agents/bibliography_agent.md` |
| source_verification_agent | `agents/source_verification_agent.md` |
| synthesis_agent | `agents/synthesis_agent.md` |
| report_compiler_agent | `agents/report_compiler_agent.md` |
| editor_in_chief_agent | `agents/editor_in_chief_agent.md` |
| devils_advocate_agent | `agents/devils_advocate_agent.md` |
| ethics_review_agent | `agents/ethics_review_agent.md` |
| socratic_mentor_agent | `agents/socratic_mentor_agent.md` |
| risk_of_bias_agent | `agents/risk_of_bias_agent.md` |
| meta_analysis_agent | `agents/meta_analysis_agent.md` |
| monitoring_agent | `agents/monitoring_agent.md` |

---

## Reference Files

| Reference | Purpose | Used By |
|-----------|---------|---------|
| `references/apa7_style_guide.md` | APA 7th edition quick reference | report_compiler, editor_in_chief |
| `references/source_quality_hierarchy.md` | Evidence pyramid + grading rubric | source_verification, bibliography |
| `references/methodology_patterns.md` | Research design templates | research_architect |
| `references/logical_fallacies.md` | 30+ fallacies catalog | devils_advocate |
| `references/ethics_checklist.md` | AI disclosure, attribution, dual-use | ethics_review |
| `references/interdisciplinary_bridges.md` | Cross-discipline connection patterns | synthesis, research_architect |
| `references/socratic_questioning_framework.md` | 6 types of Socratic questions + 30+ prompt patterns | socratic_mentor |
| `references/failure_paths.md` | 12 failure scenarios with triggers and recovery paths | all agents |
| `references/mode_selection_guide.md` | Mode selection flowchart and comparison table | orchestrator |
| `references/irb_decision_tree.md` | Portable human-subjects navigation aid; not an authority, universal taxonomy, or pathway determination | ethics_review, research_architect |
| `shared/references/human_subjects_authority_protocol.md` | Exact authority selection, replay validation, actor/consumer filtering, and fail-closed resolved-context gate | ethics_review, research_architect |
| `shared/human_subjects_authority_registry.json` | Bounded jurisdiction profiles with exact requirement IDs, authority anchors, obligated actors, and consumer scopes | ethics_review, research_architect |
| `shared/contracts/human_subjects/resolved_authority_context.schema.json` | Pointer-only resolved-context shape; consumers still require deterministic replay validation | ethics_review, research_architect |
| `shared/references/review_pathway_rule_trace_protocol.md` | Candidate-name ownership, exact selected-profile predicate partition, replay, render, surface lint, and non-consumer boundary (#669) | ethics_review, research_architect |
| `shared/contracts/human_subjects/review_pathway_trace_request.schema.json` | Closed caller-owned candidate mapping; every selected-profile `pathway_trace` requirement is accounted for exactly once | dispatching layer |
| `shared/contracts/human_subjects/review_pathway_rule_trace.schema.json` | Closed candidate-only predicate trace; replay and surface lint remain mandatory | ethics_review, research_architect |
| `shared/references/submission_packet_manifest_protocol.md` | Deterministic packet inventory, authority replay, status, and non-authorization boundary (#667) | ethics_review, research_architect |
| `shared/contracts/human_subjects/submission_packet_manifest.schema.json` | Pointer-only deterministic packet-manifest shape; consumers still require exact replay validation | ethics_review, research_architect |
| `shared/references/authority_content_coverage_advisory_protocol.md` | Replay-bound authority-profile content observations, evidence-row/1.1 provenance, and noninterference boundary (#681) | ethics_review, research_architect |
| `shared/contracts/human_subjects/content_coverage_advisory.schema.json` | Closed `LLM-ADVISORY` carrier; consumers still require finalizer replay validation | ethics_review, research_architect |
| `shared/contracts/evidence/evidence_row_v1_1.schema.json` | Requirement/expectation/artifact-bound bounded excerpt rows for the #681 advisory surface | ethics_review |
| `references/equator_reporting_guidelines.md` | EQUATOR reporting guideline mapping | research_architect, report_compiler |
| `references/preregistration_guide.md` | Preregistration decision tree + platforms + checklist | research_architect |
| `shared/references/cross_document_consistency_advisory_protocol.md` | Exact preregistration sidecar ownership/replay plus #672 advisory and #660 coexistence boundaries | research_architect, academic-paper intake, pipeline orchestrator |
| `shared/contracts/passport/preregistration_artifact.schema.json` | Closed persistent preregistration handoff receipt; companion bytes remain separately named | dispatching layer, intake, pipeline orchestrator |
| `references/systematic_review_toolkit.md` | Cochrane v6.4, PRISMA 2020, RoB 2, ROBINS-I, I² guide, GRADE, protocol registration | risk_of_bias, meta_analysis, bibliography, report_compiler |
| `references/literature_monitoring_strategies.md` | Google Scholar alerts, PubMed alerts, RSS feeds, Retraction Watch, citation tracking, monitoring cadence | monitoring_agent |
| `references/argumentation_reasoning_framework.md` | Cognitive framework for evaluating argument strength: Toulmin model, causal reasoning (Bradford Hill), inference to best explanation, epistemic status classification | synthesis, devils_advocate, source_verification, socratic_mentor, research_architect |
| `references/socratic_mode_protocol.md` | Full 5-layer Socratic dialogue flow, management rules, auto-end conditions | socratic_mentor, research_question |
| `references/systematic_review_protocol.md` | Full PRISMA pipeline, checkpoint rules, meta-analysis procedures | risk_of_bias, meta_analysis, bibliography, report_compiler |
| `references/cross_agent_quality_definitions.md` | Peer-reviewed source tiers, currency standards, severity definitions | all agents |
| `references/changelog.md` | Full version history | — |

---

## Templates

| Template | Purpose |
|----------|---------|
| `templates/research_brief_template.md` | Quick mode output format |
| `templates/literature_matrix_template.md` | Source x Theme analysis matrix |
| `templates/evidence_assessment_template.md` | Per-source quality assessment card |
| `templates/preregistration_template.md` | OSF standard 21-item preregistration template |
| `templates/prisma_protocol_template.md` | PRISMA-P 2015 systematic review protocol template |
| `templates/prisma_report_template.md` | PRISMA 2020 systematic review report template (27 items) |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/exploratory_research.md` | Full 6-phase pipeline walkthrough |
| `examples/systematic_review.md` | PRISMA-style literature review |
| `examples/policy_analysis.md` | Applied comparative policy research |
| `examples/socratic_guided_research.md` | Complete Socratic mode multi-turn dialogue (12 rounds) |
| `examples/handoff_to_paper.md` | deep-research full mode handoff to academic-paper |
| `examples/review_mode.md` | Review mode: 3-agent review pipeline for policy recommendation text |
| `examples/fact_check_mode.md` | Fact-check mode: source verification of HEI claims with per-claim verdicts |
| `examples/idea_diversity_coverage_gap_advisory.md` | #257 Socratic wording-pattern + lit-review distributional-skew advisories |

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 2.12.1 |
| Last Updated | 2026-08-15 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | academic-paper v1.0+ (downstream) |
