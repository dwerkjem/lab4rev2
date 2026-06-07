"""Command-line entry point for the project.

:author: Derek R. Neilson

This module defines the project's Typer application and should remain
lightweight by design.

Typer is a command-line interface (CLI) framework used throughout this project.
It provides decorators such as :meth:`typer.Typer.command` for registering CLI
commands.

See Also:
    `Typer documentation`_
"""

from pathlib import Path

import typer
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

app = typer.Typer()

DB_PATH = Path("database/data.db").absolute()


@app.command(
    help=(
        "Use the `in_memory` flag to create the database only in memory "
        "with no long-term persistence."
    )
)
def create_engine_command(in_memory: bool = False) -> Engine:
    """Create a SQLite database engine.

    Creates either an in-memory SQLite database or, by default, a persistent
    database at :data:`DB_PATH`, which points to ``database/data.db``.

    :param in_memory: If ``True``, create an in-memory database. If ``False``,
        create a persistent database at :data:`DB_PATH`.
    :type in_memory: bool
    :returns: A SQLAlchemy engine representing the configured database connection.
    :rtype: sqlalchemy.engine.Engine

    The SQLAlchemy database URL has the general form::

        dialect[+driver]://user:password@host/dbname[?key=value...]

    The default project database URL has the form::

        sqlite+pysqlite:///database/data.db

    If ``in_memory`` is ``True``, the database URL has the form::

        sqlite+pysqlite:///:memory:

    See Also:
        `SQLAlchemy Engine documentation`_
        `Typer documentation`_

    .. _SQLAlchemy Engine documentation:
       https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine

    .. _Typer documentation:
       https://typer.tiangolo.com/
    """
    if not in_memory:
        engine = create_engine(f"sqlite+pysqlite:///{DB_PATH}")
    else:
        engine = create_engine("sqlite+pysqlite:///:memory:")

    return engine


if __name__ == "__main__":
    app()
