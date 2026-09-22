# Reflect Daily Journal Form

This reference records the form visible at `reflect.today` on September 11, 2026. Treat it as the current observed structure; verify the live form if the interface changes.

## Form Actions and Notices

- Date shown in the journal dialog.
- `发布日记` publishes the journal.
- `保存为草稿（随时编写）` saves work in progress.
- `AI Generate` generates content in the site.
- A notice may report monthly questions due on the 15th.
- Daily Report behavior: ignore monthly questions entirely. Do not inspect, generate, fill, or remind the user about them.
- Default behavior is to generate the report in chat without interacting with the live form.
- Fill fields on `reflect.today` only when the user explicitly instructs the skill to fill the webpage.
- When filling is requested, open a new Google Chrome tab at `https://www.reflect.today/`. Never reuse or take over an existing Reflect tab.
- After filling, stop for user inspection. Do not click `保存为草稿（随时编写）` or `发布日记` without a separate explicit instruction.

## Quick Notes

- Label: `Quick notes (Optional)`
- Purpose: capture ideas, tasks, highlights, or anything worth remembering throughout the day.
- Visibility: the team can see these notes.
- Limit: 500 characters.
- Daily Report behavior: skip this field by default. Do not generate or fill it unless the user explicitly asks.

## 1. 工作总结（试试语音）

- Required.
- Limit: 9,999 characters.
- Supports marking selected text as important and restoring the default text color.
- Prompts the user to cover results, unfinished work, initiative, work beyond expectations, feedback to colleagues, evidence behind conclusions, and useful meeting notes or summaries.
- Follow-up choice: `你今天的待办事项都完成了吗？` — `是` / `否`.
- Follow-up choice: `Do you have any tasks unfinished for over a week?` — `Yes` / `No`.

### Confirmed generation rules

- Use the user's Git commit history as the source material for the work summary.
- If the user specifies a date, collect commits for that date.
- If the user does not specify a date, default to the current date in the user's local timezone.
- Search recursively under `/Users/mad/workspace` and collect commits from every Git repository found there.
- Skip folders that are not Git repositories.
- Group or retain repository identity while collecting commits so work from different projects is not confused.
- Search commits reachable from every local branch under `refs/heads/*`, not only the currently checked-out branch.
- Do not include commits that exist only on remote-tracking branches or tags. Count a commit only once when it is reachable from multiple local branches.
- Include only commits whose Git author name or author email contains `madma`, matched case-insensitively.
- Include only committed work. Exclude unstaged changes, staged-but-uncommitted changes, and untracked files.
- Inspect both each commit message and its actual diff when preparing the summary. Treat the commit message as context, not as a complete or necessarily accurate description.
- Use the committed diff as the primary source of truth when the message and implementation differ. Do not claim outcomes that cannot be supported by the committed changes.
- Format the work summary as copyable plain-text numbered paragraphs using `1、`, `2、`, and so on. Never use Markdown ordered-list syntax such as `1. item`.
- Write one numbered list item per commit. Do not merge multiple commits into one item, even when they concern the same feature.
- Write the summary in Chinese.
- Preserve professional names in their original form, including technical terms, product names, framework names, component names, class and method names, APIs, and other established identifiers. Do not translate them mechanically into Chinese.
- Each numbered item must explain what was completed, the key implementation changes, and the resulting effect or value.
- Only state effects or value that the commit supports directly or that can be derived reasonably from the code change; do not invent business impact.
- Default `你今天的待办事项都完成了吗？` to `是`. Use `否` only when the user explicitly says the day's tasks were not all completed.
- Default `Do you have any tasks unfinished for over a week?` to `No`. Use `Yes` only when the user explicitly says such an overdue task exists.
- When generating or previewing the report in chat, omit both status questions and their answers entirely.
- Apply these default answers only when filling the corresponding controls on the live `reflect.today` form, unless the user explicitly overrides them.

## 2. 我学会了如何在未来取胜：人工智能工具的使用、提示词优化和有效AI资源的分享（成为你自己的宝贵智慧）

