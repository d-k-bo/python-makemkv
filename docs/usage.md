# Usage

To get information about discs, you need to instantiate a
[`makemkv.MakeMKV`][makemkv.MakeMKV] object which provides its [`info()`][makemkv.MakeMKV.info]
method.

```python
from makemkv import MakeMKV
from pprint import pp

makemkv = MakeMKV('/dev/sr0')
disc_info = makemkv.info()
pp(disc_info)
```

To create a mkv file from the first title of the first disc you can use
[`makemkv.MakeMKV.mkv()`][makemkv.MakeMKV.mkv]. Since this will take some
time you can define a function that analyzes the program\'s progress or you
can use the [`makemkv.ProgressParser`][makemkv.ProgressParser] class to show pretty progress bars
(this requires [rich](https://github.com/Textualize/rich) to be installed).

```python
from makemkv import MakeMKV, ProgressParser

with ProgressParser() as progress:
    makemkv = MakeMKV(0, progress_handler=progress.parse_progress)
    makemkv.mkv(0, '~/Videos/Really Cool Movie (2021)')
```

python-makemkv uses the [`logging`][logging] module from Python's standard library,
see [Logging HOWTO](https://docs.python.org/3/howto/logging.html) to change
the output format or verbosity. To change the verbosity of specific
messages, you can modify the [`makemkv.output_codes.MESSAGE_CODES`][message_codes]
dictionary accordingly. If you think that the log level of a specific
message isn't appropriate for most users, feel free to open an issue or a
pull request.
