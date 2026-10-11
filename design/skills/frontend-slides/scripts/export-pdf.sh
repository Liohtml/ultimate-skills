#!/usr/bin/env bash
# export-pdf.sh — Export an HTML presentation to PDF
#
# Usage:
#   bash scripts/export-pdf.sh <path-to-html> [output.pdf] [--compact] [--no-open]
#
# Examples:
#   bash scripts/export-pdf.sh ./my-deck/index.html
#   bash scripts/export-pdf.sh ./presentation.html ./presentation.pdf
#
# What this does:
#   1. Starts a local server on 127.0.0.1 to serve the HTML's folder (fonts and assets need HTTP)
#   2. Uses Playwright to screenshot each slide at 1920x1080
#   3. Combines all screenshots into a single PDF
#   4. Cleans up the server and temp files
#
# Playwright resolution (nothing is installed globally):
#   - An already-installed Playwright (resolvable from the current directory or
#     NODE_PATH, or in the global npm root) is reused when it can launch Chromium.
#     Browsers are looked up where Playwright normally keeps them
#     (PLAYWRIGHT_BROWSERS_PATH, else its per-user cache).
#   - Otherwise playwright@SLIDES_PLAYWRIGHT_VERSION (pinned, default below) is
#     installed into a temp dir with --ignore-scripts, and its Chromium is
#     downloaded into that browser cache if missing.
#
# Environment overrides:
#   SLIDES_PLAYWRIGHT_VERSION  exact Playwright version to install (default: 1.63.0)
#   SLIDES_CHROMIUM_PATH       existing Chrome/Chromium binary to use instead of a
#                              Playwright-managed browser (skips the browser download)
#
# The PDF preserves colors, fonts, and layout — but not animations.
# Perfect for email attachments, printing, or embedding in documents.
set -euo pipefail

# Pinned Playwright version for the temp-dir install. Bump deliberately.
DEFAULT_PLAYWRIGHT_VERSION="1.63.0"

# ─── Colors ────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

info()  { echo -e "${CYAN}ℹ${NC} $*"; }
ok()    { echo -e "${GREEN}✓${NC} $*"; }
warn()  { echo -e "${YELLOW}⚠${NC} $*"; }
err()   { echo -e "${RED}✗${NC} $*" >&2; }

# ─── Parse flags ──────────────────────────────────────────

# Default resolution: 1920x1080 (full HD, ~1-2MB per slide)
# Compact resolution: 1280x720 (HD, ~50-70% smaller files)
VIEWPORT_W=1920
VIEWPORT_H=1080
COMPACT=false
OPEN_PDF=true

usage() {
    echo "Usage: bash scripts/export-pdf.sh <path-to-html> [output.pdf] [--compact] [--no-open]"
    echo ""
    echo "Examples:"
    echo "  bash scripts/export-pdf.sh ./my-deck/index.html"
    echo "  bash scripts/export-pdf.sh ./presentation.html ./slides.pdf"
    echo "  bash scripts/export-pdf.sh ./presentation.html --compact   # smaller file size"
    echo ""
    echo "Options:"
    echo "  --compact   render at 1280x720 instead of 1920x1080 (50-70% smaller PDF)"
    echo "  --no-open   do not open the PDF after export"
    echo ""
    echo "Environment: SLIDES_PLAYWRIGHT_VERSION (default ${DEFAULT_PLAYWRIGHT_VERSION}), SLIDES_CHROMIUM_PATH"
}

POSITIONAL=()
for arg in "$@"; do
    case $arg in
        --compact)
            COMPACT=true
            VIEWPORT_W=1280
            VIEWPORT_H=720
            ;;
        --no-open)
            OPEN_PDF=false
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        -*)
            err "Unknown option: $arg"
            usage >&2
            exit 1
            ;;
        *)
            POSITIONAL+=("$arg")
            ;;
    esac
done
# (the ${arr[@]+...} form keeps `set -u` happy on bash 3.2 when no positional args were given)
set -- ${POSITIONAL[@]+"${POSITIONAL[@]}"}

