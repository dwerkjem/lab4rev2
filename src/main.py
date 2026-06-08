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
from typing import Annotated

import typer
import sqlalchemy as sqla
from prometheus_client import Counter, start_http_server

APP_RUNS_TOTAL = Counter("app_runs_total", "Amount of times the project was ran.")

app = typer.Typer()

DB_PATH: Path = Path("database/data.db").absolute()


def create_engine(in_memory: bool) -> sqla.engine.Engine:
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
        engine = sqla.create_engine(f"sqlite+pysqlite:///{DB_PATH}")
    else:
        engine = sqla.create_engine("sqlite+pysqlite:///:memory:")

    return engine


InMemoryOption = Annotated[
    bool,
    typer.Option(help="Whether to start with database in memory or not."),
]

MetricsPortOption = Annotated[
    int,
    typer.Option(help="Port to expose Prometheus metrics on."),
]


@app.command()
def start_app(
    in_memory: InMemoryOption = False,
    metrics_port: MetricsPortOption = 8000,
) -> None:
    start_http_server(metrics_port)
    APP_RUNS_TOTAL.inc()
    create_engine(in_memory)


if __name__ == "__main__":
    app()
