---
name: posts-author
description: Author a posts/ draft end-to-end — read the contract for the target platform, draft platform-native (never copy-paste across platforms), self-review against the rubric, run posts-eval, request human input when audience/route/reject is uncertain. Use when asked to write or revise any file under posts/.
---

# posts-author

You are about to write or revise a `posts/` draft. **Stop and read this in full before touching any file.** This SKILL is the agent-facing counterpart to `contracts/posts/v1.1` and `tools/posts-eval.py`. Past authoring runs have accumulated specific failure modes — they are listed below and you should not repeat them.

## Inviolable rules

These rules are derived from `contracts/posts/v1-common.md` + the three platform contracts + `contracts/posts/EVOLUTION.md`. Violating any of them means the draft will either fail `posts-eval` or be rejected by the human editor.

1. **Read the contract before drafting.**
   - `contracts/posts/v1-common.md` — always
   - `contracts/posts/<platform>/v1.md` — the target platform
   - If you write for multiple platforms, read all relevant contracts; **never** lift one platform's draft and adapt it. Platform-native re-write is mandatory (v1-common §5 #5).
2. **Don't invent dimensions or thresholds.** If a draft seems "off" on a dimension not in the contract, surface it to the human and propose a v-next revision — do not silently up-weight your own preference.
3. **`audience` field is required.** v1.1 §2 lists it; dogfood shows past drafts omitted it. Filling it lets `posts-eval` run the routing check. If you cannot infer a specific audience, **stop and ask the human** — do not write `"所有人"` or skip the field.
4. **Run `posts-eval` before declaring done.** Every FAIL must be fixed by re-drafting (not by deleting the check). Every WARN must be either fixed or explicitly acknowledged in the post block (`acknowledged: <reason>`).
5. **Mandatory order: draft → posts-eval → humanizer → checklist.** Never humanize before eval — humanizer rewrites natural language and may break links, numbers, or proper nouns that eval relies on.
6. **Dig-hole must have candy.** Any phrase like "详见 / 在 repo 里有完整记录 / 后续会讲" requires an adjacent URL, screenshot, or explicit Part 1/N declaration with publish-time anchor. See x-cn/v1.md §2.4.
7. **Don't bypass hard rejects.** If posts-eval returns FAIL on audience-mismatch (xiaohongshu §6 #5), AI-red-flag count ≥3 (common §3 #5), or ad-law极限词 (xiaohongshu §6 #1) — do not "soften" the draft to pass. Re-route the draft to a different platform or discard.

## Authoring workflow

```
1. READ the contract for the target platform
   → contracts/posts/v1-common.md (always)
   → contracts/posts/<x-cn|xiaohongshu|moments>/v1.md
   → If multiple platforms requested, treat as N separate authoring jobs

2. IDENTIFY route + audience
   → If user specified platform → use it (but verify audience match)
   → If user didn't specify → propose route per v1-common §6 (X for 判断/讨论,
     xiaohongshu for 方法/系统, moments for 状态/熟人感)
   → audience: ask the human for the specific reader segment if unclear.
     For xiaohongshu, check against v1.1 §6 #5 three-tier table
     (核心技术画像 reject / 半技术允许 / 核心画像无限制)

3. DRAFT platform-native content
   → Use the platform's §1.2 写作规则 as scaffold
   → Never adapt another platform's text — start from the topic+audience
   → Length:
     • x-cn: each tweet ≤140 中文字符, thread 5-12 推
     • xiaohongshu: 800-1300 字甜区, <500 不发, >1800 拆系列
     • moments: 30-150 甜区, >300 警戒, >500 折叠

4. SELF-REVIEW against contract before running eval
   This catches the high-frequency mistakes posts-eval can't catch:
   → Hook: does the first line / first tweet stand alone in 0.5s?
     Not "一个不寻常的 X" / "聊聊 X" / "今天分享一个" / "说一下 X 为什么值得"
   → 营销腔: any "不是 X 是 Y" pairs? 三/四字短句堆叠? 元价值断言
     ("真正的差异化" / "稀缺性" / "天然吸引")?
   → 挖坑给糖: every "详见/后续/答案在" has a URL or Part N+time anchor?
   → audience 路由: does the body actually serve the declared audience?

5. RUN posts-eval
   → python tools/posts-eval.py <path-to-draft-file>
   → FAIL → go back to step 3, do not "soften" to pass
   → WARN → either fix (preferred) or acknowledge in post block:
     "### posts-eval
      acknowledged: hook:anti-pattern — 故意软抽象，因为...(reason)"

6. WRITE the post block to posts/ (or create new file per naming convention)
   → File: posts/<platform>.md (legacy, multi-block) OR
     posts/<platform>-YYYY-MM-DD-<主体>.md (new, one-block-per-file)
   → Format: see posts/README.md
   → Required metadata fields: 状态, 来源, 首发平台, audience, tone (optional but recommended)
   → Status: draft

7. (handoff to humanizer)
   → Now read skills/humanizer-usage.md
   → Run humanizer-zh on the "### 平台草稿 / X thread 草稿 / ..." section
   → Append humanizer signature to post block (see humanizer-usage.md §6)

8. (handoff to checklist)
   → ops/social-post-checklist.md
```