# ─── Input validation ─────────────────────────────────────

if [[ $# -lt 1 || $# -gt 2 ]]; then
    usage >&2
    exit 1
fi

PLAYWRIGHT_VERSION="${SLIDES_PLAYWRIGHT_VERSION:-$DEFAULT_PLAYWRIGHT_VERSION}"
if [[ ! "$PLAYWRIGHT_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    err "SLIDES_PLAYWRIGHT_VERSION must be an exact version such as ${DEFAULT_PLAYWRIGHT_VERSION} (got: $PLAYWRIGHT_VERSION)"
    exit 1
fi
if [[ -n "${SLIDES_CHROMIUM_PATH:-}" && ! -x "$SLIDES_CHROMIUM_PATH" ]]; then
    err "SLIDES_CHROMIUM_PATH is not an executable file: $SLIDES_CHROMIUM_PATH"
    exit 1
fi

INPUT_HTML="$1"
if [[ ! -f "$INPUT_HTML" ]]; then
    err "File not found: $INPUT_HTML"
    exit 1
fi

# Resolve to absolute path
INPUT_HTML=$(cd "$(dirname "$INPUT_HTML")" && pwd)/$(basename "$INPUT_HTML")

# Output PDF path: use second argument or derive from input name
if [[ $# -ge 2 ]]; then
    OUTPUT_PDF="$2"
else
    OUTPUT_PDF="$(dirname "$INPUT_HTML")/$(basename "$INPUT_HTML" .html).pdf"
fi

# Resolve output to absolute path (the Node export script runs with absolute paths only)
OUTPUT_DIR=$(dirname "$OUTPUT_PDF")
mkdir -p "$OUTPUT_DIR"
OUTPUT_PDF="$(cd "$OUTPUT_DIR" && pwd)/$(basename "$OUTPUT_PDF")"

echo ""
echo -e "${BOLD}╔══════════════════════════════════════╗${NC}"
echo -e "${BOLD}║       Export Slides to PDF            ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════╝${NC}"
echo ""

# ─── Step 1: Check dependencies ───────────────────────────

info "Checking dependencies..."

if ! command -v node &>/dev/null || ! command -v npm &>/dev/null; then
    err "Node.js (with npm) is required but not installed."
    err ""
    err "Install Node.js:"
    err "  macOS:   brew install node"
    err "  or visit https://nodejs.org and download the installer"
    exit 1
fi

ok "Node.js found"

# ─── Step 2: Create the export script ─────────────────────

# We use a temporary Node.js script with Playwright to:
# 1. Start a local server (so fonts load correctly)
# 2. Navigate to each slide
# 3. Screenshot each slide at 1920x1080 (16:9 landscape)
# 4. Combine into a single PDF

TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT
TEMP_SCRIPT="$TEMP_DIR/export-slides.mjs"

# Figure out which directory to serve (the folder containing the HTML)
SERVE_DIR=$(dirname "$INPUT_HTML")
HTML_FILENAME=$(basename "$INPUT_HTML")

cat > "$TEMP_SCRIPT" << 'EXPORT_SCRIPT'
// export-slides.mjs — Playwright script to export HTML slides to PDF
//
// How it works:
// 1. Starts a local HTTP server (needed for fonts/assets to load)
// 2. Opens the presentation in a headless browser at 1920x1080
// 3. Counts the total number of slides
// 4. Screenshots each slide one by one
// 5. Generates a PDF with all slides as landscape pages

import { createRequire } from 'module';
import { createServer } from 'http';
import { readFileSync, mkdirSync, unlinkSync } from 'fs';
import { join, extname, resolve, sep } from 'path';

// Playwright package directory chosen by export-pdf.sh (reused install or temp-dir install)
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PACKAGE_DIR);
const LAUNCH_OPTIONS = process.env.SLIDES_CHROMIUM_PATH
  ? { executablePath: process.env.SLIDES_CHROMIUM_PATH }
  : {};

const SERVE_DIR = resolve(process.argv[2]);
const HTML_FILE = process.argv[3];
const OUTPUT_PDF = process.argv[4];
const SCREENSHOT_DIR = process.argv[5];
const VP_WIDTH = parseInt(process.argv[6]) || 1920;
const VP_HEIGHT = parseInt(process.argv[7]) || 1080;

// ─── Simple static file server ────────────────────────────
// (We need HTTP so that Google Fonts and relative assets load correctly)

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.eot': 'application/vnd.ms-fontobject',
};

const server = createServer((req, res) => {
  // Decode URL-encoded characters (e.g., %20 → space) so filenames with spaces resolve correctly.
  // Query strings and fragments are ignored; malformed escapes get a 400.
  let pathname;
  try {
    pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
  } catch {
    res.writeHead(400);
    res.end('Bad request');
    return;
  }
  const filePath = resolve(SERVE_DIR, '.' + (pathname === '/' ? '/' + HTML_FILE : pathname));
  // Never serve anything outside the deck's folder
  if (filePath !== SERVE_DIR && !filePath.startsWith(SERVE_DIR + sep)) {
    res.writeHead(403);
    res.end('Forbidden');
    return;
  }
  try {
    const content = readFileSync(filePath);
    const ext = extname(filePath).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIME_TYPES[ext] || 'application/octet-stream' });
    res.end(content);
  } catch {
    res.writeHead(404);
    res.end('Not found');
  }
});

// Find a free port (loopback only: the deck's folder is never exposed to the network)
const port = await new Promise((resolve) => {
  server.listen(0, '127.0.0.1', () => resolve(server.address().port));
});

console.log(`  Local server on port ${port}`);

// ─── Screenshot each slide ────────────────────────────────

const browser = await chromium.launch(LAUNCH_OPTIONS);
const page = await browser.newPage({
  viewport: { width: VP_WIDTH, height: VP_HEIGHT },
});

// Load the presentation
await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'networkidle' });

