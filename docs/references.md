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

### src.main.start_app(in_memory=False)

Start the CLI app.

* **Parameters:**
  **in_memory** (`bool`) – If `True`, use an in-memory SQLite database.
* **Return type:**
  `None`

<a id="module-src.observability"></a>

Sets up logging and metrics for the application.

* **author:**
  Derek R. Neilson
* **var logger:**
  Application logger configured for OpenTelemetry.
* **var meter:**
  OpenTelemetry meter used to create counters and histograms.

This module configures OpenTelemetry logging and metrics, then exposes
the `track_command` decorator for tracking CLI command execution.

### src.observability.configure_logging()

Configures and returns the app logger.

* **Return type:**
  `Logger`

### src.observability.configure_metrics()

Configures the metrics

### src.observability.track_command(command_name)

Track command execution with logs and metrics.

The wrapped function records the number of command runs, active operations,
errors, and command duration.

* **Parameters:**
  **command_name** (`str`) – Name of the command being tracked. Format not required but should be name-of-command
* **Return type:**
  `Callable`[[`TypeVar`(`F`, bound= `Callable`[`...`, `Any`])], `TypeVar`(`F`, bound= `Callable`[`...`, `Any`])]

### Example

```python
from src.observability import logger, track_command

@track_command("some-command")
def some_command():
    logger.info("Command executed")
```
