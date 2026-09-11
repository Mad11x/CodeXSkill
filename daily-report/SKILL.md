---
name: daily-report
description: Prepare structured daily journal content for the Reflect form at reflect.today. Use when the user wants to collect, draft, refine, or fill a daily report, work journal, daily reflection, or any of the numbered Reflect form sections.
---

# Daily Report

Help the user prepare content for the Reflect daily journal form.

Before drafting or filling any section, read [references/reflect-form.md](references/reflect-form.md). It records the current fields, limits, required states, and conditional sections observed in the form.

## Generate a Report

1. Resolve the report date from the user's request. Use today in the local timezone when no date is given.
2. Run `scripts/collect_commits.py --date YYYY-MM-DD` to discover every Git repository under `/Users/mad/workspace` and collect `madma` commits reachable from all local branches. The output includes commit metadata, stats, and patches.
3. Read every returned commit message and diff. Use the diff as the source of truth and keep repository identities distinct.
4. Draft only the enabled sections and conditional sections defined in the reference. Respect every character limit.
5. If no matching commits exist, say so and ask whether to use another date or source. Do not invent work.
6. When a Friday or Saturday mistake section is required but the week's commits do not support a concrete mistake, ask the user for one. Do not invent a mistake or say that no mistake occurred.
7. Browse for current internet-industry information when generating section 10, prioritizing recent primary sources. Keep source links available when returning the report in chat.

Use Chinese for generated journal prose while preserving professional and code identifiers in their original form.

## Live Form

Default to generating the report in chat only. Interact with `reflect.today` and fill the live form only when the user explicitly instructs the skill to do so. A request to generate, preview, revise, or review a report does not authorize live form interaction.

When live filling is authorized, always create a new Google Chrome tab and navigate it directly to `https://www.reflect.today/`. Do not claim, reuse, or modify an existing Reflect tab. Use the new tab for the full filling workflow.

After filling the live form, stop and let the user inspect it. Do not save a draft or publish the journal unless the user explicitly gives that separate instruction.
