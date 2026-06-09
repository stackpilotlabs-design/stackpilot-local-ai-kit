# PDF Build Guide — Local AI Starter Kit for Mac

> This document covers the complete PDF generation workflow for the Local AI Starter Kit for Mac.
> Source file: `BOOK.md` + `metadata.yaml`
> Output file: `local-ai-starter-kit-v1.0.pdf`

---

## Prerequisites

### 1. Install Pandoc

Pandoc converts `BOOK.md` to PDF via a LaTeX intermediate.

**macOS (recommended — via Homebrew):**

```bash
brew install pandoc
```

**Verify installation:**

```bash
pandoc --version
```

Pandoc 3.x is required. If you have an older version, upgrade before building:

```bash
brew upgrade pandoc
```

---

### 2. Install a LaTeX Distribution (XeLaTeX)

XeLaTeX is required for custom fonts and proper Unicode handling. On macOS, install MacTeX.

**Option A — Full MacTeX (~4 GB, installs everything):**

```bash
brew install --cask mactex
```

After installation, reload your shell or run:

```bash
eval "$(/usr/libexec/path_helper)"
```

**Option B — BasicTeX (~100 MB, minimal install + manual packages):**

```bash
brew install --cask basictex
```

Then install required LaTeX packages via `tlmgr`:

```bash
sudo tlmgr update --self
sudo tlmgr install xetex fontspec geometry fancyhdr booktabs longtable array \
  caption hyperref xcolor listings mdframed parskip microtype lm-math
```

**Verify XeLaTeX is available:**

```bash
xelatex --version
```

---

### 3. Install Recommended Fonts

The build uses three fonts. Install them before running the build command.

| Role | Recommended Font | Free Alternative |
|---|---|---|
| Body text | Georgia | TeX Gyre Termes |
| Sans-serif | Helvetica Neue (macOS built-in) | Source Sans Pro |
| Monospace (code blocks) | JetBrains Mono | Fira Mono |

**Install JetBrains Mono (if not already installed):**

```bash
brew install --cask font-jetbrains-mono
```

**Verify fonts are available to XeLaTeX:**

```bash
fc-list | grep -i "JetBrains"
fc-list | grep -i "Georgia"
```

If Georgia is missing (unlikely on macOS), substitute `TeX Gyre Termes` by editing `metadata.yaml`:

```yaml
mainfont: "TeX Gyre Termes"
```

---

## Build Commands

All commands assume you are in the `docs/products/local-ai-starter-kit/` directory.

```bash
cd /path/to/stackpilot-local-ai-kit/docs/products/local-ai-starter-kit
```

---

### Required: `--resource-path`

**Every build command must include `--resource-path`** pointing to the repository root. Without it, all embedded images fail silently — Pandoc replaces each image with its alt-text description and produces a text-only PDF.

**Why this flag is required:**

Image paths in `BOOK.md` use the form `assets/screenshots/filename.png` — relative to the repository root. Pandoc resolves relative image paths from its working directory, not from `BOOK.md`'s location on disk. When the build is run from `docs/products/local-ai-starter-kit/`, the path `assets/` resolves to `docs/products/local-ai-starter-kit/assets/`, which does not exist. The actual asset directory is at the repository root.

`--resource-path` tells Pandoc where to search for external resources (images, included files). Setting it to the repository root corrects this mismatch.

**Without `--resource-path` (broken — images not embedded):**
```
[WARNING] Could not fetch resource assets/screenshots/phoenix-lmstudio-settings.png: replacing image with description
[WARNING] Could not fetch resource assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png: replacing image with description
... (13 warnings, text-only PDF, 245 KB)
```

**With `--resource-path` (correct — all images embedded):**
```
(no warnings, full PDF with images, ~3.6 MB)
```

Set the variable once and reuse it in all commands:

```bash
REPO="/path/to/stackpilot-local-ai-kit"
```

---

### Standard Build

```bash
REPO="/path/to/stackpilot-local-ai-kit"

pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --highlight-style=monochrome \
  --variable geometry:margin=2.5cm \
  --variable linestretch=1.4 \
  --variable fontsize=11pt \
  -o local-ai-starter-kit-v1.0.pdf
```

---

### Build With Custom Heading Font and Cover Page Spacing

```bash
REPO="/path/to/stackpilot-local-ai-kit"

pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --highlight-style=monochrome \
  --variable geometry:"top=3cm, bottom=3cm, left=2.5cm, right=2.5cm" \
  --variable linestretch=1.4 \
  --variable fontsize=11pt \
  --variable mainfont="Charter" \
  --variable monofont="Menlo" \
  --variable colorlinks=true \
  --variable linkcolor=black \
  --variable urlcolor=black \
  -o local-ai-starter-kit-v1.0.pdf
```

---

### Quick Draft Build (faster, no TOC)

Use during layout review to iterate quickly:

```bash
REPO="/path/to/stackpilot-local-ai-kit"

pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --highlight-style=monochrome \
  --variable geometry:margin=2.5cm \
  -o local-ai-starter-kit-draft.pdf
```

---

### Build With Page Numbers in Footer

