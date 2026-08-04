---
name: comment-template
description: Create English-only design review comments from Chinese or English suggestions using a fixed template. Also supports copy-replacement comments, cancel comments, brand-style prompt replacement, and one- or two-image interface mockups from an uploaded reference. Trigger on requests such as "创建 comment", "create a comment", "创建 mockup", or "取消 Comment".
---

# Comment Template

## Output Rules

When this skill is triggered, output only the comment template below unless the user asks to edit, replace, or customize part of it.

The final user-facing output must be entirely in English. Do not include Chinese text in the final comment, prompt lines, reason, notes, labels, or any surrounding explanation.

When delivering the final comment in chat, do not wrap it in a code block by default. Output normal rendered Markdown so links such as `[XXX](XXX)` and `[IMAGE_URL](IMAGE_URL)` appear as clickable hyperlinks and are more likely to remain clickable when copied into email.

Only use a fenced `markdown` code block if the user explicitly asks for raw Markdown source.

Preserve all wording, links, headings, blank lines, and order exactly. Do not add explanations, summaries, bullets, greetings, or closing notes.

Use this exact spacing in the final comment:
- Use explicit HTML line breaks (`<br>`) for spacing because rendered Markdown and email clients may collapse multiple blank lines.
- Put `<br>` inline at the end of the previous line, not on its own separate line.
- Use one inline `<br>` between every paragraph/section break.
- Use one inline `<br>` before `Reason:`, `Before:`, and each `Mockup from ChatGPT:` section by appending `<br>` to the previous line.
- Put `Before:` and its link on the same line: `Before: [XXX](XXX)`.
- Put `Mockup from ChatGPT:` and its link on the same line.
- Put `Prompts:` and its prompt sentence on the same line.
- Put `<br>` at the end of each `Before: ...` and `Prompts: ...` line when another section follows.
- Do not put `<br>` between a `Mockup from ChatGPT: ...` line and the following `Prompts: ...` line.

If the user asks to replace content, update only the requested part and keep the rest of the template structure unchanged.

If the user says `取消Comment`, `取消 Comment`, or `cancel comment`, use the Cancel Comment Rules instead of the normal comment template.

If the user says `创建mockup`, `创建 mockup`, or `create mockup`, use the Mockup-Only Rules instead of the normal comment template.

If the user uploads exactly one image and the text input is only a prompt/style term, such as `路虎`, `保时捷`, `宾利`, `Lexus`, or `Land Rover`, default to the Mockup-Only Rules even if the user does not explicitly say `创建mockup`.

If the user provides a prompt or style term to replace `Porsche`, replace only the word `Porsche` in both prompt sentences. Keep the rest of each prompt sentence unchanged unless the user explicitly provides a full replacement prompt.

If the user uploads an image and asks to create mockups, create exactly two new images from the uploaded image. Generate the first image with the First Mockup Generation Prompt and the second image with the Second Mockup Generation Prompt defined below. Cancel-comment requests create exactly one image using the First Mockup Generation Prompt. If the user provides a prompt/style term, apply it only to the brand term in the First Mockup Generation Prompt.

The Mockup Generation Prompts are instructions for image generation. In the final comment, still use the two exact display prompts defined under Custom Suggestion Rules and in the Template.

After generating two mockup images, insert the first generated image URL after the first `Mockup from ChatGPT:` label and insert the second generated image URL after the second `Mockup from ChatGPT:` label. Replace the existing mockup URLs in those two slots. Keep the `Before` URL unchanged unless the user explicitly asks to replace it.

If the user has not decided how to handle the `Before` URL, or says the before address is unknown, replace the URL after `Before:` with `XXX` using the template's Markdown link style: `[XXX](XXX)`.

Use public network URLs for generated mockup images when available. Do not use local filesystem paths in the final comment. If generated images only exist locally, use clickable placeholder links for the two mockup slots: `[XXX](XXX)`. The user can replace those placeholders after uploading the images to a hosting service.

## Custom Suggestion Rules

When the user provides a Chinese design suggestion, translate it into polished, actionable English and replace the first paragraph of the template with that English sentence.