// Wait for fonts to load
await page.evaluate(() => document.fonts.ready);

// Extra wait for animations to settle on the first slide
await page.waitForTimeout(1500);

// Freeze motion: decks reveal content with CSS transitions/animations (with
// stagger delays) when a slide becomes .visible, so later slides would be
// captured mid-fade. With zero durations every slide renders its final state.
await page.addStyleTag({ content: '*, *::before, *::after { transition-duration: 0s !important; transition-delay: 0s !important; animation-duration: 0s !important; animation-delay: 0s !important; }' });

// Count slides
const slideCount = await page.evaluate(() => {
  return document.querySelectorAll('.slide').length;
});

console.log(`  Found ${slideCount} slides`);

if (slideCount === 0) {
  console.error('  ERROR: No .slide elements found in the presentation.');
  console.error('  Make sure your HTML uses <div class="slide"> or <section class="slide">.');
  await browser.close();
  server.close();
  process.exit(1);
}

// Screenshot each slide
mkdirSync(SCREENSHOT_DIR, { recursive: true });
const screenshotPaths = [];

for (let i = 0; i < slideCount; i++) {
  // Navigate to slide by simulating the presentation's navigation
  // Most frontend-slides presentations use a currentSlide index and show/hide
  await page.evaluate((index) => {
    const slides = document.querySelectorAll('.slide');

    // Try multiple navigation strategies used by frontend-slides:

    // Strategy 1: Direct slide manipulation (most common in generated decks)
    slides.forEach((slide, idx) => {
      if (idx === index) {
        slide.style.display = '';
        slide.style.opacity = '1';
        slide.style.visibility = 'visible';
        slide.style.position = 'relative';
        slide.style.transform = 'none';
        slide.classList.add('active', 'visible');
      } else {
        slide.style.display = 'none';
        slide.classList.remove('active', 'visible');
      }
    });

    // Strategy 2: If there's a SlidePresentation class instance, use it
    if (window.presentation && typeof window.presentation.goToSlide === 'function') {
      window.presentation.goToSlide(index);
    }

    // Strategy 3: Scroll-based (some decks use scroll snapping)
    slides[index]?.scrollIntoView({ behavior: 'instant' });
  }, i);

  // Wait for any slide transition animations to finish
  await page.waitForTimeout(300);

  // Wait for intersection observer animations to trigger
  await page.waitForTimeout(200);

  // Force all .reveal elements on the current slide to be visible
  // (animations normally trigger on scroll/intersection, but we need them visible now)
  await page.evaluate((index) => {
    const slides = document.querySelectorAll('.slide');
    const currentSlide = slides[index];
    if (currentSlide) {
      currentSlide.querySelectorAll('.reveal').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
      });
    }
  }, i);

  await page.waitForTimeout(100);

  const screenshotPath = join(SCREENSHOT_DIR, `slide-${String(i + 1).padStart(3, '0')}.png`);
  await page.screenshot({ path: screenshotPath, fullPage: false });
  screenshotPaths.push(screenshotPath);
  console.log(`  Captured slide ${i + 1}/${slideCount}`);
}

