# python-makemkv

[![PyPI](https://img.shields.io/pypi/v/makemkv.svg?logo=pypi)](https://pypi.python.org/pypi/makemkv)
[![Python](https://img.shields.io/pypi/pyversions/makemkv.svg?logo=python)](https://pypi.python.org/pypi/makemkv)
[![License](https://img.shields.io/pypi/l/makemkv.svg)](https://pypi.python.org/pypi/makemkv)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![CI](https://github.com/d-k-bo/python-makemkv/actions/workflows/ci.yml/badge.svg)](https://github.com/d-k-bo/python-makemkv/actions/workflows/ci.yml)
[![Codecov](https://img.shields.io/codecov/c/github/d-k-bo/python-makemkv)](https://app.codecov.io/gh/d-k-bo/python-makemkv)

python-makemkv is a simple python wrapper for [MakeMKV](https://www.makemkv.com/) (written by
GuinpinSoft inc.). While it can be imported as a module, it also offers
a command-line interface that tries to be more intuitive than
`makemkvcon`.

## Requirements

python-makemkv requires Python 3.9 or later.

Additionally, a copy of MakeMKV is required, which can be downloaded
from their [website](https://www.makemkv.com/). If MakeMKV isn't installed at the default location, you also need to ensure
that `makemkvcon` can be run from the terminal, e. g. by adding its
location to your PATH environment variable.

## Installation

python-makemkv can be installed using pip.

```
pip install makemkv
```

If you want to use the CLI, you need to install it with

```
pip install makemkv[cli]
```

or install [click](https://github.com/pallets/click) and [rich](https://github.com/Textualize/rich) manually.

## Usage

See full documentation on [Read the
Docs](https://python-makemkv.readthedocs.io/en/latest/index.html).

To get information about discs, you need to instantiate a
`makemkv.MakeMKV` object which provides its `makemkv.MakeMKV.info()`
method.

```python
from pprint import pp
from makemkv import MakeMKV

makemkv = MakeMKV('/dev/sr0')
disc_info = makemkv.info()
pp(disc_info)

```

To create a mkv file from the first title of the first disc you can use
`makemkv.MakeMKV.mkv()`. Since this will take some time you can define a
function that analyzes the program\'s progress or you can use the
`makemkv.ProgressParser` class to show pretty progress bars
(this requires [rich](https://github.com/Textualize/rich) to be installed).

```python
from makemkv import MakeMKV, ProgressParser

with ProgressParser() as progress:
    makemkv = MakeMKV(0, progress_handler=progress.parse_progress)
    makemkv.mkv(0, '~/Videos/Really Cool Movie (2021)')
```

python-makemkv uses the `logging` module from Python's standard library,
see [Logging HOWTO](https://docs.python.org/3/howto/logging.html) to change
the output format or verbosity. To change the verbosity of specific
messages, you can modify the `makemkv.output_codes.MESSAGE_CODES`
dictionary accordingly. If you think that the log level of a specific
message isn't appropriate for most users, feel free to open an issue or a
pull request.

## Command-line interface

```
Usage: pymakemkv COMMAND [OPTIONS]

Options:
  -n, --disc-nr NR      Specify disc number. Alternatively you can specify an
                        input with -i/--input. Defaults to 0.
  -i, --input PATH      Specify input, can be either a device, a .IFO file or
                        a VIDEO_TS folder.
  -l, --minlength SECS  Specify minimum title length in seconds.
  -c, --cache MB        Specify size of read cache in megabytes.
  -f, --info-file FILE  Write disc info to file.
  -j, --json            Show disc info in JSON format.
  -v, --verbose         Show more detailed logs.
  -q, --quiet           Don't show logs.
  --no-bar              Don't show progress bars.
  --no-info             Don't show disc info.
  --help                Show this message and exit.
  -t, --title NR        Select title to be ripped, can be either an integer
                        starting with 0 or the keyword "all". Defaults to 0.
                        [Commands: mkv]
  -o, --output DIR      Specify output directory for created mkv files.
                        Defaults to current directory. [Commands: mkv, backup]
  -d, --decrypt         Decrypt stream files during backup. [Commands: backup]

Commands:
  backup  Backup whole disc.
  info    Display information about a disc.
  mkv     Copy titles from disc.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please use [nox](https://nox.thea.codes/en/stable/tutorial.html) to format, lint, type-check and test your code by calling `nox` in your project directory.

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for more information.