- Required.
- Limit: 999 characters.
- The input guidance says: `经常反思或更新自己工具和方法的人，进步速度会快很多倍。` and `始终思考如何更快、更聪明、更好地完成工作。`
- Generate a reflection that identifies a concrete tool, method, prompt approach, or reusable resource learned or improved that day, then explain how it can make future work faster, smarter, or better.
- Do not merely repeat the day's completed features or describe the daily-report generation process.
- Ground the reflection in the selected day's committed work. Prefer one coherent, reusable lesson over a list of unrelated observations.
- When supported by the commits, explain how the method helps expose edge cases, reduce omissions or rework, and improve delivery speed or accuracy.
- Write in Chinese while preserving professional names in their original form.

## 3. 工作中或行业内出现的奇怪、不明确、荒谬、最令人困扰或自上个月以来发生奇怪变化的事情？或者我今天无法解决的问题？

- Required.
- Limit: 999 characters.
- Encourages questions that need team help, challenges to processes or tasks, product invention ideas, manual work that could be automated, deeper thought about current work, and meaningful changes in the industry.

### Confirmed generation rules

- Generate this section automatically from the selected day's committed work; do not require the user to provide a separate topic.
- Inspect the implementation for unresolved product questions, technical risks, unclear requirements, workflow weaknesses, automation opportunities, or behavior that still needs validation.
- Generate exactly two concise angles by default:
  1. One concrete technical or code-level question exposed by the implementation.
  2. One broader non-code question about the product, users, workflow, business, or industry derived from the day's work.
- Keep each angle focused on one issue rather than listing many questions.
- Format the two angles as copyable plain-text numbered paragraphs using `1、` and `2、`, but do not add labels such as `代码层面`, `代码之外`, `技术问题`, or `产品思考`.
- Prefer a concrete question that the day's work genuinely exposes and that would benefit from further thought or team input.
- Questions do not need to describe urgent or high-priority problems. Prefer useful, lightweight observations when the implementation exposes duplicated rules, scattered checks, inconsistent behavior, recurring edge cases, small maintenance risks, or modest automation opportunities.
- Keep the proposed response proportional to the issue. Do not automatically turn a minor observation into a ticket, owner, deadline, escalation, or team-wide process.
- Do not present an issue already resolved by the commit as if it were still unresolved. When a completed fix reveals a broader concern, state that the immediate issue was fixed and ask about the remaining pattern, such as whether repeated visibility checks should gradually be centralized.
- Write in Chinese while preserving professional names in their original form.

## 4. 我或团队今天或过去几天犯下的小错误或失误

- Conditional for the Daily Report workflow even though the observed form displayed a required marker.
- Intended for discovering small problems and continuous improvement, not as a formal error log.
- Each mistake requires a category selected through `Select a category` before text can be entered.
- Default category: `I found my mistake by myself:`.
- Limit: 999 characters per observed mistake entry.
- Supports `Add another mistake` for multiple entries.
- If a leader has already discussed the issue, the form suggests the pattern `我的协调员在公开场合批评了我：...`.
- The input guidance says, in substance:
  - Not admitting a mistake is a bigger mistake.
  - If you never make mistakes, it means you have done nothing.
  - Recording mistakes promptly supports growth; rarely doing so is itself a problem.
  - The more mistakes recorded here, the better AI can help prevent them from recurring.
  - Explain why a task was not completed within the week when applicable.

### Confirmed constraints

- When generating or previewing a report in chat, output this section only when the selected report date is Friday or Saturday, or when the user explicitly requests it. On other days, omit it from chat output.
- When filling the live `reflect.today` form, inspect the form itself. If section 4 is displayed as required, it must be completed regardless of the generated content date: select `I found my mistake by myself:` and enter one concrete, evidence-based mistake. Never leave a displayed required mistake category or text blank.
- Search for a suitable mistake across the current calendar week, from Monday through the selected report date. Do not limit the search to the report date and do not inspect later dates in the same week.
- Use the same repository, local-branch, committed-work, and `madma` author filters defined for the work summary.
- Commit messages that contain only task names follow the user's company convention. Never describe that convention as a mistake, weak documentation, or a process problem.
- Do not invent a mistake when neither the commits nor the user provides reliable evidence of one.
- Do not fill this field with a claim that there was no mistake; the field expects a concrete self-identified mistake under the default category.
- If live filling requires this field but the available evidence does not support a concrete mistake, ask the user for one before completing the form instead of silently skipping it.

## 5. 下一个工作日最重要或最困难的任务

- No required marker was visible.
- Limit: 400 characters.
- Covers the highest-priority or hardest next task, why it matters, why the chosen approach is necessary, the next action, and the biggest problem to solve this week.
- Daily Report behavior: skip this field by default. Do not generate or fill it unless the user explicitly requests it.