await browser.close();
server.close();

// ─── Combine screenshots into PDF ─────────────────────────
// Use a second Playwright page to generate a PDF from the screenshots

console.log('  Assembling PDF...');

const browser2 = await chromium.launch(LAUNCH_OPTIONS);
const pdfPage = await browser2.newPage();

// Build an HTML page with all screenshots, one per page
const imagesHtml = screenshotPaths.map((p) => {
  const imgData = readFileSync(p).toString('base64');
  return `<div class="page"><img src="data:image/png;base64,${imgData}" /></div>`;
}).join('\n');

const pdfHtml = `<!DOCTYPE html>
<html>
<head>
<style>
  * { margin: 0; padding: 0; }
  @page { size: ${VP_WIDTH}px ${VP_HEIGHT}px; margin: 0; }
  .page {
    width: ${VP_WIDTH}px;
    height: ${VP_HEIGHT}px;
    page-break-after: always;
    overflow: hidden;
  }
  .page:last-child { page-break-after: auto; }
  img {
    width: ${VP_WIDTH}px;
    height: ${VP_HEIGHT}px;
    display: block;
    object-fit: contain;
  }
</style>
</head>
<body>${imagesHtml}</body>
</html>`;

await pdfPage.setContent(pdfHtml, { waitUntil: 'load' });
await pdfPage.pdf({
  path: OUTPUT_PDF,
  width: `${VP_WIDTH}px`,
  height: `${VP_HEIGHT}px`,
  printBackground: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});

await browser2.close();

// Clean up screenshots
screenshotPaths.forEach(p => unlinkSync(p));

console.log(`  ✓ PDF saved to: ${OUTPUT_PDF}`);
EXPORT_SCRIPT

# ─── Step 3: Find or install Playwright ───────────────────
# Prefer a Playwright that is already installed and can launch Chromium; otherwise
# install the pinned version into the temp dir (never globally, no install scripts).

info "Setting up Playwright (headless browser for screenshots)..."

# Prints the directory of an already-installed playwright package, if any.
find_installed_playwright() {
    local dir groot
    # 1. Resolvable from the current directory (project node_modules) or NODE_PATH
    dir=$(node -e 'try { console.log(require("path").dirname(require.resolve("playwright"))) } catch {}' 2>/dev/null) || true
    if [[ -n "$dir" && -f "$dir/package.json" ]]; then
        echo "$dir"
        return
    fi
    # 2. Global npm install
    groot=$(npm root -g 2>/dev/null) || true
    if [[ -n "$groot" && -f "$groot/playwright/package.json" ]]; then
        echo "$groot/playwright"
    fi
}

# Succeeds when the playwright package in $1 can launch Chromium.
playwright_can_launch() {
    PW_PACKAGE_DIR="$1" node -e '
        const { chromium } = require(process.env.PW_PACKAGE_DIR);
        const opts = { timeout: 30000 };
        if (process.env.SLIDES_CHROMIUM_PATH) opts.executablePath = process.env.SLIDES_CHROMIUM_PATH;
        chromium.launch(opts).then((b) => b.close()).then(() => process.exit(0), () => process.exit(1));
    ' &>/dev/null
}

