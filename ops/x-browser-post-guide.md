# X Browser Post Guide

通过 bb-browser 自动化发推。Human review 后，用此命令替代手动 copy-paste。

## 前提条件

1. Chromium 已启动并监听调试端口：
   ```bash
   ss -tlnp | grep 19825
   ```
   如果没有输出，先启动：
   ```bash
   bb-browser daemon
   sleep 2
   bb-browser daemon status
   ```

2. 确认已登录 x.com：
   ```bash
   bb-browser eval "document.cookie" --json | grep -E "twid|ct0"
   ```
   应返回 `twid` 和 `ct0` cookie。

## 步骤 1：提取当前 queryId 和 feature flags

X 会定期轮换 queryId 和 feature flags，发推前必须重新提取。

### 提取 queryId

```bash
bb-browser eval '
(async () => {
  const resp = await fetch("https://abs.twimg.com/responsive-web/client-web/main.ede5acfa.js");
  const text = await resp.text();
  const idx = text.indexOf("CreateTweet");
  if (idx < 0) return "CreateTweet not found";
  return text.substring(Math.max(0, idx - 200), idx + 200);
})()
' --json
```

在输出中搜索 `queryId: \"...\""`，复制 queryId 值（格式如 `H-t2v_HvFR07ZBP9aOeKoA`）。

### 提取 featureSwitches

```bash
bb-browser eval '
(async () => {
  const resp = await fetch("https://abs.twimg.com/responsive-web/client-web/main.ede5acfa.js");
  const text = await resp.text();
  const idx = text.indexOf("H-t2v_HvFR07ZBP9aOeKoA");
  if (idx < 0) return "queryId not found";
  const after = text.substring(idx, idx + 5000);
  const fsMatch = after.match(/featureSwitches:\[([^\]]+)\]/);
  if (!fsMatch) return "featureSwitches not found";
  const switches = fsMatch[1].split(",").map(s => s.replace(/"/g, "").trim());
  return JSON.stringify({featureSwitches: switches});
})()
' --json
```

### 提取 fieldToggles

```bash
bb-browser eval '
(async () => {
  const resp = await fetch("https://abs.twimg.com/responsive-web/client-web/main.ede5acfa.js");
  const text = await resp.text();
  const idx = text.indexOf("H-t2v_HvFR07ZBP9aOeKoA");
  if (idx < 0) return "queryId not found";
  const after = text.substring(idx, idx + 8000);
  const fieldMatch = after.match(/fieldToggles:\[([^\]]+)\]/);
  if (fieldMatch) {
    const toggles = fieldMatch[1].split(",").map(s => s.replace(/"/g, "").trim());
    return JSON.stringify({fieldToggles: toggles});
  }
  return "fieldToggles not found";
})()
' --json
```

## 步骤 2：发推

将下方命令中的三个占位符替换后执行：

- `YOUR_QUERY_ID` — 步骤1提取的 queryId
- `YOUR_FEATURES_JSON` — 步骤1的 featureSwitches（转成 JSON object，全部设为 true，忽略已知的 read-only 标志）
- `YOUR_FIELDTOGGLES_JSON` — 步骤1的 fieldToggles（转成 JSON object，全部设为 true）
- `YOUR_TWEET_TEXT` — 要发布的文本（注意：中文直接写即可，不需要转义）

```bash
bb-browser eval '
(async () => {
  const ct0 = document.cookie.split(";").map(c=>c.trim()).find(c=>c.startsWith("ct0="))?.split("=")[1];
  const bearer = decodeURIComponent("AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA");
  const _h = {
    "Authorization": "Bearer " + bearer,
    "X-Csrf-Token": ct0,
    "X-Twitter-Auth-Type": "OAuth2Session",
    "X-Twitter-Active-User": "yes",
    "Content-Type": "application/json"
  };
  const queryId = "YOUR_QUERY_ID";
  const features = YOUR_FEATURES_JSON;
  const fieldToggles = YOUR_FIELDTOGGLES_JSON;
  const variables = {
    tweet_text: "YOUR_TWEET_TEXT",
    media: { media_entities: [], possibly_sensitive: false },
    semantic_annotation_ids: [],
    dark_request: false
  };
  const url = "/i/api/graphql/" + queryId + "/CreateTweet" +
    "?variables=" + encodeURIComponent(JSON.stringify(variables)) +
    "&features=" + encodeURIComponent(JSON.stringify(features)) +
    "&fieldToggles=" + encodeURIComponent(JSON.stringify(fieldToggles));
  try {
    const resp = await fetch(url, {
      method: "POST",
      headers: _h,
      credentials: "include"
    });
    const data = await resp.json();
    return JSON.stringify({status: resp.status, rest_id: data?.data?.create_tweet?.tweet_results?.result?.rest_id, text: data?.data?.create_tweet?.tweet_results?.result?.legacy?.full_text}, null, 2);
  } catch(e) {
    return JSON.stringify({error: e.message});
  }
})()
' --json
```

**成功响应**：`rest_id` 即为新发推文的 ID，拼接到 `https://x.com/{username}/status/{rest_id}` 查看。

## 故障排除

| 症状 | 解决方法 |
|------|---------|
| 404 `Query not found` | queryId 已轮换，重新提取 |
| 403 / auth errors | ct0 过期，重新登录 x.com |
| 200 但 tweet_results 为空 | features/fieldToggles 与 queryId 不匹配，重新提取 |
| `Cannot connect to Chrome CDP` | Chromium 未启动，先运行 `bb-browser daemon` |

## 限制

- 不支持图片/视频上传（仅文本）
- queryId 和 feature flags 会定期轮换，需定期重新提取
- 建议配合 xurl CLI 使用（更稳定），本指南仅作为补充