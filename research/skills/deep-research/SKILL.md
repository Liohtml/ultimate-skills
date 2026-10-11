---
name: deep-research
description: "Multi-agent (13-agent) research team for rigorous, source-verified research on any topic, with 8 modes: full research report, quick brief, review of a provided text, lit-review, fact-check, three-way (WHY/HOW/WHAT) literature scan, Socratic guided research dialogue, and systematic review with optional PRISMA meta-analysis. Covers question formulation, methodology, source verification, synthesis, risk of bias, APA 7.0 reports and ethics review. Use for deep research, evidence synthesis or fact-checking. For writing the paper itself use academic-paper; for peer-reviewing a manuscript use academic-paper-reviewer; for research-to-publication in one run use academic-pipeline; for market or competitor research use competitor-analysis. Triggers: deep research, literature review, systematic review, meta-analysis, PRISMA, fact-check, guide my research, 深度研究, 文獻回顧, 系統性回顧, 後設分析, 事實查核, 引導我的研究, 심층 연구, 문헌 조사, 체계적 문헌고찰, 메타분석, revisión de literatura, metaanálisis."
metadata:
  version: "2.12.1"
  last_updated: "2026-08-15"
  status: active
  data_access_level: raw
  task_type: open-ended
  related_skills:
    - academic-paper
    - academic-pipeline
---

# Deep Research — Universal Academic Research Agent Team

