---
title: Introduction
description: Learn how to install iolys, connect your AI providers, and build with agents inside Visual Studio.
---

<div class="doc-eyebrow">THE IOLYS DOCUMENTATION</div>

# Your AI workspace.<br>Inside Visual Studio.

<p class="doc-lead">Connect your preferred models, give them the right context, and move from a question to a reviewed change. One familiar workflow, across AI providers.</p>

<div class="intro-actions">
<a class="doc-button" href="guide/installation.md">Install iolys <span aria-hidden="true">→</span></a>
<a class="text-action" href="guide/quickstart.md">Run your first task <span aria-hidden="true">↗</span></a>
</div>

<div class="doc-meta"><span class="status-dot"></span> For Visual Studio on Windows <span class="meta-separator">/</span> Currently in beta</div>

## Start here

Choose a starting point. Each guide takes you through the controls you will use in iolys.

<div class="route-grid">
<a class="route-card" href="providers/index.md"><span class="route-icon" aria-hidden="true">↔</span><strong>Connect a provider</strong><span>Use a coding subscription, an API key, or a local model.</span><span class="route-link">Find your setup →</span></a>
<a class="route-card" href="guide/quickstart.md"><span class="route-icon" aria-hidden="true">⌘</span><strong>Make your first change</strong><span>Open a solution, describe a task, and review the result.</span><span class="route-link">Follow the quickstart →</span></a>
<a class="route-card" href="customization/permissions.md"><span class="route-icon" aria-hidden="true">◇</span><strong>Stay in control</strong><span>Choose a mode and decide what your agent can do.</span><span class="route-link">Understand permissions →</span></a>
<a class="route-card" href="customization/skills.md"><span class="route-icon" aria-hidden="true">✳</span><strong>Make it your workflow</strong><span>Reuse skills, create custom agents, and connect MCP tools.</span><span class="route-link">Explore Agent Skills →</span></a>
</div>

## What is iolys?

iolys is an AI development workspace for Visual Studio. It connects your solution, models, conversations, and development tools in one interface. You bring a provider account, API credentials, or a local model; iolys supplies the workflow around it.

An agent can inspect project files, explain code, propose a plan, make changes, and use Visual Studio's build and test tools. The available actions depend on the model, enabled tools, selected mode, and permissions.

<figure class="product-figure">
<img src="assets/screenshots/theme/conversation-dark.png" alt="iolys conversation showing a cancellation-support task, completed tool calls, a code response, and the model and permission selectors." loading="lazy" width="1400" height="1520">
<figcaption>A task, its tool activity, and your next message in the same workspace. Screenshots illustrate the interface; models and controls can vary by version.</figcaption>
</figure>

## Choose your workflow

| If you want to… | Start with… |
| --- | --- |
| Use Claude Code, Codex, Kimi, or Kiro | [Managed CLI providers](providers/index.md#choose-a-connection) |
| Connect hosted models or your own endpoint | [API providers](providers/api-providers.md) |
| Use local or remote Ollama models | [Ollama](providers/ollama.md) |
| Ask about a file, selection, or screenshot | [Files, images, and context](guide/context.md) |
| Work on several tasks independently | [Parallel workspaces](guide/parallel-workspaces.md) |
| Review an agent's edits | [Review and undo changes](guide/review.md) |
| Understand usage, quotas, and estimates | [Usage and costs](guide/usage.md) |

## Build on your team's conventions

Package a repeatable process as an [Agent Skill](customization/skills.md), give a specialized role its own [custom agent](customization/agents.md), or add external capabilities through [MCP servers](customization/mcp.md). These features work within the permissions you choose.

Read [Data and privacy](reference/privacy.md) to understand provider requests, locally saved conversations, product analytics, and optional diagnostics.

## Get help

Start with [Troubleshooting](guide/troubleshooting.md) for connection, model, tool, and session issues. For questions and feedback, join the [iolys Discord community](https://discord.com/invite/NMnFZmPsc5). Product news and release articles are available on the [iolys website](https://getiolys.com/).
