"""Generate the Gumroad cover image for Course Creator Pack.

1200x675 hero. Dark creator-tool cover, orange accent, exact buyer-facing text.
This is intentionally deterministic so Gumroad cover updates do not rely on
AI image text rendering.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
BG = (45, 45, 56)
FOOTER = (32, 32, 43)
INK = (246, 246, 242)
MUTED = (190, 190, 190)
DIM = (155, 155, 155)
ACCENT = (239, 128, 80)
OUT = Path(__file__).parent / "cover.png"


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "arialbd.ttf" if bold else "arial.ttf",
        "segoeuib.ttf" if bold else "segoeui.ttf",
        "calibrib.ttf" if bold else "calibri.ttf",
    ]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def _center(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill) -> None:
    draw.text(((W - _text_width(draw, text, font)) // 2, y), text, font=font, fill=fill)


def _bullet(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font) -> None:
    draw.ellipse([(x, y + 13), (x + 5, y + 18)], fill=MUTED)
    draw.text((x + 14, y), text, font=font, fill=MUTED)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    title_font = _font(72, bold=True)
    pack_font = _font(74, bold=True)
    subtitle_font = _font(30)
    callout_font = _font(22, bold=True)
    bullet_font = _font(21)
    footer_font = _font(20)

    _center(d, 96, "COURSE CREATOR", title_font, INK)
    _center(d, 184, "PACK", pack_font, ACCENT)
    _center(d, 272, "7 AI Agents + Launch Flow EXE", subtitle_font, MUTED)

    line_y = 324
    d.rectangle([(300, line_y), (900, line_y + 2)], fill=ACCENT)

    callout = "NEW: Windows .exe included"
    callout_w = _text_width(d, callout, callout_font)
    pad_x, pad_y = 18, 9
    callout_x = (W - callout_w) // 2 - pad_x
    callout_y = 346
    d.rounded_rectangle(
        [
            (callout_x, callout_y),
            (callout_x + callout_w + pad_x * 2, callout_y + 42),
        ],
        radius=10,
        outline=ACCENT,
        width=2,
    )
    d.text((callout_x + pad_x, callout_y + pad_y), callout, font=callout_font, fill=INK)

    left_x, right_x = 80, 620
    top_y, gap = 424, 36
    left_items = [
        "Launch Email Sequencer.exe",
        "Sales Page Critique",
        "Refund De-escalator",
        "Customer Q&A",
    ]
    right_items = [
        "Affiliate Outreach",
        "Testimonial Collector",
        "Lesson Outliner",
        "OpenRouter-Powered",
    ]
    for i, item in enumerate(left_items):
        _bullet(d, left_x, top_y + i * gap, item, bullet_font)
    for i, item in enumerate(right_items):
        _bullet(d, right_x, top_y + i * gap, item, bullet_font)

    d.rectangle([(0, 620), (W, H)], fill=FOOTER)
    footer = "Double-click Launch Email Sequencer.exe. Run setup.bat for all 7 agents."
    _center(d, 641, footer, footer_font, DIM)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
