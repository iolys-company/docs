---
title: Git and GitHub
description: Inspect repository changes, prepare commits, and work with pull requests through managed command tools.
---

# Git and GitHub

iolys can inspect your repository, prepare commits, and work with GitHub pull requests through managed command tools. You describe the outcome; the agent uses the available commands under your selected permissions.

## Set up the repository

Open a solution in a Git repository. Git must be available; iolys can use Git on PATH or the Git installation bundled with Visual Studio.

For GitHub, open **Settings > GitHub** under **Integrations**, install the managed CLI when prompted, and connect your account in the browser. See [GitHub setup](settings.md#connect-github). A separate system `gh` installation does not replace the managed CLI.

Open **Tools and Skills > Tools > Run CLI commands > Integrations** to check Git and GitHub read/write rights. A [custom agent](../customization/agents.md) also needs the relevant tool and integration permissions. Plan accepts recognized managed reads; switch to Agent for repository changes.

## Inspect before changing

Start with a focused request:

```text
Inspect the current branch, staged and unstaged changes, and recent commits.
Explain which changes belong to the CSV export task and propose a commit message.
```

Managed reads include status, diff, history, branch listings, and supported GitHub queries. For an existing pull request, ask:

```text
Review the current branch's pull request and its checks. Explain any failing
checks and identify the files involved.
```

GitHub operations are scoped to the workspace's configured repository. An explicit repository or pull request URL must match that repository; cross-repository commands do not inherit ordinary read access.

## Commit and publish deliberately

First [review the file changes](review.md) and relevant tests. Inspect the staged diff too: a Git commit includes the entire index, including work staged before this task.

When ready, give an explicit instruction naming the intended branch and destination. For example, adapted to your repository:

```text
Commit the reviewed CSV export changes with the message "Add CSV export".
Push feature/csv-export to origin, then create a draft pull request targeting
main. Describe the behavior change and the tests run.
```

Creating a pull request does not itself push the branch. Specify both actions when you want both. The agent's available operations and any approval prompts still apply to your request.

Ordinary Git and GitHub writes share a repository-scoped grant. Prompts can offer **Approve once**, **Allow repository writes for this session**, or **Reject**. Review the scope before granting continuing access. Merging a pull request requires a separate confirmation of its exact head, even when ordinary writes have been approved.

## Handle command failures

Git hooks and configured commit signing remain enabled. If a commit fails, read the reported cause and correct it before retrying. An unrecognized command option can require exact approval instead of inheriting the permission for a simpler command.

Use [parallel workspaces](parallel-workspaces.md) for independent branches and [permissions](../customization/permissions.md) to review or revoke grants. The [tool reference](../reference/tools.md) explains managed command execution and its boundaries.
