# Providers and model routing

> Model-selection matrix, web-asset purpose table, Gemini REST pattern, multi-turn editing note and common-mistakes table adapted from [jezweb/claude-skills](https://github.com/jezweb/claude-skills) `plugins/design-assets/skills/ai-image-generator` at commit `e875a6b` (MIT, (c) 2025 Jeremy Dawes). **Changes:** advert for a managed service, author-specific save paths and regional advice removed; the outdated claim that Gemini cannot render text corrected; model IDs aligned with the official lists in [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) (`gemini-api-dev`, commit `eaa2325`) and GPT Image 2.5 notes from [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) (MIT, checked 2026-09-09); inline heredoc calls replaced by the bundled scripts; API key moved from URL query to header; hard-coded prices dropped (they drift - check the provider's pricing page).

**Model IDs change often.** Before the first live call in a session, verify: `python3 scripts/gemini_image.py --list-models` for Gemini, and the OpenAI models page (or a failed call's error message) for GPT Image. Never invent an ID.

## Which model for which job

| Need | First choice | Why / fallback |
|---|---|---|
| Photoreal scenes, lifestyle, stock-style photos, environmental depth | Gemini `gemini-3.1-flash-image` (Nano Banana 2) | Strong depth and scene complexity; fast. Final client work at higher detail: `gemini-3-pro-image` (Nano Banana Pro). |
| Readable in-image text: posters, OG images with headlines, infographics, pricing cards, UI mockups, multi-script copy | `gpt-image-2` or `gpt-image-2.5-*` | Most reliable typography. Nano Banana Pro also renders text well; check spelling either way. |
| Many variants of one idea (style exploration, A/B options) | `gpt-image-2` with `--n` up to 10 | Variants share composition and palette. Ask before paying for more than one. |
| Multi-reference compositing (product into a lifestyle scene, logo onto packaging) | `gpt-image-2` / `gpt-image-2.5-sunburst` edit, or Gemini with several `--image` inputs (Pro accepts up to 14) | Label each input by index and role. |
| Precise edits that must preserve everything else | `gpt-image-2.5-sunburst` edit, or Gemini edit | Repeat invariants every iteration. |
| **Transparent PNG** (icons, cutouts, stickers) | `gpt-image-1.5` or a `gpt-image-2.5-*` model with `--background transparent` | **`gpt-image-2` cannot do transparency; Gemini returns no alpha.** Alternative: generate on a flat chroma background and cut out locally. |
| Cheap, fast drafts | `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) or GPT Image `--quality low` | Promote the winning direction to a stronger model. |
| Consistent vector icon sets, logos matching an existing SVG system | **Not an image model** - use `icon-set-generator` or edit the SVG | Bitmaps don't scale or theme. |

Rule of thumb: any image whose value depends on exact readable text → GPT Image 2/2.5 (and verify every character). Transparency → gpt-image-1.5 or 2.5. Otherwise → Gemini Flash Image for speed, Pro for finals.

## Web asset purposes

| Purpose | Aspect | Script flags (OpenAI / Gemini) |
|---|---|---|
| Hero banner, no text | 16:9 or 21:9 | `--size 1536x864` / `--aspect-ratio 16:9`; ultra-wide `--size 2048x864` / `--aspect-ratio 21:9` |
| Hero with headline baked in (rare - prefer HTML text) | 16:9 or 3:1 | GPT Image 2 `--size 2304x768` |
| Service / feature card | 4:3 or 3:4 | `--size 1024x768`-class sizes / `--aspect-ratio 4:3` |
| Profile / avatar | 1:1 | `--size 1024x1024` / `--aspect-ratio 1:1` |
| OG / social share (1200×630 target) | ≈1.91:1 | `--size 1536x800` then resize / `--aspect-ratio 16:9` then crop |
| Instagram post | 1:1 or 4:5 | `--size 1024x1280` / `--aspect-ratio 4:5` |
| Mobile hero / story | 9:16 | `--size 864x1536` / `--aspect-ratio 9:16` |
| Icon / badge / sticker (transparent) | 1:1 | `--model gpt-image-1.5 --background transparent` |
| Tileable texture / background pattern | 1:1 | say "seamless tileable" in the prompt; verify the seams by tiling it 2×2 |

Keep headlines, buttons, nav and other UI copy in HTML/CSS, not baked into images - images with text are not accessible, not translatable and not editable. Bake text only into genuine artwork (posters, packaging, signage, product labels).

## Gemini (Nano Banana) specifics

- Endpoint: `POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`, key in the `x-goog-api-key` header. `scripts/gemini_image.py` wraps it with the standard library only.
- Current image models (per `gemini-api-dev`): `gemini-3.1-flash-image` (Nano Banana 2), `gemini-3-pro-image` (Nano Banana Pro), `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite). `gemini-2.5-*` / `gemini-2.0-*` models are legacy - don't use them.
- `generationConfig.imageConfig`: `aspectRatio` (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, plus extreme `1:4`, `4:1`, `1:8`, `8:1` on some models) and `imageSize` (`1K`, `2K`, `4K`; `512px` on Flash). The script exposes them as `--aspect-ratio` and `--image-size`.
- Inputs: pass reference or edit images with repeated `--image` (sent as inline base64, ~20 MB request limit). The text prompt says which image is the edit target and which are references.
- Responses may contain text parts ("Here is your image...") alongside the image; the script prints them as `model_text`. Output has no alpha channel.
- **Multi-turn editing** (chat-style "now make the wall blue") requires sending the previous model turn back **with its `thoughtSignature` parts intact**; dropping them breaks the edit chain. The bundled script is single-turn: to iterate, pass the previous output as `--image` and restate the invariants ("keep the people, desk and window unchanged; only change the wall color to ocean blue").
- Timeouts: allow up to ~3 minutes (`--timeout 180` default).

## GPT Image specifics

See [openai-cli.md](openai-cli.md) for flags, sizes and limits. Highlights: `gpt-image-2` has flexible sizes (multiples of 16, ≤3840, ≤3:1), no transparency, and needs `input_fidelity` omitted; 2.5 models add `xhigh`/`max` quality and transparency; generation can take ~2 minutes.

## Other providers and MCP servers

If the session already exposes an image-generation tool or MCP server (Replicate, fal, a local ComfyUI/Stable Diffusion bridge, a Gemini/OpenAI MCP, a host-native image tool), prefer it over the scripts - the prompting guidance in this skill is provider-neutral. For open-weight models (FLUX, SDXL/SD3, LoRAs), read [model-agnostic-prompting.md](model-agnostic-prompting.md): negative prompts, CFG and trigger words behave differently there.

## Common mistakes

| Mistake | Fix |
|---|---|
| Building the request with `curl` and a quoted prompt | Use the scripts - shell escaping breaks on apostrophes and newlines. |
| Key in the URL (`?key=...`) | Header only (`x-goog-api-key` / `Authorization`); URLs end up in logs and proxies. |
| "Beautiful, professional, high quality, 4K" | Concrete specs: "85mm f/1.8, golden-hour side light, shallow depth of field". Set size with flags, not words. |
| Not saying what to exclude | End with a short targeted Avoid line: "no text, no watermark, no logos". |
| Transparent PNG from `gpt-image-2` or Gemini | `gpt-image-1.5` / 2.5 with `--background transparent`, or cut out locally. |
| Treating a 200 response as success | Open the image and check text, anatomy, edges, invariants before using it. |
| Silently retrying after a 400/403/policy error | Report the error; do not reword around a safety refusal or switch models without asking. |
| Assuming yesterday's model ID still exists | `--list-models` / docs check before the first call. |
