# Issue 015 · Commit Log

```
commit b15e3f2 (HEAD -> main, tag: issue-015)
Author: 之哲 & Hermes
Date:   2026-06-26

    Issue 015: 当中国高校开始「砍文科给 AI 让路」，高考生的家长怎么办？

    原创 之哲 UIEVENTS事历 · 公众号长文
    数据采集: 2026-06-25~26
    发布窗口: 2026 高考出分后 48h (6/25-6/27)
    字数: 3,013 (preview) / 6,615 (full draft)
```

## 版本演进

| 版本 | 日期 | 字数 | 评分 | 关键变化 |
|---|---|---|---|---|
| v1.0 | 06-25 | 3,350 | — | 11 英文源 + 7 步框架 |
| v1.1 | 06-26 | 5,796 | 88 B+ | +6 中文官方源 |
| v1.2 | 06-26 | 6,615 | 99 A- | +情感锚 +体验层 +叙事重组 |
| v1.3 | 06-26 | 6,600 | — | humanizer (em dash 104→6) |
| preview | 06-26 | 3,013 | — | 公众号格式 |

## CRA 修复路径

```
v1.1 88/120 (B+) → contract review → 3 优先修复 → v1.2 99/120 (A-) → humanizer → 2/13 red flags → preview
  LF-3  6→8  「填志愿那个晚上」情感锚
  LF-11 6→8  体验层 4 真实信号（无编造）
  LF-4  7→8  周伯文从 5.3 移到 3.0
```

## 数据来源

| 类型 | 数量 | 代表 |
|---|---|---|
| 英文一手抓取 | 11 URL | Rest of World / HN Algolia / Anthropic 5th Report / arXiv / Texas Tribune |
| 中文官方抓取 | 6 URL | eol.cn ×4 / 澎湃 ×1 / 国务院政策库 ×1 |
| 总 URL | 17 | 15 域名 |
| 真实抓取占比 | ~80% | |

## 关键校正

- CUC 砍 5 个专业（非网络流传的 16 个）— 基于 restofworld 原文
- 教育部 5 年撤销 1.22 万 + 新增 1.02 万 — eol.cn 2026-04-28 官方数据
- "具身智能"为 2026 交叉学科门类新专业，9 所高校（哈工大、北航等）获批

## 文件清单

```
drafts/015/
├── draft-v1.0.md        (20 KB)    原始版
├── draft-v1.1.md        (30 KB)    +中文源补强
├── draft-v1.2.md        (34 KB)    +锚点+体验层+叙事重组
├── draft-v1.3.md        (34 KB)    humanizer 版
├── review-v1.1.md       (25 KB)    合同审查 88/120
├── review-v1.2.md       (42 KB)    合同审查 99/120
├── evolution.md          (21 KB)    5 条演化记录
└── preview.md            (13 KB)    公众号发布版
```

## 发布状态

- [x] draft 完成 (v1.3)
- [x] contract review 通过 (99/120 A-)
- [x] humanizer 完成 (em dash 104→6)
- [x] preview 生成 (3,013 字)
- [ ] 配图
- [ ] 公众号发布
