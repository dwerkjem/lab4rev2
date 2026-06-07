# User Guide

This guide will walk you through `fvh-manager` and covers topics such as how to install and use fvh-manager.

## Installation

<a id="prerequisites"></a>

### User Prerequisites

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

### Minimal Getting Started

Make sure you run these commands from the project directory

Run this once:

```bash
uv sync
```

Then run this to start on every subsequent run:

```bash
uv run fvh-manager
```

### Activate Completion by Operating System and Shell

If desired, you can activate shell completions by running one of the following commands, depending on your operating system and shell:

| Operating system   | Shell      | Activation command                    |
|--------------------|------------|---------------------------------------|
| Linux/macOS        | Bash       | `source completions/fvh-manager.bash` |
| Linux/macOS        | Zsh        | `source completions/_fvh-manager`     |
| Linux/macOS        | Fish       | `source completions/fvh-manager.fish` |
| Windows            | PowerShell | `. .\completions\fvh-manager.ps1`     |

Once shell completions are activated, make sure your virtual environment is active. You can then run the program with:

```bash
fvh-manager
```

To view available completions, type:

```bash
fvh-manager <tab>
```

## Developer Installation

Meet all previous [prerequisites](#prerequisites) and additional ones as specified bellow.

Install developer dependencies:

```bash
uv sync --all-groups
```

Verify that `pdflatex` is installed:

```bash
pdflatex -v
```

Verify that `git` is installed:

```bash
git -v
```

Verify that `lefthook` is installed:

```bash
lefthook -v
```
