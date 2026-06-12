# Fountain View Hall

## Install Requirements

No GPUs, high-powered CPU, or even graphical interfaces are needed. It could be ran over SSH thanks to the lightweight TUI. 

* Python 3.13:
    * see [version](.python-version) and [requirements](requirements.txt)

* 200 MB of space

Follow the [uv install instructions](https://docs.astral.sh/uv/getting-started/installation/) and run:

```cmd
uv sync
```

run with:

```cmd
uv run fvh
```

## Tests

I am using `pytest` to test most things run `uv run pytest` to launch the testing suite.

## Pseudocode

To view pseudocode go to the [pseudocode markdown](docs/Pseudocode.md) page