## 6. 今天我做了哪些对客户或行业有益的事情？

- No required marker was visible.
- Limit: 2,000 characters.
- Focuses on customer satisfaction, contributions beyond normal duties, value created, technical or product-experience improvements, and relevant new-product exploration.

### Confirmed generation rules

- Generate this section automatically from the selected day's commits and actual diffs, using the same repository, local-branch, committed-work, and `madma` author filters as the work summary.
- Write in Chinese as copyable plain-text numbered paragraphs using `1、`, `2、`, and so on, while preserving professional names in their original form.
- Group related commits when they contribute to the same customer or industry benefit; unlike the work summary, this section does not require one item per commit.
- Focus on concrete improvements to customer experience, stability, usability, efficiency, safety, or product value.
- Omit purely internal cleanup that has no meaningful customer or industry benefit.
- Do not claim benefits that the committed changes do not support.

## 7. 本周提出的疑问（优先考虑产品和工作流程问题）

- Required.
- Limit: 400 characters.
- Must include a screenshot of a question posted in a group.
- The URL must come from one of the groups listed by the form: `MPU(如果父母不理解，产品就失败了)保持初心`, `LV UI：对称，用户就是奢侈品`, `质疑一切DLEngineers：讨论与分享`, or `DE4产品/客服/市场`.
- Daily Report behavior: skip this field by default, including its screenshot and URL. Do not generate or fill it unless the user explicitly enables or requests it.

## 8. Weekly Self-Review

- Required on Fridays.
- Answer each item with `Yes` or `No`:
  1. Did the work directly advance the core business or quarterly priorities rather than unrelated busywork?
  2. Was a measurable, concrete result delivered rather than activity alone?
  3. Was a tough or challenging problem addressed proactively?
  4. Was anything blocked by missing decisions, resources, or collaboration?
  5. Was a failed attempt reviewed honestly and the approach adjusted?
  6. Did the user proactively help teammates or improve a process?

### Confirmed answers

- When generating or previewing a report in chat, output this section only when the selected report date is Friday.
- When filling the live `reflect.today` form, inspect the form itself. If section 8 is displayed, it is mandatory: answer all six questions even when the generated content refers to another date or the report-date context is ambiguous. Never leave a displayed Weekly Self-Review partially filled or blank.
- Use these fixed answers unless the user explicitly overrides them:
  1. `Yes`
  2. `Yes`
  3. `Yes`
  4. `No`
  5. `Yes`
  6. `Yes`

## 9. 不可能的挑战

- No required marker or character limit was visible.
- Requests a bold, nearly impossible goal that pushes limits, inspires creativity, and invites unconventional solutions.
- Daily Report behavior: generate and fill this field for every report.
- Generate one ambitious and measurable challenge with explicit constraints and business value. Prefer themes involving AI, product growth, and customer experience rather than an ordinary engineering task.
- An accepted direction is improving SeniorMatch's registration-to-first-meaningful-interaction conversion substantially through AI personalization without increasing advertising or manual operating costs, while preserving authenticity, privacy, and match quality.

## 10. 添加任何你想分享的内容

- No required marker or character limit was visible.
- Examples include reflections about books, gratitude, goals, or actions that build on personal strengths.

### Confirmed generation rules

- Generate this section from recent developments in the internet industry, not from the user's Git history or daily work.
- Browse the web at generation time because industry information changes. Prefer recent primary sources such as official company announcements, engineering blogs, standards, research, or regulatory publications.
- Prefer one concise, useful industry observation, resource, trend, or reflection rather than a news roundup.
- Explain why the development matters to internet products, engineering, users, or industry competition instead of merely repeating the announcement.
- Avoid repeating the work summary, AI-method lesson, unresolved questions, mistake reflection, or customer-benefit section.
- Write in Chinese while preserving professional names in their original form.

## 11. 自我评价徽章

- No required marker was visible.
- Provides several badge choices.
- Supports uploading a custom badge.
- The form encourages informal performance and goal discussions with a supervisor.
- Daily Report behavior: exclude this field from the workflow. Do not output a badge choice or upload a custom badge.

## 12. 上传照片

- No required marker was visible.
- Supports selecting and uploading a photo.
- Daily Report behavior: exclude this field from the workflow. Do not output or upload a photo.