## Anti-patterns observed in past drafts

From `contracts/posts/EVOLUTION.md` dogfood (PR #16 → posts-eval v1) and from the v1.1 修订 evidence.

| Anti-pattern | Where it happened | Why it's wrong |
|---|---|---|
| `audience` field omitted | post-2026-05-24-001 / -002 (PR #16) | Contract v1.1 §2 requires it; routing check can't run; downstream agent has no reader anchor |
| Soft-abstract hook ("一个不寻常的 X") | post-2026-05-24-002 first tweet | 0.5s 钩子失效; x-cn §2.1 anti-pattern → score ceiling 8 |
| Meta-value assertion ("真正的差异化" / "天然吸引" / "可以自我繁殖") | post-002 list items | common §4.4 AI red flag — self-coronation without evidence |
| 挖坑不给糖 ("在 repo 里有完整记录" no URL) | post-002 §4 推 | x-cn §2.4 default -5; no Part 1/N exemption applied |
| 一稿多投 (same text adapted across platforms) | (hypothetical, easy to fall into) | v1-common §5 #5: platform-native rewrite is required, not optional |
| Humanizer before posts-eval | (process order error) | humanizer 重写自然语言，会破坏链接/数字/专有名词 → eval 抓不到原 draft 的真实问题 |
| Soften draft to dodge FAIL (e.g. rename audience to bypass routing) | (gaming the rubric) | bb-adapter-evolver hard rule #8: honesty over politeness; if a FAIL is the right outcome, accept it |
| List-item marketing stack ("1. 真正的差异化 / 2. 不消耗 / 3. 自我繁殖 / 4. 天然吸引") | post-002 third tweet | posts-eval can't catch this (structural, not string); SKILL is responsible: if items are all 元价值断言, rewrite them as concrete consequences with examples |

## Workflow gates — stop and ask the human

These are decisions you cannot make alone:

1. **Audience unclear.** If `audience` would be `"所有人"` / `"感兴趣的人"` / unspecified — stop, ask for the specific reader segment.
2. **Multi-platform routing.** If two or more platforms score equally well in your routing — stop, propose the trade-off (e.g. "X 适合传播观点，xiaohongshu 适合沉淀方法，要哪个？").
3. **posts-eval returns FAIL.** Especially for `hard-reject:audience-mismatch` or `hard-reject:ad-law` — do not silently rewrite to pass; ask the human "this looks like a route error, should we move it to <other platform> instead?"
4. **Dig-hole references that can't be supplied.** If the draft references PR/issue/commit but the repo is private / the link doesn't exist yet — ask "should I keep the reference (and accept -5) or drop it?"
5. **Sensitive content not covered by contract.** Personal info, real names, third-party data, dated medical/legal/financial claims — common §3 hard rejects exist, but ask explicitly when borderline.
6. **Cross-language draft.** If audience is bilingual (e.g. 海外华人 AI 圈) and the draft mixes English/Chinese heavily — ask whether to lean one way (humanizer choice depends on it).

## Reading order before authoring

1. **This file** (you are here)
2. `contracts/posts/v1-common.md` — universal scoring + hard rejects
3. `contracts/posts/<platform>/v1.md` — platform-specific dimensions + thresholds
4. `tools/README.md` — how to run posts-eval and interpret output
5. `posts/README.md` — post block output format
6. `contracts/posts/EVOLUTION.md` — cross-session context (what we've learned)
7. (only after writing) `skills/humanizer-usage.md` — humanize handoff
8. (only after humanizing) `ops/social-post-checklist.md` — pre-publish gates

## Quick reference: posts-eval invocation

```bash
# Score a single draft
python tools/posts-eval.py posts/x.md

# Walk a directory (skips README.md and long-form-assessment.md)
python tools/posts-eval.py posts/

# JSON output for downstream automation
python tools/posts-eval.py --json posts/x.md
```

Exit codes: `0` = no FAIL, `1` = ≥1 FAIL, `2` = usage error.

## What this SKILL does NOT cover

- **Long-form drafting (`drafts/NNN/`).** Different rubric, different cadence. Don't apply posts contract to public-account essays.
- **inbox capture.** `inbox/` is append-only and not scored. See `inbox/README.md`.
- **Cross-post strategy (which platforms together, in what order).** That's a `topics/` concern — escalate to the human.
- **Publishing mechanics (when to post, who reposts, ad spend).** Out of contract scope; lives in `ops/`.
