"""
Name: Derek R. Neilson
Description: This is the entry point and should be left light by design.

Info on Type.
Typer is a command line interface (CLI) tool that will be used throughout this project.
It defines some decorators, ``@app.command`` see https://typer.tiangolo.com for details.
"""

from pathlib import Path

import typer
from sqlalchemy import create_engine


# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

app = typer.Typer()  # initializes typer

db_path = Path("database/data.db").absolute()


@app.command(
    help="Use the `in_memory` flag to make the data base only in memory no long term persistence"
)
def create_engine_command(in_memory: bool = False):
    if not in_memory:
        engine = create_engine(f"sqlite:///{db_path}")
    else:
        engine = create_engine("sqlite+pysqlite:///:memory:")
    return engine


if __name__ == "__main__":
    app()
