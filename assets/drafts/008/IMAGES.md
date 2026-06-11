# drafts/008 — Image Sources Reference

> Generated: 2026-06-11
> For: `drafts/008/draft-v1.2.md` "Dario 的'树懒'提案：Anthropic CEO 为什么现在求监管？"

Each image is mapped to the article paragraph that references it, with the source URL, license, and a one-line note.

---

## Direct External Sources (8 images, 7 sources)

| File | Use in draft | Source | License | Notes |
|------|--------------|--------|---------|-------|
| `treebeard.jpg` | Opening Treebeard metaphor (Section 1 intro) | https://en.wikipedia.org/wiki/Treebeard | CC BY-SA 3.0 (Wikipedia commons) | 250×178 thumbnail, LOTR character portrait |
| `faa-seal.png` | FAA-style mandatory testing (Section 1 #1) | https://en.wikipedia.org/wiki/Federal_Aviation_Administration | Public Domain (US gov seal) | Official seal of FAA |
| `state-bills-card.png` | CA SB 53 / NY RAISE / IL SB 315 (Section 2) | Self-rendered from Dario essay Section 1 | n/a (custom card) | 1400×800, color-coded bill summary |
| `economic-index.png` | Anthropic Economic Index reference (Section 1 #4) | https://www.anthropic.com/economic-index | © Anthropic (used as primary source) | 2964×1656, original Anthropic publication image |
| `mythos-cyber-callout.png` | Claude Mythos Preview cybersecurity signal (Section 2) | Self-rendered from Dario essay Section 1 | n/a (custom card) | 1400×800, quote + 4 risk areas |
| `hn-summary-card.png` | HN 138 pts / 198 comments (Section 3) | Self-rendered from HN Algolia API | n/a (custom card) | 1400×900, dark theme, top-3 quotes |
| `dario-3-essay-timeline.png` | Three-essay framework (Section 2) | Self-rendered from darioamodei.com | n/a (custom card) | 1400×700, color-coded timeline |
| `fable5-launch-hero.png` | Mythos Preview / cybersecurity context (Section 2) | https://www.anthropic.com/news/claude-fable-5-mythos-5 | © Anthropic (official announcement) | 2880×1620, official Fable 5/Mythos 5 launch hero |

## Dario's Own Essay Covers (3 images)

| File | Source | Notes |
|------|--------|-------|
| `dario-policy-og.jpg` | https://darioamodei.com/post/policy-on-the-ai-exponential | Official OG image from his own blog (the article being analyzed) |
| `dario-interp-og.jpg` | https://darioamodei.com/post/the-urgency-of-interpretability | Essay #2 in the three-essay framework |
| `dario-deepseek-og.jpg` | https://darioamodei.com/post/on-deepseek-and-export-controls | Essay #1 in the three-essay framework |

## Open-Weight Logos (2 images, for Section 3 #2 "强制闭源" point)

| File | Source | License | Notes |
|------|--------|---------|-------|
| `mistral-logo.png` | https://en.wikipedia.org/wiki/Mistral_AI | CC BY-SA 4.0 (Wikipedia commons) | 250×177, Mistral AI official logo |
| `qwen-logo.png` | https://en.wikipedia.org/wiki/Qwen | CC BY-SA 4.0 (Wikipedia commons) | 330×97, Qwen official logo |

## Draft Section Mapping (for content review)

```
Section 1 (开场)         → treebeard.jpg
Section 1 #1 (FAA)       → faa-seal.png
Section 1 #4 (经济)       → economic-index.png
Section 1 #1-#4 综述      → state-bills-card.png
Section 2 (三段论)        → dario-3-essay-timeline.png
Section 2 (Mythos 信号)  → mythos-cyber-callout.png + fable5-launch-hero.png
Section 3 (社区反弹)      → hn-summary-card.png
Section 3 #2 (强制闭源)  → mistral-logo.png + qwen-logo.png
全文 (Dario 系列)        → dario-policy-og.jpg / interp / deepseek
```

## Important Caveats

1. **`mistral-logo.png` is 848 bytes** — likely a small/colormapped placeholder. Visually OK but pixelated at large size. For published 公众号 cover use, recommend re-rendering or replacing with a higher-res source from Mistral press kit.
2. **`fable5-launch-hero.png` is 5.3MB** — high-res, may slow down web display. Consider compressing to <500KB for production.
3. **All `*og.jpg` are official blog cover images** — safe to use as editorial reference (citing Dario's own blog as the analyzed source).
4. **Wikipedia commons images are CC BY-SA** — require attribution. Treebeard image must attribute "Wikipedia contributors, Treebeard page".
5. **Custom-rendered cards (`*-card.png`, `*-callout.png`)** are generated from Dario's own essay text — safe to use as analytical commentary.

## Suggested Pick for 公众号 Cover

For the public WeChat cover (no internal distribution), recommend:

- **Primary candidate**: `dario-3-essay-timeline.png` (best narrative density, neutral tone, no third-party IP risk)
- **Alternative**: `hn-summary-card.png` (dark theme matches Fable 5 cards we made earlier, provides social proof angle)
- **Avoid for cover**: `fable5-launch-hero.png` (Anthropic trademark, 5MB too large)

## Re-render Instructions

```bash
cd /home/zhang/research/dario-ai-exponential-policy
python3 render_state_bills.py
python3 render_cards.py
```

Both scripts are self-contained. Modify the data structures at the top to update content; the layouts are template-bound.
