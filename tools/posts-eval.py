#!/usr/bin/env python3
"""posts-eval — Static checker for posts/ drafts against contracts/posts/v1.1.

Mechanical checks only. Subjective dimensions (hook strength, retweetability,
真实感) require LLM judgment and live in the agent SKILL, not here.

Inspired by bb-adapter-evolver/tools/bb-eval. Mirrors its philosophy:
- declare what's mechanically checkable (URL constants, response shape, ...)
  → here: 字数限制, AI 词汇频次, 极限词, audience 路由, 黑话密度...
- defer subjective judgment to the human / LLM reviewer
- output PASS / WARN / FAIL with line-citable detail

Usage:
    python tools/posts-eval.py posts/x.md
    python tools/posts-eval.py posts/                  # walks .md files
    python tools/posts-eval.py --json posts/x.md       # for agent ingestion
    python tools/posts-eval.py --all posts/            # include published/rejected posts
    python tools/posts-eval.py -h                      # show help
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

# Force UTF-8 stdout on Windows (default is cp936/gbk → 中文乱码)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class Severity(Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


@dataclass
class CheckResult:
    name: str
    severity: Severity
    message: str = ""
    detail: list = field(default_factory=list)


@dataclass
class PostBlock:
    id: str
    title: str
    metadata: dict
    sections: dict
    raw: str
    body: str
    file_path: str
    platform: str


# ---------- Parser ----------

POST_HEADER_RE = re.compile(r"^## (post-\d{4}-\d{2}-\d+(?:-\d+)?)[：:](.+?)$", re.MULTILINE)
SECTION_RE = re.compile(r"^### (.+?)$", re.MULTILINE)
META_RE = re.compile(r"^(状态|来源|首发平台|是否升级长文|audience|tone|goal)[：:]\s*(.+?)$", re.MULTILINE)

# Section names that hold the publishable draft body
BODY_SECTION_KEYS = [
    "平台草稿",
    "X thread 草稿",
    "X 草稿",
    "朋友圈草稿",
    "小红书草稿",
    "笔记草稿",
    "正文",
]


def parse_posts_file(path: Path) -> list[PostBlock]:
    text = path.read_text(encoding="utf-8")
    matches = list(POST_HEADER_RE.finditer(text))
    blocks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        raw = text[start:end]
        block_id = m.group(1)
        title = m.group(2).strip()
        meta = dict(META_RE.findall(raw))

        sections = {}
        sec_matches = list(SECTION_RE.finditer(raw))
        for j, sm in enumerate(sec_matches):
            sec_start = sm.end()
            sec_end = sec_matches[j + 1].start() if j + 1 < len(sec_matches) else len(raw)
            name = sm.group(1).strip()
            sections[name] = raw[sec_start:sec_end].strip()

        body = ""
        for k in BODY_SECTION_KEYS:
            if k in sections:
                body = sections[k]
                break

        platform = infer_platform(path, meta)
        blocks.append(PostBlock(
            id=block_id,
            title=title,
            metadata=meta,
            sections=sections,
            raw=raw,
            body=body,
            file_path=str(path),
            platform=platform,
        ))
    return blocks


def infer_platform(path: Path, meta: dict) -> str:
    name = path.stem.lower()
    if name == "x" or name.startswith("x-"):
        return "x-cn"
    if name == "xiaohongshu" or name.startswith("xiaohongshu-"):
        return "xiaohongshu"
    if name == "moments" or name.startswith("moments-"):
        return "moments"
    p = meta.get("首发平台", "").strip()
    if p in ("X", "x", "Twitter"):
        return "x-cn"
    if p in ("小红书", "xiaohongshu"):
        return "xiaohongshu"
    if p in ("朋友圈", "微信朋友圈", "moments", "Moments"):
        return "moments"
    return "unknown"


# ---------- Common checks (v1.1 common layer) ----------

AI_VOCAB = ["赋能", "生态", "闭环", "底层逻辑", "纵深", "抓手", "链路", "心智"]
EMPTY_CONCLUSIONS = ["未来可期", "值得期待", "让我们拭目以待"]
PROMO_TONE = ["必看", "干货满满", "收藏起来", "建议收藏"]
VAGUE_ATTR = ["专家表示", "研究显示", "数据表明", "业内人士"]
CHATBOT_ARTIFACTS = ["希望对你有帮助", "如有疑问欢迎评论"]
META_VALUE_ASSERTIONS = ["真正的差异化", "稀缺性", "示范性", "天然吸引", "可以自我繁殖", "自我繁殖"]


def ai_smell_score(n: int) -> str:
    if n == 0:
        return "9-10"
    if n == 1:
        return "7-8"
    if n == 2:
        return "5-6"
    if n == 3:
        return "3-4"
    return "0-2"


def check_required_fields(post: PostBlock) -> list[CheckResult]:
    """v1.1 common §2 — required draft fields."""
    results = []
    for f in ["状态", "来源", "首发平台"]:
        if f in post.metadata:
            results.append(CheckResult(f"meta:{f}", Severity.PASS))
        else:
            results.append(CheckResult(f"meta:{f}", Severity.WARN, f"缺字段 {f}"))
    if "audience" not in post.metadata:
        results.append(CheckResult(
            "meta:audience",
            Severity.WARN,
            "缺 audience 字段（v1.1 §2 要求；当前 posts/ 普遍未填）",
        ))
    return results


def check_ai_red_flags(post: PostBlock) -> list[CheckResult]:
    """v1.1 common §4.4 AI red flag detection."""
    text = post.body or post.raw
    flags: list[tuple[str, str]] = []

    # AI vocab ≥3 occurrences total
    vocab_count = sum(text.count(v) for v in AI_VOCAB)
    if vocab_count >= 3:
        hits = {v: text.count(v) for v in AI_VOCAB if text.count(v) > 0}
        flags.append(("ai-vocab", f"AI 词汇出现 {vocab_count} 次: {hits}"))

    for term in EMPTY_CONCLUSIONS:
        if term in text:
            flags.append(("empty-conclusion", f'空泛结论 "{term}"'))
            break
    for term in PROMO_TONE:
        if term in text:
            flags.append(("promo-tone", f'促销腔 "{term}"'))
            break
    for term in VAGUE_ATTR:
        if term in text:
            flags.append(("vague-attribution", f'vague attribution "{term}"'))
            break
    for term in CHATBOT_ARTIFACTS:
        if term in text:
            flags.append(("chatbot-artifact", f'Chatbot artifact "{term}"'))
            break

    # "不是 X 是 Y" ≥2 次 (v1.1)
    nxy = re.findall(r"不是[^，。、,.\n]{1,20}[，。、,.\s]+是", text)
    if len(nxy) >= 2:
        flags.append(("not-x-but-y", f'"不是 X 是 Y" {len(nxy)} 次（v1.1 营销叠加）'))

    # 三/四字短句堆叠 ≥3 连续 (v1.1)
    short_runs = re.findall(
        r"(?:[一-鿿]{1,4}[。！？]\s*){3,}", text
    )
    if short_runs:
        flags.append((
            "short-sentence-stacking",
            f"三/四字短句堆叠 {len(short_runs)} 处",
        ))

    # 元价值断言 (v1.1)
    meta_hits = [t for t in META_VALUE_ASSERTIONS if t in text]
    if meta_hits:
        flags.append(("meta-value-assertion", f"元价值断言 {meta_hits}"))

    # em dash 滥用
    em_count = text.count("——") + text.count("—")
    if em_count >= 5:
        flags.append(("em-dash-abuse", f"em dash {em_count} 次"))

    # 排比堆砌
    parallel = len(re.findall(r"不仅[^，。、,.\n]{1,20}而且", text))
    if parallel >= 3:
        flags.append(("parallelism", f'"不仅...而且..." {parallel} 次'))

    # 过度结构化：短文出现数字 emoji
    digit_emoji = sum(text.count(c) for c in "1️⃣2️⃣3️⃣4️⃣5️⃣")
    if digit_emoji > 0 and len(text) < 500:
        flags.append(("over-structure", f"短文出现数字 emoji"))

    results = []
    for name, msg in flags:
        results.append(CheckResult(f"ai-flag:{name}", Severity.WARN, msg))

    n = len(flags)
    if n >= 3:
        results.append(CheckResult(
            "ai-flag:hard-reject",
            Severity.FAIL,
            f"{n} 个 AI red flag 触发 common §3 #5（AI 痕迹严重），直接 rejected",
        ))
    else:
        results.append(CheckResult(
            "ai-flag:count",
            Severity.PASS if n == 0 else Severity.WARN,
            f"{n} 个 red flag，§4.4 AI 痕迹分: {ai_smell_score(n)}",
        ))
    return results


# ---------- x-cn checks (v1.1) ----------

HOOK_SOFT_ABSTRACT = ["一个不寻常的", "一件值得说的事", "聊聊", "想说一下", "聊一下"]
HOOK_META_DESC = [
    r"这是一篇关于",
    r"下面.{1,5}推讲",
    r"今天写一下",
    r"这条\s*thread",
]
HOOK_VALUE_PREVIEW = [r"说一下.{1,10}为什么", r"今天分享一个", r"想公开一下"]

TRANSL_OLD = [
    r"在.{1,10}的背景下",
    r"针对.{1,10}而言",
    r"进行优化",
    r"进行分析",
    r"进行讨论",
    r"差异性",
    r"同质性",
]
TRANSL_NEW = [
    (r"[^。！？\n]{5,40}[。！？]\s*这两?个?\s*(?:PR|issue|功能).{1,20}是什么[？?]", "短句自问自答"),
    (r"(?:看起来|看上去).{1,20}[。！？]\s*其实是", "setup-punch"),
]

DIG_HOLE = [
    "详见",
    "在 X 里有完整记录",
    "在 repo 里有完整记录",
    "后续会讲",
    "答案在",
    "后续展开",
    "下次展开",
    "留着以后写",
    "等我有时间",
    "在 repo 里都有",
]


def split_tweets(body: str) -> list[str]:
    """Split a thread body into individual tweets by **N/** or N/ markers."""
    parts = re.split(r"\n\*\*\d+/\*\*\n|\n\d+/\s*\n", body)
    return [p.strip() for p in parts if p.strip()]


def check_x_cn(post: PostBlock) -> list[CheckResult]:
    results = []
    body = post.body or post.raw

    tweets = split_tweets(body)
    long_tweets = []
    for i, t in enumerate(tweets):
        chars = len(re.sub(r"\s", "", t))
        if chars > 140:
            long_tweets.append((i, chars))
    if long_tweets:
        results.append(CheckResult(
            "len:tweet-overflow",
            Severity.WARN,
            f"{len(long_tweets)} 条推超过 140 中文字符",
            detail=[f"tweet[{i}]: {c} 字符" for i, c in long_tweets],
        ))
    else:
        results.append(CheckResult("len:tweet", Severity.PASS))

    # Hashtag detection: \w covers ASCII, add CJK range for Chinese hashtags
    hashtags = re.findall(r"#[\w一-鿿]+", body)
    if len(hashtags) > 2:
        results.append(CheckResult(
            "fmt:hashtag-overflow",
            Severity.WARN,
            f"{len(hashtags)} 个 hashtag（上限 2）",
        ))

    md_h = re.findall(r"^#{1,6} ", body, re.MULTILINE)
    if md_h:
        results.append(CheckResult(
            "fmt:markdown-heading",
            Severity.FAIL,
            f"{len(md_h)} 个 markdown 标题（X 不渲染）",
        ))

    # Hook anti-pattern (v1.1 §2.1)
    first = tweets[0] if tweets else body[:200]
    hook_hits = []
    for pat in HOOK_SOFT_ABSTRACT:
        if pat in first:
            hook_hits.append(f'软抽象 "{pat}"')
    for pat in HOOK_META_DESC:
        if re.search(pat, first):
            hook_hits.append(f"元描述 /{pat}/")
    for pat in HOOK_VALUE_PREVIEW:
        if re.search(pat, first):
            hook_hits.append(f"价值预告 /{pat}/")
    if hook_hits:
        results.append(CheckResult(
            "hook:anti-pattern",
            Severity.WARN,
            f"第一推 anti-pattern（v1.1 §2.1，钩子分上限 8）",
            detail=hook_hits,
        ))

    # Translationese
    old_hits = []
    for pat in TRANSL_OLD:
        m = re.findall(pat, body)
        if m:
            old_hits.append(f"/{pat}/ {len(m)} 次")
    if old_hits:
        results.append(CheckResult(
            "translationese:old",
            Severity.WARN,
            "老式 GPT 译文腔",
            detail=old_hits,
        ))

    new_hits = []
    for pat, label in TRANSL_NEW:
        m = re.findall(pat, body)
        if m:
            new_hits.append(f"{label} ({len(m)} 次)")
    if new_hits:
        results.append(CheckResult(
            "translationese:new-rhetoric",
            Severity.WARN,
            "新式英文修辞腔（v1.1 §2.3，每次 -3）",
            detail=new_hits,
        ))

    # 挖坑不给糖 (v1.1 §2.4)
    dig_issues = []
    for w in DIG_HOLE:
        if w in body:
            idx = body.find(w)
            ctx = body[max(0, idx - 80) : idx + 120]
            if not re.search(r"https?://", ctx):
                dig_issues.append(f'"{w}" 附近无链接')
    if dig_issues:
        # Part 1/N exemption: series threads get lighter penalty
        is_series = bool(re.search(r"(?:Part\s*)?[1１一]\s*/\s*[NnXx\d]|系列\s*[1一]", body))
        if is_series:
            results.append(CheckResult(
                "retweet:dig-hole-series",
                Severity.WARN,
                "挖坑不给糖（系列 Part 1/N 豁免，-1 而非 -5）",
                detail=dig_issues,
            ))
        else:
            results.append(CheckResult(
                "retweet:dig-hole",
                Severity.WARN,
                "挖坑不给糖（v1.1 §2.4，-5）",
                detail=dig_issues,
            ))

    # PR/issue 引用但无 github 链接
    pr_refs = re.findall(r"(?:PR\s*#\d+|issue\s*#\d+)", body)
    if len(pr_refs) >= 2 and not re.search(r"github\.com", body):
        results.append(CheckResult(
            "retweet:inaccessible-ref",
            Severity.WARN,
            f"{len(pr_refs)} 个 PR/issue 引用但无 github 链接 (-3)",
        ))

    return results


