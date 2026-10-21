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

## OpenCode Zen (October 4, 2026)

- Extension: `src/Iolys.Core/Providers/OpenCode/OpenCodeProvider.cs`, `OpenCodeZenModels.cs`, `OpenCodeZenPricing.cs`, `OpenCodeGoogleApiClient.cs`; `docs/provider/opencode_zen/README.md` and its demonstration captures.
- [Official Zen documentation](https://opencode.ai/docs/zen/) and [models.dev API](https://models.dev/api.json), provider `opencode`.
- [OpenCode source revision 907b3bc](https://github.com/anomalyco/opencode/tree/907b3bc518fa48e90e8ec24dd327d13eee71c36c).

## Ollama (October 5, 2026)

- User workflows and capabilities: `docs/provider/ollama/README.md`, `docs/ollama_provider.md`, and `screenshots/ollama-model-memory/README.md`.
- Connection labels checked against `src/Iolys.VisualStudio/Chat/ManageModels/ManageModelsWindow.xaml` and `src/Iolys.VisualStudio/Providers/Ollama/ManageModels/OllamaModelsPanel.xaml`.
- Dark-only screenshots copied unchanged from `docs/provider/ollama/img/` to `assets/docs/provider/ollama/img/`: connection, download progress, model picker, custom context, reasoning levels, memory tools, vision chat, performance tooltip, and installation error.
- Memory popup copied unchanged from `screenshots/ollama-model-memory/Dark-600-popup.png` to `assets/screenshots/ollama-model-memory/`. All captures render production WPF controls with offline demonstration data; captions do not present them as live model results or performance benchmarks.

## Workflow additions (October 17, 2026)

- DeepSeek standalone tools and the estimate applied by iolys: [PR #284](https://github.com/iolys-company/iolys/pull/284), `docs/tools/deepseek_web_search.md`, and `src/Iolys.Core/Providers/DeepSeek/DeepSeekModelPricing.cs` at revision `3348268aad8eb9f2d562120e96fc789da9547bc8`. The per-request amount is described as an iolys estimate; promotional API billing remains subject to the provider's account record.
- Title bar Chat entry point: [PR #272](https://github.com/iolys-company/iolys/pull/272).
- External `run_cli` working directories and approval scope: [PR #270](https://github.com/iolys-company/iolys/pull/270).
- Managed commit amendment and remote branch deletion: [PR #273](https://github.com/iolys-company/iolys/pull/273) and [PR #268](https://github.com/iolys-company/iolys/pull/268).
- Compact tool-call hover previews: the separate tooltip change in [PR #278](https://github.com/iolys-company/iolys/pull/278).

## OpenCode reasoning, usage, and tools (October 21, 2026)

- Effort choices and defaults checked against `src/Iolys.Core/Providers/OpenCode/OpenCodeModels.cs` and `OpenCodeZenModels.cs` in `vs_assistant`. The guides show examples of integration profiles, not a permanent available-model catalog.
- Account counters, context, tool forwarding, and conditional costs checked against `OpenCodeProvider.cs`, `OpenCodeOpenAiProvider.cs`, `OpenCodeZenPricing.cs`, and `docs/provider/{opencode_go,opencode_zen}/README.md`.
- Go's `conversation-tools.png` and `usage-limit.png` are unchanged copies of the extension's WPF demonstration captures. Existing `reasoning-level.png` is now displayed in the Go guide alongside context and usage captures.
- Zen's updated `reasoning-level.png` comes from `Iolys.PublicWebSite/src/Iolys.PublicWebsite/wwwroot/img/providers/opencode-zen/`. It was rendered from real WPF controls using the website's `tools/opencode-zen/render-reasoning.ps1`, with the six GPT-6 Luna choices verified against the implementation. The existing Zen context capture is now displayed in the guide. All captures use demonstration data and make no live account, provider, or billing claim.
- Native-tool boundaries checked against the extension integration and the official [OpenCode built-in tools](https://opencode.ai/docs/tools/) and [hosted web search](https://opencode.ai/v2/docs/console/websearch/) documentation. These upstream services are not enabled by the iolys Go/Zen API-key connections.