PW_PACKAGE_DIR=""
EXISTING_PW=$(find_installed_playwright)
if [[ -n "$EXISTING_PW" ]]; then
    EXISTING_VERSION=$(node -p 'require(process.argv[1]).version' "$EXISTING_PW/package.json" 2>/dev/null || echo "unknown")
    if playwright_can_launch "$EXISTING_PW"; then
        PW_PACKAGE_DIR="$EXISTING_PW"
        ok "Using installed Playwright ${EXISTING_VERSION} ($EXISTING_PW)"
    else
        warn "Installed Playwright ${EXISTING_VERSION} cannot launch Chromium; using a pinned temp install instead"
    fi
fi

if [[ -z "$PW_PACKAGE_DIR" ]]; then
    info "Installing playwright@${PLAYWRIGHT_VERSION} into a temp dir (may take a moment)..."
    echo ""

    # Minimal package.json so npm installs into $TEMP_DIR/node_modules
    cat > "$TEMP_DIR/package.json" << 'PKG'
{ "name": "slide-export", "private": true, "type": "module" }
PKG

    (cd "$TEMP_DIR" && npm install --no-save --no-audit --no-fund --ignore-scripts \
        --loglevel=error "playwright@${PLAYWRIGHT_VERSION}") >"$TEMP_DIR/npm-install.log" 2>&1 || {
        err "Failed to install playwright@${PLAYWRIGHT_VERSION}:"
        tail -n 20 "$TEMP_DIR/npm-install.log" >&2
        exit 1
    }
    PW_PACKAGE_DIR="$TEMP_DIR/node_modules/playwright"

    # Download Chromium for this Playwright version (a no-op if it is already cached)
    if [[ -z "${SLIDES_CHROMIUM_PATH:-}" ]]; then
        node "$PW_PACKAGE_DIR/cli.js" install chromium >"$TEMP_DIR/browser-install.log" 2>&1 || {
            err "Failed to install Chromium for Playwright ${PLAYWRIGHT_VERSION}:"
            tail -n 20 "$TEMP_DIR/browser-install.log" >&2
            err "Try: npx --yes playwright@${PLAYWRIGHT_VERSION} install chromium"
            err "or point SLIDES_CHROMIUM_PATH at an installed Chrome/Chromium."
            exit 1
        }
    fi
    ok "Playwright ${PLAYWRIGHT_VERSION} ready"
fi
echo ""

# ─── Step 4: Run the export ───────────────────────────────

SCREENSHOT_DIR="$TEMP_DIR/screenshots"

info "Exporting slides to PDF..."
echo ""

if [[ "$COMPACT" == "true" ]]; then
    info "Using compact mode (1280×720) for smaller file size"
fi

PW_PACKAGE_DIR="$PW_PACKAGE_DIR" node "$TEMP_SCRIPT" "$SERVE_DIR" "$HTML_FILENAME" "$OUTPUT_PDF" "$SCREENSHOT_DIR" "$VIEWPORT_W" "$VIEWPORT_H" || {
    err "PDF export failed."
    exit 1
}

# ─── Step 5: Success (the EXIT trap removes the temp dir) ──

echo ""
echo -e "${BOLD}════════════════════════════════════════${NC}"
ok "PDF exported successfully!"
echo ""
echo -e "  ${BOLD}File:${NC}  $OUTPUT_PDF"
echo ""
FILE_SIZE=$(du -h "$OUTPUT_PDF" | cut -f1 | xargs)
echo "  Size: $FILE_SIZE"
echo ""
echo "  This PDF works everywhere — email, Slack, Notion, print."
echo "  Note: Animations are not preserved (it's a static export)."
echo -e "${BOLD}════════════════════════════════════════${NC}"
echo ""

# Open the PDF automatically (best effort; skipped with --no-open)
if [[ "$OPEN_PDF" == "true" ]]; then
    if [[ "$(uname -s)" == "Darwin" ]]; then
        open "$OUTPUT_PDF" &>/dev/null || true
    elif command -v xdg-open &>/dev/null; then
        xdg-open "$OUTPUT_PDF" &>/dev/null || true
    fi
fi
