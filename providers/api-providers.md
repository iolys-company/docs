---
title: API providers
description: Configure OpenAI, Anthropic, Gemini, Groq, NVIDIA NIM, and compatible endpoints in iolys.
---

# API providers

Connect hosted models with an API key or use your own compatible endpoint. API credentials are separate from the subscriptions connected through [Claude Code](claude-code.md), [Codex](codex.md), [Kimi](kimi.md), and [Kiro](kiro.md).

## Common setup

1. Obtain a key from the provider account you intend to use.
2. Open **Manage Models**, select **Add Provider**, and choose the provider.
3. Enter the key. For a compatible endpoint, also enter its server URL and instance name. Select **Create** to validate the connection and add the provider.
4. Inspect the returned models. Use **Test Connection** in the provider panel to refresh discovery or after changing connection details.
5. Set a default model where offered and select the models you want in the conversation picker.
6. Return to Chat, choose a tool-capable model, and follow the [quickstart](../guide/quickstart.md).

Use the key-management link in the provider form when available. Keep credentials in provider settings rather than chat messages or project files. Access, quotas, model availability, and charges are controlled by the provider account.

## OpenAI

Choose **OpenAI** and set the server URL to `https://api.openai.com/v1` for the official API. Enter an instance name and OpenAI API key, select **Create**, and choose a model returned by the endpoint. The saved provider panel labels this address **Base URL**.

The same provider type also accepts OpenAI-compatible services. Its default local gateway address is not the official OpenAI API address, so check the URL before testing. Available tools, images, reasoning, and supported request formats depend on the endpoint and selected model.

## Anthropic

Choose **Anthropic** and enter your Anthropic API key. The official endpoint is preset. Use **Test Connection**, select a discovered model, and review **Advanced settings** when you need to configure thinking or output limits. Apply settings after changing them.

This is the API-key connection. To use an eligible Claude subscription through the managed CLI, follow [Claude Code](claude-code.md).

## Google Gemini, Groq, and NVIDIA NIM

These providers have preset endpoints. Select the corresponding provider, enter its key, test the connection, and choose a discovered model.

| Provider | Key source shown by iolys | Endpoint configured by iolys |
| --- | --- | --- |
| Google Gemini | Google AI Studio | `https://generativelanguage.googleapis.com/v1beta/openai` |
| Groq | Groq Console | `https://api.groq.com/openai/v1` |
| NVIDIA NIM | NVIDIA Build | `https://integrate.api.nvidia.com/v1` |

Use capability badges rather than assuming every model offers function tools, vision, or configurable reasoning. These hosted presets do not configure a separately deployed private model server.

## Compatible endpoints

For a local gateway, organizational proxy, or self-hosted API, choose the protocol your endpoint implements:

- **OpenAI** accepts a custom base URL. The current add-provider form requires a nonempty API token even for a local gateway; use a credential accepted by your gateway. An unauthenticated endpoint cannot be added with an empty token through this form. Use the gateway's documented API root, not its web dashboard.
- **Anthropic-compatible** is available in builds that expose this provider. Supply its base URL, model ID, and required authentication, then verify that connection and model listing work in your installed version. For Databricks, prefer the dedicated [Databricks provider](databricks.md).

Compatibility depends on the routes and features your gateway implements. Successful model discovery is not proof that streaming, tool calls, images, or every reasoning option will work. Test a small conversation before a larger task.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Authentication error | Key value, correct provider account, endpoint, and required access. |
| Create stays disabled | Fill every required field, including the API token. Instance names must start with a letter or digit and use at most 30 letters, digits, spaces, hyphens, or underscores. |
| No models | Model-list permission, base URL, network access, and account eligibility. |
| Unknown model | Use the exact model or deployment ID accepted by the endpoint. |
| Tools or images are rejected | Select a model supporting the capability; inspect gateway compatibility. |
| A limit or payment error occurs | Check provider Usage where available and the account dashboard. |

Continue with [tool selection](../customization/tools.md), [MCP servers](../customization/mcp.md), and [usage and context](../guide/usage.md).

Use the dedicated [OpenCode Zen](opencode-zen.md) entry for Zen keys. It chooses each verified model protocol and supplies conditional Zen cost estimates. A generic OpenAI-compatible connection does not provide this routing.