# ---------- xiaohongshu checks (v1.1) ----------

XHS_AD_WORDS = ["最佳", "第一", "唯一", "绝对", "最强", "最神", "永远不"]
XHS_TECH_AUDIENCE = ["工程师", "程序员", "后端", "前端", "coding agent", "AI builder", "DevOps", "运维"]
XHS_SEMI_TECH_AUDIENCE = ["产品经理", "PM", "数据分析师", "运营", "增长"]
XHS_BEGINNER_HINT = ["想学", "入门", "小白", "新手"]
TECH_PREREQ_TERMS = ["git", "commit", "PR", "命令行", "CLI", "API", "function", "json", "yaml", "terminal", "bash"]


def check_xiaohongshu(post: PostBlock) -> list[CheckResult]:
    results = []
    body = post.body or post.raw

    title_chars = len(re.sub(r"\s", "", post.title))
    if title_chars > 20:
        results.append(CheckResult(
            "title:length",
            Severity.WARN,
            f"标题 {title_chars} 字（>20 -3）",
        ))

    body_chars = len(re.sub(r"\s", "", body))
    if body_chars < 500:
        results.append(CheckResult(
            "len:under",
            Severity.WARN,
            f"正文 {body_chars} 字（<500 直接 needs_revision）",
        ))
    elif body_chars > 1800:
        results.append(CheckResult(
            "len:over",
            Severity.WARN,
            f"正文 {body_chars} 字（>1800 必须拆系列）",
        ))

    ad_hits = [w for w in XHS_AD_WORDS if w in body]
    if ad_hits:
        results.append(CheckResult(
            "hard-reject:ad-law",
            Severity.FAIL,
            f"广告法极限词 {ad_hits}",
        ))

    audience = post.metadata.get("audience", "")
    if not audience:
        results.append(CheckResult(
            "audience:missing",
            Severity.WARN,
            "audience 未填，无法做路由检查",
        ))
    else:
        # Avoid false positives: "工程师的妻子" should NOT match as tech audience
        # Only match if word is a primary subject (not preceded by 的/给/为/向)
        def is_primary_audience(word: str, text: str) -> bool:
            if word not in text:
                return False
            idx = text.find(word)
            if idx > 0 and text[idx - 1] in "的给为向":
                return False
            return True

        tech = [w for w in XHS_TECH_AUDIENCE if is_primary_audience(w, audience)]
        semi = [w for w in XHS_SEMI_TECH_AUDIENCE if is_primary_audience(w, audience)]
        beginner = any(h in audience for h in XHS_BEGINNER_HINT)
        if tech and not beginner:
            results.append(CheckResult(
                "hard-reject:audience-mismatch",
                Severity.FAIL,
                f"audience 含核心技术画像 {tech}（v1.1 §6 #5）→ reroute x-cn",
            ))
        elif semi:
            results.append(CheckResult(
                "audience:semi-tech",
                Severity.WARN,
                f"audience 含半技术画像 {semi}（v1.1 §6）→ §3.3 二阶判据约束",
            ))

    # Reader-base alignment (v1.1 §3.3)
    code_hits = [t for t in TECH_PREREQ_TERMS if re.search(rf"\b{re.escape(t)}\b", body, re.IGNORECASE)]
    if code_hits:
        results.append(CheckResult(
            "actionable:tech-prereq",
            Severity.WARN,
            f"方法涉及技术前置 {code_hits}（v1.1 §3.3 二阶判据，可执行分上限 6）",
        ))

    return results


