# Command-line interface

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
