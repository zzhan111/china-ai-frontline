# prompts/

Vendored upstream prompts used as **offline / unrecognized-agent fallback** by `skills/humanizer-usage.md`.

## What's in here

| File | Source | License |
|---|---|---|
| `humanizer-zh.md` | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) @ 91f3d39 | MIT |
| `humanizer.md` | [blader/humanizer](https://github.com/blader/humanizer) @ 8b3a178 | MIT |
| `LICENSES.md` | Full MIT text for both upstreams | — |

## When these are used

Normal path (preferred): `tools/install-humanizer.py` clones the upstream repos to `external/{humanizer-zh,humanizer}/`. Agents that recognize SKILL.md files (Claude Code, OpenCode, etc.) invoke those directly.

Fallback path (this directory): when `external/` install is unavailable — offline machine, restricted network, unrecognized agent framework — any LLM can read `prompts/humanizer-{zh,}.md` and perform the humanize step directly.

## How to refresh

```
python tools/install-humanizer.py --refresh-prompts
```

This re-fetches the upstream SKILL.md files via `gh api` (or `curl` fallback) and overwrites `humanizer-zh.md` / `humanizer.md` in place, preserving the attribution header.

## What NOT to do

- Do not hand-edit `humanizer-zh.md` or `humanizer.md` — your changes will be overwritten on next refresh
- If you want to customize humanize behavior, propose changes upstream or fork
