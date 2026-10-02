---
title: Tool reference
description: Built-in iolys tools and the conditions under which agents can use them.
---

# Tool reference

Use this catalog to configure [custom agents](../customization/agents.md) or understand tool calls. Check **Tools and Skills** for the selected conversation's available tools.

All tools remain subject to provider/model support, enablement, active-agent restrictions, and [permissions](../customization/permissions.md).

## Inspect the workspace

| Tool | Purpose |
| --- | --- |
| `search_files` | Find files by name, path, or glob pattern. |
| `read_file` | Read text, with pagination for long files. |
| `read_image` | Load a supported image for a model that can process image input. |
| `grep` | Search file contents with regular expressions. |
| `list_directory` | List a directory's contents. |
| `current_document` | Identify the active Visual Studio document. |
| `get_projects_in_solution` | List projects in the open solution. |
| `get_files_in_project` | List a project's files, optionally filtered. |
| `get_errors` | Retrieve compilation errors and warnings, optionally filtered by file and severity. |
| `get_tests` | Discover tests and filter the results. |

Inspection tools work in Agent and Plan when dependencies are available. IDE results require a connected Visual Studio instance and relevant solution state.

## Change and validate code

| Tool | Purpose and availability |
| --- | --- |
| `write_file` | Create or edit files. Agent mode. |
| `apply_patch` | Apply a batch of file additions, updates, or deletions with prevalidation and rollback handling. Agent mode. |
| `move_files` | Move or rename files. Agent mode. |
| `remove_file` | Delete one workspace file and update supported loaded project membership. Agent mode. |
| `run_build` | Build the solution or supported target; available in Agent and Plan. |
| `run_tests` | Run tests with supported selection/filtering; available in Agent and Plan. |
| `run_cli` | Execute managed CLI requests and bounded batches. Plan accepts recognized reads only. |
| `shell_command` | Execute Windows PowerShell 5.1 scripts or recognized managed commands. Plan accepts recognized managed reads, not ordinary scripts. |

`remove_file` does not delete directories or stage Git changes. It rejects unsupported project items and requires unsaved documents/projects to be saved first. Recorded workspace changes support review and undo, subject to conflict checks. Build and test execution can create artifacts even in Plan.

Managed command integrations classify supported Git, GitHub, text, and .NET operations. Configure their rights under **Run CLI commands > Integrations**. Historical identifiers `git_read`, `git_write`, `github_read`, and `github_write` are internal compatibility/permission categories, not tools to select for a new agent. Use `run_cli` with explicit integration rights.

## Plan, clarify, and customize

| Tool | Purpose and availability |
| --- | --- |
| `update_plan` | Create or update the active Markdown task plan; Agent and Plan. |
| `read_plan` | Read the active plan; Agent and Plan. |
| `clarify_requirements` | Present a structured question with selectable answers; requires an interactive client. |
| `skill` | Load a skill's instructions for extension-managed providers. Native skill providers use their own integration. |
| `create_skill` | Create a validated workspace or global skill; Agent mode. |
| `create_agent_profile` | Create a validated workspace or global `.agent.md` definition; Agent mode. |
| `ollama_load_model` | Load a model into an Ollama server's memory; Ollama only. |
| `ollama_unload_model` | Unload a model from an Ollama server's memory; Ollama only. |

## Provider-native and MCP tools

Provider-native capabilities are separate from this catalog. Examples include Claude Code's `WebSearch`/`WebFetch`, Codex's `web.run` and image generation, Kimi's search/fetch/skill tools, and Kiro's retained native tools. OpenRouter and DeepSeek can expose native web capabilities; Databricks search is controlled by its provider setting.

These capabilities depend on the model, endpoint, account, and installed CLI. Some cannot be individually disabled. See [Providers](../providers/index.md) and [tool selection](../customization/tools.md).

Connected [MCP servers](../customization/mcp.md) add their enabled tools dynamically. Custom-agent definitions refer to them as `server-id/tool-name` or the deliberate wildcard `server-id/*`.
