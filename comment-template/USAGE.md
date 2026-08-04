# Comment Template 使用说明

## 什么时候使用

当你需要把中文或英文的设计建议整理成格式统一、可以直接复制到邮件或评审系统的英文评论时使用。它也适合制作文字替换评论、取消某条评论，以及根据界面截图生成指定品牌风格的 mockup。

## 怎么使用

- 说“帮我创建一个 comment：删除按钮前应该增加确认弹窗”，会得到完整的英文评审评论和对应 Reason。
- 说“替换文字：Change 免费试用 to 开始体验”，会生成文案替换格式，并保留模板中的链接和 prompt 区域。
- 上传一张界面截图并说“创建 mockup，Apple”，会按 Apple 风格生成新的界面 mockup。
- 说“取消 Comment：这个改动会降低主要操作的可见性”，会得到取消评论结构和简洁的拒绝理由。

## 要准备什么

普通评论不需要额外配置。生成 mockup 时需要先上传一张清晰的界面截图；如需特定风格，同时提供品牌或风格名称。若没有 Before 或 mockup 的公共链接，输出会保留可替换的链接占位。

## 输出什么

普通模式输出固定结构的英文设计评论，包括建议、Reason、Before、两组 mockup 链接和 prompts。Mockup-only 模式输出实际使用的图像生成描述与生成图片；取消评论模式输出一条精简的英文取消评论。

## 使用注意事项

The generated review comment is designed for direct use in email and design-review tools. Check the Before link before sending, replace placeholder links when no public image URL is available, and provide a clear screenshot when requesting mockups. The skill keeps the original interface color tone unless the request explicitly asks for a visual change. For reliable results, state whether the task is a normal suggestion, a copy replacement, a mockup-only request, or a cancellation. When naming a brand style, use the exact spelling that should appear in the final English prompts.