```bash
REPO="/path/to/stackpilot-local-ai-kit"

pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --toc \
  --toc-depth=2 \
  --highlight-style=monochrome \
  --variable geometry:"top=3cm, bottom=3cm, left=2.5cm, right=2.5cm" \
  --variable fontsize=11pt \
  --variable mainfont="Charter" \
  --variable monofont="Menlo" \
  --variable pagestyle=fancy \
  --include-in-header header.tex \
  -o local-ai-starter-kit-v1.0.pdf
```

Create `header.tex` alongside `BOOK.md` for the fancy header/footer:

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\fancyhead[L]{\small Local AI Starter Kit for Mac}
\fancyhead[R]{\small StackPilot Labs}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
```

---

## Table of Contents Configuration

The TOC is generated automatically from headings in `BOOK.md`.

**TOC depth:** `--toc-depth=2` includes `##` chapter headings only. Increase to `3` to include `###` section headings.

**Section numbering:** `--number-sections` adds `1.`, `1.1`, `1.2` etc. to all headings. Remove this flag if you prefer unnumbered chapters.

**Excluding front matter from numbering:** Front matter sections (Copyright, Disclaimer, etc.) will be numbered alongside chapters if `--number-sections` is set. To suppress numbering for specific headings, append `{.unnumbered}` in `BOOK.md`:

```markdown
## Copyright Notice {.unnumbered}
## Disclaimer {.unnumbered}
## About StackPilot Labs {.unnumbered}
```

This is the recommended approach for a publication-quality output — the ten main chapters should be numbered, front/back matter should not.

---

## Figure Handling

Screenshots and figures are referenced in `BOOK.md` as relative paths from the original source files. During the build, Pandoc resolves image paths relative to the `BOOK.md` file location.

### Image Path Check

All screenshot references in the manuscript use this format:

```markdown
![Caption](../../assets/screenshots/filename.png)
```

From `docs/products/local-ai-starter-kit/BOOK.md`, the path `../../assets/screenshots/` resolves to `assets/screenshots/` at the repository root — which is where the images are stored.

**Verify paths before building:**

```bash
# Run from docs/products/local-ai-starter-kit/
grep -o '!\[.*\](.*\.png)' BOOK.md | grep -o '([^)]*\.png)' | tr -d '()'
```

All listed paths should exist. A missing image causes Pandoc to emit a warning and produce a broken image placeholder in the PDF.

### Image Sizing

By default, Pandoc scales images to fit the page width. For screenshots that are too large or too small, control sizing with Pandoc's attribute syntax:

```markdown
![Caption](path/to/image.png){ width=90% }
```

or in absolute dimensions:

```markdown
![Caption](path/to/image.png){ width=12cm }
```

### Figure Captions

Pandoc generates figure captions automatically from the alt text of images. The manuscript uses the convention:

```markdown
> Figure 7.1: Head-to-head comparison (Gemma 4 E4B vs. Qwen3 4B)

![Figure 7.1](../../assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png)
```

The blockquote provides context before the image; the alt text becomes the LaTeX figure caption. This is consistent throughout the manuscript.

---

## Metadata Configuration

`metadata.yaml` controls document-level settings. Key fields:

| Field | Purpose | Notes |
|---|---|---|
| `title` | Document title (used in PDF metadata) | Does not generate a visible title page when `title-page: false` |
| `subtitle` | Subtitle (PDF metadata only) | |
| `author` | Author (PDF metadata, footer if configured) | |
| `date` | Publication date | |
| `lang` | Language code | `en` for English — affects hyphenation |
| `mainfont` | Body text font | Must be installed and visible to XeLaTeX |
| `monofont` | Code block font | Set `Scale=0.85` to keep code readable |
| `toc-depth` | TOC heading depth | 2 = chapter + section only |
| `number-sections` | Section numbering | Set to `false` to disable in YAML or omit flag |
| `colorlinks` | Coloured hyperlinks in PDF | Set to `true`, then set `linkcolor` / `urlcolor` to `black` for print |

**Note:** Settings in `metadata.yaml` can be overridden by command-line `--variable` flags. Command-line flags take precedence.

---

## Font Fallback Reference

If Georgia or Helvetica Neue are unavailable, use these free alternatives which are widely available on macOS and via Homebrew Cask fonts:

| Role | Primary | Free Fallback | Install |
|---|---|---|---|
| Body | Georgia | TeX Gyre Termes | bundled with MacTeX |
| Body alternative | — | Charter | `brew install --cask font-charter` |
| Sans | Helvetica Neue | Source Sans Pro | `brew install --cask font-source-sans-pro` |
| Mono | JetBrains Mono | Fira Mono | `brew install --cask font-fira-mono` |
| Mono alternative | — | IBM Plex Mono | `brew install --cask font-ibm-plex-mono` |

Update `metadata.yaml` to switch fonts:

```yaml
mainfont: "TeX Gyre Termes"
sansfont: "Source Sans Pro"
monofont: "Fira Mono"
```

---

## Build Workflow (End-to-End)

Use this sequence for a final release build.

