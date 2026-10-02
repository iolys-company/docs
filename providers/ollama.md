---
title: Ollama
description: Connect local or remote Ollama servers, manage models, and configure their context allocation in iolys.
---

# Ollama

Connect iolys to a local or remote Ollama server to work with models you manage yourself. Multiple named Ollama instances are supported, so you can keep separate connections for different servers.

## Connect a server

1. Install and start Ollama on the machine that will run inference.
2. Open **Manage Models** in iolys, select **Add Provider**, and choose **Ollama**.
3. Enter an **Instance name** and **Server URL**. The local default is `http://localhost:11434`.
4. Select **Create** and wait for the model list. Ollama does not require an API token in this form.
5. If the server has no models, enter a model name in **Add model** and start the download.
6. Return to Chat and select a model from that Ollama instance.

For a remote server, use an address reachable from the machine running the iolys server. The provider connects to an existing Ollama service; adding it does not install or start a remote service for you.

## Manage models

The panel lists available models and marks models that are **Running**. **Add model** downloads a model on the connected Ollama server and displays progress. **Delete** removes a model from that server, so take care when several applications or users share it.

The Ollama-specific load and unload tools can manage which model is held in memory when those [tools](../customization/tools.md) are enabled. Model downloads, loading time, memory requirements, and inference speed depend on the model and server hardware.

## Choose a context size

Each model offers **Fast**, **Balanced**, **Max**, and **Custom** context presets. These adjust the model's context allocation; they are not reasoning-effort settings.

Start with **Balanced**. Use **Fast** for a smaller allocation, **Max** when the machine can accommodate the model's full context, or **Custom** for an explicit value. **Detect preset** can inspect the running model and suggest a preset for the current environment. A larger context can increase memory use, so reduce it if loading fails or performance becomes unsuitable.

## Tools, images, and thinking

Choose a model advertising tool support for the full development workflow. Shared workspace tools, [MCP tools](../customization/mcp.md), [skills](../customization/skills.md), and [permissions](../customization/permissions.md) remain available according to the selected model and task configuration.

Image attachments require a vision-capable model. Reported thinking can stream separately from the answer, but the Ollama provider does not offer a graded reasoning-effort selector. A model's name alone is not enough to establish these capabilities.

The context view shows conversation consumption using the configured context allocation. Ollama has no provider subscription Usage view or monetary cost estimate in iolys. See [usage and context](../guide/usage.md).

## Troubleshooting

| Problem | Action |
| --- | --- |
| Cannot load the model list | Confirm Ollama is running and the server URL is reachable; use Retry. |
| The list is empty | Add a model and wait for its download to complete. |
| Loading fails or inference is slow | Check available server memory, choose a smaller model, or reduce the context preset. |
| A remote model download fails | Check the remote server's connectivity and disk space. |
| Tool calls fail | Verify model tool support and the selected iolys tools; try a small focused task. |

Try the [quickstart](../guide/quickstart.md) once the model is available.
