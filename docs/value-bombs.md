# Value Bombs: Kandidaten für die nächste Kurationsrunde

> Stand: 2026-09-23 · Kuratiert aus den Ergebnissen von 4 Scout-Agenten (engineering, product, design, research-and-docs).
> Ursprünglich eine **Empfehlung**. **Stand der Umsetzung (Welle 2, 2026-09-23):** Welle 1 und der Großteil von Welle 2 sind umgesetzt. Den Status jedes Kandidaten zeigt Abschnitt 0. Die Abschnitte 1 bis 5 bleiben als ursprüngliche Analyse unverändert, deshalb stehen dort teils noch die Upstream-Namen.

## 0. Umsetzungsstatus

Legende: ✅ integriert (eigener Skill) · 🔀 in einen bestehenden Skill gemergt · ⏸ zurückgestellt · ❌ verworfen. Pfade und Commits je Quelle stehen in [`PROVENANCE.csv`](../PROVENANCE.csv).

| Rang | Kandidat | Status | Ergebnis im Katalog | Anmerkung / Grund |
|---:|---|---|---|---|
| 1 | `diagnosing-bugs` | 🔀 | `engineering/debugging-and-error-recovery` | Feedback-Loop-Phase, Hypothesen und getaggte Logs gemergt, dazu `hitl-loop.template.sh`. Aus obra `systematic-debugging` kam nur `find-polluter.sh` mit. |
| 2 | `web-interface-guidelines` | ✅ | `design/web-interface-review` | Regeln eingebettet und auf `e3d624b` gepinnt, kein WebFetch zur Laufzeit. |
| 3 | `verification-before-completion` | ✅ | `engineering/verification-before-completion` | Ton entschärft, Inhalt behalten. |
| 4 | `mcp-builder` | ✅ | `engineering/mcp-builder` | Apache-2.0. Veraltete Default-Modell-ID und Parallel-`tool_use`-Bug in `evaluation.py` behoben. |
| 5 | `subagent-driven-development` | ✅ | `engineering/subagent-driven-development` | Von anderen superpowers-Skills entkoppelt, Workspace heißt jetzt `.sdd/`, Reviewer-Prompt gebündelt. |
| 6 | `review-animations` (+ `animate`) | ✅ | `design/motion-craft` | Build- und Review-Modus, `disable-model-invocation` entfernt. |
| 7 | `interface-design` | ✅ | `design/interface-design` | Die Slash-Commands sind jetzt `references/`. |
| 8 | `humanizer` | ✅ | `writing/humanizer` | Neues Plugin `writing`. |
| 9 | `minto-pyramid` | ✅ | `writing/minto-pyramid` | tyroneross `pyramid-audit` gekürzt als `references/audit-report.md` (Apache-2.0) übernommen. Die Buch-Zitatanker wurden nicht übernommen. |
| 10 | `validate-data` | ✅ | `product/validate-data` | Apache-2.0. Connector- und Slash-Command-Reste entfernt. |
| 11 | `obviously-awesome` | ✅ | `product/product-positioning` | Umbenannt, Affiliate-Links entfernt. |
| 12 | `iterate-pr` (+ `receiving-code-review`) | ✅ | `engineering/iterate-pr` | Bot-Liste konfigurierbar (`PR_REVIEW_BOTS`). receiving-code-review liegt als Referenz bei. |
| 13 | `gha-security-review` | ✅ | `security/gha-security-review` | Liegt im neuen Plugin `security` statt in `engineering`, dort ist die Audit-Seite zu Hause. |
| 14 | `good-strategy-bad-strategy` | ✅ | `product/strategy-kernel` | Umbenannt, gepaart mit `strategy-red-team`. |
| 15 | `wcag-2.2-aa` (+ masuP9) | ✅ | `design/accessibility-audit` | Umbenannt, weil Punkte in Skill-Namen nicht erlaubt sind. masuP9-Modi gemergt. Die W3C-Spec wird nicht mitgeliefert, nur verlinkt. |
| 16 | `saas-metrics-coach` | ✅ | `product/saas-metrics-coach` | Benchmarks als Heuristik gekennzeichnet. |
| 17 | `copy-editing` + `product-marketing` | ✅ / ❌ | `writing/copy-editing` | `product-marketing` verworfen: überschneidet sich mit `product-positioning`/`value-proposition` und hängt an der Kontextdatei-Konvention. |
| 18 | `supabase-postgres-best-practices` | ✅ | `engineering/postgres-best-practices` | Herstellerneutral umbenannt. Neon-Referenzen zu Backup, Upgrades und Migrationssicherheit (Apache-2.0) gemergt. |
| 19 | `startup-competitors` (Teile) | 🔀 | `product/competitor-analysis` | Evidenz-Labels, Honesty-Regeln und Verification-Pass. |
| 20 | `long-horizon-prompting` | ✅ | `engineering/long-horizon-prompting` | `claim-*`-IDs entfernt. `cdc-prompt-annotated.md` nicht übernommen (wörtliche Kopie des OpenAI-Prompts), nur verlinkt. |
| 21 | `citation-management` | ⏸ | – | Das Plugin `research-tools` (MIT) wurde in Welle 2 nicht angelegt. |
| 22 | `customer-research` | ❌ | – | Überschneidet sich mit `interview-script` und `user-personas`. |
| 23 | `impeccable` (craft-floor + critique) | 🔀 | `design/redesign-existing-projects` | Zwei Referenzdateien, Apache-2.0, mit Änderungsvermerk. |
| 24 | `frontend-slides` | ✅ | `design/frontend-slides` | Ohne `deploy.sh` und `bold-template-pack`. |
| 25 | `writing-skills` / `skill-creator` | ❌ | – | skill-creator ist in Claude Code bereits eingebaut. Ein `meta`-Plugin lohnt sich nicht. |
| 26 | `property-based-testing`, `differential-review`, `fp-check` | ❌ | – | CC-BY-SA. `fp-check` und `differential-review` sind Solidity-lastig und überschneiden sich mit `vuln-triage`. Das Share-Alike-Plugin heißt jetzt `security-cc-by-sa` und enthält stattdessen `supply-chain-risk-auditor` und `variant-analysis`. |
| 27 | `variance-analysis` | ❌ | – | FP&A-Nische. |
| 28 | `scientific-critical-thinking` | ⏸ | – | Wartet auf `research-tools`. |
| 29 | `markitdown` | ⏸ | – | Dünner Wrapper, wartet auf `research-tools`. |

