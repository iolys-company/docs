# Documentation source map

Initial source review: 2 October 2026. Paths below refer to the local `vs_assistant` source repository unless stated otherwise. They are maintenance references, not public site links. Only the explicitly included Markdown folders in `docfx.json` become website content.

| Documentation area | Existing Markdown sources |
| --- | --- |
| Introduction, installation, quickstart | `docs/marketing/Product Features.md`, `docs/marketing/visual-studio-marketplace.md`, `docs/brand.md` |
| Conversations, context, review, settings | `docs/chat_reading.md`, `docs/session_persistence.md`, `docs/review-prompt.md`, `docs/marketing/Product Features.md` |
| Parallel workspaces | `docs/marketing/Product Features.md`, `docs/visual_studio_instance_notifications.md` |
| Provider guides | `docs/provider/{claude_code,codex,kimi,kiro,openrouter,opencode_go,databricks}/README.md`, `docs/ollama_provider.md` |
| Reasoning, speed, usage | `docs/provider/reasoning_effort.md`, `docs/provider_service_tiers.md`, `docs/provider_model_capabilities.md`, provider guides |
| Native tools and provider differences | `docs/tools/native_tools_by_provider.md`, `docs/tools/{claude,codex,kimi,kiro}_tools.md`, `docs/tools/deepseek_web_search.md`, `docs/tools/databricks_web_search.md` |
| Tool catalog and permissions | `docs/tools/iolys_tools.md`, `docs/tools/git_command_classification.md`, `docs/tools/github_command_classification.md`, current tool registration and UI |
| Skills and custom agents | `docs/SHARED_SKILLS_SPEC.md` checked against shipped parsers/UI, `docs/marketing/Product Features.md`, current agent-profile parser and creator skill |
| MCP | `docs/tools/mcp_servers.md`, current configuration dialog and execution-policy code |
| Privacy and troubleshooting | `docs/backend-enrollment.md`, `docs/backend-snapshots.md`, `docs/send-diagnostics.md`, `docs/session_persistence.md` |

The proposed steering synchronization in `docs/SHARED_STEERING_SPEC.md` is not described as a shipped feature. Product Features' old fixed tool counts are omitted because the current tool catalog has changed. Installation follows the public product documentation's Visual Studio 2026 requirement; the source VSIX manifest accepts a broader version range.

The brand palette and logo come from `Iolys.PublicWebSite/src/Iolys.PublicWebsite/wwwroot/css/site.css`, `img/brand-lab/13-code-compass-128.webp`, and `favicon.ico`. The header wordmark follows that website's `Pages/Shared/_Layout.cshtml` and `wwwroot/css/themes/iolite-sun.css`: the compass replaces the "o", with monospace lettering and an offset shadow. Screenshots from `vs_assistant` preserve their source-relative paths beneath `assets/`. The DeepSeek guide also draws on `Iolys.PublicWebSite/docs/deepseek-provider-page.md`; its images are copied from that website's `wwwroot/img/providers/deepseek/` to `assets/docs/provider/deepseek/img/`. Screenshots are illustrative and may show earlier model names or menu arrangements.

The visual walkthroughs reuse inspected screenshots from `vs_assistant/docs/images/`, `docs/screenshots/`, `docs/provider/`, and `screenshots/`. The Codex speed selector at `assets/website/codex-fast-mode.png` comes from `Iolys.PublicWebSite/src/Iolys.PublicWebsite/Content/Posts/2026/iolys-september-update-1-agents-codex-speed-mode/images/codex-fast-mode.png`. Images are copied unchanged; captions identify demonstration data and provider-specific examples. The SVGs in `assets/diagrams/` are explanatory diagrams authored for these guides, based on the workflows described in the source map above; they are not interface screenshots.

The GIF at `assets/diagrams/agent-creator-workflow.gif` is an illustrated example authored for the custom-agents guide, based on `vs_assistant/src/Iolys.VisualStudio.Server/BuiltInSkills/agent-creator/SKILL.md` and the verified skill-picker workflow. It shows the request, scope and tool choices, a sample generated definition, and selection for a new conversation. It is explicitly labeled as an illustration, not a screen recording. Regenerate it with `scripts/render-agent-creator-demo.py` using Python, Pillow, and the Windows Segoe UI and Consolas fonts. The same GIF is copied to `vs_assistant/docs/marketing/marketplace-images/agent-creator-workflow.gif` for the source documentation.
