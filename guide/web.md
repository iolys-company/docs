---
title: Companion web interface
description: Continue iolys conversations in a local browser connected to the correct Visual Studio workspace.
---

# Companion web interface

The companion web interface lets you use iolys chat in your browser while the local server connects it to Visual Studio. It uses the same conversations and agent engine as the extension. Opening a task in the browser does not create a separate copy of its history or workspace.

## Open the web interface

1. Open your solution in Visual Studio and wait for iolys to connect.
2. Configure a [provider](../providers/index.md) in the extension if you have not already done so.
3. Select **View > Iolys Web**. iolys opens your default browser and handles authorization to the local server.
4. On **Visual Studio instances**, choose the workspace you want to use. Check its solution name and full path, especially when several worktrees contain the same solution.
5. Open a listed conversation or select **New conversation**.

The initial page lists connected instances even when you launched it from a particular Visual Studio window. Selecting an instance is therefore an explicit choice. In Chat, **Choose another Visual Studio instance** returns to that list.

Use the extension's launch command instead of assuming a fixed localhost port. This interface is served locally; the documented workflow does not provide phone pairing or public remote access.

## Work on a shared conversation

The web chat supports streamed replies and tool activity, conversation history, renaming, new tasks, and deletion. Its composer lets you choose the provider/model, available reasoning effort and speed options, **Agent** or **Plan**, custom agents, and permissions.

You can respond to permission requests and structured clarification questions, queue follow-up messages, and use **Stop generating** to cancel work. Cancellation does not undo completed changes.

Use **+ > Active document** to attach the selected instance's active file reference, or **Add file...** and the `#` context picker to find a file. Context chips can be removed before sending. See [Files, images, and context](context.md) for what a file reference includes.

Because state is shared, a rename, message, or deletion concerns the same task you see in Visual Studio. Starting another task in the same solution also uses the same checkout. Create a [parallel workspace](parallel-workspaces.md) when tasks need separate files.

## Use Visual Studio for IDE-specific work

Keep the extension available for provider installation and sign-in, tool and MCP configuration, editor-selection capture, Visual Studio diff review, and worktree management. The browser is a companion chat interface, rather than a replacement for every IDE control.

If **No Visual Studio instance is connected** appears, open a solution with the extension and reload the page. If an instance has disconnected, return to the instance list and select an available workspace. For **No model provider is available**, configure the provider in Visual Studio. For server or update errors, follow [Troubleshooting](troubleshooting.md).