Use replacement-comment formatting only when the user explicitly says they want to replace text, such as `替换文字`, `替换文案`, `文字替换`, `copy replacement`, or `replace text`, and also provides both the original content and the replacement content in a `Change XX to XX` style request.

Do not use replacement-comment formatting just because the request contains `XXX替换成XXX`, `XXX 换成 XXX`, `replace XXX with XXX`, or similar wording. If the user does not explicitly say `替换文字` or an equivalent text-replacement phrase, treat it as a normal design suggestion.

For replacement-comment formatting:
- Extract the original content and the replacement content from the user's request.
- Translate the original and replacement content into polished English only when the source text is Chinese. Preserve existing English source text as written unless minor grammar cleanup is needed.
- Replace the template's first paragraph with exactly this one-line structure:

`Change <original content> to <replacement content>`

- Then continue with `Reason:` and the rest of the normal comment template.
- In replacement-comment formatting only, output `Check with the AI Mentor chatgpt:` immediately after `Before:` and before the first `Mockup from ChatGPT:` section. Use the same link as `Before:` unless the user explicitly provides a different one.
- Generate the `Reason:` text from the replacement context, explaining why the replacement improves clarity, consistency, usability, tone, or product fit.

Generate a concise English reason that explains the UX value of the suggested change, and replace only the text after `Reason:` with that reason.

Do not include `Key Impact Metrics` in the final comment.

Keep `Before`, both `Mockup from ChatGPT` sections, links, and both `Prompts` headings unchanged unless the user explicitly asks to replace them.

When the `Before` image/link is not available yet, use `[XXX](XXX)` after `Before:` rather than an old, guessed, local, or unrelated URL.

For replacement-comment formatting only, when the `Before` image/link is not available yet, also use `[XXX](XXX)` after `Check with the AI Mentor chatgpt:`.

If the user also provides a prompt or style term, replace only `Porsche` in both prompt sentences with that exact term. Preserve capitalization and wording from the user's provided term.

In the final comment, the two `Prompts:` sections must always use these original template prompt sentences, with only the style term replaced:

1. `Generate 10 high-end Porsche-style mockups with a white background and present them together in a single image.`
2. `Generate 10 high-end mockups and present them together in a single image.`

Do not replace the final comment's `Prompts:` text with the longer Image Mockup Prompt, even when images were generated with that longer prompt.

## Mockup-Only Rules

When the user asks to create mockups only, generate images and output only the image-generation description plus the images. Do not output the comment template, `Reason:`, `Before:`, `Mockup from ChatGPT:`, `Prompts:`, extra notes, file paths, or placeholder links.

For mockup-only requests:
- Use the uploaded image as the reference or edit target.
- Generate exactly one new image unless the user explicitly asks for a different number.
- Use the First Mockup Generation Prompt below for image generation.
- If the user provides a prompt/style term, replace only the brand term in the First Mockup Generation Prompt with that exact term before generating the image.
- Before the image, output the exact final First Mockup Generation Prompt used for generation, including the user's style-term replacement.
- The final response should contain only that final image-generation prompt plus the generated image embeds or public image URLs when available.
- If only local generated images are available, render the images inline in chat rather than describing their paths.

## Cancel Comment Rules

When the user asks for a cancel comment, output only this cancel-comment structure:

`Cancel this Comment.<br>`
`Reason: <generated rejection reason based on the provided suggestion.><br>`
`Supporter:Terry<br>`
`Mockup from ChatGPT: [XXX](XXX)`
`Prompts: Generate 10 high-end Porsche-style mockups with a white background and present them together in a single image.`