**Zusätzlich integriert (aus den Design- und Security-Scouts, nicht in der ursprünglichen Rangliste):**
- `design/image-generation`: Basis ist openai/skills `imagegen` (Apache-2.0), für Claude Code umgeschrieben, dazu ein eigenes Gemini-Skript. Gemergt wurden jezweb `ai-image-generator` (Provider-Routing), wuyoscar `craft.md` (Prompt-Handwerk, ohne Galerie) und replicate `prompt-images` (Apache-2.0).
- `design/icon-set-generator` (jezweb).
- Plugin `security`, alle Skills mit Autorisierungs- und Scope-Gates: `threat-model`, `static-vuln-scan` und `vuln-triage` (anthropics/defending-code-reference-harness, Apache-2.0), `skill-scanner` (getsentry, Apache-2.0), `web-pentest` und `llm-app-security-audit` (briiirussell, MIT).
- Plugin `security-cc-by-sa`: `supply-chain-risk-auditor` und `variant-analysis` (trailofbits, CC-BY-SA-4.0).

**Zusätzlich verworfen:**

*Image Generation*
- `banana-claude`: ca. 22k Zeilen Python. Nur die Ideen „Pixel-Review“ und „Text im Bild ist Daten“ wurden in eigenen Worten übernommen.
- `nano-banana-pro` (jlouage): API-Key im argv, liest `~/.claude/.env`.
- fal `character-design`: Lizenz nur im README behauptet, an die genmedia-CLI gebunden.
- openai/plugins `imagegen-website-concepts`: MIT nur im Manifest. Nur Ideen, paraphrasiert in `image-to-code/references/concept-fidelity.md`.
- wuyoscar `gallery-*.md`: Drittanbieter-Prompts.
- robonuggets, devonjones, op7418, rknall: keine Lizenz.

*Design*
- `favicon-gen` / `web-asset-generator`: geringer Hebel, 766 Zeilen.
- anthropics `frontend-design`: Duplikat von `design-taste-frontend`.

*Security*
- getsentry `security-review`: Referenzen unter CC-BY-SA, 7 referenzierte Dateien fehlen upstream.
- abelreqma `modern-threat-modeling`: Überschneidung mit `threat-model`.
- agamm `owasp-security`: Überschneidung mit `security-and-hardening`.
- briiirussell `siem-detection` und `red-team-engagement`: Nische bzw. zu offensiv.
- trailofbits `static-analysis`/semgrep: braucht die CLI, dupliziert die Starter von `variant-analysis`.
- `semgrep/skills`: keine OSI-Lizenz.
- transilienceai: Umgehung von Allowlists.
- Masriyan, trilwu: stark offensiv.
- timothybrush: keine Lizenz.
- Eyadkelleh: gebündelte Payloads.
- anthropics `patch`: noch nicht bewertet.

*Writing*
- kemalcanyapali `business-writing`: kapitelweise Nacherzählung des Minto-Buchs („OCR pages“), rechtliches Risiko.
- IrtezaAsadRizvi `karpathy-article-writing`: imitiert die Stimme einer realen Person.
- die übrigen 5 tyroneross-Skills: Duplikate.

**Offene Pflegepunkte:**
- `mcp-builder` (Default-Modell, MCP-Spec/SDK) etwa halbjährlich prüfen.
- Modell-IDs in `image-generation` vor dem ersten Live-Call prüfen.
- Die datierten Vendor- und arXiv-Claims in `long-horizon-prompting` bei jedem Update prüfen.
- `frontend-slides` `export-pdf.sh` installiert Playwright ungepinnt.

## 1. Kurzfazit und Methode

**Kurzfazit.** Die größten Lücken im Katalog sind nicht „noch mehr Engineering-Best-Practices“. Es fehlen **Verifikations-Gates und geschlossene Loops**: Feedback-Loop vor Hypothese, Beweis vor „fertig“, PR bis grün, Analyse-QA vor dem Teilen. Dazu kommen ganze Disziplinen, die heute gar nicht abgedeckt sind: MCP-Server-Bau, UI-Code-Review, Motion, Dashboards/Product-UI, Business-Writing/Prosa, Positionierung, Datenanalyse-QA und Datenbanken. Welle 1 bringt mit 9 Skills, alle MIT oder Apache-2.0, den größten Hebel bei geringer Überschneidung.

**Methode.**
- **Untersuchte Repos (Auswahl):** obra/superpowers, mattpocock/skills, anthropics/skills, anthropics/knowledge-work-plugins, anthropics/financial-services-plugins, getsentry/skills, trailofbits/skills, supabase/agent-skills, neondatabase/postgres-skills, SonOfBytes/skills-postgres, wondelai/skills, coreyhaines31/marketingskills, tyroneross/pyramid-principle, millwright-labs/minto-pyramid-skill, blader/humanizer, alirezarezvani/claude-skills, ferdinandobons/startup-skill, deanpeters/Product-Manager-Skills, vercel-labs/web-interface-guidelines, vercel-labs/agent-skills, emilkowalski/skills, Dammyjay93/interface-design, 84emllc/claude-wcag-skill, masuP9/a11y-specialist-skills, pbakaus/impeccable, zarazhangrui/frontend-slides, raphaelsalaja/userinterface-wiki, nextlevelbuilder/ui-ux-pro-max-skill, indi256s/dataviz-skill, K-Dense-AI/claude-scientific-skills, muratcankoylan/Agent-Skills-for-Context-Engineering, appautomaton/document-SKILLs sowie weitere Awesome-Listen (travisvn, ComposioHQ) und kleinere Sammlungen, insgesamt rund 55 Klone.
- **Latte, die ein Skill nehmen musste:**
  1. **Lizenz**: OSI- oder CC-Lizenz, die Weitergabe erlaubt, **im Clone selbst geprüft**, nicht nur aus dem README übernommen. Ohne Lizenz ist ein Skill nicht übernehmbar. NC-Lizenzen dürfen nur ins isolierte `research/` oder in ein eigenes NC-Plugin. Für CC-BY-SA gilt Share-Alike, also ein eigenes Plugin.
  2. **Mechanismus statt Ratschlag**: ein prüfbares Gate, eine Entscheidungsregel, ein Skript oder eine Eval. Allgemeine Best-Practice-Listen wurden abgewertet.
  3. **Überschneidung** mit den 39 bestehenden Skills: Ersetzt oder schärft der Kandidat einen bestehenden Skill, oder schließt er eine echte Lücke?
  4. **Kosten**: Token-Last, Kopplung an fremde Skills, Binaries oder Tools, Pflegeaufwand.
