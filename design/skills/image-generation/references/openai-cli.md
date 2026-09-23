# OpenAI Images: CLI and API reference (`scripts/image_gen.py`)

> Merged and adapted from [openai/skills](https://github.com/openai/skills) `skills/.system/imagegen/references/cli.md` and `image-api.md` at commit `49f948f` (Apache-2.0). **Modified by ultimate-skills:** the CLI is the primary OpenAI path here (not a Codex "explicit-only fallback"); `$CODEX_HOME` paths replaced; model list, sizes and parameters updated for GPT Image 2 / 2.5 (from OpenAI docs as summarised by [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) `references/models.md`, MIT, checked 2026-09-09). Licensed under the Apache License 2.0 (see `../LICENSE.txt`).

## What the CLI does

- `generate`: new image(s) from a prompt → `POST /v1/images/generations`
- `edit`: edit one or more existing images (optional mask) → `POST /v1/images/edits`
- `generate-batch`: many different prompts from a JSONL file, run concurrently

Real API calls need **network access to api.openai.com** and `OPENAI_API_KEY`. `--dry-run` needs neither (and does not need the `openai` package) - use it to show the user the exact request before a paid call.

## Setup

```bash
pip install openai          # or: uv pip install openai
pip install pillow          # optional, only for --downscale-max-dim
export OPENAI_API_KEY=...   # set in the shell / secret store; never paste it into chat
```

Run the script from the skill folder path; in a Claude Code plugin install that is `${CLAUDE_PLUGIN_ROOT}/skills/image-generation/scripts/image_gen.py`. Below, `$IMAGE_GEN` stands for that path.

## Models (verify before relying on them - IDs change)

| Model | Use for | Notes |
|---|---|---|
| `gpt-image-2` (script default) | In-image text, posters, UI mockups, infographics, multi-reference compositing, batches of variants | **No `background=transparent`.** `input_fidelity` must be omitted (the script drops it). |
| `gpt-image-2.5-flare` | Fast everyday generation and drafts | Quality also accepts `xhigh`, `max`. Transparent background supported. There is no bare `gpt-image-2.5` ID. |
| `gpt-image-2.5-sunburst` | Precise reference edits, detail-sensitive work | As above. Dated snapshots end in `-2026-09-08`. |
| `gpt-image-1.5` | Native transparent PNG cutouts / icons when 2.5 is not available | Legacy sizes only; weaker text rendering. |
| `gpt-image-1`, `gpt-image-1-mini` | Legacy / cheapest drafts | Legacy sizes only. |

Override the default with `--model` or the `IMAGEGEN_OPENAI_MODEL` environment variable. If the user names an ambiguous model ("GPT 2.5"), ask which one instead of guessing; never switch models silently after an error. Some accounts need **organization verification** before GPT Image models work - a 403 on the first call usually means that.

## Parameters

| Parameter | Values | Notes |
|---|---|---|
| `--size` | `auto`, `1024x1024`, `1536x1024`, `1024x1536`; GPT Image 2 / 2.5 also any `WIDTHxHEIGHT` | 2 / 2.5: edges multiples of 16, max edge 3840, long:short ≤ 3:1, 655,360–8,294,400 total pixels; above 2560×1440 is experimental. Examples: `1536x864` (16:9), `2048x864` (≈21:9 banner), `1024x1280` (4:5), `864x1536` (9:16). |
| `--quality` | `low`, `medium`, `high`, `auto`; 2.5 also `xhigh`, `max` | Cost/latency dial. `low` for exploration, `medium`/`high` for finals; discuss cost before `xhigh`/`max`. |
| `--n` | 1–10 | Variants of **one** prompt. More than 1 needs the user's OK (each is billed). |
| `--background` | `transparent`, `opaque`, `auto` | Output transparency, not the scene backdrop. Transparent needs `png`/`webp` and a model that supports it. |
| `--output-format` | `png` (default), `jpeg`, `webp` | |
| `--output-compression` | 0–100 | jpeg/webp only. |
| `--moderation` | `auto` (default), `low` | |
| `--image` (edit) | repeatable, up to 16 | Order matters - describe each by index and role in the prompt. Under 50 MB each. |
| `--mask` (edit) | one PNG with alpha | Masking is prompt-guided; exact shapes are not guaranteed. |
| `--input-fidelity` (edit) | `low`, `high` | Not for `gpt-image-2`. `gpt-image-1.5` preserves the first 5 inputs at higher fidelity; `high` raises input-token cost. |

Output is `data[].b64_json`; the script decodes and writes files. A 200 response is not proof the image is right - always inspect it.

## Quick start

Dry-run (no API call):

```bash
python3 "$IMAGE_GEN" generate --prompt "Test" --out output/imagegen/test.png --dry-run
```

Generate:

```bash
python3 "$IMAGE_GEN" generate \
  --prompt "A cozy alpine cabin at dawn" \
  --size 1536x864 --quality medium \
  --out output/imagegen/alpine-cabin.png
```

Edit (invariants in the prompt):

```bash
python3 "$IMAGE_GEN" edit \
  --image public/img/hero.png \
  --prompt "Replace only the background with a warm sunset; keep the product, its edges and label text unchanged" \
  --out public/img/hero-sunset.png
```

Transparent cutout / icon:

```bash
python3 "$IMAGE_GEN" generate --model gpt-image-1.5 \
  --prompt "Minimal ceramic mug product cutout, soft studio light, no text" \
  --background transparent --output-format png \
  --out public/img/mug-cutout.png
```

Generate with the structured-prompt fields (the script assembles the labeled spec from `SKILL.md`; pass `--no-augment` to send the prompt as-is):

```bash
python3 "$IMAGE_GEN" generate \
  --prompt "A minimal hero image of a ceramic coffee mug" \
  --use-case "product-mockup" \
  --style "clean product photography" \
  --composition "wide product shot with usable negative space for page copy" \
  --constraints "no logos, no text" \
  --out output/imagegen/mug-hero.png
```

Also write a downscaled web copy (`-web` suffix, needs Pillow):

```bash
python3 "$IMAGE_GEN" generate --prompt "..." --downscale-max-dim 1600 --out public/img/hero.png
```

Batch of different prompts (confirm the count and cost with the user first):

```bash
mkdir -p tmp/imagegen output/imagegen/batch
cat > tmp/imagegen/prompts.jsonl << 'EOF'
{"prompt":"Cavernous hangar interior with a compact shuttle parked near the center","use_case":"stylized-concept","composition":"wide-angle, low-angle","lighting":"volumetric light rays through drifting fog","constraints":"no logos or trademarks; no watermark","size":"1536x1024"}
{"prompt":"Gray wolf in profile in a snowy forest","use_case":"photorealistic-natural","composition":"eye-level","constraints":"no logos or trademarks; no watermark","size":"1024x1024"}
EOF

python3 "$IMAGE_GEN" generate-batch --input tmp/imagegen/prompts.jsonl --out-dir output/imagegen/batch --concurrency 5
rm -f tmp/imagegen/prompts.jsonl
```

## Behaviour notes

- Reruns fail if a target file already exists unless you pass `--force`. Prefer a versioned sibling name (`hero-v2.png`) over `--force`.
- `--out-dir` names one-off outputs `image_1.<ext>`, `image_2.<ext>`, ...; in batch mode a per-job `out` is a filename under `--out-dir`.
- Per-job JSONL overrides: `size`, `quality`, `background`, `output_format`, `output_compression`, `moderation`, `n`, `model`, `out`, and the prompt fields (`use_case`, `scene`, `subject`, `style`, `composition`, `lighting`, `palette`, `materials`, `text`, `constraints`, `negative`).
- Single `generate`/`edit` calls never retry (SDK retries disabled). `generate-batch` retries only rate-limit (429) and timeout errors, up to `--max-attempts` (default 3); policy, auth and quota errors are reported, not retried.
- Generation can take up to ~2 minutes on complex prompts; the client timeout is 300 s.
- Do not write one-off SDK runners for normal requests; if the script lacks something, say what is missing.
