# research

## Overview
Rigorous research and academic-writing pipelines: a universal **deep-research** agent team, a multi-agent **academic-paper** writing pipeline, a 5-reviewer **peer-review** simulation, and the **academic-pipeline** orchestrator that chains them (research → write → integrity → review → revise). The four skills are self-contained as a set: the cross-skill protocols and JSON contracts they cite as `shared/...` are vendored in [`shared/`](./shared/). The `scripts/*.py` validators and `docs/design/...` specs mentioned in the skills live only in the [upstream repo](https://github.com/Imbad0202/academic-research-skills/tree/ebc21bf2429643fe4c2495aa99e1bbacd926772b) (pinned at `ebc21bf`, upstream v3.23.0) and are optional/advisory. Upstream's fifth skill, `sr-screener`, and its `/ars-*` slash commands are not included; the skills mark them as "not included here". Curated from [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills).

## ⚠️ License — non-commercial
This plugin is **CC-BY-NC-4.0** (© 2026 Cheng-I Wu) — **attribution required, non-commercial use only, no relicensing**. It is the only non-commercial plugin in this marketplace and is isolated here so you can drop it for a commercially usable set. See [`LICENSE`](./LICENSE) and [`../NOTICE.md`](../NOTICE.md).

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install research@ultimate-skills
```

## Skills
4 skills (see the table in the [root README](../README.md#research)): `deep-research`, `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`.

These are heavy multi-agent pipelines; expect long, structured runs. Note Claude Code also ships a built-in `deep-research` skill for lighter needs.

## Local restructuring and upstream syncs
To keep each `SKILL.md` under 500 lines, all four skills were restructured locally (`deep-research`, `academic-paper` and `academic-pipeline` in wave 3, `academic-paper-reviewer` in upstream sync 2): whole sections were moved verbatim from `SKILL.md` into new files under `references/`, and `SKILL.md` keeps each heading with a short summary of the rules that always apply and a "Read references/X.md when …" pointer. Upstream still has those sections inline. Before merging upstream changes into these skills, read [`MERGE_MAPS.md`](./MERGE_MAPS.md): it maps every moved section to its new file and gives the sync procedure and a check that no upstream line was dropped.

## License
CC-BY-NC-4.0. See [`LICENSE`](./LICENSE) and [`../NOTICE.md`](../NOTICE.md).