> Adapted from [Imbad0202/academic-research-skills `deep-research`](https://github.com/Imbad0202/academic-research-skills/tree/95929c00fc066730b40cf268fd1250b04f00356a/deep-research) (© 2026 Cheng-I Wu), licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — see `../../LICENSE`. **Modified by ultimate-skills:** description rewritten, `shared/` paths pointed at the vendored `../../shared/`, upstream-only scripts and docs marked as optional links (details in the [marketplace CHANGELOG](https://github.com/Liohtml/ultimate-skills/blob/main/CHANGELOG.md)). Non-commercial use only.

Universal deep research tool — a domain-agnostic 13-agent team for rigorous academic research on any topic.

**v2.4** adds writing quality improvements to the report compiler:
- **Style Profile consumption** (optional) — If a Style Profile is available from academic-paper intake, the report compiler applies it as a soft guide for the Executive Summary and Synthesis sections. Discipline conventions and report objectivity take priority.
- **Writing Quality Check** — The report compiler uses `academic-paper/references/writing_quality_check.md` as a diagnostic guide before finalizing (prompts for judgment subordinate to author and venue requirements, not quotas), and flags claims the cited sources do not support as `[MATERIAL GAP]` rather than hedging them (#825).

> **Routing discipline (v3.9.2):** this skill assumes cross-skill routing has already settled — ambiguous cross-phase materials should have been clarified upstream.

## Quick Start

**Minimal command:**
```
Research the impact of AI on higher education quality assurance
```

**Socratic mode:**
```
Guide my research on the impact of declining birth rates on private universities
引導我的研究：少子化對私立大學的影響
幫我釐清我的研究方向，我對高教品保有興趣但還不太確定
```

**Execution:**
1. Scoping — Research question + methodology blueprint
2. Investigation — Systematic literature search + source verification
3. Analysis — Cross-source synthesis + bias check
4. Composition — Full APA 7.0 report
5. Review — Editorial + ethics + vulnerability scan
6. Revision — Final polished report

---

## Trigger Conditions

### Trigger Keywords

Multilingual trigger keyword lists (English, Spanish, Traditional Chinese, Korean) for research, literature/systematic review, meta-analysis, PRISMA, evidence synthesis, fact-check, APA report, WHY/HOW/WHAT (3W) scan, guided research and topic monitoring/alerts.
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when deciding whether a request in one of these languages should trigger this skill.

### Socratic Mode Activation

Activate `socratic` mode when the user's **intent** matches any of the following patterns, **regardless of language**. Detect meaning, not exact keywords.

**Intent signals** (any one is sufficient):
1. User has no clear research question and wants guided thinking
2. User asks to be "led", "guided", or "mentored" through research
3. User expresses uncertainty about what to research or where to start
4. User wants to brainstorm, explore, or clarify a research direction
5. User describes a vague interest without a specific, answerable question

**Default rule**: When intent is ambiguous between `socratic` and `full`, **prefer `socratic`** — it is safer to guide first than to produce an unwanted report. The user can always switch to `full` later.

**Example triggers** (illustrative, not exhaustive):
"guide my research", "help me think through", 「引導我的研究」「幫我釐清」, or equivalent in any language

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Writing a paper (not researching) | `academic-paper` |
| Reviewing a paper (structured review) | `academic-paper-reviewer` |
| Full research-to-paper pipeline | `academic-pipeline` |

### Quick Mode Selection Guide

| Your Situation 你的狀況 | Recommended Mode | Spectrum |
|----------------|-----------------|----------|
| Vague idea, need guidance / 有模糊想法，需要引導 | `socratic` | originality |
| Clear RQ, need comprehensive research / 有明確 RQ，需要完整研究 | `full` | balanced |
| Need a quick brief (30 min) / 需要快速摘要 | `quick` | fidelity |
| Have a paper to evaluate before citing / 有論文需要評估 | `review` | balanced |
| Need literature review for a topic / 需要文獻回顧 | `lit-review` | fidelity |
| Need a fast paper-comparison scan / 需要快速比較多篇論文 | `three-way-scan` | fidelity |
| Need to verify specific claims / 需要查核特定事實 | `fact-check` | fidelity |
| Need systematic review / meta-analysis / 系統性回顧或後設分析 | `systematic-review` | fidelity |

**Spectrum** (v3.2): *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light. See `shared/mode_spectrum.md` for the full cross-skill spectrum table.

Not sure? Start with `socratic` — it will help you figure out what you need.
不確定？先用 `socratic` 模式——它會幫你釐清你需要什麼。

---

## Agent Team (13 Agents)

| # | Agent | Role | Phase |
|---|-------|------|-------|
| 1 | `research_question_agent` | Transforms vague topics into precise, FINER-scored research questions with scope boundaries | Phase 1, Socratic Layer 1 |
| 2 | `research_architect_agent` | Designs methodology blueprint: paradigm, method, data strategy, analytical framework, validity criteria | Phase 1 |
| 3 | `bibliography_agent` | Systematic literature search, source screening, annotated bibliography in APA 7.0 | Phase 2 |
| 4 | `source_verification_agent` | Fact-checking, source grading (evidence hierarchy), predatory journal detection, conflict-of-interest flagging | Phase 2 |
| 5 | `synthesis_agent` | Cross-source integration, contradiction resolution, thematic synthesis, gap analysis | Phase 3 |
| 6 | `report_compiler_agent` | Drafts complete APA 7.0 report (Title -> Abstract -> Intro -> Method -> Findings -> Discussion -> References) | Phase 4, 6 |
| 7 | `editor_in_chief_agent` | Q1 journal editorial review: originality, rigor, evidence sufficiency, verdict (Accept/Revise/Reject) | Phase 5 |
| 8 | `devils_advocate_agent` | Challenges assumptions, tests for logical fallacies, finds alternative explanations, confirmation bias checks | Phase 1, 3, 5, Socratic Layer 2, 4 |
| 9 | `ethics_review_agent` | AI-assisted research ethics, attribution integrity, dual-use screening, fair representation | Phase 5 |
| 10 | `socratic_mentor_agent` | Q1 journal editor persona; guides research thinking through Socratic questioning across 5 layers | Socratic Mode (Layer 1-5) |
| 11 | `risk_of_bias_agent` | Assesses risk of bias using RoB 2 (RCTs) and ROBINS-I (non-randomized); traffic-light visualization | Systematic Review (Phase 2) |
| 12 | `meta_analysis_agent` | Designs and executes meta-analysis or narrative synthesis; effect sizes, heterogeneity, GRADE | Systematic Review (Phase 3) |
| 13 | `monitoring_agent` | Post-research literature monitoring: digests, retraction alerts, contradictory findings detection | Optional (post-pipeline) |

---

## Mode Selection Guide

See `references/mode_selection_guide.md` for the detailed guide.

```
User Input
    |
    +-- Already have a clear research question?
    |   +-- Yes --> Need PRISMA-compliant systematic review / meta-analysis?
    |   |           +-- Yes --> systematic-review mode
    |   |           +-- No --> Need a full report?
    |   |                      +-- Yes --> full mode
    |   |                      +-- No --> Only need literature?
    |   |                                 +-- Yes --> Need rapid paper comparison?
    |   |                                            +-- Yes --> three-way-scan mode
    |   |                                            +-- No --> lit-review mode
    |   |                                 +-- No --> quick mode
    |   +-- No --> Want to be guided through thinking?
    |              +-- Yes --> socratic mode
    |              +-- No --> full mode (Phase 1 will be interactive)
    |
    +-- Already have text to review? --> review mode
    +-- Only need fact-checking? --> fact-check mode
```

---

## Orchestration Workflow (6 Phases)

```
User: "Research [topic]"
     |
=== Phase 1: SCOPING (Interactive) ===
     |
     |-> [research_question_agent] -> RQ Brief
     |   - FINER criteria scoring (Feasible, Interesting, Novel, Ethical, Relevant)
     |   - Scope boundaries (in-scope / out-of-scope)
     |   - 2-3 sub-questions
     |
     |-> [research_architect_agent] -> Methodology Blueprint
     |   - Research paradigm (positivist / interpretivist / pragmatist)
     |   - Method selection (qualitative / quantitative / mixed)
     |   - Data strategy (primary / secondary / both)
     |   - Analytical framework
     |   - Validity & reliability criteria
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 1
         - RQ clarity and answerable?
         - Method appropriate for question?
         - Scope too broad or too narrow?
         - Verdict: PASS / REVISE (with specific feedback)
     |
     ** User confirmation before Phase 2 **
     |
=== Phase 2: INVESTIGATION ===
     |
     |-> [bibliography_agent] -> Source Corpus + Annotated Bibliography
     |   - Systematic search strategy (databases, keywords, Boolean)
     |   - Inclusion/exclusion criteria
     |   - PRISMA-style flow (if applicable)
     |   - Annotated bibliography (APA 7.0)
     |
     +-> [source_verification_agent] -> Verified & Graded Sources
         - Evidence hierarchy grading (Level I-VII)
         - Predatory journal screening
         - Conflict-of-interest flagging
         - Currency assessment (publication date relevance)
         - Source quality matrix
     |
=== Phase 3: ANALYSIS ===
     |
     |-> [synthesis_agent] -> Synthesis Narrative + Gap Analysis
     |   - Thematic synthesis across sources
     |   - Contradiction identification & resolution
     |   - Evidence convergence/divergence mapping
     |   - Knowledge gap analysis
     |   - Theoretical framework integration
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 2
         - Cherry-picking check
         - Confirmation bias detection
         - Logic chain validation
         - Alternative explanations explored?
         - Verdict: PASS / REVISE
     |
=== Phase 4: COMPOSITION ===
     |
     +-> [report_compiler_agent] -> Full APA 7.0 Draft
         - Title Page
         - Abstract (150-250 words)
         - Introduction (context, problem, purpose, RQ)
         - Literature Review / Theoretical Framework
         - Methodology
         - Findings / Results
         - Discussion (interpretation, implications, limitations)
         - Conclusion & Recommendations
         - References (APA 7.0)
         - Appendices (if applicable)
     |
=== Phase 5: REVIEW (Parallel) ===
     |
     |-> [editor_in_chief_agent] -> Editorial Verdict + Line Feedback
     |   - Originality assessment
     |   - Methodological rigor
     |   - Evidence sufficiency
     |   - Argument coherence
     |   - Writing quality (clarity, conciseness, flow)
     |   - Verdict: ACCEPT / MINOR REVISION / MAJOR REVISION / REJECT
     |
     |-> [ethics_review_agent] -> Research-Integrity Review + Human-Subjects Administrative Status
     |   - AI disclosure compliance
     |   - Attribution integrity
     |   - Dual-use screening
     |   - Fair representation check
     |   - Integrity verdict only: CLEARED / CONDITIONAL / BLOCKED
     |   - Human subjects: readiness and authorization reported separately; institutional determination required
     |   - Authority-bound planning: exact requirement IDs + actor/consumer scope only after the #666 replay-validated resolved-context gate
     |   - Candidate rule trace: display only a replay-validated and surface-linted #669 artifact; never use it as a pathway result or workflow input
     |   - Packet structure: consume only a replay-validated #667 manifest; deterministic status never becomes authorization or content adequacy
     |   - Content coverage: consume only a replay-validated #681 `LLM-ADVISORY`; preserve deterministic status and report efficacy as `UNMEASURED`
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 3
         - Final vulnerability scan
         - Strongest counter-argument test
         - "So what?" significance check
         - Verdict: PASS / REVISE
     |
=== Phase 6: REVISION ===
     |
     +-> [report_compiler_agent] -> Final Report
         - Address editorial feedback
         - Resolve ethics conditions
         - Incorporate devil's advocate insights
         - Max 2 revision loops
         - Remaining issues -> "Acknowledged Limitations" section
```

### Checkpoint Rules

1. ⚠️ **IRON RULE**: **Devil's Advocate** has 3 mandatory checkpoints; **Critical-severity** issues block progression
2. Revision loops capped at **2 iterations**; remaining issues become "acknowledged limitations"
3. ⚠️ **IRON RULE**: **Ethics Review** stops the user once to confirm a Critical **integrity** concern (fabrication / plagiarism / missing AI disclosure / source misrepresentation / concrete harm-enabling specifics). Overridable with recorded reasoning — it confirms, it does not veto. Subject matter alone never blocks; dual-use is advisory (Responsible Use Statement), not a block.
4. User confirmation required after Phase 1 before proceeding

---

## Phase-by-phase Invocation Contract (v3.9.2)

ARS pipeline runs in 6 phases. Two invocation modes:

**Mode A — orchestrator-driven (default):** `pipeline_orchestrator_agent` (in `academic-pipeline` skill) runs all phases end-to-end with state tracking via Material Passport.

**Mode B — phase-by-phase (cross-session resume):** User invokes one agent per phase across sessions for long-running projects. Common pattern via `ARS_PASSPORT_RESET=1` + `resume_from_passport=<hash>` (see `academic-pipeline/references/passport_as_reset_boundary.md`).

In Mode B, **single-phase agents (Bucket A per `docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md`) stay strictly within their assigned phase for writes**. Reads from upstream phases are allowed. Multi-phase agents (Bucket B: `devils_advocate_agent`, `report_compiler_agent`) do exactly the work specified by the caller's invocation for that phase — no extension to other phases in the same call.

> **Path note (Ultimate Skills):** `shared/...` paths refer to this plugin's vendored [`../../shared/`](../../shared/) directory. `scripts/*.py` validators and `docs/design/...` specs live only in the upstream repo ([Imbad0202/academic-research-skills@95929c0](https://github.com/Imbad0202/academic-research-skills/tree/95929c00fc066730b40cf268fd1250b04f00356a)); they are optional/advisory and not required to run this skill.

Routing into Mode B requires explicit user signal — `/ars-<mode>` slash command or `[direct-mode]` prefix. Ambiguous cross-phase input defaults to clarification before processing.

**Enforcement (v3.9.2):** Phase Boundary blocks on Bucket A agents + advisory verifier (`scripts/check_pipeline_integrity.py`) + a deterministic PreToolUse write-scope guard in hook-enabled runtimes (#134 rescope, PR #294). Multi-phase envelope remains forward-scope (#134 Slices 3-5).

---

## Socratic Mode: Guided Research Dialogue

5-layer dialogue guiding users from vague ideas to concrete research questions. Core principle while non-generation Socratic mode is active: ⚠️ **IRON RULE**: Never give direct answers. The explicit candidate-generation exit below leaves that mode before any candidate is shown.

**Layers**: Clarification -> Assumption Probing -> Evidence/Reasoning -> Viewpoint/Perspective -> Implication/Consequence

**Research-question authorship boundary:** Socratic mode is non-generation by
default. Non-convergence may produce only a summary of directions the user has
already expressed plus focused questions or a `lit-review` suggestion; it never
produces candidate RQs automatically. If the user explicitly asks the system to
propose candidates, announce the exit from non-generation Socratic mode and
emit `[SOCRATIC-NON-GENERATION-EXIT: explicit_user_request]` on a standalone
line before any clearly labeled AI-generated candidate. Never switch silently.

> See `references/socratic_mode_protocol.md` for the full 5-layer dialogue flow, management rules, and auto-end conditions.

### Opt-in Reading Probe (v3.5.1)

Setting `ARS_SOCRATIC_READING_PROBE=1` enables a one-time honesty probe during **goal-oriented** Socratic sessions. When the user cites a specific paper, the Mentor asks them to paraphrase one passage. Decline is logged without penalty. Default OFF. See `agents/socratic_mentor_agent.md` §"Optional Reading Probe Layer".

---

## Systematic Review Mode

PRISMA 2020-compliant systematic review with optional meta-analysis. Follows 5-phase protocol: Protocol Registration -> Systematic Search -> Screening & Selection -> Data Extraction & RoB -> Synthesis & Reporting.

> **v3.4.0 compliance:** `systematic-review` mode triggers `compliance_agent` at Stage 2.5 (Methods items) and Stage 4.5 (remaining items + RAISE 8-role matrix). PRISMA-trAIce Mandatory failures block the pipeline. See `shared/compliance_checkpoint_protocol.md`.

> See `references/systematic_review_protocol.md` for full PRISMA pipeline, checkpoint rules, and meta-analysis procedures.

---

## Operational Modes

| Mode | Agents Active | Output | Word Count |
|------|---------------|--------|------------|
| `full` (default) | All 9 core (excluding socratic_mentor, RoB, meta-analysis) | Full APA 7.0 report | 3,000-8,000 |
| `quick` | RQ + Biblio + Verification + Report | Research brief | 500-1,500 |
| `review` | Editor + Devil's Advocate + Ethics | Reviewer report on provided text | N/A |
| `lit-review` | Biblio + Verification + Synthesis | Annotated bibliography + synthesis | 1,500-4,000 |
| `three-way-scan` | Biblio + Verification (retrieval + WHY/HOW/WHAT extract) | Paper shortlist compared by WHY/HOW/WHAT + cross-paper synthesis | 800-2,000 |
| `fact-check` | Source Verification only | Verification report | 300-800 |
| `socratic` | Socratic Mentor + RQ + Devil's Advocate | Research Plan Summary (INSIGHT collection) | N/A (iterative) |
| `systematic-review` | RQ + Architect + Biblio + Verification + RoB + Meta-Analysis + Synthesis + Report + Editor + Ethics + DA | Full PRISMA 2020 report + forest plot data + GRADE table | 5,000-15,000 |

---

## Three-Way Scan Mode (WHY / HOW / WHAT)

Use `three-way-scan` for a disciplined paper shortlist compared per paper by WHY (problem and why it matters) / HOW (strategy or method) / WHAT (findings, artifacts, open gaps), followed by a cross-paper synthesis (common WHY, divergent HOW, strongest WHAT, unresolved global gap). It is lighter than `lit-review`; escalate to `lit-review` or `systematic-review` when the user needs a broader evidence matrix, thematic synthesis or PRISMA-like coverage.
Read [`references/three_way_scan_mode.md`](references/three_way_scan_mode.md) when running `three-way-scan` mode (retrieval priorities and the per-paper output template).

---

## Failure Paths

See `references/failure_paths.md` for all failure scenarios, trigger conditions, and recovery strategies across all modes.

Key failure path summary:

| Failure Scenario | Trigger Condition | Recovery Strategy |
|---------|---------|---------|
| RQ cannot converge | Phase 1 / Layer 1 exceeds multiple rounds while still vague | Full mode may use its candidate workflow; Socratic mode summarizes user-expressed directions or suggests `lit-review`, with no candidate generation unless the user explicitly exits non-generation mode |
| Insufficient literature | bibliography_agent finds < 5 sources | Expand search strategy, alternative keywords |
| Methodology mismatch | RQ type misaligned with method capability | Return to Phase 1, suggest 3 alternative methods |
| Devil's Advocate CRITICAL | Fatal logical flaw discovered | STOP, explain the issue, require correction |
| Ethics BLOCKED | Critical integrity issue (not subject matter) | Stop the user once to confirm; list issues + remediation path; overridable with recorded reasoning |
| Socratic non-convergence | > 10 rounds without convergence | Suggest switching to full mode |
| User abandons mid-process | Explicitly states they don't want to continue | Save progress, provide re-entry path |
| Only Chinese-language literature | English search returns empty | Switch to Chinese academic databases |

---

## Literature Monitoring (Optional Post-Pipeline)

Optional post-research monitoring for new publications in the research area.

> See `references/literature_monitoring_strategies.md` for setup instructions across academic databases.

---

## Handoff Protocol: deep-research → academic-paper

When the user asks to write a paper from the research, hand `academic-paper` the RQ Brief, Methodology Blueprint, Annotated Bibliography, Synthesis Report, (socratic mode) INSIGHT Collection and Research Plan Summary, and exactly one builder-produced `preregistration-artifact/1.0` sidecar (an unavailable receipt still counts; plus its explicitly named companion bytes when `status=provided`).
Only the deterministic `build-preregistration-artifact` builder, run by a shell-capable dispatcher (the non-shell `research_architect_agent` supplies only the caller declaration and companion handle), may create or update that sidecar; `academic-paper` intake strict-validates it and its companion and carries both byte-for-byte, never rebuilding them from prose or a template, and omission or silent substitution is invalid.
Read [`references/handoff_and_integration.md`](references/handoff_and_integration.md) when handing off to `academic-paper` (intake skip rules, builder invocation contract, example).

---

## Full Academic Pipeline

See `academic-pipeline/SKILL.md` for the complete workflow.

---

## Agent File References

Each agent in the Agent Team table is defined in `agents/<agent_name>.md` (e.g. `agents/research_question_agent.md`).
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when you need the full agent-to-definition-file table.

---

## Reference Files

Topic references in `references/`: `apa7_style_guide.md`, `source_quality_hierarchy.md`, `methodology_patterns.md`, `logical_fallacies.md`, `ethics_checklist.md`, `interdisciplinary_bridges.md`, `argumentation_reasoning_framework.md`, `socratic_mode_protocol.md`, `socratic_questioning_framework.md`, `failure_paths.md`, `mode_selection_guide.md`, `equator_reporting_guidelines.md`, `preregistration_guide.md`, `systematic_review_protocol.md`, `systematic_review_toolkit.md`, `literature_monitoring_strategies.md`, `cross_agent_quality_definitions.md`, `changelog.md`; source-lookup API protocols `semantic_scholar_api_protocol.md`, `crossref_api_protocol.md`, `openalex_api_protocol.md`, `arxiv_api_protocol.md` (used by `bibliography_agent` / `source_verification_agent`) and `chinese_literature_api_protocol.md` (standalone client, not wired into the verification gate). Human subjects: `references/irb_decision_tree.md` is a portable navigation aid only, never an authority, universal taxonomy or pathway determination; authority selection, replay validation and the fail-closed resolved-context gate live in `shared/references/human_subjects_authority_protocol.md` (#666), next to the pathway rule trace (#669), packet manifest (#667), content coverage (#681) and cross-document/preregistration-sidecar (`cross_document_consistency_advisory_protocol.md`) protocols in `shared/references/`, their schemas in `shared/contracts/`.
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when you need the purpose of a reference file or which agents use it.

---

## Templates

Output templates in `templates/`: `research_brief_template.md` (quick mode output format), `literature_matrix_template.md` (source × theme matrix), `evidence_assessment_template.md` (per-source quality card), `preregistration_template.md` (OSF 21-item preregistration), `prisma_protocol_template.md` (PRISMA-P 2015 protocol) and `prisma_report_template.md` (PRISMA 2020 report, 27 items).
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when producing one of these outputs (full template table).

---

## Examples

Worked examples in `examples/` cover the full 6-phase pipeline, systematic review, policy analysis, Socratic dialogue, handoff to `academic-paper`, review mode, fact-check mode and the #257 idea-diversity advisories.
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when you need a worked example for a mode.

---

## Output Language

Follows the user's language. Academic terminology kept in English. Socratic mode uses natural conversational style.

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes:

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **Confirmation bias in source selection** | Only finding sources that support the hypothesis | Devil's Advocate checkpoint must include counter-evidence search |
| 2 | **Cherry-picking evidence** | Citing one supportive study while ignoring three contradicting ones | Report the full evidence landscape including conflicting findings |
| 3 | **Vibe citing** | Mixing elements from 2-3 real papers into a fabricated reference | Every reference must be verified independently; mashup fabrication is the hardest to detect |
| 4 | **⚠️ IRON RULE: Treating "difficult to verify" as acceptable** | Marking a reference as "uncertain" instead of FAIL | Gray zone = FAIL. If you cannot confirm it exists, it does not go in the report |
| 5 | **Skipping phases** | Jumping to synthesis before completing source verification | Complete each phase fully; Phase N output is Phase N+1 input |
| 6 | **Shallow Socratic mode** | Giving answers disguised as questions ("Wouldn't you say X is true?") | Ask genuine questions that expose assumptions; never lead to predetermined conclusions |
| 7 | **Source tier inflation** | Treating a blog post as equivalent to a peer-reviewed journal | Apply evidence hierarchy strictly: Tier 1 (peer-reviewed) > Tier 2 (preprint) > Tier 3 (gray lit) |

## Quality Standards

1. ⚠️ **IRON RULE**: **Every claim must have a citation** — no unsupported assertions
2. **Evidence hierarchy** — meta-analyses > RCTs > cohort studies > case reports > expert opinion (field-neutral baseline; grading is **discipline-relative** — a source meeting its own field's gold standard can reach Grade A even at a low design level. See `references/source_quality_hierarchy.md` §Grading Rubric + §Field-Specific Adjustments)
3. **Contradiction disclosure** — if sources disagree, report both sides with evidence quality comparison
4. **Limitation transparency** — every report must have an explicit limitations section
5. **AI disclosure** — all reports include a statement that AI-assisted research tools were used
6. **Reproducibility** — search strategies, inclusion criteria, and analytical methods must be documented for replication
7. **Socratic integrity** — while non-generation Socratic mode is active, never give direct answers; always guide through questions. A candidate response is lawful only after the explicit exit marker and is outside that mode.

## Cross-Agent Quality Alignment

Unified definitions across all agents. ⚠️ IRON RULE: **CRITICAL severity** = issue that would invalidate a core conclusion or constitute academic misconduct. Requires immediate resolution.

> See `references/cross_agent_quality_definitions.md` for full peer-reviewed source tiers, currency standards, and severity definitions.

---

## Integration with Other Skills

Domain-agnostic; combinable with domain-specific skills (e.g. `academic-paper` for research-to-publication, socratic + `academic-paper` plan, systematic-review + `academic-paper` for a PRISMA paper).
Read [`references/handoff_and_integration.md`](references/handoff_and_integration.md) when combining this skill with another skill.

---

## Model Tiering (#517, optional)

Applies only when `ARS_MODEL_TIERING` is set (`economy` or `quality-boost`); unset (default) means every agent inherits the session model, and unknown values warn once and behave as unset.
Read [`references/handoff_and_integration.md`](references/handoff_and_integration.md) when `ARS_MODEL_TIERING` is set (routing rules; canonical table in `shared/model_tiering.md`).

---

## Version Info

Skill version, last-updated date, maintainer and downstream dependencies (mirrors `metadata` in the frontmatter).
Read [`references/skill_overview_details.md`](references/skill_overview_details.md) when you need the maintainer or dependency versions.

---

## Version History

> See `references/changelog.md` for full version history.
