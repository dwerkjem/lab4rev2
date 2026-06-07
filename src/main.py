"""
Name: Derek R. Neilson
Description: This is the entrypoint and should is left light by design.

Info on Type.
Typer is a command line interface (CLI) tool that will be used thought this project.
It defines some decorators `@app.command` see [Typer](https://typer.tiangolo.com) for details
"""

import typer

app = typer.Typer(help="")  # initializes typer


@app.command()
def main() -> None:
    pass


if __name__ == "__main__":
    app()
