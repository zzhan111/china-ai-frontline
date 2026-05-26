# posts/ — 社媒发布包

## 作用

`posts/` 把 `inbox/` 里的想法变成可发布内容。

一个 post block = 一条社媒内容的全生命周期记录（草稿 + 竞品 + 平台版本 + 发布反馈）。

## 文件约定

按平台一个文件：

```
posts/x.md
posts/xiaohongshu.md
posts/moments.md
```

**不按时间分文件，不按主题分目录**。等内容量真的大到难以管理，再拆。

## Post block 格式

```markdown
## post-YYYY-MM-DD-NNN：<一句话标题>

状态：draft | published | archived
来源：inbox/YYYY-MM.md#YYYY-MM-DD-HH-MM
首发平台：X / 小红书 / 朋友圈
是否升级长文：待观察 | 是（→ topics/NNN-slug.md）| 否

### 一句话观点

<最核心的观点，一句话>

### 近似实现 / 需要调查

- <竞品 / 近似产品 / 相似内容>
- ...

### 平台草稿

<可直接复制粘贴发布的内容>

### Humanizer

humanizer: zh@<version-or-date> | en@<version-or-date> | skipped(reason: ...)

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
```

## 状态生命周期

```
draft → published → archived
            ↓
        (满足升级标准) → topics/NNN-slug.md
```

升级标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)。

## 编号约定

`post-YYYY-MM-DD-NNN`，其中 `NNN` 是当日序号（001 起）。

## 不要做的事

- 不要为单条 post 单独建文件
- 不要把竞品和反馈拆到独立 `research/`、`feedback/` 目录
- 不要把未验证的想法直接搬进 `topics/` 或 `drafts/`
