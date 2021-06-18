python-makemkv
==============

python-makemkv is a simple python wrapper for MakeMKV (written by GuinpinSoft inc.). While it can be imported as a module, it also offers a command-line interface that tries to be more intuitive than ``makemkvcon``.

Requirements
------------

python-makemkv requires Python 3.9 or later.

Additionally, a copy of MakeMKV is required, which can be downloaded from their `website <https://www.makemkv.com/>`_. You also need to ensure that ``makemkvcon`` can be run from the terminal, e. g. by adding its location to your PATH environment variable.

Installation
------------

python-makemkv can be installed using pip.

.. code:: bash

    pip install makemkv

Usage
-----

See full documentation on `Read the Docs <https://python-makemkv.readthedocs.io/en/latest/index.html>`_.

Python module
~~~~~~~~~~~~~~~~~~

To get information about discs, you need to instantiate a ``makemkv.MakeMKV`` object which provides its ``makemkv.MakeMKV.info()`` method.

.. code:: python

  from makemkv import MakeMKV

  makemkv = MakeMKV('/dev/sr0')
  disc_info = makemkv.info()
  print(disc_info)

To create a mkv file from the first title of the first disc you can use ``makemkv.MakeMKV.mkv()``.
Since this will take some time you can define a function that analyzes the program's progress or you can use the ``makemkv.ProgressParser`` class to show pretty progress bars.

.. code:: python

  from makemkv import MakeMKV, ProgressParser

  with ProgressParser() as progress:
      makemkv = MakeMKV(0, progress_handler=progress.parse_progress)
      makemkv.mkv(0, '~/Videos/Really Cool Movie (2021)')

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

.. code::

  Usage: pymakemkv [OPTIONS] COMMAND [ARGS]...

  Options:
    -n, --disc-nr NR      Specify disc number. Alternatively you can specify an
                          input with -i/--input. Defaults to 0.
  
    -i, --input PATH      Specify input, can be either a device, a .IFO file or
                          a VIDEO_TS folder.
  
    -o, --output DIR      Specify output directory for created mkv files.
                          Defaults to current directory.
  
    -t, --title NR        Select title to be ripped, can be either an integer
                          starting with 0 or the keyword "all". Defaults to 0.
  
    -d, --decrypt         Decrypt stream files during backup.
    -l, --minlength SECS  Specify minimum title length in seconds.
    -c, --cache MB        Specify size of read cache in megabytes.
    -f, --info-file FILE  Write disc info to file.
    -j, --json            show disc info in JSON format.
    -v, --verbose         Show more detailed logs.
    -q, --quiet           Don't show logs.
    --no-bar              Don't show progress bars.
    --no-info             Dont' show disc info.
    --help                Show this message and exit.
  
  Commands:
    backup  Backup whole disc.
    f       Run universal firmware tool.
    info    Display information about a disc.
    mkv     Copy titles from disc.