- **Stichproben** wurden in den Klonen an den Top-Kandidaten gemacht: LICENSE-Datei und HEAD-SHA, SKILL.md gelesen, behauptete Risiken geprüft (z. B. `disable-model-invocation`, Binary-Aufrufe bei impeccable, Cowork-Abschnitte bei skill-creator, fehlende Lizenz bei doc-coauthoring).
- **Korrekturen an Scout-Aussagen:** Der `scripts/`-Ordner von `diagnosing-bugs` enthält im geprüften Commit **nur** `hitl-loop.template.sh`. Die gemeldeten sdd-workspace-Skripte gibt es dort nicht. Neu hinzu kommt nur `agents/openai.yaml`, das irrelevant ist. `anthropics/skills` hat **keine** LICENSE im Repo-Root. Lizenzen gelten dort je Skill-Ordner (`LICENSE.txt`).

## 2. Top-Value-Bombs (gerankt, dedupliziert)

| Rang | Skill | Quelle | Lizenz | Ziel-Plugin | Wert in einem Satz | Überschneidung / ersetzt? | Score |
|---:|---|---|---|---|---|---|---:|
| 1 | `diagnosing-bugs` | [mattpocock/skills@c55ee46](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs) | MIT | engineering | Keine Hypothese ohne einen bereits ausgeführten, deterministischen roten Befehl; 10 Wege zum Feedback-Loop. | **Merge** in `debugging-and-error-recovery` (Phase 1 + Hypothesen + getaggte Logs) | 9 |
| 2 | `web-interface-guidelines` | [vercel-labs/web-interface-guidelines@e3d624b](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md) | MIT | design | 190 prüfbare UI-Code-Regeln mit `file:line`-Findings, in Sekunden auf jeden Diff anwendbar. | Neu; ergänzt `frontend-ui-engineering` | 9 |
| 3 | `verification-before-completion` | [obra/superpowers@5bf4e78](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/verification-before-completion) | MIT | engineering | Gate vor jeder „fertig/grün/gefixt“-Aussage: Befehl frisch ausführen, Output lesen, erst dann behaupten. | Neu als eigenständiges Gate | 8.5 |
| 4 | `mcp-builder` | [anthropics/skills@34040c9](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/mcp-builder) | Apache-2.0 | engineering | MCP-Server bauen mit messbarem Ergebnis: 10 verifizierte QA-Paare als LLM-Usability-Eval. | Neu (kein MCP im Katalog) | 8.5 |
| 5 | `subagent-driven-development` | [obra/superpowers@5bf4e78](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/subagent-driven-development) | MIT | engineering | Plan-Ausführung mit Implementer- und Reviewer-Subagents, Ledger übersteht Compaction, max. 5 Fix-Runden. | Neu; ergänzt `planning-…`/`incremental-…` | 8.5 |
| 6 | `review-animations` (+ `STANDARDS.md`) | [emilkowalski/skills@85e8e23](https://github.com/emilkowalski/skills/tree/85e8e2363b713506e1d5b6e07a0eb2da66be1bc3/skills/review-animations) | MIT | design | Entscheidbare Motion-Regeln: Frequenztabelle, Easing-Kurven, Dauer-Budgets, Interruptibility. | Neu; ergänzt `design-taste-frontend` | 8 |
| 7 | `interface-design` | [Dammyjay93/interface-design@2f9be32](https://github.com/Dammyjay93/interface-design/tree/2f9be3206855bcb2d1d0af262c8bae25cba6658d/.claude/skills/interface-design) | MIT | design | Schließt die explizite Lücke „not dashboards/product UI“ mit Intent-Brief und konkreten Hierarchie-Regeln. | Neu; komplementär zu `design-taste-frontend` | 8 |
| 8 | `humanizer` | [blader/humanizer@9862685](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/SKILL.md) | MIT | neues `writing` | Entfernt KI-Schreibtells nach 25 gewichteten Mustern und fügt dabei nachweislich keine Fakten hinzu. | Neu (Prosa bisher gar nicht abgedeckt) | 8 |
| 9 | `minto-pyramid` | [millwright-labs/minto-pyramid-skill@49d1f58](https://github.com/millwright-labs/minto-pyramid-skill/tree/49d1f584f5661f4dd47c834f5a7f9f0c4c4279d0) | MIT | neues `writing` | Answer-first/SCQA für Entscheidungsdokumente, mit Step-0-Gate und mitgelieferter Eval-Suite. | Neu; schlägt tyroneross als Basis | 8 |
| 10 | `validate-data` | [anthropics/knowledge-work-plugins@1bd4282](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/data/skills/validate-data) | Apache-2.0 | product | QA-Gate für Analysen mit Pitfall-Katalog inkl. Detektions-SQL und 3-stufigem Verdikt. | Neu; ergänzt `ab-test-analysis` | 8 |
| 11 | `obviously-awesome` | [wondelai/skills@c172996](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/obviously-awesome) | MIT | product | Dunfords 5-Schritt-Positionierung mit Canvas, 0–10-Rubrik und Kategorie-Entscheidung. | Neu; upstream von `value-proposition` | 8 |
| 12 | `iterate-pr` (+ `receiving-code-review` als Abschnitt) | [getsentry/skills@c2f99a5](https://github.com/getsentry/skills/tree/c2f99a5b04b4cd992ec3022d7c2c3e23e938d241/skills/iterate-pr) · [obra/superpowers@5bf4e78](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/receiving-code-review) | Apache-2.0 + MIT | engineering | PR-Loop bis CI grün und Feedback adressiert; Skripte liefern CI- und Review-Zustand als JSON. | Neu; schließt Lücke zwischen CI- und Review-Skill | 7.5 |
| 13 | `gha-security-review` | [getsentry/skills@c2f99a5](https://github.com/getsentry/skills/tree/c2f99a5b04b4cd992ec3022d7c2c3e23e938d241/skills/gha-security-review) | Apache-2.0 | engineering | Exploit-orientiertes GitHub-Actions-Review mit Pflicht-PoC und expliziter „nicht melden“-Liste. | Neu; ergänzt `security-and-hardening` | 7.5 |
| 14 | `good-strategy-bad-strategy` | [wondelai/skills@c172996](https://github.com/wondelai/skills/tree/c172996495bed0fcd26896a9416b2093fd7073f0/good-strategy-bad-strategy) | MIT | product | Rumelt-Kernel plus Negations- und Paste-Test: baut eine Strategie, die echte Entscheidungen trifft. | Neu; Paar mit `strategy-red-team` | 7.5 |
| 15 | `wcag-2.2-aa` | [84emllc/claude-wcag-skill@792755f](https://github.com/84emllc/claude-wcag-skill/tree/792755fef05b863fc27c71cf808e6b64e599ac8f) | MIT (+ W3C-Doc-Lizenz für Spec) | design | 4-Pass-Audit mit axe-Injection, kombinierbar mit `browser-testing-with-devtools`. | Neu; masuP9-Ideen einmergen | 7.5 |
| 16 | `saas-metrics-coach` | [alirezarezvani/claude-skills@19392f7](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/saas-metrics-coach) | MIT | product | Deterministische Unit-Economics-Skripte mit segmentabhängigen Benchmarks, Top-3-Issues. | Neu | 7 |
| 17 | `copy-editing` + `product-marketing` | [coreyhaines31/marketingskills@5b2c000](https://github.com/coreyhaines31/marketingskills/tree/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills) | MIT | product (oder `writing`) | Seven Sweeps plus geteilte Kontextdatei für alle Marketing-Aufgaben. | Neu; `copywriting` nur optional | 7 |
| 18 | `supabase-postgres-best-practices` | [supabase/agent-skills@8331f91](https://github.com/supabase/agent-skills/tree/8331f910845103c08d51f6ca1d86ebb7d1f745e3/skills/supabase-postgres-best-practices) | MIT | engineering | 64-Zeilen-Router über 30 Postgres-Regeln (falsch/richtig-SQL), lädt nur Benötigtes. | Neu (kein DB-Skill) | 7 |
| 19 | `startup-competitors` (Teile) | [ferdinandobons/startup-skill@a5f97c3](https://github.com/ferdinandobons/startup-skill/tree/a5f97c317b93caedbb49d28f20e9ec283b2ec087/startup-competitors) | MIT | product | Evidenz-Labels und Verification-Agent für Wettbewerbsanalysen. | **Merge** in `competitor-analysis` | 7 |
| 20 | `long-horizon-prompting` | [muratcankoylan/Agent-Skills-for-Context-Engineering@6dbe1a1](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/6dbe1a1d868eab51a3bc9011b0f55e2891513e40/skills/long-horizon-prompting) | MIT | engineering | Brief für autonome/Multi-Agent-Läufe: Erfolgsprädikat, Liste unzulässiger Ergebnisse, Persistenz nur mit Gate. | Neu; ergänzt `doubt-driven-development` | 6.5 |
| 21 | `citation-management` | [K-Dense-AI/claude-scientific-skills@49c6e97](https://github.com/K-Dense-AI/claude-scientific-skills/tree/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/citation-management) | MIT | neues `research-tools` (MIT) | Ausführbare Zitat-Validierung (DOI-Auflösung, Metadaten-Abgleich) gegen halluzinierte Referenzen. | Ergänzt NC-`research` um MIT-Werkzeug | 6.5 |
| 22 | `customer-research` | [coreyhaines31/marketingskills@5b2c000](https://github.com/coreyhaines31/marketingskills/tree/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/customer-research) | MIT | product | Asset- und Watering-Hole-Mining mit Konfidenz-Labels und Bias-Korrekturen. | Teilweise `user-personas` | 6.5 |
| 23 | `impeccable` (nur craft-floor + critique) | [pbakaus/impeccable@e0881d2](https://github.com/pbakaus/impeccable/tree/e0881d2de397d5e9761d7b35ff5017d8f5ebf69b) | Apache-2.0 | design | 44-Zeilen-Qualitätsboden und Nielsen-Heuristik-Scoring. | **Merge** in `redesign-existing-projects` | 6.5 |
| 24 | `frontend-slides` | [zarazhangrui/frontend-slides@9906a34](https://github.com/zarazhangrui/frontend-slides/tree/9906a34d640d2111f724544cbc50f7f130569ae1) | MIT | design | HTML-Decks auf fester 1920×1080-Bühne mit dokumentierten Fehler-Fixes. | Neu | 6.5 |
| 25 | `writing-skills` / `skill-creator` | [obra/superpowers@5bf4e78](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/writing-skills) · [anthropics/skills@34040c9](https://github.com/anthropics/skills/tree/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator) | MIT · Apache-2.0 | neues `meta` | Skills per TDD bzw. Evals messbar machen. | skill-creator ist **bereits eingebautes Plugin** | 6 |
| 26 | `property-based-testing`, `differential-review` + `fp-check` | [trailofbits/skills@32e34f8](https://github.com/trailofbits/skills/tree/32e34f8173796e3566a51aee877dc96bc5191f64/plugins) | **CC-BY-SA-4.0** | neues `security-testing` (CC-BY-SA) | Starke PBT-Entscheidungsregeln bzw. ein Gate gegen False Positives in Security-Reviews. | Nur in separatem Share-Alike-Plugin | 6.5 |
| 27 | `variance-analysis` | [anthropics/knowledge-work-plugins@1bd4282](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/finance/skills/variance-analysis) | Apache-2.0 | product | Plan-Ist-Zerlegung, die zur Gesamtsumme reconcilen muss. | Neu, aber Nischen-Publikum (FP&A) | 6 |
| 28 | `scientific-critical-thinking` | [K-Dense-AI/claude-scientific-skills@49c6e97](https://github.com/K-Dense-AI/claude-scientific-skills/tree/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/scientific-critical-thinking) | MIT | `research-tools` (MIT) | GRADE/RoB-Evidenzbewertung für Claims. | Teilweise `academic-paper-reviewer` (NC) | 6 |
| 29 | `markitdown` | [K-Dense-AI/claude-scientific-skills@49c6e97](https://github.com/K-Dense-AI/claude-scientific-skills/tree/49c6e97775eaa18ba791bebe23162a70ae601c18/skills/markitdown) | MIT | `research-tools` (MIT) | Legale Office/PDF→Markdown-Ingestion. | Neu, aber dünner Wrapper | 5.5 |

**Hinweis zur Lizenzlage:** Die Plugins `engineering`, `product` und `design` sind heute reine MIT-Plugins. Mit Apache-2.0-Skills wird daraus „MIT + Apache-2.0 (je Skill)“. Beide Lizenzen sind permissiv und kommerziell nutzbar. Dafür braucht es: LICENSE.txt im Skill-Ordner bzw. `LICENSES/`, einen NOTICE-Eintrag, einen Vermerk über Änderungen („modified by ultimate-skills“) und eine Zeile in `PROVENANCE.csv`. CC-BY-SA gehört **nie** in ein MIT-Plugin.

## 3. Die Top 10 im Detail

### 1. `diagnosing-bugs` → Merge in `debugging-and-error-recovery`
- **Was es bringt:** Der bestehende Debugging-Skill (300 Zeilen) beschreibt „reproduce → localize → reduce → fix → guard“. Er erzwingt aber nicht, *dass* die Reproduktion tatsächlich existiert. `diagnosing-bugs` macht genau das zur harten Bedingung.
- **Mechanismus:** Phase 1 ist erst abgeschlossen, wenn es **einen** benannten Befehl gibt, der bereits ausgeführt wurde, auf genau dieses Symptom rot geht und deterministisch, schnell und unbeaufsichtigt läuft. Dazu kommt eine priorisierte Liste mit 10 Loop-Typen (Test → curl → CLI-Snapshot → Headless → Trace-Replay → Harness → Fuzz → `git bisect run` → Differential → HITL-Skript). Bei Flakes wird die Reproduktionsrate erhöht, statt eine saubere Repro zu erzwingen. Danach folgen 3–5 falsifizierbare, gerankte Hypothesen und Debug-Logs mit eindeutigem Präfix, damit das Aufräumen ein einziger grep ist. Secrets werden redigiert.
- **Einarbeitung:** **Mergen.** Phase 1 (Feedback-Loop plus Completion-Kriterium), die Regel zu Hypothesen und getaggte Logs kommen als neuer Kern an den Anfang von `debugging-and-error-recovery`. Die bestehenden fehlerspezifischen Triage-Abschnitte bleiben. `scripts/hitl-loop.template.sh` wird mitgenommen, `agents/openai.yaml` verworfen. Der CONTEXT.md-Verweis wird generisch formuliert („Architektur-Doku/ADRs, falls vorhanden“).
- **Voraussetzungen:** Bash.
- **Risiken:** Der Merge verändert einen bestehenden addyosmani-Skill. Die Provenienz muss beide Quellen nennen, Attribution MIT+MIT.

### 2. `web-interface-guidelines` → neuer Skill `design/web-interface-review`
- **Was es bringt:** Ein lint-artiger UI-Review-Pass, den es heute nicht gibt. Findings kommen als `file:line`.
- **Mechanismus:** 190 Zeilen, jede Regel im Code prüfbar und mit konkretem Fix, z. B. kein `outline-none` ohne Ersatz, `min-w-0` an Flex-Kindern, `tabular-nums`, `autocomplete` an Inputs, kein Paste-Blocking, kein `transition: all`, Hydration- und Dark-Mode-Fallen.
- **Einarbeitung:** **As-is übernehmen, aber inline.** Der Vercel-Skill in `vercel-labs/agent-skills` lädt `command.md` zur Laufzeit per WebFetch. Stattdessen wird `command.md` zum Commit gepinnt eingebettet, mit einer schlanken SKILL.md-Frontmatter und Trigger-Beschreibung. React/Next/Tailwind-spezifische Regeln werden als „stack-spezifisch“ markiert.
- **Voraussetzungen:** Keine.
- **Risiken:** Gering. Die Regeln veralten langsam, deshalb bei jedem Update neu pinnen.

### 3. `verification-before-completion` → neuer Skill `engineering/verification-before-completion`
- **Was es bringt:** Adressiert den häufigsten Agentenfehler, nämlich Erfolg zu melden, ohne ihn geprüft zu haben. Mit 120 Zeilen ist er praktisch kostenlos und gilt für jede Aufgabe.
- **Mechanismus:** IDENTIFY → RUN (frisch, vollständig) → READ (Exit-Code, Fehler zählen) → VERIFY → erst dann CLAIM. Eine Tabelle ordnet jeder Behauptung die nötige Evidenz zu („Linter ≠ Build“, „Agent-Report ≠ Diff, VCS-Diff prüfen“). Für Regressionstests gibt es den Red-Green-Revert-Check.
- **Einarbeitung:** **Kürzen.** Der Ton wird entschärft („Skip any step = lying“ → sachlich), der Abschnitt „Rationalization Prevention“ gestrafft. Der Skill wird als Checkpoint von `subagent-driven-development`, `incremental-implementation` und `test-driven-development` verlinkt.
- **Voraussetzungen:** Keine.
- **Risiken:** Teilweise Doppelung mit den „Verification“-Abschnitten der addyosmani-Skills. Das ist akzeptabel, weil nur dieser Skill auf Abschluss-Behauptungen triggert.

### 4. `mcp-builder` → neuer Skill `engineering/mcp-builder`
- **Was es bringt:** Eine ganze fehlende Disziplin: MCP-Server bauen, die ein LLM tatsächlich gut bedienen kann.
- **Mechanismus:** 4 Phasen (Research/Plan → Implementieren → Review/Test → Evaluieren). Die Best-Practices-Referenz behandelt Tool-Naming, Pagination, Antwortformate, handlungsleitende Fehler, Kontextbudget sowie API-Abdeckung vs. Workflow-Tools. Der Kern ist `scripts/evaluation.py`: 10 verifizierte QA-Paare als XML messen, ob ein LLM mit den Tools echte Aufgaben löst.
- **Einarbeitung:** **As-is übernehmen**, inklusive `reference/` (wird bei Bedarf geladen) und `scripts/`. `LICENSE.txt` bleibt, mit NOTICE-Eintrag.
- **Voraussetzungen:** Node oder Python, MCP-SDK, Anthropic-API-Key für die Eval.
- **Risiken:** Die Spec-Versionen in den Referenzen veralten, deshalb halbjährlich prüfen. Die Referenzen umfassen etwa 2000 Zeilen, werden aber nur on-demand geladen.

### 5. `subagent-driven-development` → neuer Skill `engineering/subagent-driven-development` (Welle 2)
- **Was es bringt:** Kein Skill im Katalog führt einen Plan mit Subagents aus. Dieser löst dabei den teuersten beobachteten Fehler: Nach einer Compaction verliert der Controller den Faden und dispatcht erledigte Tasks erneut.
- **Mechanismus:** Eine Ledger-Datei in einem git-ignorierten Workspace ist die Wahrheit, nicht das Gedächtnis. Eine Pre-Flight-Tabelle prüft den Plan auf Konflikte. Konflikte werden als `Ruling: was — warum — Kosten falls falsch` festgehalten, statt anzuhalten. Es gibt genau vier benannte Stop-Bedingungen, Modell-Stufen je Rolle und maximal 5 Fix-Runden; ab Runde 4 übernimmt ein frischer, stärkerer Implementer. Am Ende läuft ein Review über den ganzen Branch.
- **Einarbeitung:** **Als Bundle übernehmen und entkoppeln.** Mitgenommen werden `implementer-prompt.md`, `task-reviewer-prompt.md`, `re-review-prompt.md` und `scripts/`. Die Verweise `superpowers:using-git-worktrees` und `superpowers:finishing-a-development-branch` werden durch `git-workflow-and-versioning` ersetzt. Der Verweis `../requesting-code-review/code-reviewer.md` wird durch `code-review-and-quality` ersetzt oder der Reviewer-Prompt eingebettet. „Never pause between tasks“ wird zu „pausiert nur bei den 4 Stop-Bedingungen“ entschärft. Als Checkpoint wird `verification-before-completion` verlinkt.
- **Voraussetzungen:** Subagent/Task-Tool, git, eine Plan-Datei.
- **Risiken:** Hohe Token-Kosten (etwa 1050 Zeilen inklusive Prompts). Das Umschreiben der Referenzen ist echte Arbeit, deshalb Welle 2.

### 6. `review-animations` + `STANDARDS.md` → neuer Skill `design/motion-craft`
- **Was es bringt:** Macht „fühlt sich poliert an“ entscheidbar. Motion ist die größte Lücke zwischen Amateur-UI und Premium-UI, und `design-taste-frontend` hat dafür keinen Review-Prozess.
- **Mechanismus:** Eine Frequenztabelle legt fest, dass Tastatur-Aktionen und Aktionen mit 100+ Aufrufen pro Tag nicht animiert werden. Enter/Exit nutzen ein starkes Custom-Ease-out, nie ease-in. UI-Motion bleibt unter 300 ms. Popover skalieren von der transform-origin des Triggers aus, nie von `scale(0)`. Animationen müssen unterbrechbar sein, nur transform/opacity werden animiert, Reduced-Motion und Hover-Media werden gegated.
- **Einarbeitung:** **Kürzen und mergen.** `review-animations/SKILL.md` (120 Zeilen) und `STANDARDS.md` (187 Zeilen) bilden die Basis. Aus `emil-design-eng` kommt nur das „Soll das überhaupt animieren?“-Framework und die Before/After/Why-Tabelle dazu. Die Persona-Anweisung „Initial Response“ fällt weg. `disable-model-invocation: true` (im Clone bestätigt) wird entfernt, damit der Skill bei UI-Motion-Arbeit automatisch triggert.
- **Voraussetzungen:** Keine. Die Beispiele verwenden CSS und Framer Motion.
- **Risiken:** Web- und React-lastig.

### 7. `interface-design` → neuer Skill `design/interface-design`
- **Was es bringt:** `design-taste-frontend` sagt selbst (Zeile 8): „Not dashboards, not data tables, not multi-step product UI.“ Genau diese Lücke schließt der Skill.
- **Mechanismus:** Ein Intent-Brief (Person, Aufgabenverb, Gefühl) und eine Domain-Exploration: 5+ Domänenkonzepte, eine Farbwelt, ein Signature-Element und 3 benannte Defaults, die vermieden werden sollen. Dazu harte Hierarchie-Regeln: ein Fokuspunkt, eine Type-Scale mit durchgerechneten px-Werten (14px@1.25), Gewicht und Farbe statt Größe, Dichte in px. Der Test lautet: Produktname entfernen – erkennt man noch, wofür die UI ist?
- **Einarbeitung:** **As-is übernehmen, leicht kürzen** (prosa-lastige Passagen). Der Skill wird aus `design-taste-frontend` als Weiterleitung für Product-UI verlinkt.
- **Voraussetzungen:** Keine.
- **Risiken:** Keine Skripte; die Verifikation ist reine Selbstkritik. Mit `web-interface-review` und `motion-craft` kombinieren.

### 8. `humanizer` → neues Plugin `writing` (MIT)
- **Was es bringt:** Prosa ist heute gar nicht abgedeckt, obwohl PRDs, ADRs und Memos Prosa sind. Der Skill ist ein sicherer Schlussdurchgang für jede Text-Ausgabe.
- **Mechanismus:** 25 Muster, nach Stärke gewichtet. Muster 1–5 rechtfertigen einen Eingriff schon bei einmaligem Auftreten, schwächere nur in Kombination. Der Ablauf ist mark → draft → check → final. Es werden **keine** Fakten, Namen, Zahlen oder Zitate hinzugefügt, und verlorene Claims zählen als Fehler. Voice-Matching erfolgt über eine Stichprobe. Ein Datei-Modus lässt Code, YAML und Links unangetastet.
- **Einarbeitung:** **As-is übernehmen** (374 Zeilen) und nur auf expliziten Auftrag triggern lassen. `agents/openai.yaml` entfällt. Der Skill wird als finaler Pass nach `copy-editing` positioniert.
- **Voraussetzungen:** Keine.
- **Risiken:** Auf Englisch getunt. Kann mit Hausstilen kollidieren, die Gedankenstriche oder Fett-Labels nutzen; die Voice-Stichprobe hat Vorrang.

### 9. `minto-pyramid` → Plugin `writing`
- **Was es bringt:** Answer-first-Struktur für Entscheidungsdokumente. `minto-pyramid` ordnet die Argumente, `humanizer` glättet den Stil.
- **Mechanismus:** Ein Step-0-Gate verweigert die Pyramide für Timelines, Runbooks und Tutorials. Danach folgen SCQA und die Minto-Logikprüfung. Neues Wissen oder eigene Arithmetik ist verboten. Die mitgelieferte Eval-Suite (`evals/cases.json`, `RESULTS.md`) dokumentiert, wie ein Verbotsregel-Fehler durch einen positiven Output-Contract behoben wurde. Das ist zugleich ein gutes Vorbild für alle anderen Skills.
- **Einarbeitung:** **As-is übernehmen** (161 Zeilen, mit `evals/`). Aus `tyroneross/pyramid-principle` (Apache-2.0) kommt **optional** nur `pyramid-audit` dazu: Ein 5-Check-Audit mit festem Verdikt (Share as-is / Minor edits / Restructure) und Quellanker je Finding, falls ein Review-Modus gewünscht ist. Die übrigen 5 tyroneross-Skills (~3k Zeilen Referenzen) werden nicht übernommen.
- **Voraussetzungen:** Keine.
- **Risiken:** Die Evals liefen nur auf Sonnet.

### 10. `validate-data` → `product` (oder neues Plugin `data`)
- **Was es bringt:** Den fehlenden „Check your work“-Schritt für alle Analyse-Skills. Er ist das Analytics-Gegenstück zu `code-review-and-quality`.
- **Mechanismus:** 8 Schritte: Methodik, Pre-Delivery-Checkliste, Pitfall-Katalog mit Detektion (Join-Explosion samt Row-Count-SQL, Survivorship Bias, unvollständige Perioden, Nenner-Verschiebung, Durchschnitt von Durchschnitten, Zeitzonen, Selektion auf das Outcome, Simpson), Nachrechnen der Kernzahlen, Chart-Integrität und die Frage, ob das Narrativ aus den Daten folgt. Ergebnis ist ein Verdikt (Ready / Share with caveats / Needs revision) plus Pflicht-Caveats.
- **Einarbeitung:** **Kürzen.** Der `CONNECTORS.md`-Verweis (Zeile 9) und die `/validate-data`-Usage-Blöcke (Zeilen 16 und 367–375) fallen weg. `explore-data` und `statistical-analysis` werden vorerst nicht übernommen.
- **Voraussetzungen:** Zugriff auf die Analyse (eingefügt, SQL oder Datei).
- **Risiken:** Die SQL-Beispiele setzen ein Data-Warehouse voraus. Apache-2.0-Attribution ist nötig.

**Knapp dahinter (ohne eigenen Abschnitt):** `obviously-awesome` (Welle 1-fähig), `iterate-pr`, `gha-security-review` und `good-strategy-bad-strategy`. Details siehe Tabelle und Plan.

## 4. Verworfen

| Kandidat | Grund |
|---|---|
| `anthropics/skills` → `doc-coauthoring` | **Keine Lizenz** (kein LICENSE.txt im Ordner, keine Frontmatter-Lizenz, kein Root-LICENSE, im Clone geprüft). Nur die Idee „Reader Testing mit kontextfreiem Subagent“ darf in eigenen Worten nachgebaut werden. |
| `anthropics/skills` → `docx`/`pdf`/`pptx`/`xlsx` | Proprietär („All rights reserved“). |
| `appautomaton/document-SKILLs` | Nahezu wörtliche MIT-Umetikettierung der proprietären Anthropic-Skills, also License Laundering. |
| `SonOfBytes/skills-postgres` | Inhaltlich der beste Postgres-Skill, aber **ohne Lizenz**. |
| `indi256s/dataviz-skill` | Ohne Lizenz. |
| `deanpeters/Product-Manager-Skills` (business-health-diagnostic u. a.) | CC-BY-NC-SA, nicht kommerziell. `saas-metrics-coach` (MIT) deckt den Bereich ab. |
| `trailofbits` → `agentic-actions-auditor` | CC-BY-SA; `gha-security-review` (Apache) deckt den Kern ab. Nur verlinken. |
| `nextlevelbuilder/ui-ux-pro-max-skill` | 3,1 MB CSV-DB, die genau die Default-Cluster erzeugt, die die Anti-Slop-Skills verbieten (Test: „fintech dashboard“ → Slate #0F172A + Grün). |
| `raphaelsalaja/userinterface-wiki` | Duplikat von Motion (Emil) und Vercel-Guidelines. Einzig Audio-UI und Prefetch sind neu; das rechtfertigt keinen eigenen Skill. |
| `anthropics/skills` → `frontend-design` | Duplikat von `design-taste-frontend`. Die Liste der Default-Cluster und der Zwei-Pass-Plan-Check werden als Idee in `design-taste-frontend` übernommen (mit Apache-Attribution), nicht als eigener Skill. |
| `masuP9/a11y-specialist-skills` | Duplikat von `wcag-2.2-aa`. Nur „NT statt raten“ und der Mockup-Review-Pfad werden in den 84em-Skill gemergt. `npx`-CLI und `mcp__playwright__*`-Frontmatter werden verworfen. |
| `tyroneross/pyramid-principle` (5 von 6 Skills) | Duplikat von `minto-pyramid`, ~3k Zeilen Referenzen. Nur `pyramid-audit` ist optional (siehe #9). |
| `anthropics/knowledge-work-plugins` → `data-visualization` | Der eingebaute `/dataviz`-Skill ist stärker (mit Palette-Validator). Dieser ist Notebook-lastig und generisch. |
| `anthropics/knowledge-work-plugins` → `memory-management` | Überschneidet sich mit Claude-Code-Memory. Schreibt Personendaten über Kollegen in Repo-Dateien (Datenschutz). |
| `coreyhaines31` → `cro`/`signup`/`onboarding`/`churn-prevention` | Breite, aber generische Best-Practice-Listen ohne eigenen Mechanismus, 1231 Zeilen. Zurückgestellt; frühestens `churn-prevention` ohne Vendor-Abschnitt. |
| `coreyhaines31` → übrige ~45 Marketing-Skills, `tools/` | Sponsor- und Partner-Inhalte, starke Querverlinkung, Bloat. |
| `obra/superpowers` → `systematic-debugging` | Duplikat von `diagnosing-bugs` plus bestehendem Debugging-Skill. Nur `find-polluter.sh` käme als Helper in Frage. |
| `muratcankoylan` → `advanced-evaluation`, `hosted-agents`, `bdi-mental-states` | Zielgruppe sind Agent-Builder; teils dangling `claim-*`-IDs. Überschneidet sich mit den skill-creator-Gradern. |
| `neondatabase/postgres-skills` | Apache-2.0 und brauchbar, aber als eigener Skill redundant zu Supabase. Nur die Migrations-, Backup- und Upgrade-Referenzen dienen als Quelle für einen Migrations-Addendum (Welle 2). |
| `anthropics/financial-services-plugins` → `audit-xls` | Setzt einen Excel-Add-in-Kontext („selected range“) voraus. |
| `K-Dense` → `search_google_scholar.py` | Scraping, ToS-Risiko, fragil. |

## 5. Einarbeitungsplan in Wellen

Für **jede** Übernahme gilt dieselbe Checkliste: Upstream-LICENSE nach `LICENSES/` kopieren (bei Apache zusätzlich `LICENSE.txt` im Skill-Ordner und einen NOTICE-Hinweis auf Änderungen), eine Zeile in `PROVENANCE.csv` (Repo, Commit-SHA, Pfad, Lizenz, „modified: ja/nein“), einen NOTICE.md-Eintrag hinzufügen, das Verzeichnis nach der `name:`-Frontmatter benennen, fremde Cross-Links (`superpowers:*`, wondelai- und coreyhaines-Geschwister) auf Katalog-Skills umbiegen oder löschen, und die README-Tabelle aktualisieren.

### Welle 1: No-Brainer (permissiv, geringe Überschneidung, wenig Umbau)
| Skill | Aktion | Ziel |
|---|---|---|
| `web-interface-guidelines` | inline eingebettet, gepinnt | design |
| `verification-before-completion` | Ton entschärfen, kürzen | engineering |
| `diagnosing-bugs` | in `debugging-and-error-recovery` mergen | engineering |
| `mcp-builder` | as-is (Apache) | engineering |
| `interface-design` | as-is, leicht kürzen | design |
| `review-animations` + `STANDARDS.md` | als `motion-craft` kürzen, auto-invoke | design |
| `humanizer` | as-is | neues Plugin `writing` (MIT) |
| `minto-pyramid` | as-is inkl. `evals/` | `writing` |
| `obviously-awesome` | Cross-Links bereinigen, Referenzen auf Langzitate prüfen | product |

Danach umfasst der Katalog etwa 47 Skills und 5 Plugins. `writing` wird im Marketplace-Manifest eingetragen.

### Welle 2: Hoher Wert, aber Umbau oder Entkopplung nötig
- `subagent-driven-development` als Bundle entkoppeln (siehe #5), mit Verweis auf `verification-before-completion`.
- `iterate-pr` generalisieren (Sentry-Bots `sentry`/`warden`/`seer` → konfigurierbare Bot-Liste); `receiving-code-review` wird als Abschnitt „Feedback annehmen“ eingebettet (Formel „your human partner“ entfernen).
- `gha-security-review` (Apache) als `engineering/gha-security-review` übernehmen.
- `validate-data` (Connector- und Slash-Command-Reste entfernen) nach `product`.
- `good-strategy-bad-strategy` nach `product`, Paar-Verlinkung mit `strategy-red-team`.
- `saas-metrics-coach` inkl. Skripte nach `product`; Benchmarks als Heuristik kennzeichnen, Autor „Abbas Mir“ in PROVENANCE nennen.
- `supabase-postgres-best-practices` nach `engineering` plus ein kleiner eigener Migrations-Addendum (expand/contract, `lock_timeout`, `CREATE INDEX CONCURRENTLY`), gestützt auf Neon-Referenzen (Apache).
- `wcag-2.2-aa` genericisieren (84EM-, WordPress- und VPAT-Framing raus), masuP9-Ideen einmergen, W3C-Spec nur on-demand und mit Copyright-Hinweis.
- `startup-competitors`: Honesty-Protocol und Verification-Agent in `competitor-analysis` mergen, nicht als eigenen Skill.
- `copy-editing` + `product-marketing` (Kontextdatei von `.agents/` in eine neutrale Konvention umbenennen) nach `writing` oder `product`.

### Welle 3: Optional, Nische oder Lizenz-Isolation
- **Neues Plugin `security-testing` (CC-BY-SA-4.0, isoliert wie `research/`):** `property-based-testing`, `differential-review` + `fp-check` (Smart-Contract-Bias beachten; `allowed-tools` bereinigen).
- **Neues Plugin `research-tools` (MIT):** `citation-management` (ohne Google-Scholar), `scientific-critical-thinking` (OpenRouter-Abschnitt entfernen), `markitdown`. Damit bekommt das NC-`research`-Plugin eine kommerziell nutzbare Verifikationsschicht.
- `long-horizon-prompting` (mit `references/`, damit die `claim-*`-IDs aufgelöst werden) nach `engineering`.
- `impeccable`: nur `craft-floor.md` + `critique.md` (ohne die Binary-Aufrufe) als Referenzen in `redesign-existing-projects` mergen; Apache-NOTICE und Änderungsvermerk.
- `frontend-slides` ohne `deploy.sh` und `bold-template-pack` nach `design`.
- `customer-research`, `variance-analysis`: nur bei konkretem Bedarf.
- `writing-skills` / `skill-creator`: Nur wenn der Marketplace unabhängig vom eingebauten `anthropic-skills:skill-creator` sein soll. Dann eher `writing-skills` (MIT, Verweis auf `engineering/test-driven-development` umbiegen) als ein neues `meta`-Plugin. Der Wert liegt vor allem darin, **künftige Kurationsrunden** mit Evals abzusichern.
