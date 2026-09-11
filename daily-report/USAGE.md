# Daily Report 使用说明

## 生成日报

- `生成今天的日报`：读取 `/Users/mad/workspace` 下所有 Git 仓库的本地分支，整理当天由 `madma` 提交的内容。
- `生成昨天的日报`：使用昨天的日期。
- `生成 2026-09-10 的日报`：使用明确指定的日期。

生成结果默认只显示在聊天中，不会操作网页。

## 填写网页

明确说 `填写到 reflect.today` 后，Skill 会在 Google Chrome 中新建标签页并打开 `https://www.reflect.today/`，不会复用已有页面。填写完成后会停下等待检查，不会自动保存草稿或发布。

## 数据范围

- 只统计已经提交的 commit。
- 检查所有本地分支，不读取仅存在于远程分支或 tag 的提交。
- 只统计作者名称或邮箱中包含 `madma` 的提交。
- 同时分析 commit message 和实际 diff，并以 diff 为主要事实依据。
