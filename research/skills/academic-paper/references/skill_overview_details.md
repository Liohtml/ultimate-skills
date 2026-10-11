Moved verbatim from SKILL.md sections 'Trigger Keywords', 'File Structure', 'Integration with Other Skills', 'Model Tiering (#517, optional)' and 'Version Info' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`, `templates/...`, `examples/...`); `deep-research/...` is the sibling skill directory (`../../deep-research/...` from this file); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory. `tw-hei-intelligence`, `report-to-website` and `notebooklm-slides-generator` under Integration with Other Skills are other skills named by upstream; they are not part of this marketplace.

# Academic Paper — Skill Overview Details

## Trigger Conditions

### Trigger Keywords

**English**: write paper, academic paper, paper outline, write abstract, revise paper, literature review paper, check citations, convert to LaTeX, convert format, format paper, conference paper, journal article, thesis chapter, research paper, guide my paper, help me plan my paper, step by step paper, draft manuscript, write methodology, write discussion, parse reviews, revision roadmap, help me with my revision, I got reviewer comments, should we push back, conference rebuttal, grant panel response, convert citations

**Español**: redactar artículo, trabajo académico, esquema de artículo, escribir resumen, enmendar mi artículo, artículo de revisión bibliográfica, verificar citas, convertir a LaTeX, convertir formato, artículo de conferencia, artículo de revista, capítulo de tesis, artículo de investigación, guía mi artículo, ayúdame a planificar mi artículo, escribir artículo paso a paso, redactar manuscrito, escribir metodología, escribir discusión, analizar opiniones de revisores, ruta de revisión, ayúdame con mi revisión, recibí comentarios de revisores, convertir formato de citas

**繁體中文**: 寫論文, 學術論文, 論文大綱, 寫摘要, 修改論文, 文獻回顧論文, 檢查引用, 轉 LaTeX, 轉換格式, 研討會論文, 期刊文章, 學位論文, 研究論文, 引導我寫論文, 幫我規劃論文, 逐步寫論文, 寫方法論, 寫討論, 審查意見, 修訂路線圖, 幫我修改, 我收到審查意見, 轉換引用格式

**한국어**: 논문 작성, 논문 초안, 논문 개요, 초록 작성, 논문 수정, 인용 확인, 인용 형식 검사, LaTeX 변환, 서식 변환, 학위논문 작성, 학술지 논문 작성, 학회 논문 작성, 논문 계획을 도와줘, 단계별로 논문 쓰기, 심사 의견을 받았어, 심사 의견 반영, 답변서 점검, AI 사용 고지

---

## File Structure

**Agent definitions**: `agents/{agent_name}.md` — one file per agent (12 total, matching Agent Team table above).

**References** (28 files in `references/`):
- Citation: `apa7_extended_guide`, `apa7_chinese_citation_guide`, `citation_format_switcher`
- Writing: `academic_writing_style`, `writing_quality_check`, `writing_judgment_framework`
- Structure: `paper_structure_patterns` (6 types), `abstract_writing_guide`, `intro_title_rhetoric_guide` (CARS moves + title checklist)
- Domain: `hei_domain_glossary` (bilingual), `journal_submission_guide`, `latex_template_reference`, `domain_evidence_profiles` (advisory screening profiles)
- Process: `failure_paths` (12 scenarios), `mode_selection_guide` (11 modes), `plan_mode_protocol`, `workflow_phase_details`, `revision_patch_protocol` (#390 Mode B commands + marker lifecycle)
- Ethics: `credit_authorship_guide` (CRediT 14 roles), `funding_statement_guide`, `statistical_visualization_standards`
- Disclosure (v3.2): `disclosure_mode_protocol` (default venue applicability/status bundle: `REQUIRED`, `ACTION_ONLY`, `NOT_REQUIRED`, `UNKNOWN`, plus typed halts; separate policy-anchor rendering), `venue_disclosure_policies` (v2 database: ICLR, NeurIPS, Nature, Science, ACL, EMNLP, plus medical-publishing policy targets — ICMJE, NEJM, The Lancet, JAMA, BMJ, PLOS, Frontiers, publisher-wide Chinese Nursing Journals Publishing House 中华护理杂志社, journal-level International Eye Science 国际眼科杂志)
- Integrity (v3.3): `anti_leakage_protocol` (knowledge isolation), `vlm_figure_verification` (optional VLM figure check)
- Policy anchors (#108): `policy_anchor_table`, `policy_anchor_disclosure_protocol`
- Meta: `changelog` (version history)
- Also: `deep-research/references/apa7_style_guide.md` (base reference, extended here)

**Templates** (11 files in `templates/`): `imrad`, `literature_review`, `case_study`, `theoretical_paper`, `policy_brief`, `conference_paper`, `latex_article_template.tex`, `bilingual_abstract`, `credit_statement`, `funding_statement`, `revision_tracking` (4 status types).

**Examples** (9 files in `examples/`): `imrad_hei_example`, `literature_review_example`, `plan_mode_guided_writing`, `chinese_paper_example`, `revision_mode_example`, `revision_recovery_example`, `clinical_citation_verification_checklist`, `clinical_epistemic_status_example`, `version_family_reconciliation_example`.

---

## Integration with Other Skills

```
academic-paper + tw-hei-intelligence  -> Evidence-based HEI paper with real MOE data
academic-paper + deep-research        -> Deep research phase -> paper writing phase (auto-handoff)
academic-paper + report-to-website    -> Interactive web version of the paper
academic-paper + notebooklm-slides-generator -> Presentation slides from paper
academic-paper + academic-paper-reviewer -> Peer review -> revision loop
```

---

## Model Tiering (#517, optional)

When `ARS_MODEL_TIERING` is set, the dispatching session routes this skill's agents per `shared/model_tiering.md` (canonical: the full 43-agent judgment/execution table + rules). Compact rule:

- **Unset (default):** every agent inherits the session model — byte-equivalent pre-#517 behavior.
- **`economy`** (frontier-tier session): execution-type agents dispatch ONE tier below the session model — floor Opus-class, never lower; judgment-type agents stay on the session model. No-op at or below the floor (announce once).
- **`quality-boost`** (below-frontier session): judgment-type agents at the checkpoint surfaces (Stage 2.5/4.5 gates; the opt-in Stage 4→5 claim–ref audit; final review) jump UP to the frontier tier (however many tiers away — not a single increment); nothing is ever downgraded. No-op at the frontier (announce once).
- Unknown values → warn once, behave as unset. Tiers are relative positions, never hard-pinned model ids. When a direction is active, route repeated same-stage calls to the SAME worker so its prompt cache accumulates, where the protocol permits (never merging seats that must stay blind; `shared/model_tiering.md`); unset means dispatch shapes stay byte-equivalent too.

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 3.3.1 |
| Last Updated | 2026-08-15 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | deep-research v1.0+ (upstream), academic-paper-reviewer v1.0+ (downstream) |
