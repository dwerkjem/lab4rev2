# User Guide

This guide will walk you through `fvh-manager` and covers topics such as how to install and use fvh-manager.

## Installation

### Prerequisites

To verify you meet all prerequisites, run:

```bash
uv --version
```

Expected output:

```text
uv 0.x.x
```

Not:

```text
command not found: uv
```

#### IMPORTANT
Make sure the `uv` command runs before running the program.

If `uv --version` fails, use [this guide](https://docs.astral.sh/uv/#installation) to install uv.

### Activate Completion by Operating System and Shell

If desired, you can activate shell completions by running one of the following commands, depending on your operating system and shell:

| Operating system   | Shell      | Completion file                | Activation command                    |
|--------------------|------------|--------------------------------|---------------------------------------|
| Linux              | Bash       | `completions/fvh-manager.bash` | `source completions/fvh-manager.bash` |
| Linux              | Zsh        | `completions/_fvh-manager`     | `source completions/_fvh-manager`     |
| Linux              | Fish       | `completions/fvh-manager.fish` | `source completions/fvh-manager.fish` |
| macOS              | Bash       | `completions/fvh-manager.bash` | `source completions/fvh-manager.bash` |
| macOS              | Zsh        | `completions/_fvh-manager`     | `source completions/_fvh-manager`     |
| macOS              | Fish       | `completions/fvh-manager.fish` | `source completions/fvh-manager.fish` |
| Windows            | PowerShell | `completions/fvh-manager.ps1`  | `. .\completions\fvh-manager.ps1`     |
