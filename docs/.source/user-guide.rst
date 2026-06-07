User Guide
==========

This guide will walk you through ``fvh-manager`` and covers topics such as how to install and use fvh-manager.

Installation
------------

.. _prerequisites:

User Prerequisites
~~~~~~~~~~~~~~~~~~

To verify you meet all prerequisites, run:

.. code:: bash

    uv --version

Expected output:

.. code:: text

    uv 0.x.x

Not:

.. code:: text

    command not found: uv

.. important::

    Make sure the ``uv`` command runs before running the program.

If ``uv --version`` fails, use `this guide <https://docs.astral.sh/uv/#installation>`__ to install uv.

Minimal Getting Started
~~~~~~~~~~~~~~~~~~~~~~~

Make sure you run these commands from the project directory

Run this once:

.. code:: bash

    uv sync

Then run this to start on every subsequent run:

.. code:: bash

    uv run fvh-manager


Activate Completion by Operating System and Shell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If desired, you can activate shell completions by running one of the following commands, depending on your operating system and shell:

.. list-table::
    :header-rows: 1

    * - Operating system
      - Shell
      - Activation command
    * - Linux/macOS
      - Bash
      - ``source completions/fvh-manager.bash``
    * - Linux/macOS
      - Zsh
      - ``source completions/_fvh-manager``
    * - Linux/macOS
      - Fish
      - ``source completions/fvh-manager.fish``
    * - Windows
      - PowerShell
      - ``. .\completions\fvh-manager.ps1``

Once shell completions are activated, make sure your virtual environment is active. You can then run the program with: 

.. code:: bash 

  fvh-manager 
  
To view available completions, type: 

.. code:: bash

  fvh-manager <tab>

Developer Installation
----------------------

Meet all previous :ref:`prerequisites <prerequisites>` and additional ones as specified bellow.

Install developer dependencies for python:

.. code:: bash

    uv sync --all-groups

Verify that ``pdflatex`` is installed:

.. code:: bash

    pdflatex -v

Verify that ``git`` is installed:

.. code:: bash

    git -v

Verify that ``lefthook`` is installed:

.. code:: bash

    lefthook -v