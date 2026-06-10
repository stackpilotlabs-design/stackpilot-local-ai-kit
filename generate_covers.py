#!/usr/bin/env python3
"""
Terminal Evidence — Cover Generator
Generates 4 production PNG assets from the final approved specification (Rev 2).

Run from repo root:
  .venv/bin/python generate_covers.py

Output: assets/covers/
  cover-v1.png        1280 × 1920  PDF cover / Gumroad product cover
  cover-square.png    1080 × 1080  X (Twitter) / Gumroad social share
  cover-linkedin.png  1080 × 1350  LinkedIn image post (4:5)
  cover-og.png        1200 × 628   OG link preview
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ── Font paths ─────────────────────────────────────────────────────────────────
_HOME  = Path.home()
_JBM   = _HOME / "Library/Fonts"
_INTER = Path("/tmp/inter_fonts/extras/ttf")

JBM_REG = str(_JBM   / "JetBrainsMono-Regular.ttf")
JBM_SB  = str(_JBM   / "JetBrainsMono-SemiBold.ttf")
JBM_B   = str(_JBM   / "JetBrainsMono-Bold.ttf")
INT_D   = str(_INTER  / "InterDisplay-SemiBold.ttf")   # title display lines
INT_SB  = str(_INTER  / "Inter-SemiBold.ttf")          # "for Mac" qualifier

# ── Color palette — Terminal Evidence Rev 2 ────────────────────────────────────
BG         = (10,  10,  10)    # #0A0A0A  background
WHITE      = (255, 255, 255)   # #FFFFFF  headline text
GREEN      = (0,  210, 106)    # #00D26A  brand / prompt / PASS
SUBTITLE   = (117, 117, 117)   # #757575  subtitle  (↑ from #666, +15%)
BENCH_MDL  = (106, 106, 106)   # #6A6A6A  bench model names  (↑ from #555)
BENCH_UNIT = (77,  77,  77)    # #4D4D4D  bench tok/s labels  (↑ from #3A3)
BENCH_LBL  = (70,  70,  70)    # #464646  BENCHMARK RESULTS label  (↑ from #3D3, +15%)
BENCH_BUL  = (58, 106, 74)     # #3A6A4A  bullet dots  (↑ from #2A4)
SEPARATOR  = (28,  28,  28)    # #1C1C1C  separator line
MUTED      = (28,  28,  28)    # #1C1C1C  version text

# ── Cover dimensions ───────────────────────────────────────────────────────────
W, H  = 1280, 1920
LEFT  = 80
RIGHT = W - LEFT     # = 1200  (right content boundary)

# ── Font sizes at 1280 × 1920 ─────────────────────────────────────────────────
FS_BRAND  = 43    # JBM SemiBold — brand line "STACKPILOT LABS"
FS_PROMPT = 118   # JBM Bold    — "$_" prompt accent
FS_TITLE  = 160   # InterDisplay SemiBold — "Local AI", "Starter Kit"
FS_PLAT   = 120   # Inter SemiBold — "for Mac" (platform qualifier, ~75% of title)
FS_SUB    = 43    # JBM Regular — subtitle (2 lines)
FS_BLBL   = 37    # JBM Regular — "BENCHMARK RESULTS" label
FS_BENCH  = 46    # JBM Regular / Bold / SemiBold — benchmark row text
FS_VER    = 34    # JBM Regular — version metadata

# ── Vertical positions (top of text bounding box) ─────────────────────────────
# Zone 1 (0–7%   =     0–134px): brand line
# Zone 2 (7–16%  =   134–307px): $_ prompt accent
# Zone 3 (16–55% =  307–1056px): title block (3 lines, centered within zone)
# Zone 4 (55–64% = 1056–1229px): subtitle (2 lines)
# Zone 5 (~68%   =        ~1306): separator rule
# Zone 6 (68–84% = 1306–1613px): benchmark strip
# Zone 7 (84–95%            )  : whitespace — do not fill
# Zone 8 (~96%   =     ~1843px): version metadata
Y_BRAND  = 80
Y_PROMPT = 152
Y_TITLE1 = 440     # "Local AI"    — zone 3, padded to center block
Y_TITLE2 = 622     # "Starter Kit" — Y_TITLE1 + FS_TITLE + 22
Y_PLAT   = 806     # "for Mac"     — Y_TITLE2 + FS_TITLE + 24
Y_SUB1   = 1066    # subtitle line 1 — zone 4
Y_SUB2   = 1120    # subtitle line 2 — + FS_SUB + 11
Y_SEP    = 1308    # separator
Y_BLBL   = 1338    # "BENCHMARK RESULTS"
Y_GEMMA  = 1390    # Gemma 4 E4B row
Y_QWEN3  = 1450    # Qwen3 4B row
Y_VER    = 1858    # version text

# ── Benchmark strip column x-positions ────────────────────────────────────────
X_BULLET = LEFT - 8   # bullet dot
X_MODEL  = LEFT + 18  # model name
X_SPEED  = 640        # speed value (right-side data column)
X_UNIT_G = 762        # "tok/s" for Gemma  (after "33.6" = 4 mono chars)
X_UNIT_Q = 800        # "tok/s" for Qwen3  (after "46–50" = 5 mono chars)
X_PASS   = 1003       # "PASS" column


# ── Helpers ────────────────────────────────────────────────────────────────────

def txt_w(font: ImageFont.FreeTypeFont, text: str) -> int:
    return int(font.getlength(text))


def draw_tracked(draw, x, y, text, font, fill, tracking=0):
    """Draw text with per-character additional letter-spacing (tracking)."""
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill, anchor="lt")
        x += txt_w(font, ch) + tracking
    return x


def load_fonts(sx=1.0):
    """Load all required fonts, scaled by sx relative to 1280px base width."""
    def sz(n): return max(8, int(n * sx))
    return {
        "brand"  : ImageFont.truetype(JBM_SB,  sz(FS_BRAND)),
        "prompt" : ImageFont.truetype(JBM_B,   sz(FS_PROMPT)),
        "title"  : ImageFont.truetype(INT_D,   sz(FS_TITLE)),
        "plat"   : ImageFont.truetype(INT_SB,  sz(FS_PLAT)),
        "sub"    : ImageFont.truetype(JBM_REG, sz(FS_SUB)),
        "blbl"   : ImageFont.truetype(JBM_REG, sz(FS_BLBL)),
        "bench"  : ImageFont.truetype(JBM_REG, sz(FS_BENCH)),
        "bench_b": ImageFont.truetype(JBM_B,   sz(FS_BENCH)),
        "bench_s": ImageFont.truetype(JBM_SB,  sz(FS_BENCH)),
        "ver"    : ImageFont.truetype(JBM_REG, sz(FS_VER)),
    }


# ── Render functions ───────────────────────────────────────────────────────────

def render_cover(output_w=W, output_h=H, include_bench=True) -> Image.Image:
    """
    Render the full cover at any size by proportionally scaling all metrics.
    Default is the production 1280 × 1920 canvas.
    """
    img = Image.new("RGB", (output_w, output_h), BG)
    d   = ImageDraw.Draw(img)

    sx = output_w / W
    sy = output_h / H

    def lx(v): return int(v * sx)
    def ly(v): return int(v * sy)

    f = load_fonts(sx=sx)

    # Zone 1 — Brand line
    brand_track = max(1, int(f["brand"].size * 0.12))
    draw_tracked(d, lx(LEFT), ly(Y_BRAND),
                 "STACKPILOT LABS", f["brand"], GREEN, tracking=brand_track)

    # Zone 2 — Prompt accent
    d.text((lx(LEFT), ly(Y_PROMPT)), "$_",
           font=f["prompt"], fill=GREEN, anchor="lt")

    # Zone 3 — Title block
    d.text((lx(LEFT), ly(Y_TITLE1)), "Local AI",
           font=f["title"], fill=WHITE, anchor="lt")
    d.text((lx(LEFT), ly(Y_TITLE2)), "Starter Kit",
           font=f["title"], fill=WHITE, anchor="lt")
    d.text((lx(LEFT), ly(Y_PLAT)),   "for Mac",
           font=f["plat"],  fill=WHITE, anchor="lt")

    # Zone 4 — Subtitle
    d.text((lx(LEFT), ly(Y_SUB1)),
           "A Practical Guide to Running, Benchmarking,",
           font=f["sub"], fill=SUBTITLE, anchor="lt")
    d.text((lx(LEFT), ly(Y_SUB2)),
           "and Choosing Local AI Models on Apple Silicon",
           font=f["sub"], fill=SUBTITLE, anchor="lt")

    # Zone 5 — Separator rule
    d.line([(lx(LEFT), ly(Y_SEP)), (lx(RIGHT), ly(Y_SEP))],
           fill=SEPARATOR, width=max(1, round(sy)))

    if not include_bench:
        return img

    # Zone 6 — Benchmark strip
    blbl_track = max(1, int(f["blbl"].size * 0.10))
    draw_tracked(d, lx(LEFT), ly(Y_BLBL),
                 "BENCHMARK RESULTS", f["blbl"], BENCH_LBL, tracking=blbl_track)

    # Gemma 4 E4B row
    d.text((lx(X_BULLET), ly(Y_GEMMA)), "\u00b7",         font=f["bench"],   fill=BENCH_BUL, anchor="lt")
    d.text((lx(X_MODEL),  ly(Y_GEMMA)), "Gemma 4 E4B",    font=f["bench"],   fill=BENCH_MDL, anchor="lt")
    d.text((lx(X_SPEED),  ly(Y_GEMMA)), "33.6",           font=f["bench_b"], fill=WHITE,      anchor="lt")
    d.text((lx(X_UNIT_G), ly(Y_GEMMA)), "tok/s",          font=f["bench"],   fill=BENCH_UNIT, anchor="lt")
    d.text((lx(X_PASS),   ly(Y_GEMMA)), "PASS",           font=f["bench_s"], fill=GREEN,      anchor="lt")

    # Qwen3 4B row
    d.text((lx(X_BULLET), ly(Y_QWEN3)), "\u00b7",         font=f["bench"],   fill=BENCH_BUL, anchor="lt")
    d.text((lx(X_MODEL),  ly(Y_QWEN3)), "Qwen3 4B",       font=f["bench"],   fill=BENCH_MDL, anchor="lt")
    d.text((lx(X_SPEED),  ly(Y_QWEN3)), "46\u201350",     font=f["bench_b"], fill=WHITE,      anchor="lt")
    d.text((lx(X_UNIT_Q), ly(Y_QWEN3)), "tok/s",          font=f["bench"],   fill=BENCH_UNIT, anchor="lt")
    d.text((lx(X_PASS),   ly(Y_QWEN3)), "PASS",           font=f["bench_s"], fill=GREEN,      anchor="lt")

    # Zone 8 — Version (bottom-right, right-aligned to RIGHT margin)
    ver_text = "v1.0 \u00b7 June 2026"
    ver_w = txt_w(f["ver"], ver_text)
    d.text((lx(RIGHT) - ver_w, ly(Y_VER)),
           ver_text, font=f["ver"], fill=MUTED, anchor="lt")

    return img


def render_og() -> Image.Image:
    """
    Render 1200 × 628 OG / link-preview image.
    Left panel: scaled portrait cover slice (top ~55%, title visible).
    Right panel: full content redrawn at OG scale with benchmark strip.
    """
    og = Image.new("RGB", (1200, 628), BG)
    d  = ImageDraw.Draw(og)

    # Left: portrait cover, cropped to top 60% (title + prompt visible),
    # scaled to 628px tall panel
    full = render_cover(include_bench=False)
    crop_h = int(H * 0.60)            # top 60% of portrait
    crop = full.crop((0, 0, W, crop_h))
    panel_h = 628
    panel_w = int(panel_h * W / crop_h)   # preserve aspect ratio
    panel_w = min(panel_w, 440)            # cap left panel width
    panel_h_actual = int(panel_w * crop_h / W)
    # If panel_h_actual < 628, pad top/bottom with black
    panel_img = crop.resize((panel_w, panel_h_actual), Image.LANCZOS)
    pad_top = (628 - panel_h_actual) // 2
    og.paste(panel_img, (0, pad_top))

    # Vertical divider
    d.line([(panel_w, 0), (panel_w, 628)], fill=SEPARATOR, width=1)

    # Right panel
    rx  = panel_w + 42
    rw  = 1200 - rx - 36

    # Font sizes for OG right panel
    def ogf(path, size): return ImageFont.truetype(path, size)
    f_brand  = ogf(JBM_SB,  15)
    f_prompt = ogf(JBM_B,   40)
    f_title  = ogf(INT_D,   52)
    f_plat   = ogf(INT_SB,  40)
    f_sub    = ogf(JBM_REG, 14)
    f_blbl   = ogf(JBM_REG, 13)
    f_bench  = ogf(JBM_REG, 14)
    f_benchb = ogf(JBM_B,   14)
    f_benchs = ogf(JBM_SB,  14)
    f_ver    = ogf(JBM_REG, 11)

    # Brand
    draw_tracked(d, rx, 38, "STACKPILOT LABS", f_brand, GREEN, tracking=2)

    # Prompt
    d.text((rx, 64), "$_", font=f_prompt, fill=GREEN, anchor="lt")

    # Title block
    d.text((rx, 118), "Local AI",    font=f_title, fill=WHITE, anchor="lt")
    d.text((rx, 176), "Starter Kit", font=f_title, fill=WHITE, anchor="lt")
    d.text((rx, 234), "for Mac",     font=f_plat,  fill=WHITE, anchor="lt")

    # Subtitle
    d.text((rx, 290), "A Practical Guide to Running, Benchmarking,",
           font=f_sub, fill=SUBTITLE, anchor="lt")
    d.text((rx, 310), "and Choosing Local AI Models on Apple Silicon",
           font=f_sub, fill=SUBTITLE, anchor="lt")

    # Separator
    d.line([(rx, 342), (1164, 342)], fill=SEPARATOR, width=1)

    # Benchmark rows
    bx_model = rx + 12
    bx_speed = rx + 192
    bx_unit  = rx + 238
    bx_unit_q = rx + 256   # wider for "46–50"
    bx_pass  = rx + 320

    d.text((rx,        364), "\u00b7",       font=f_bench,  fill=BENCH_BUL, anchor="lt")
    d.text((bx_model,  364), "Gemma 4 E4B",  font=f_bench,  fill=BENCH_MDL, anchor="lt")
    d.text((bx_speed,  364), "33.6",         font=f_benchb, fill=WHITE,      anchor="lt")
    d.text((bx_unit,   364), "tok/s",        font=f_bench,  fill=BENCH_UNIT, anchor="lt")
    d.text((bx_pass,   364), "PASS",         font=f_benchs, fill=GREEN,      anchor="lt")

    d.text((rx,         385), "\u00b7",      font=f_bench,  fill=BENCH_BUL, anchor="lt")
    d.text((bx_model,   385), "Qwen3 4B",    font=f_bench,  fill=BENCH_MDL, anchor="lt")
    d.text((bx_speed,   385), "46\u201350",  font=f_benchb, fill=WHITE,      anchor="lt")
    d.text((bx_unit_q,  385), "tok/s",       font=f_bench,  fill=BENCH_UNIT, anchor="lt")
    d.text((bx_pass,    385), "PASS",        font=f_benchs, fill=GREEN,      anchor="lt")

    # Version
    ver_text = "v1.0 \u00b7 June 2026"
    ver_w = txt_w(f_ver, ver_text)
    d.text((1164 - ver_w, 606), ver_text, font=f_ver, fill=MUTED, anchor="lt")

    return og


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).parent / "assets/covers"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Terminal Evidence covers (Rev 2) …\n")

    # 1 — cover-v1.png  1280 × 1920
    cover = render_cover(W, H, include_bench=True)
    p = out_dir / "cover-v1.png"
    cover.save(str(p), "PNG", compress_level=1)
    print(f"  \u2713  cover-v1.png          {W} \u00d7 {H}")

    # 2 — cover-square.png  1080 × 1080
    # Crop full-width 1280 × 1280 square from top of cover, resize to 1080 × 1080
    sq = cover.crop((0, 0, W, W)).resize((1080, 1080), Image.LANCZOS)
    p  = out_dir / "cover-square.png"
    sq.save(str(p), "PNG", compress_level=1)
    print(f"  \u2713  cover-square.png      1080 \u00d7 1080")

    # 3 — cover-linkedin.png  1080 × 1350 (4:5)
    # Crop 1280 × 1600 from top of cover (includes benchmark strip), resize
    li = cover.crop((0, 0, W, 1600)).resize((1080, 1350), Image.LANCZOS)
    p  = out_dir / "cover-linkedin.png"
    li.save(str(p), "PNG", compress_level=1)
    print(f"  \u2713  cover-linkedin.png    1080 \u00d7 1350")

    # 4 — cover-og.png  1200 × 628
    og = render_og()
    p  = out_dir / "cover-og.png"
    og.save(str(p), "PNG", compress_level=1)
    print(f"  \u2713  cover-og.png          1200 \u00d7 628")

    print(f"\nAll files saved to {out_dir}")


if __name__ == "__main__":
    main()
