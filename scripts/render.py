#!/usr/bin/env python3
"""Front-page renderer for the 25 November 2026 world-news image.

Draws the make.fun bounty entry "Sum up 25 November's world news
in one image" (news-image-20261125) as a 1024x1024 PNG using only
Pillow. No network calls, no generated pictures, no randomness:
running it twice writes the same bytes.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
OUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "entry.png"

# Palette: warm paper, navy masthead, gold date line.
PAPER_BG = (250, 247, 240)
MASTHEAD = (16, 38, 59)
HEADLINE_INK = (20, 32, 46)
SUMMARY_INK = (61, 74, 87)
FOOTER_GREY = (120, 128, 138)
DATE_GOLD = (232, 179, 75)
DIVIDER = (214, 208, 196)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def _font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


TITLE_FONT = _font("DejaVuSerif-Bold.ttf", 66)
KICKER_FONT = _font("DejaVuSerif.ttf", 24)
HEADLINE_FONT = _font("DejaVuSans-Bold.ttf", 31)
SUMMARY_FONT = _font("DejaVuSans.ttf", 23)
SMALL_FONT = _font("DejaVuSans.ttf", 20)
TAG_FONT = _font("DejaVuSans-Bold.ttf", 21)
NUMBER_FONT = _font("DejaVuSans-Bold.ttf", 26)

MARGIN = 48
TEXT_X = 132
TEXT_W = PAGE_W - MARGIN - TEXT_X
FIRST_ROW_Y = 204
ROW_HEIGHT = 140
ROW_GAP = 8

EDITION_DATE = "W E D N E S D A Y  ·  2 5  N O V E M B E R  2 0 2 6"
FOOTER_DATE = "25 November 2026"


def day_stories():
    """The five stories of 25 November 2026, each with a tag colour."""
    return [
        {
            "kicker": "HORMUZ",
            "accent": (15, 118, 110),
            "title": "Two tankers hit mines in Strait of Hormuz",
            "dek": "Iran says two oil tankers struck naval mines and caught fire in the Strait of Hormuz, raising fears for global energy shipping.",
        },
        {
            "kicker": "TARIFFS",
            "accent": (29, 78, 137),
            "title": "US proposes tariffs on 14 economies",
            "dek": "Washington plans new tariffs on 14 trading partners, including China, the EU and India, after a probe into excess factory capacity.",
        },
        {
            "kicker": "MARKETS",
            "accent": (180, 35, 24),
            "title": "Wall Street slides 2.2% on AI doubts",
            "dek": "The S&P 500 falls 2.2% and the Nikkei 2.8% as AI-spending doubts deepen; Brent crude rises 1.1% to $89.73 after Gulf attacks.",
        },
        {
            "kicker": "HUAWEI",
            "accent": (194, 65, 12),
            "title": "Huawei convicted in US criminal trial",
            "dek": "A Brooklyn jury convicts Huawei on 10 of 12 counts, including bank fraud, wire fraud and conspiracy to steal trade secrets.",
        },
        {
            "kicker": "SPACE",
            "accent": (109, 40, 217),
            "title": "China flies Pakistan's first astronaut",
            "dek": "Shenzhou-24 docks with the Tiangong station carrying Pakistan's first astronaut — the first foreign guest aboard China's station.",
        },
    ]


def split_summary(canvas, text):
    """Greedy word wrap of a story summary into at most two lines."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if canvas.textlength(trial, font=SUMMARY_FONT) <= TEXT_W:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise ValueError(f"summary spills to {len(lines)} lines: {text!r}")
    return lines


def _centred(canvas, y, text, font, fill):
    width = canvas.textlength(text, font=font)
    canvas.text(((PAGE_W - width) / 2, y), text, font=font, fill=fill)


def draw_masthead(canvas):
    canvas.rectangle([0, 0, PAGE_W, 148], fill=MASTHEAD)
    _centred(canvas, 26, "THE WORLD TODAY", TITLE_FONT, (255, 255, 255))
    _centred(canvas, 106, EDITION_DATE, SMALL_FONT, DATE_GOLD)


def draw_kicker(canvas):
    _centred(canvas, 160, "Five stories that defined the day", KICKER_FONT, SUMMARY_INK)
    canvas.line([MARGIN, 196, PAGE_W - MARGIN, 196], fill=DIVIDER, width=2)


def draw_story(canvas, index, story, total):
    y = FIRST_ROW_Y + index * (ROW_HEIGHT + ROW_GAP)
    canvas.ellipse([MARGIN, y + 8, 104, y + 64], fill=story["accent"])
    numeral = f"{index + 1}"
    nw = canvas.textlength(numeral, font=NUMBER_FONT)
    canvas.text((MARGIN + (56 - nw) / 2, y + 18), numeral, font=NUMBER_FONT, fill=(255, 255, 255))
    canvas.text((TEXT_X, y + 2), story["kicker"], font=TAG_FONT, fill=story["accent"])
    if canvas.textlength(story["title"], font=HEADLINE_FONT) > TEXT_W:
        raise ValueError(f"headline too wide for one line: {story['title']!r}")
    canvas.text((TEXT_X, y + 30), story["title"], font=HEADLINE_FONT, fill=HEADLINE_INK)
    for j, line in enumerate(split_summary(canvas, story["dek"])):
        canvas.text((TEXT_X, y + 74 + j * 30), line, font=SUMMARY_FONT, fill=SUMMARY_INK)
    if index < total - 1:
        canvas.line([MARGIN, y + ROW_HEIGHT - 4, PAGE_W - MARGIN, y + ROW_HEIGHT - 4], fill=DIVIDER, width=2)


def draw_footer(canvas):
    _centred(canvas, 966, f"Summarised from major news outlets  ·  {FOOTER_DATE}", SMALL_FONT, FOOTER_GREY)
    _centred(canvas, 992, "Code-rendered summary image", SMALL_FONT, FOOTER_GREY)


def main():
    page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER_BG)
    canvas = ImageDraw.Draw(page)
    draw_masthead(canvas)
    draw_kicker(canvas)
    stories = day_stories()
    for i, story in enumerate(stories):
        draw_story(canvas, i, story, len(stories))
    draw_footer(canvas)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    page.save(OUT_PATH, format="PNG", optimize=True)
    print(f"wrote {OUT_PATH}  {OUT_PATH.stat().st_size} bytes  {page.size}")


if __name__ == "__main__":
    main()
