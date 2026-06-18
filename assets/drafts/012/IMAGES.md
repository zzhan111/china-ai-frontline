# 012 配图素材索引

## 渲染卡片

| File | Use in draft | Source | License | Notes |
|------|-------------|--------|---------|-------|
| `timeline-48h.png` | §01 48h 时间线 | Self-rendered (Pillow) | n/a | 1800×581, 4 events: 06-02 → 06-17 |
| `routes-framework.png` | §06 三条路线对比 | Self-rendered (Pillow) | n/a | 1780×500, 3-column layout: 账户层/赔付层/协议层 |

## Draft section mapping

| Draft section | Image | Placement suggestion |
|--------------|-------|---------------------|
| §01 48h 窗口 | `timeline-48h.png` | 时间线结束后（"同一周里，中国 AI 支付的四个主要玩家都完成了产品就位的动作"之后） |
| §06 三条路线 | `routes-framework.png` | 对比表之后（"它们不是谁对谁错"段落之后） |

## Render instructions

```bash
cd /home/zhang/china-ai-frontline/assets/drafts/012
python3 render_cards.py
```

## Suggested 公众号 cover

`routes-framework.png` — 三条路线框架是全文核心论点，适合作为封面。备选：`timeline-48h.png` 如果更强调时间紧迫感。

## Attribution notes

All cards self-rendered, no external attribution required.