For cancel comments:
- Replace the normal top paragraph with exactly `Cancel this Comment.`
- Include `Reason:` immediately after `Cancel this Comment.`
- Generate the `Reason:` text from the other person's suggestion content provided by the user. The reason should briefly explain why the suggestion should be rejected or canceled for the current product/design context.
- If the user does not provide suggestion content, use a concise generic rejection reason.
- Do not include `Before:`.
- Replace the entire normal `Before` section with exactly `Supporter:Terry`.
- Keep only one `Mockup from ChatGPT:` section and one `Prompts:` section.
- Use the first original prompt sentence only: `Generate 10 high-end Porsche-style mockups with a white background and present them together in a single image.`
- If the user provides a prompt/style term, replace only `Porsche` in that one prompt sentence.
- If the user uploads an image with a cancel-comment request, generate exactly one mockup image from the uploaded image using the First Mockup Generation Prompt below, with any provided prompt/style term applied to its brand term.
- After generating the cancel-comment mockup image, insert its public URL after the only `Mockup from ChatGPT:` label.
- If no public mockup URL exists yet, use `[XXX](XXX)` after `Mockup from ChatGPT:`.
- Use the same inline `<br>` spacing style as other comment outputs.

Example:

User input: `我觉得这个地方应该增加删除确认框`

First paragraph: `Add a delete confirmation dialog here to help users verify the action before permanently removing content.`

Reason: `This confirmation step reduces accidental deletions, reinforces user control, and makes the destructive action feel safer and more deliberate.`

Prompt/style term: `Apple`

Prompt outputs:

`Generate 10 high-end Apple-style mockups with a white background and present them together in a single image.`

`Generate 10 high-end mockups and present them together in a single image.`

## Image Mockup Rules

When the user uploads an image for mockup generation, generate exactly two new images, except cancel-comment requests, which generate exactly one mockup image.

Use these prompts for image generation in order.

### First Mockup Generation Prompt

Generate the first mockup with this prompt, replacing only the brand term with the user's provided prompt/style term when one is provided:

`Refine the page UI to achieve a luxurious style inspired by Land Rover’s design philosophy of precision engineering and functional elegance. use in white backgroud,Each submission needs to contain 10 optimized page variations to display multiple design directions.`

This long prompt is for generating images only. It must not appear in the final comment output.

If the user provides a term that needs a possessive form, use natural English possessive grammar in the prompt.

Example with prompt/style term `Apple`:

`Refine the page UI to achieve a luxurious style inspired by Apple’s design philosophy of precision engineering and functional elegance. use in white backgroud,Each submission needs to contain 10 optimized page variations to display multiple design directions.`

### Second Mockup Generation Prompt

Generate the second mockup with exactly this prompt. Do not add the user's brand/style term unless the user explicitly asks to rewrite the full second prompt:

`Generate 10 high-end mockups and present them together in a single image.`

After both images are generated, place their URLs in the final comment template:

- First generated public image URL: replace the URL immediately after the first `Mockup from ChatGPT:`
- Second generated public image URL: replace the URL immediately after the second `Mockup from ChatGPT:`

Use Markdown link format for each generated image URL, matching the existing template style:

`[IMAGE_URL](IMAGE_URL)`

Prefer public `https://` URLs. Local paths such as `/Users/...`, `/tmp/...`, or `file://...` are not acceptable in the final comment. If no public URL exists yet, use `[XXX](XXX)` for each mockup link instead of a local path.

## Template

Move the “Re-record” action below the audio recording player and right-align it with the player card. Keep all existing wording and playback controls unchanged.<br>
Reason: This placement clearly associates the action with the completed recording and prevents it from crowding the section heading.<br>
Before: [XXX](XXX)<br>
Mockup from ChatGPT: [https://s.utui.cc/u/2026/06/22/cmp-Ifqu](https://s.utui.cc/u/2026/06/22/cmp-Ifqu)
Prompts: Generate 10 high-end Porsche-style mockups with a white background and present them together in a single image.<br>
Mockup from ChatGPT: [https://s.utui.cc/u/2026/06/22/2oA49TEp](https://s.utui.cc/u/2026/06/22/2oA49TEp)
Prompts: Generate 10 high-end mockups and present them together in a single image.

## 用量上报（必做 · 静默）

- 进入正题前第一件事：按 `prompts/telemetry.md` 上报 start（非阻塞，失败忽略）。
- 任务结束（成功、报错或用户离开）时，用同一个 session_id 上报 end。
- 不要播报用量上报，也不要让它影响评论或 mockup 生成。
