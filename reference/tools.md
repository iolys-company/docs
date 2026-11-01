---
title: Tool reference
description: Built-in iolys tools, subagent collaboration parameters, provider tools, and the conditions under which agents can use them.
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
| `run_cli` | Execute managed CLI requests and bounded batches, including in an external `workdir` after path approval. Plan accepts recognized reads only. |
| `shell_command` | Execute scripts with iolys-managed PowerShell 7 or recognized managed commands. The first script needs internet access to prepare the runtime. Plan accepts recognized managed reads, not ordinary scripts. |

`remove_file` does not delete directories or stage Git changes. It rejects unsupported project items and requires unsaved documents/projects to be saved first. Recorded workspace changes support review and undo, subject to conflict checks. Build and test execution can create artifacts even in Plan.

Managed command integrations classify supported Git, GitHub, text, and .NET operations. Configure their rights under **Run CLI commands > Integrations**. Historical identifiers `git_read`, `git_write`, `github_read`, and `github_write` are internal compatibility/permission categories, not tools to select for a new agent. Use `run_cli` with explicit integration rights.

For commands targeting another worktree or repository, see [Run commands in another folder](../customization/tools.md#run-commands-in-another-folder). Folder approval and repository-write approval are separate.

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

## Delegate and coordinate

The **Collaboration** group lets a coordinator delegate parts of a task and collect the results. [Subagents](../guide/subagents.md) are enabled by default; use **Settings > Subagent settings** to enable or disable them and set workspace capacity. These tools require a compatible provider/model and access through the selected agent's tool selection.

| Tool | Purpose |
| --- | --- |
| `list_agent_profiles` | Discover the built-in standard agent, read-only Explorer, and custom roles. |
| `list_agent_models` | Discover compatible configured models, reasoning efforts, and speed tiers. |
| `spawn_agent` | Root coordinator only: start a direct child with a focused task; a custom profile is optional. |
| `list_agents` | Inspect visible agents and workspace capacity, including occupied coordinator slots. |
| `send_message` | Deliver information without starting a turn. |
| `followup_task` | Assign more work to an existing child, preserving its conversation; active children queue the assignment. |
| `wait_agent` | Wait for messages, results, status, or permission requests, for up to 60 seconds per call. |
| `report_agent_status` | Report progress or a blocker to the parent. |
| `interrupt_agent` | Cancel a descendant and its active children while retaining history. |
| `resolve_agent_permission` | Let the root coordinator deny, escalate, or approve within previously delegated authority. |

### Discover agents and models

`list_agent_profiles`, `list_agent_models`, and `list_agents` take optional `offset` (default **0**) and `maxResults` (default **20**, maximum **50**). Continue from the returned `nextCursor` while `hasMore` is true. `list_agent_models` also accepts an optional `providerName` filter.

Use `list_agents` to check `workspaceCapacity` and `occupiedSlots` before spawning work. The workspace limit includes running coordinators and children, including turns waiting for messages or permission. Other conversations in the same workspace can occupy slots too. Collaboration tools cannot change this global limit.

### Start a child with spawn_agent

Delegation has **two levels including the coordinator**. Only the root coordinator is offered `spawn_agent`; child calls are also refused by the server with `depth_limit`, even when a custom role selects this tool. Children can ask their coordinator to create another direct child. This restriction does not reduce how many children can work in parallel within workspace capacity. Older deeper conversations remain readable.

| Argument | Required | Meaning |
| --- | --- | --- |
| `name` | Yes | Task label, unique among siblings; up to 80 characters. |
| `task` | Yes | Focused assignment; up to 16,000 characters. |
| `requestId` | Yes | Stable key for this operation; see retry rules below. |
| `agentProfileId` | No | Omit or use `builtin:agent` for a standard agent. Use `builtin:explorer` for read-only investigation under Plan restrictions, or an ID returned by `list_agent_profiles` for a custom role. |
| `providerName`, `model` | No | Compatible configured provider and model. When omitted, use a configured default or inherit the coordinator's selection. |
| `reasoningEffort`, `serviceTier` | No | Supported reasoning and speed settings. Same-model children inherit the coordinator's requested values unless overridden. |
| `contextSummary` | No | Additional task context; up to 16,000 characters. |

For example, the coordinator can call `spawn_agent` with these arguments to investigate code using Explorer:

```json
{
  "name": "Trace data loading",
  "task": "Trace how the results grid loads data. Return relevant files, symbols, and possible empty-result paths.",
  "agentProfileId": "builtin:explorer",
  "requestId": "trace-data-loading-1"
}
```

Children have separate conversations and share workspace files. Standard and custom agents inherit the coordinator's mode; Explorer uses Plan restrictions even when the coordinator is in Agent mode. All children inherit the coordinator's tool and permission restrictions. A provider whose non-disableable native tools conflict with those restrictions cannot run that child. Spawning does not create a worktree, install a CLI, or sign in to a provider.

### Send messages and follow-up work

| Tool | Required arguments and behavior |
| --- | --- |
| `send_message` | `targetAgentId`, `message`, `requestId`. The message can contain up to 8,000 characters; it delivers information without starting another turn. |
| `followup_task` | `targetAgentId`, `task`, `requestId`. The task can contain up to 16,000 characters; it reuses the child's conversation and queues the assignment if the child is active. Workspace capacity still applies. |
| `report_agent_status` | `status`, `summary`, `requestId`. Status is `working` or `blocked`; the summary can contain up to 1,000 characters. |
| `interrupt_agent` | `targetAgentId`, `requestId`. Cancels the descendant and its active children; retains their conversations and does not undo file changes. |
| `resolve_agent_permission` | `permissionRequestId`, `decision`, `requestId`. Root coordinator only; decision is `approve`, `deny`, or `escalate`. Approval requires previously delegated authority and an eligible one-time approval option. Other requests must be escalated to the user. |

Use the agent's session ID as `targetAgentId`. The coordinator can address its children; children can exchange notes with the coordinator. Siblings and unrelated agent trees are outside that scope. The coordinator assigns follow-up work and interrupts children. Existing deeper histories retain their descendant addressing and cleanup behavior. Messages never grant permissions.

Every operation in this table, and `spawn_agent`, requires a `requestId`. Reuse it only for an identical retry by the same caller. Reusing it with different arguments fails. If an operation was interrupted, inspect the agent history before assigning new work.

### Wait for results

`wait_agent` takes no required arguments. Optional `agentIds` filters visible agents, and `timeoutMs` controls the wait: **30,000** by default, at most **60,000**, or **0** for an immediate check. Without an explicit `afterSequence`, it resumes from the saved inbox position; unfiltered reads advance that position. Set `afterSequence: 0` to replay available events, or use the returned `nextCursor` to continue reading explicitly. Check `hasMore` for additional events.

Ending a coordinator turn cancels outstanding descendant work, so required results must be collected before the final response. For progress, conversation links, permission prompts, and statistics, see the [subagent workflow](../guide/subagents.md#follow-progress-and-open-conversations).

## DeepSeek web tools

The [DeepSeek provider](../providers/deepseek-visual-studio-2026.md#search-the-web-and-read-pages) adds these tools under **DeepSeek Web Tools** on Flash and Pro. Both are available in Agent and Plan, subject to their toggles and the active agent's tool selection. Other providers do not receive them.

| Tool | Purpose and arguments |
| --- | --- |
| `deepseek_search` | Search the web with `query` (1–128 characters), `count` (1–50, default 10), and `need_content` (default false). Optional `ori_question` and IP `localization` provide additional search context. |
| `deepseek_fetch` | Read a page as Markdown using an HTTP(S) `url` without credentials. `maxChars` limits the returned text to 1–20,000 characters, default 12,000. |

Results flag truncated content. For a custom agent with selected tools, include each required identifier in its `tools` list. These are function tools, separate from the model's native `web_search`. Successful non-empty responses contribute to [DeepSeek's estimated conversation costs](../providers/deepseek-visual-studio-2026.md#check-balance-and-costs).

## Provider-native and MCP tools

Provider-native capabilities are separate from this catalog. Examples include Claude Code's `WebSearch`/`WebFetch`, Codex's `web.run` and image generation, Kimi's search/fetch/skill tools, Grok's web search and fetch tools, and Kiro's retained native tools. OpenRouter and DeepSeek can expose native web capabilities; Databricks search is controlled by its provider setting.

These capabilities depend on the model, endpoint, account, and installed CLI. Some cannot be individually disabled. See [Providers](../providers/index.md) and [tool selection](../customization/tools.md).

Connected [MCP servers](../customization/mcp.md) add their enabled tools dynamically. Custom-agent definitions refer to them as `server-id/tool-name` or the deliberate wildcard `server-id/*`.
