---
title: Files, images, and context
description: Attach files, editor selections, and images while controlling what accompanies your next message.
---

# Files, images, and context

A focused prompt works best with the code or image needed to answer it. iolys supports explicit attachments and tools that inspect the open solution. These serve different purposes: an attachment tells the agent what you want it to consider, while a tool lets it investigate further within its permissions.

## Attach an editor selection

1. Select code in a Visual Studio editor.
2. In Chat, open **+ > Selection**.
3. Check the context chip above the input, then write your request.

The attachment captures the selected text, including unsaved edits, with its file and line range. It is a snapshot taken when you add it. Later editor changes do not update that snapshot; remove and add it again to capture a newer selection.

You can also right-click in the editor and choose **iolys actions > Add Selection to Chat**. This adds context without sending a message or replacing your draft.

```text
Explain why this method can return an empty result even when the service
returns records. Trace the relevant callers before proposing a fix.
```

## Reference a file

Use **+ > Active document** or **iolys actions > Add Active File to Chat** to identify the current file. An active-document attachment supplies its absolute path and display name, rather than copying the full editor buffer. The agent can inspect the file with its available tools. Use **Selection** when the exact unsaved text matters.

Other ways to supply files include:

- **+ > Add file...** in the composer.
- Typing **#** to open file search and select relevant context.
- Selecting files in Solution Explorer and choosing **Add to iolys Context**.
- Dropping files onto Chat.

For a multi-file task, start with the entry point and the relevant tests. Let the agent locate additional dependencies instead of attaching an entire repository.

## Add an image

Paste or attach an image when you want to discuss a screenshot, UI layout, or diagram. Select a model with image support; the model picker uses a **Vision** indicator where that capability is available.

```text
Compare this screenshot with the current settings page. Identify the layout
differences, then propose the smallest changes needed to match it.
```

The `read_image` tool can also inspect supported local image files when exposed by the provider. Image capability and available image tools vary by model and connection route. If an attachment is rejected, check the selected model and the [provider guide](../providers/index.md).

## Control what is sent

Explicit IDE context is never attached automatically. The chips make the pending selection or active-document references visible; remove a chip before sending to exclude that item from the next prompt. Those attachments are sent once with the next admitted or queued message and remain attached when a queued message is edited, retried, reordered, or steered.

Removing a chip does not revoke the agent's ability to read the same file through a tool. Manage that access with [permissions](../customization/permissions.md) and [tool selection](../customization/tools.md).

Selection snapshots are supplied to the model as untrusted reference material, separate from your request. If a file contains instructions meant for another system, state the task you actually want performed in your message.

## Inspect context consumption

Select **Context window usage** beside the composer to see the available breakdown of messages, file context, tools, and instructions. Context usage differs from account quota and cost; see [Usage and session statistics](usage.md).
