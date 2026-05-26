# Social Post Checklist

`posts/` 下每条 draft 在发布前后都过这一个清单。**不为每个平台单独开一份**。

## 发布前检查

- [ ] 第一行是否有明确观点？
- [ ] 是否只讲一个核心想法？
- [ ] 是否不像公众号摘录？
- [ ] 是否有具体场景、例子或判断？
- [ ] 是否有一个可回复的问题？
- [ ] 是否已经找过近似产品、近似实现或相似内容？
- [ ] 是否适合当前平台？（平台职责见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）
- [ ] **是否已运行 humanizer 去除 AI 味？**（中文 `humanizer-zh`，英文 `humanizer`；各 agent 工具的调用方式见 [`skills/humanizer-usage.md`](../skills/humanizer-usage.md)。若跳过须在 post block 注明原因）
- [ ] 是否值得现在发，而不是继续打磨？

## 发布后记录

回填到对应 post block 的"发布后反馈"区：

- [ ] 发布时间
- [ ] 链接
- [ ] 主要反馈
- [ ] 高质量回复
- [ ] 是否值得升级成长文（升级标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）
