---
name: proposta-economica
description: "Generates official Lemons in the Room PDF price quotes."
version: 1.0.0
author: Niccolò Cesareo-Santoro, Lemons in the Room
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Finance, Sales, PDF, Proposals, Productivity]
    category: productivity
---

# Proposta Economica Skill

Generates formal, branded Lemons in the Room commercial proposals (A4 PDF) from raw quote sheets or source draft PDFs.

## When to Use

- "Fai la proposta economica", "genera proposta per [cliente]", "crea preventivo".
- When given a raw PDF draft or quote details to convert to the official design.

## Prerequisites

- Assets are in this skill's `assets/` folder (the skill directory shown when the skill loads):
  - Fonts: Open Runde (included). Recoleta Alt is a licensed font and is NOT in the repo: copy `RecoletaAlt-Regular.ttf` and `RecoletaAlt-Bold.ttf` from the company brand folder into `assets/`. Without them headlines fall back to a default serif.
  - Logos & icons: Lemons brown and white
  - Cover images: `cover_1..5.webp`, `proposal_hero.jpg`
  - Render script: `render_proposal.py` (needs `pip install playwright` and `playwright install chromium`)

## Procedure

1. **Extract data from source PDF / prompt**:
   - `client_name`: Client / hospital name.
   - `n_visori`: Headsets count per package.
   - `anni`: Duration (1, 2, or 3 years).
   - `activation_cost`: Gross LEMO START activation fee.
   - `premium_cost` / `renewal_cost`: Renewal fee from year 2.
   - `sconti[]`: Itemized discount lines (exact labels and amounts).
   - `totale`: Final total amount.
   - Layout variant: Standard (box unico), Cards (comparativa), or Lemo Smile (odontoiatria).
2. **Setup assets in temp directory**:
   ```bash
   SKILL="<this skill's directory>/assets"
   WORK="$(mktemp -d)"
   cp "$SKILL"/* "$WORK"/
   ```
3. **Build HTML**:
   - Page 1: Cover with `proposal_hero.jpg`, Lemons logo, and optional client logo.
   - Page 2: Detailed quote table with dynamically calculated Y positions.
   - Page 3: Subscriptions comparison (CARE, PREMIUM, ADVANCED) — omitted for LEMO SMILE.
4. **Render PDF**:
   ```bash
   python3 "$SKILL/render_proposal.py" "$WORK/proposta_cliente.html" "$HOME/Desktop/PDF Generati/[Cliente] - Proposta Economica.pdf"
   ```
5. Confirm output path to user.