```bash
# 0. Set the repo root path — required for image embedding
REPO="/path/to/stackpilot-local-ai-kit"
# Example (absolute path):
# REPO="/Users/nivedit/Learning/Business/Using_AI/AI_Productivity/StackPilotLabs/01_product/stackpilot-local-ai-kit"

# 1. Navigate to the guide directory
cd "$REPO/docs/products/local-ai-starter-kit"

# 2. Verify images are present
ls "$REPO/assets/screenshots/"
ls "$REPO/assets/comparisons/"

# 3. Run a draft build to check layout
#    --resource-path is required: without it all 13 images fail silently
pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --highlight-style=monochrome \
  --variable geometry:margin=2.5cm \
  -o local-ai-starter-kit-draft.pdf

# 4. Open draft and review:
#    - Title page layout
#    - TOC accuracy and page numbers
#    - Screenshot sizing and placement
#    - Figure caption alignment
#    - Code block formatting
#    - Table layout (Version Information, decision matrix tables)
#    - Page breaks at chapter boundaries
#    - Front matter section numbering (should be unnumbered)
open local-ai-starter-kit-draft.pdf

# 5. Apply any layout adjustments to BOOK.md or metadata.yaml

# 6. Run the release build with full options
pandoc BOOK.md \
  --metadata-file metadata.yaml \
  --pdf-engine=xelatex \
  --resource-path="$REPO" \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --highlight-style=monochrome \
  --variable geometry:"top=3cm, bottom=3cm, left=2.5cm, right=2.5cm" \
  --variable linestretch=1.4 \
  --variable fontsize=11pt \
  --variable mainfont="Charter" \
  --variable monofont="Menlo" \
  --variable colorlinks=true \
  --variable linkcolor=black \
  --variable urlcolor=black \
  -o local-ai-starter-kit-v1.0.pdf

# 7. Final review
open local-ai-starter-kit-v1.0.pdf

# 8. Confirm page count, verify all figures render, check no broken images
```

---

## Common Build Errors and Fixes

| Error | Likely cause | Fix |
|---|---|---|
| `xelatex not found` | MacTeX / BasicTeX not installed or not on PATH | Run `eval "$(/usr/libexec/path_helper)"` or restart terminal after install |
| `Font "Georgia" not found` | Font name mismatch or font not available | Run `fc-list \| grep -i georgia` to check; use fallback font |
| `Font "JetBrains Mono" not found` | Font not installed | `brew install --cask font-jetbrains-mono` |
| `Could not fetch resource assets/...` warning (×13) | `--resource-path` missing from build command — Pandoc resolves `assets/` from cwd, not repo root | Add `--resource-path="$REPO"` where `REPO` is the absolute path to `stackpilot-local-ai-kit/`. **All images will silently become alt-text if this flag is omitted.** |
| `missing image` warning | Image path does not resolve from `BOOK.md` location | Check paths with `grep -o '!\[.*\](.*\.png)' BOOK.md` |
| `! LaTeX Error: File not found` | Missing LaTeX package | Run `sudo tlmgr install <package-name>` |
| `Unicode character not in font` | Body font missing a character (e.g., em dash, copyright symbol) | Switch to TeX Gyre Termes or Charter which have broad Unicode coverage |
| TOC shows front matter sections numbered | `--number-sections` applied to all headings | Add `{.unnumbered}` to front/back matter `##` headings in `BOOK.md` |
| Code blocks using proportional font | `monofont` not applied | Ensure `--variable monofont="JetBrains Mono"` is in the build command |

---

## Source Files

| File | Purpose | Modify? |
|---|---|---|
| `BOOK.md` | Combined manuscript (front matter + content + back matter) | Only for layout fixes. Never edit CONTENT.md directly. |
| `metadata.yaml` | Pandoc document metadata and LaTeX settings | Yes — fonts, margins, TOC depth |
| `PDF-BUILD.md` | This file — build instructions and reference | Update if build process changes |
| `FRONTMATTER.md` | Front matter source | Yes — if content changes, re-run assembly |
| `CONTENT.md` | Manuscript source (frozen) | No — frozen at v1.0 |
| `BACKMATTER.md` | Back matter source | Yes — if content changes, re-run assembly |

**Re-assembly command** (run if FRONTMATTER.md or BACKMATTER.md are updated):

```bash
cd docs/products/local-ai-starter-kit

{
  cat FRONTMATTER.md
  printf '\n\n\\newpage\n\n'
  tail -n +3 CONTENT.md
  printf '\n\n\\newpage\n\n'
  cat BACKMATTER.md
} > BOOK.md

# Strip internal organizational headings
python3 -c "
import re, sys
path = 'BOOK.md'
strip = {'# Front Matter — Local AI Starter Kit for Mac', '## Title Page', '## Subtitle', '# Back Matter — Local AI Starter Kit for Mac'}
lines = open(path).readlines()
out = ['\n' if l.rstrip('\n') in strip else l for l in lines]
content = ''.join(out)
content = re.sub(r'^\s*\n+---\n+', '', content, count=1)
open(path, 'w').write(content)
print('BOOK.md rebuilt.')
"
```

---

*PDF-BUILD.md — Local AI Starter Kit for Mac — v1.0 — StackPilot Labs*
