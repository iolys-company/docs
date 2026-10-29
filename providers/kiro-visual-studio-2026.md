---
title: Develop C# projects with Kiro in Visual Studio 2026
description: Work on C# projects with Kiro in Visual Studio 2026 using iolys. Connect your account, use workspace tools and images, and track reported credits.
---

<a id="kiro"></a>

# Develop C# projects with Kiro in Visual Studio 2026

Work on your C# projects in Visual Studio 2026 with your Kiro account and iolys. The managed Kiro CLI connects you to shared workspace tools, image attachments, and reported credits.

<p><a class="doc-button" href="https://marketplace.visualstudio.com/items?itemName=iolys.iolys-visual-studio">Install iolys for Visual Studio <span aria-hidden="true">→</span></a></p>

## Set up Kiro

1. Open **Manage Models**, select **Add Provider**, and choose **Kiro**.
2. Install Kiro CLI using the provider's version controls.
3. Select **Connect**. iolys checks the managed CLI's authentication and opens an interactive sign-in window if needed. Follow Kiro's sign-in instructions.
4. After sign-in, iolys verifies authentication, reconnects, and refreshes the model catalog.
5. Select a discovered model in Chat and send a message.

Existing CLI authentication is reused without opening a sign-in window. Signing in to Kiro IDE alone does not verify the managed CLI's authentication. A system CLI on PATH does not replace the executable managed by iolys.

![Kiro installation and model selection](../assets/docs/provider/kiro/img/models-kiro.png)

*Illustrative models and versions.*

## Models and images

Use the model picker for current model and effort choices. Effort options can appear after capability discovery finishes. An unsupported or rejected effort blocks the prompt rather than silently applying a different value.

Attach images directly in the composer when **Vision** is available. Kiro's image capability comes from the live CLI connection. PNG, JPEG, GIF, BMP, and WebP are accepted locally, subject to file and encoded payload limits. The shared encoder can resize supported images for transport.

The iolys `read_image` tool is hidden for Kiro because this integration does not support image results from MCP tools. Attach the image itself rather than asking a tool to open it.

## Native tools and permissions

Kiro exposes five native tools: **Knowledge**, **Subagent**, **Use AWS**, **Fetch URL**, and **Web Search**. They cannot be disabled individually in the session picker. AWS operations still depend on your AWS configuration and permissions.

![Kiro's Model Tools section listing Knowledge, Subagent, Use AWS, Fetch URL, and Web Search without checkboxes](../assets/docs/provider/kiro/img/conversation-native-tools.png)

*Kiro's five native tools are listed without individual switches. The surrounding conversation is a demonstration.*

Shared [iolys tools](../customization/tools.md) follow your selected agent, mode, and [permissions](../customization/permissions.md). Native Kiro permission requests are a separate path and appear in the permission UI. **Plan mode restricts iolys tools but does not guarantee that every native Kiro action is read-only.** Review native requests accordingly.

Project [skills](../customization/skills.md) use the shared `.agents/skills` directory through a Kiro compatibility link. A real directory already occupying `.kiro/skills` is preserved and can prevent that link from being created.

## Usage and maintenance

Open **Usage** for the account's credit consumption, limit, plan, and reset label when reported. Completed turns can also show provider-reported credits. Credits are not dollars, and missing metering does not mean a free request. See [usage and context](../guide/usage.md).

![Kiro Usage showing consumed credits, the plan limit, and the reset label](../assets/docs/provider/kiro/img/usage-kiro.png)

*Compare consumed credits with the plan limit. This example uses a fictional plan and credit values.*

Update or reinstall from the managed version controls. Uninstalling this managed CLI does not sign out the normal Kiro profile or remove a separate system installation.

## Troubleshooting

| Problem | Action |
| --- | --- |
| Connect does not open sign-in | Existing CLI authentication skips sign-in. If connection still fails, check the managed executable's `whoami` result using the steps below. |
| Sign-in does not complete | Select **Connect** again and complete the interactive CLI prompts. Check the managed installation and network connection if it fails. |
| No models appear | Verify sign-in, managed version, and connectivity; refresh the catalog. |
| Image tool is missing | Attach the image directly; `read_image` is intentionally unavailable. |
| Native tool checkbox cannot be changed | Those five tools have fixed inclusion in this integration. |
| Project skills are missing | Check for a conflicting `.kiro/skills` directory. |

### Check authentication manually

If the normal **Connect** flow fails, you can check the managed CLI in PowerShell:

```powershell
$kiroCli = Join-Path $env:LOCALAPPDATA 'Iolys\Providers\KiroCli\Cli\LocalApp\Kiro-Cli\kiro-cli.exe'
& $kiroCli whoami
```

If it reports that you are not signed in, run `& $kiroCli login`, complete the sign-in instructions, and check `whoami` again. Return to iolys and select **Connect**.

If that path is absent, check the managed `Iolys\Providers\KiroCli\Cli` directory: older installations can place the executable directly there. Use that managed executable for both commands.
