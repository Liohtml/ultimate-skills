#!/usr/bin/env python3
"""Generate or edit images with Google Gemini image models (Nano Banana family).

Part of the ultimate-skills `image-generation` skill (MIT). Standard library
only - no SDK needed.

Environment:
  GEMINI_API_KEY (or GOOGLE_API_KEY)  required for live calls, not for --dry-run
  IMAGEGEN_GEMINI_MODEL               optional default model override

The key is sent in the `x-goog-api-key` header (never in the URL, so it does not
leak into logs or proxies) and is never printed. The script makes exactly one
request per run and never retries automatically, so a paid call is never
silently repeated.

Examples:
  python3 gemini_image.py --prompt "..." --aspect-ratio 16:9 --out public/img/hero.png
  python3 gemini_image.py --prompt "Change only the sky to dusk; keep everything else" \
      --image public/img/hero.png --out public/img/hero-dusk.png
  python3 gemini_image.py --list-models
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

API_ROOT = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = os.environ.get("IMAGEGEN_GEMINI_MODEL", "gemini-3.1-flash-image")
DEFAULT_OUT = "output/imagegen/gemini.png"
KNOWN_ASPECT_RATIOS = {
    "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9",
    "1:4", "4:1", "1:8", "8:1",
}
KNOWN_IMAGE_SIZES = {"512px", "1K", "2K", "4K"}
MAX_INPUT_BYTES = 20 * 1024 * 1024  # inline request limit is ~20 MB total
EXT_FOR_MIME = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def warn(msg: str) -> None:
    print(f"Warning: {msg}", file=sys.stderr)


def api_key(required: bool) -> Optional[str]:
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key and required:
        die(
            "GEMINI_API_KEY (or GOOGLE_API_KEY) is not set. Create a key at "
            "https://aistudio.google.com/apikey and export it in your shell; "
            "never paste it into chat.",
            2,
        )
    return key


def request(method: str, url: str, key: str, body: Optional[dict], timeout: int) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:2000]
        die(f"HTTP {exc.code} from Gemini API (no automatic retry):\n{detail}")
    except urllib.error.URLError as exc:
        die(f"Network error calling Gemini API: {exc.reason}")
    return {}  # unreachable


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt and args.prompt_file:
        die("Use --prompt or --prompt-file, not both.", 2)
    if args.prompt_file:
        p = Path(args.prompt_file)
        if not p.exists():
            die(f"Prompt file not found: {p}", 2)
        return p.read_text(encoding="utf-8").strip()
    if args.prompt:
        return args.prompt.strip()
    die("Missing prompt. Use --prompt or --prompt-file.", 2)
    return ""


def image_part(path_str: str) -> Dict[str, Any]:
    path = Path(path_str)
    if not path.is_file():
        die(f"Input image not found: {path}", 2)
    if path.stat().st_size > MAX_INPUT_BYTES:
        die(f"Input image too large for an inline request (>20 MB): {path}", 2)
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    if not mime.startswith("image/"):
        die(f"Not an image file: {path}", 2)
    return {"inline_data": {"mime_type": mime, "data": base64.b64encode(path.read_bytes()).decode()}}


def output_paths(out: str, count: int, mime: str) -> List[Path]:
    base = Path(out)
    ext = EXT_FOR_MIME.get(mime, base.suffix or ".png")
    if base.suffix and base.suffix.lower() != ext and not (base.suffix.lower() == ".jpeg" and ext == ".jpg"):
        warn(f"Model returned {mime}; writing {ext} instead of {base.suffix}.")
        base = base.with_suffix(ext)
    elif not base.suffix:
        base = base.with_suffix(ext)
    if count == 1:
        return [base]
    return [base.with_name(f"{base.stem}-{i}{base.suffix}") for i in range(1, count + 1)]


def list_models(timeout: int) -> None:
    key = api_key(True)
    data = request("GET", f"{API_ROOT}/models?pageSize=1000", key, None, timeout)
    names = [m.get("name", "").removeprefix("models/") for m in data.get("models", [])]
    for n in sorted(n for n in names if "image" in n):
        print(n)


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate or edit images with Gemini image models.")
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--image", action="append", default=[],
                    help="input image (edit target or reference); repeatable, order matters")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--aspect-ratio", help="e.g. 1:1, 16:9, 21:9, 9:16, 4:5")
    ap.add_argument("--image-size", help="1K, 2K, 4K (512px on some models)")
    ap.add_argument("--image-only", action="store_true",
                    help="request IMAGE modality only (default: TEXT and IMAGE)")
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--dry-run", action="store_true", help="print the request without calling the API")
    ap.add_argument("--list-models", action="store_true", help="list image-capable model IDs and exit")
    args = ap.parse_args()

    if args.list_models:
        list_models(args.timeout)
        return 0

    prompt = read_prompt(args)
    if args.aspect_ratio and args.aspect_ratio not in KNOWN_ASPECT_RATIOS:
        warn(f"Unusual aspect ratio {args.aspect_ratio}; the model may reject it.")
    if args.image_size and args.image_size not in KNOWN_IMAGE_SIZES:
        warn(f"Unusual image size {args.image_size}; expected one of {sorted(KNOWN_IMAGE_SIZES)}.")

    parts: List[Dict[str, Any]] = [{"text": prompt}] + [image_part(p) for p in args.image]
    gen_cfg: Dict[str, Any] = {"responseModalities": ["IMAGE"] if args.image_only else ["TEXT", "IMAGE"]}
    image_cfg = {k: v for k, v in (("aspectRatio", args.aspect_ratio), ("imageSize", args.image_size)) if v}
    if image_cfg:
        gen_cfg["imageConfig"] = image_cfg
    body = {"contents": [{"role": "user", "parts": parts}], "generationConfig": gen_cfg}
    url = f"{API_ROOT}/models/{args.model}:generateContent"

    if args.dry_run:
        preview = json.loads(json.dumps(body))
        for p in preview["contents"][0]["parts"]:
            if "inline_data" in p:
                p["inline_data"]["data"] = f"<{len(p['inline_data']['data'])} base64 chars>"
        print(json.dumps({"endpoint": url, "out": args.out, **preview}, indent=2))
        if not api_key(False):
            warn("GEMINI_API_KEY is not set; dry-run only.")
        return 0

    target = Path(args.out)
    if target.exists() and not args.force:
        die(f"Output already exists: {target} (use a versioned name or --force)", 2)

    key = api_key(True)
    print(f"Calling {args.model} ({len(args.image)} input image(s)); this can take up to a few minutes.",
          file=sys.stderr)
    data = request("POST", url, key, body, args.timeout)

    candidates = data.get("candidates") or []
    if not candidates:
        feedback = data.get("promptFeedback", {})
        die(f"No candidates returned (blocked or empty). promptFeedback: {json.dumps(feedback)}")
    cand = candidates[0]
    images, texts = [], []
    for part in (cand.get("content") or {}).get("parts", []):
        blob = part.get("inlineData") or part.get("inline_data")
        if blob and blob.get("data"):
            images.append((blob.get("mimeType") or blob.get("mime_type") or "image/png", blob["data"]))
        elif part.get("text") and not part.get("thought"):
            texts.append(part["text"])
    if not images:
        die(f"No image in response (finishReason={cand.get('finishReason')}). Model text: {' '.join(texts)[:1000]}")

    paths = output_paths(args.out, len(images), images[0][0])
    for path, (_, b64) in zip(paths, images):
        if path.exists() and not args.force:
            die(f"Output already exists: {path} (use a versioned name or --force)", 2)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(base64.b64decode(b64))
        print(f"Wrote {path}", file=sys.stderr)

    print(json.dumps({
        "outputs": [str(p) for p in paths],
        "model": args.model,
        "model_text": " ".join(texts).strip() or None,
        "usage": data.get("usageMetadata"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
