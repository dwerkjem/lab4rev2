# References

Command-line entry point for the project.

* **author:**
  Derek R. Neilson

This module defines the project’s Typer application and should remain
lightweight by design.

Typer is a command-line interface (CLI) framework used throughout this project.
It provides decorators such as `typer.Typer.command()` for registering CLI
commands.

#### SEE ALSO
[Typer documentation](https://typer.tiangolo.com/)

### src.main.create_engine(in_memory)

Create a SQLite database engine.

Creates either an in-memory SQLite database or, by default, a persistent
database at `DB_PATH`, which points to `database/data.db`.

* **Parameters:**
  **in_memory** (`bool`) – If `True`, create an in-memory database. If `False`,
  create a persistent database at `DB_PATH`.
* **Returns:**
  A SQLAlchemy engine representing the configured database connection.
* **Return type:**
  `Engine`

The SQLAlchemy database URL has the general form:

```default
dialect[+driver]://user:password@host/dbname[?key=value...]
```

The default project database URL has the form:

```default
sqlite+pysqlite:///database/data.db
```

If `in_memory` is `True`, the database URL has the form:

```default
sqlite+pysqlite:///:memory:
```

#### SEE ALSO
[SQLAlchemy Engine documentation](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)
[Typer documentation](https://typer.tiangolo.com/)

### src.main.start_app(in_memory=False, metrics_port=8000)

* **Return type:**
  `None`
