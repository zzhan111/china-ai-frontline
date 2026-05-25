# post-2026-05-25-001：browse.sh 的真正价值是 SDK，不是它的云端

状态：draft
来源：inbox/2026-05.md#2026-05-24-22-36
首发平台：X
audience：AI builder + 浏览器自动化研究者（懂 CDP、有本地浏览器自动化需求）
tone：观察型 + 反共识断言
是否升级长文：待观察（如果反馈好，可以升级 topic「浏览器即 API 的两条路」）

### 一句话观点

browse.sh 已经把浏览器自动化的常见 API 封装齐了；如果你已经有本地浏览器核心，正确做法是换芯，不是从头再造一遍 SDK。

### 近似实现 / 待查

- [browse.sh](https://browse.sh/) — 浏览器即 API，但和 headless 云端绑定
- [bb-browser](https://github.com/epiral/bb-browser) — 本地有头浏览器 + CDP，已经有 36+ 站点 adapter
- Playwright / Puppeteer — 通用底层，但要重新封装"自动化 SDK"层
- [browserbase](https://docs.browserbase.com/) — 商业 cloud 方案，封装类似

差异化：把 browse.sh 的 SDK 拆出来当通用适配层、bb-browser 当本地执行核心——这种"上层 API 不变 / 底层换芯"思路目前看没有公开实现。

### X thread 草稿

**1/**
如果你已经有本地浏览器（WSL chromium、360ChromeX 这类），browse.sh 的真正价值不是它的云端，是它的 SDK。

它把"浏览器自动化常见 action"封装齐了。bb-browser 这种本地核心要做的是换芯，不是从头再造一遍库。

**2/**
具体说：browse.sh 现在的 SDK 绑定它自己的 headless 实例。你调它的 API → 走它的服务端 → 走它的浏览器。

但 API 本身（点击、抓取、表单、wait_for）是和"哪个浏览器"解耦的。这是 swap 而不是 fork 的前提。

**3/**
换芯思路：
- browse.sh SDK 不变（用户视角）
- 中间一层 adapter，把它的 action 协议翻译到本地 CDP
- 本地浏览器（有头、保留登录态）执行

省下：再造一遍 SDK 的工作。
得到：自动化 + 真实登录态 + 不依赖云。

**4/**
反过来看 browse.sh 自己的设计：它做的是「浏览器即 API」，思路和 bb-browser 一致。差别只是它选了 headless 云端，bb-browser 选了本地有头。

API 抽象层共享：这是 swap 而不是 fork 的理由。

**5/**
还没动手，先放在 inbox 看反馈。

如果你也在做浏览器 agent 工具，欢迎 reply 你的思路。特别是有没有评估过 browse.sh 当 adapter target 的可行性、或者本地 CDP 适配 cloud SDK 的踩坑经验。

### posts-eval

跑分（2026-05-25，posts-eval v1 after parser fix）：

```
post-2026-05-25-001 [x-cn] browse.sh 的真正价值是 SDK，不是它的云端
  Summary: 5 PASS / 0 WARN / 0 FAIL
```

历史迭代：
- 第 1 次：4 PASS / 2 WARN / 0 FAIL（ai-flag:em-dash-abuse 9 次）
- 修了 thread 区 3 处 `——` → 句号/逗号/冒号
- 第 2 次：5 PASS / 0 WARN / 0 FAIL ✅

dogfood 过程发现的事见 `contracts/posts/EVOLUTION.md` 的 phase-2 SKILL dogfood entry。

### Humanizer

humanizer: pending（按 SKILL step 7，humanize 在 eval 之后）

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
