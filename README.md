# Lemons in the Room: Hermes skills

Shared Hermes skills for the team.

## Install everything (one line)

macOS, Linux, Git Bash:
```bash
hermes skills tap add Lemons-in-the-Room/hermes-skills && for s in lemonsintheroom-skill caveman proposta-economica lemons-slides lemons-research; do hermes skills install Lemons-in-the-Room/hermes-skills/skills/$s --yes; done
```

Windows PowerShell:
```powershell
hermes skills tap add Lemons-in-the-Room/hermes-skills; "lemonsintheroom-skill","caveman","proposta-economica","lemons-slides","lemons-research" | ForEach-Object { hermes skills install "Lemons-in-the-Room/hermes-skills/skills/$_" --yes }
```

## Update
```
hermes skills check
hermes skills update
```

## Skills
| Skill | Use |
|---|---|
| `lemonsintheroom-skill` | Company context, values, tone, writing rules |
| `caveman` | Ultra-short reply mode |
| `lemons-research` | Healthcare and MDR research with sources |
| `lemons-slides` | On-brand 16:9 PDF decks |
| `proposta-economica` | Branded PDF price quotes |

`lemons-slides` and `proposta-economica` need `pip install playwright` and `playwright install chromium`. They also need the licensed Recoleta Alt fonts, which are not in this repo: copy the `.ttf` files from the company brand folder into the skill's `assets/` folder.

## Contribute
Add or edit a folder under `skills/`, open a PR. Each skill needs a `SKILL.md` with `name` and `description`. No secrets, no licensed fonts, no client data in this repo.
