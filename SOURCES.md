# Documentation source map

Initial source review: 2 October 2026. Paths below refer to the local `vs_assistant` source repository unless stated otherwise. They are maintenance references, not public site links. Only the explicitly included Markdown folders in `docfx.json` become website content.

| Documentation area | Existing Markdown sources |
| --- | --- |
| Introduction, installation, quickstart | `docs/marketing/Product Features.md`, `docs/marketing/visual-studio-marketplace.md`, `docs/brand.md` |
| Conversations, context, review, settings | `docs/chat_reading.md`, `docs/session_persistence.md`, `docs/review-prompt.md`, `docs/marketing/Product Features.md` |
| Parallel workspaces and companion web | `docs/marketing/Product Features.md`, `docs/visual_studio_instance_notifications.md`, `docs/LOCAL_SERVER_ARCHITECTURE.md` |
| Provider guides | `docs/provider/{claude_code,codex,kimi,kiro,openrouter,opencode_go,databricks}/README.md`, `docs/ollama_provider.md` |
| Reasoning, speed, usage | `docs/provider/reasoning_effort.md`, `docs/provider_service_tiers.md`, `docs/provider_model_capabilities.md`, provider guides |
| Native tools and provider differences | `docs/tools/native_tools_by_provider.md`, `docs/tools/{claude,codex,kimi,kiro}_tools.md`, `docs/tools/deepseek_web_search.md`, `docs/tools/databricks_web_search.md` |
| Tool catalog and permissions | `docs/tools/iolys_tools.md`, `docs/tools/git_command_classification.md`, `docs/tools/github_command_classification.md`, current tool registration and UI |
| Skills and custom agents | `docs/SHARED_SKILLS_SPEC.md` checked against shipped parsers/UI, `docs/marketing/Product Features.md`, current agent-profile parser and creator skill |
| MCP | `docs/tools/mcp_servers.md`, current configuration dialog and execution-policy code |
| Privacy and troubleshooting | `docs/backend-enrollment.md`, `docs/backend-snapshots.md`, `docs/send-diagnostics.md`, `docs/session_persistence.md` |

The proposed steering synchronization in `docs/SHARED_STEERING_SPEC.md` is not described as a shipped feature. Product Features' old fixed tool counts are omitted because the current tool catalog has changed. Installation follows the public product documentation's Visual Studio 2026 requirement; the source VSIX manifest accepts a broader version range.

The brand palette and logo come from `Iolys.PublicWebSite/src/Iolys.PublicWebsite/wwwroot/css/site.css`, `img/brand-lab/13-code-compass-128.webp`, and `favicon.ico`. Copied screenshots preserve their source-relative paths beneath `assets/`. Screenshots are illustrative and may show earlier model names or menu arrangements.
