Plan for Fountain View Hall
===========================

Overview
--------

Fountain View Hall wants a program that tracks event attendance and projected revenue
for multiple bookings.

Requirements
~~~~~~~~~~~~

Program Requirements
********************

- Repeatedly prompt for event name, guest count, and estimated revenue
- Continue until the user enters "done"
- Track total events processed
- Track total guests
- Track total projected revenue
- Calculate the average guests per event
- Determine the largest event

Business Rules
**************

- Pricing Rules

  - Large events receive a discount

- Operational Rules

  - Every booking must include a guest count
  - Booking total must be calculated before the discount is applied
  - Revenue totals should be tracked

----

Planed Technology Usage
-----------------------

I planned on using various technologies throughout this project some are very necessary others save time. Each technology will be categorized and described below:

Editing/Developer Tools
~~~~~~~~~~~~~~~~~~~~~~~

Here is a non-exhaustive list of technology used:

- `Git` and `GitHub` as a VCS (version control system). [#git]_
- `uv <https://docs.astral.sh/uv/>`__ for package, project, and environment management.
- `lefthook` as a Git hook manager.
- `pre-commit` to run pre-commit scripts [#scripts]_



----

..  rubric:: Footnotes

..  [#git] Go to the `project repo <https://github.com/dwerkjem/lab4rev2>`_ to see commit history.
..  [#scripts] All scripts (in scripts directory) are written for unix systems and use the bash language.