# ---------- moments checks (v1.1) ----------

MOMENTS_PUBLIC_OPENING = ["今天想和大家分享", "借此机会", "今天和大家聊聊", "今天给大家"]
# Jargon list: exclude high-penetration words ("agent", "topic") that are now mainstream
MOMENTS_JARGON = [
    "git", "commit", "PR", "merge", "rebase", "CI/CD", "webhook", "CLI",
    "k8s", "docker", "inbox", "draft", "MCP", "repo",
]
# "agent" removed: AI agent is mainstream social discourse, not niche jargon
# "topic" removed: common English word, not tech-specific
# "API" kept: still relatively technical for moments audience


def check_moments(post: PostBlock) -> list[CheckResult]:
    results = []
    body = post.body or post.raw

    chars = len(re.sub(r"\s", "", body))
    if chars > 500:
        results.append(CheckResult(
            "len:hard-limit",
            Severity.FAIL,
            f"{chars} 字（>500 折叠后阅读率断崖）",
        ))
    elif chars > 300:
        results.append(CheckResult(
            "len:warn",
            Severity.WARN,
            f"{chars} 字（>300 需要主编特批 -3）",
        ))

    formal = [w for w in MOMENTS_PUBLIC_OPENING if w in body]
    if formal:
        results.append(CheckResult(
            "authenticity:formal-opening",
            Severity.FAIL,
            f"公开演讲腔 {formal}（§3.1 真实感红线）",
        ))

    # Jargon density (v1.1 §3.3)
    jargon_hits = []
    for t in MOMENTS_JARGON:
        for m in re.finditer(rf"\b{re.escape(t)}\b", body, re.IGNORECASE):
            jargon_hits.append(t)
    jargon_chars = sum(len(t) for t in jargon_hits)
    density = jargon_chars / max(chars, 1)
    unique = list(dict.fromkeys(jargon_hits))
    if density > 0.40:
        results.append(CheckResult(
            "relationship:jargon-fatal",
            Severity.FAIL,
            f"黑话密度 ~{density*100:.0f}%（v1.1 §3.3 >40% 分数上限 6）",
            detail=unique,
        ))
    elif density > 0.15:
        results.append(CheckResult(
            "relationship:jargon-mid",
            Severity.WARN,
            f"黑话密度 ~{density*100:.0f}%（v1.1 §3.3 15-40% -7）",
            detail=unique,
        ))
    elif jargon_hits:
        results.append(CheckResult(
            "relationship:jargon-low",
            Severity.WARN,
            f"轻量黑话 {len(jargon_hits)} 个 (-3)",
            detail=unique,
        ))

    return results


