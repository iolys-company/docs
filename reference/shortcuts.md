---
title: Keyboard and chat commands
description: Confirmed keyboard actions and slash commands in the Visual Studio chat.
---

# Keyboard and chat commands

These actions apply to the **Visual Studio chat**. Focus matters: keys used by a suggestion popup, title editor, or transcript are handled by that control. The companion web interface and Visual Studio's own editor shortcuts can differ.

## Compose a message

| Key | Action |
| --- | --- |
| **Enter** | Send the current draft when sending is available. |
| **Shift + Enter** | Insert a new line in the composer. |
| **Ctrl + V** | Paste clipboard content; a clipboard image is attached when supported. |

When slash suggestions are open, they take precedence over sending:

| Key | Action |
| --- | --- |
| **Up / Down** | Move through suggestions. |
| **Enter / Tab** | Accept the selected suggestion. |
| **Escape** | Dismiss the suggestion list. |

Accepting a suggestion inserts its text; complete and send the message separately. In the file-search popup, **Escape** closes suggestions and returns focus to the input.

## Read a conversation

| Key or gesture | Action |
| --- | --- |
| **Ctrl + mouse wheel** over chat | Adjust chat zoom in 5% steps. |
| **Ctrl + Plus / Minus**, with focus in the transcript | Increase or decrease zoom. |
| **Ctrl + 0**, with focus in the transcript | Reset zoom to 100%. |
| **Escape**, while reading in the document area | Exit reading mode and restore the previous frame mode. |

Zoom is limited to 75–200% and is saved in the local Visual Studio user settings. Enter reading mode with **Read in document area** in the toolbar. The same conversation remains available, including the composer and attachments.

Scrolling away from the bottom pauses automatic following of new content. Scrolling back to the bottom, or sending a message, resumes it.

## Other focused controls

| Control | Key | Action |
| --- | --- | --- |
| Conversation title editor | **Enter** | Confirm the edited title. |
| Conversation title editor | **Escape** | Cancel editing. |
| History sidebar splitter | **Left / Right** | Resize the sidebar. |
| Toolbar tour | **Left / Right** | Move between tour steps. |
| Toolbar tour | **Escape** | Dismiss the tour. |
| MCP Server Manager | **Ctrl + L** | Focus its search input. |

## Useful chat commands

Use the slash suggestions or **Tools and Skills > Skills** to discover skill invocations. Extension-managed providers accept `/skill:<name>`; Codex displays `/<name>` and also accepts `$<name>`. See [Skills](../customization/skills.md).

To report a problem with an existing session, use:

```text
/send_diagnostics
```

This opens a reporting card; it is not just a local export. A report can contain the complete captured conversation, attachments, and tool output. Review [data and privacy](privacy.md#diagnostic-reports) before submitting.

For the rest of the workflow, see [Chat](../guide/chat.md).
