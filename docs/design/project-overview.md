# Overview for Fountain View Hall

## Overview

Fountain View Hall wants a program that tracks event attendance and projected revenue
for multiple bookings.

<a id="program-requirements"></a>

### Program Requirements

- Repeatedly prompt for event name, guest count, and estimated revenue
- Continue until the user enters “done”
- Track total events processed
- Track total guests
- Track total projected revenue
- Calculate the average guests per event
- Determine the largest event

### Business Rules

- Pricing Rules
  - Large events receive a discount
- Operational Rules
  - Every booking must include a guest count
  - Booking total must be calculated before the discount is applied
  - Revenue totals should be tracked

---

## Planned Technology Usage

I intended to use various technologies throughout this project; some are very necessary, and others save time. Each technology will be categorized and described below:

### Editing/Developer Tools

- Git and GitHub as a VCS (version control system). <sup>[1](#git)</sup>
- [uv](https://docs.astral.sh/uv/) for package, project, and environment management.
- lefthook as a Git hook manager.
- pre-commit to run pre-commit scripts. <sup>[2](#scripts)</sup>
  - ruff for Python linting and formatting running as a pre-commit script.
- Sphinx to help build this beautiful documentation.
- pytest as a testing suite.
- Open Telemetry Protocol for observability and log management. <sup>[4](#otlp)</sup>

### Python Packages

- typer for command line interface completions and argument parsing.
- SQLite3 as a database <sup>[3](#sqlite)</sup>
- SQLAlchemy for object-relational mapping (ORM)

---

### Footnotes

* <a id='git'>**[1]**</a> Go to the [project repo](https://github.com/dwerkjem/lab4rev2) to see commit history.
* <a id='scripts'>**[2]**</a> All scripts (in the scripts directory) are written for Unix systems and use the bash language.
* <a id='sqlite'>**[3]**</a> See SQLite’s [home page](https://www.sqlite.org) for more details.
* <a id='otlp'>**[4]**</a> You can visit their [web page](https://opentelemetry.io) for more details, but essentially it is a web interface that helps you view logs and trends in data. Probably unnecessary, but I was eager to learn how to use this.