# ---------- Dispatch ----------

PLATFORM_CHECKS = {
    "x-cn": check_x_cn,
    "xiaohongshu": check_xiaohongshu,
    "moments": check_moments,
}


def eval_post(post: PostBlock) -> list[CheckResult]:
    results = check_required_fields(post) + check_ai_red_flags(post)
    if post.platform in PLATFORM_CHECKS:
        results += PLATFORM_CHECKS[post.platform](post)
    return results


# ---------- Reporting ----------

def use_color() -> bool:
    return sys.stdout.isatty()


def colorize(text: str, color: str) -> str:
    if not use_color():
        return text
    codes = {"green": "32", "yellow": "33", "red": "31", "cyan": "36", "bold": "1"}
    return f"\033[{codes[color]}m{text}\033[0m"


def severity_label(s: Severity) -> str:
    if s == Severity.PASS:
        return colorize("PASS", "green")
    if s == Severity.WARN:
        return colorize("WARN", "yellow")
    return colorize("FAIL", "red")


def render_text(reports) -> str:
    out = []
    gp = gw = gf = 0
    for path, blocks in reports:
        out.append(colorize(str(path), "cyan"))
        if not blocks:
            out.append("  (no post blocks found)")
            out.append("")
            continue
        for post, results in blocks:
            out.append(f"  {colorize(post.id, 'bold')} [{post.platform}] {post.title}")
            c = {"PASS": 0, "WARN": 0, "FAIL": 0}
            for r in results:
                c[r.severity.value] += 1
                if r.severity == Severity.PASS:
                    continue
                out.append(f"    {severity_label(r.severity)}  {r.name}")
                if r.message:
                    out.append(f"        {r.message}")
                for d in r.detail:
                    out.append(f"        · {d}")
            out.append(f"    Summary: {c['PASS']} PASS / {c['WARN']} WARN / {c['FAIL']} FAIL")
            gp += c["PASS"]
            gw += c["WARN"]
            gf += c["FAIL"]
            out.append("")
    out.append("=" * 60)
    out.append(f"TOTAL: {gp} PASS / {gw} WARN / {gf} FAIL")
    return "\n".join(out)


