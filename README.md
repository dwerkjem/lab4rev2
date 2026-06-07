# Fountain View Hall

## Running Project

### Pre-run Install

#### Requirements

No GPUs, high-powered CPU, or even graphical interfaces are needed. It could be ran over SSH thanks to the lightweight TUI. 

* Python 3.13:
    * see [version](.python-version) and [requirements](requirements.txt)

* 200 MB of space

#### Using uv (recommended)

Follow the [uv install instructions](https://docs.astral.sh/uv/getting-started/installation/) and run:

```cmd
uv sync
```

run with:

```cmd
uv run fvh-manager
```

### Activate Completion by Operating System and Shell

if so desired you can activate completions in the program by running the one of the following depending on your OS:

| Operating system | Shell      | Completion file                | Activation command                    |
| ---------------- | ---------- | ------------------------------ | ------------------------------------- |
| Linux            | Bash       | `completions/fvh-manager.bash` | `source completions/fvh-manager.bash` |
| Linux            | Zsh        | `completions/_fvh-manager`     | `source completions/_fvh-manager`     |
| Linux            | Fish       | `completions/fvh-manager.fish` | `source completions/fvh-manager.fish` |
| macOS            | Bash       | `completions/fvh-manager.bash` | `source completions/fvh-manager.bash` |
| macOS            | Zsh        | `completions/_fvh-manager`     | `source completions/_fvh-manager`     |
| macOS            | Fish       | `completions/fvh-manager.fish` | `source completions/fvh-manager.fish` |
| Windows          | PowerShell | `completions/fvh-manager.ps1`  | `. .\completions\fvh-manager.ps1`     |

If you activate the completions you can use `fvh-manager` to run and `fvh-manager <TAB>` should complete

### Tests

I am using `pytest` to test most things run `uv run pytest` to launch the testing suite.

## Pseudocode
See [plan](docs/Plan.md) for details about the planing process 