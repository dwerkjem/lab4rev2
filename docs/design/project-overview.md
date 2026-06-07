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

## Planed Technology Usage

I planned on using various technologies throughout this project some are very necessary others save time. Each technology will be categorized and described below:

### Editing/Developer Tools

- Git and GitHub as a VCS (version control system). <sup>[1](#git)</sup>
- [uv](https://docs.astral.sh/uv/) for package, project, and environment management.
- lefthook as a Git hook manager.
- pre-commit to run pre-commit scripts. <sup>[2](#scripts)</sup>
  - ruff for Python linting and formatting running as a pre-commit script.
- Sphinx to help build this beautiful documentation.
- pytest as a testing suite.

### Python Packages

- typer for command line interface completions and argument parsing.
- SQLite as a database <sup>[3](#sqlite)</sup>
- SQLAlchemy for object relational mapping (ORM)

---

### Footnotes

* <a id='git'>**[1]**</a> Go to the [project repo](https://github.com/dwerkjem/lab4rev2) to see commit history.
* <a id='scripts'>**[2]**</a> All scripts (in scripts directory) are written for unix systems and use the bash language.
* <a id='sqlite'>**[3]**</a> See SQLite’s [home page](https://www.sqlite.org) for more details.
