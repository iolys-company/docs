---
title: OpenRouter
description: Connect OpenRouter to iolys, discover and pin models, and understand credit eligibility and reported costs.
---

# OpenRouter

OpenRouter gives iolys access to an account-specific catalog of models through one API key. Its management panel helps you filter models by price, context size, and capabilities, then pin the ones you use.

## Set up OpenRouter

1. Obtain an API key from your OpenRouter account.
2. Open **Manage Models**, select **Add Provider**, and choose **OpenRouter**.
3. Enter the key and select **Create** to validate the connection and add the provider.
4. Select **Test Connection** to refresh the connection and catalog.
5. Select the models to show in the conversation picker, then return to Chat.

The endpoint is preset. For an existing connection, expand **Connection settings** to update the key. Use a model with tool support for iolys development tasks.

![OpenRouter model discovery, filters, and pinned models](../assets/docs/provider/openrouter/img/ajout-modele-openrouter.png)

*Demonstration models and prices.*

## Find and select models

Search matches model names, IDs, and descriptions. Filter by **Free** or **Paid**, minimum context size, and tool compatibility. Sort by name, input price, output price, context size, or newest entry.

Model cards show capability tags, context size, and available input/output prices per million tokens. Those token prices are not a complete quote for a request, image, or native-tool operation.

A card's checkbox pins it to the conversation picker. **Select all compatible** and **Clear selection** change pins in bulk. With no models selected, all compatible available models are shown. Filtering the discovery view does not unpin hidden models.

## Credit eligibility

iolys checks account credit and key limits during discovery. If the key is restricted to free usage, the key budget is exhausted, or account credit is depleted, only free models are retained. If account credit cannot be verified, discovery also limits the catalog to free models and invites you to test again.

After changing credits or key spending limits, run **Test Connection** again. A free model can still have upstream usage limits. **No matching models** can simply mean your filters exclude everything; **No eligible models available** means no selectable catalog entries remain.

## Images, reasoning, and tools

Choose a **Vision** model to attach an image. Supported local input formats are PNG, JPEG, GIF, and WebP, with a **20 MiB per-file limit**. Invalid or unreadable files can be skipped while the text message is still sent, so check the response and diagnostics if the image was not considered.

Reasoning effort appears only when valid model-specific metadata provides choices. A generic reasoning capability does not guarantee an effort selector.

**Web Search**, **Web Fetch**, and **Datetime** are native tools, each independently disableable. Shared [workspace tools](../customization/tools.md) and [MCP tools](../customization/mcp.md) remain governed by model support, selected agents, and [permissions](../customization/permissions.md).

## Usage and costs

Open **Usage** for account credit, key spending, key budgets, and reported bring-your-own-key usage when available. Conversation costs accumulate amounts reported by the API across model calls; iolys does not compute them by multiplying model-card prices. Missing reporting can leave local totals incomplete.

## Troubleshooting

| Problem | Action |
| --- | --- |
| Paid models are missing | Check account credit and the key's spending limit, then test again. |
| The model picker is too large | Pin the models you want in Manage Models. |
| No results match | Clear search and filters before checking connection eligibility. |
| No effort choice appears | Choose a model whose catalog advertises effort levels. |
| Costs differ from expectations | Compare reported account Usage; token-card prices exclude some possible charges. |

See [usage and context](../guide/usage.md) for interpreting session statistics.
