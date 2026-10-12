---
name: lemons-slides
description: "Creates on-brand 16:9 PDF decks for Lemons in the Room."
version: 1.0.0
author: Niccolò Cesareo-Santoro, Lemons in the Room
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Presentation, Slides, PDF, Brand, Creative]
    category: creative
---

# Lemons Slides Skill

Creates on-brand 16:9 PDF presentations for Lemons in the Room matching official company decks.

## When to Use

- "Create slides on X", "make a deck for Y", "fai una slide / un deck / una presentazione".
- Investor pitches, hospital department presentations, board reports.

## Prerequisites

- Python 3.8+
- Playwright Chromium engine:
  ```bash
  pip install playwright
  playwright install chromium
  ```

## Brand Rules (Strict)

- **Fonts**: Recoleta Alt for headlines, Open Runde for body (as in `lemons_brand.css`). Recoleta Alt is licensed and NOT in the repo: copy the `RecoletaAlt-*.ttf` files from the company brand folder into `assets/`. Open Runde loads from Google Fonts.
- **Colors**: Orange `#F05A28`, Navy `#182B6A`, Magenta `#D0358A`, BG Cream `#FAF5ED`.
- **Canvas**: 1280×720 (16:9).
- **NO BULLET LIST**: Never use `<ul>/<li>`. Use `.chips` (navy) or `.pills` (orange).
- **Language**: English default (Italian only if explicitly requested).
- **Density**: Max 8 words per headline, max 10 words per chip. One idea per slide.
- **Style Isolation**: Never style inline in HTML. Style lives in `lemons_brand.css`.

## Procedure

1. Copy CSS, logos and fonts from this skill's `assets/` folder (the skill directory shown when the skill loads) to a working directory:
   ```bash
   ASSETS="<this skill's directory>/assets"
   WORK="$(mktemp -d)"
   cp "$ASSETS"/*.css "$ASSETS"/*.png "$ASSETS"/*.ttf "$WORK"/ 2>/dev/null
   ```
2. Write HTML file `$WORK/deck_NAME.html` using the standard slide structure (`.slide.cover`, `.slide`, `.slide.closing`).
3. Render PDF via Python script:
   ```bash
   python3 "$ASSETS/render_deck.py" $WORK/deck_NAME.html $WORK/deck_NAME.pdf
   ```
4. Output saved to requested destination (default: `~/Desktop/Agent-docs/` or `~/Desktop/PDF Generati/`).