def render_json(reports) -> str:
    data = []
    for path, blocks in reports:
        for post, results in blocks:
            data.append({
                "file": str(path),
                "post_id": post.id,
                "platform": post.platform,
                "title": post.title,
                "results": [
                    {
                        "name": r.name,
                        "severity": r.severity.value,
                        "message": r.message,
                        "detail": r.detail,
                    }
                    for r in results
                ],
            })
    return json.dumps(data, ensure_ascii=False, indent=2)


# ---------- CLI ----------

SKIP_FILES = {"README.md", "long-form-assessment.md"}
SKIP_STATES = {"published", "rejected", "已发布", "已拒绝"}

HELP_TEXT = """\
posts-eval — Static checker for posts/ drafts against contracts/posts/v1.1

Usage:
    python tools/posts-eval.py [options] <file-or-dir> ...

Options:
    --json      Output JSON (for agent ingestion)
    --all       Include posts with 状态: published/rejected (skipped by default)
    -h, --help  Show this help message

Exit codes:
    0  No FAIL checks
    1  At least one FAIL
    2  Usage error

Examples:
    python tools/posts-eval.py posts/x.md
    python tools/posts-eval.py posts/
    python tools/posts-eval.py --json --all posts/
"""


def main():
    args = sys.argv[1:]

    # Handle help
    if "-h" in args or "--help" in args:
        print(HELP_TEXT)
        sys.exit(0)

    json_mode = "--json" in args
    include_all = "--all" in args
    args = [a for a in args if not a.startswith("-")]
    if not args:
        print("usage: posts-eval.py [--json] [--all] <file-or-dir> ...", file=sys.stderr)
        print("       posts-eval.py -h  for help", file=sys.stderr)
        sys.exit(2)

    paths: list[Path] = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.md")))
        elif p.exists():
            paths.append(p)
        else:
            print(f"not found: {a}", file=sys.stderr)

    reports = []
    has_fail = False
    for path in paths:
        if path.name in SKIP_FILES:
            continue
        try:
            blocks = parse_posts_file(path)
        except Exception as e:
            print(f"parse error: {path}: {e}", file=sys.stderr)
            continue
        if not blocks:
            continue
        per_block = []
        for post in blocks:
            # Skip published/rejected posts unless --all
            if not include_all:
                state = post.metadata.get("状态", "").strip().lower()
                if state in SKIP_STATES or any(s in state for s in SKIP_STATES):
                    continue
            results = eval_post(post)
            if any(r.severity == Severity.FAIL for r in results):
                has_fail = True
            per_block.append((post, results))
        if per_block:  # only add if there are posts to report
            reports.append((path, per_block))

    if json_mode:
        print(render_json(reports))
    else:
        print(render_text(reports))

    sys.exit(1 if has_fail else 0)


if __name__ == "__main__":
    main()
