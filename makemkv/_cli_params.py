from __future__ import annotations

from gettext import gettext
from pathlib import Path
from typing import Any, Callable, NamedTuple, TypedDict, TypeVar

import click

F = TypeVar("F", bound=Callable[..., Any])


class _OptionInfo(NamedTuple):
    text: str
    commands: list[str]


class HelpfulGroup(click.Group):
    def format_options(
        self, ctx: click.Context, formatter: click.HelpFormatter
    ) -> None:
        all_opts: dict[str, _OptionInfo] = {}
        for name, cmd in self.commands.items():
            for _param in cmd.get_params(ctx):
                rv = _param.get_help_record(ctx)
                if rv is not None:
                    opt, text = rv
                    if opt in all_opts:
                        all_opts[opt].commands.append(name)
                    else:
                        all_opts[opt] = _OptionInfo(text=text, commands=[name])

        dl = [
            (opt, info.text)
            if len(info.commands) == len(self.commands)
            else (opt, f"{info.text} [Commands: {', '.join(info.commands)}]")
            for opt, info in all_opts.items()
        ]

        with formatter.section(gettext("Options")):
            formatter.write_dl(dl)

        self.format_commands(ctx, formatter)

    def format_usage(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        formatter.write_usage(ctx.command_path, "COMMAND [OPTIONS]")


INFO_PARAMS = [
    click.Option(
        ["-n", "--disc-nr"],
        default=0,
        type=click.INT,
        metavar="NR",
        help="Specify disc number. "
        "Alternatively you can specify an input with -i/--input. "
        "Defaults to 0.",
    ),
    click.Option(
        ["-i", "--input"],
        type=click.Path(exists=True, resolve_path=True, path_type=Path),
        metavar="PATH",
        help="Specify input, can be either a device, "
        "a .IFO file or a VIDEO_TS folder.",
    ),
    click.Option(
        ["-l", "--minlength"],
        type=click.INT,
        metavar="SECS",
        help="Specify minimum title length in seconds.",
    ),
    click.Option(
        ["-c", "--cache"],
        type=click.INT,
        metavar="MB",
        help="Specify size of read cache in megabytes.",
    ),
    click.Option(
        ["-f", "--info-file"],
        type=click.Path(
            dir_okay=False,
            writable=True,
            resolve_path=True,
            path_type=Path,
        ),
        metavar="FILE",
        help="Write disc info to file.",
    ),
    click.Option(
        ["-j", "--json"],
        is_flag=True,
        help="Show disc info in JSON format.",
    ),
    click.Option(
        ["-v", "--verbose"],
        is_flag=True,
        help="Show more detailed logs.",
    ),
    click.Option(
        ["-q", "--quiet"],
        is_flag=True,
        help="Don't show logs.",
    ),
    click.Option(
        ["--no-bar"],
        is_flag=True,
        help="Don't show progress bars.",
    ),
    click.Option(
        ["--no-info"],
        is_flag=True,
        help="Don't show disc info.",
    ),
]

_output_param = click.Option(
    ["-o", "--output"],
    default=Path.cwd(),
    type=click.Path(
        exists=True,
        file_okay=False,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
    metavar="DIR",
    help="Specify output directory for created mkv files. "
    "Defaults to current directory.",
)

_title_param = click.Option(
    ["-t", "--title"],
    default="0",
    type=click.STRING,
    metavar="NR",
    help="Select title to be ripped, can be either "
    'an integer starting with 0 or the keyword "all". '
    "Defaults to 0.",
)
_decrypt_param = click.Option(
    ["-d", "--decrypt"],
    is_flag=True,
    help="Decrypt stream files during backup.",
)

MKV_PARAMS = INFO_PARAMS + [_title_param, _output_param]
BACKUP_PARAMS = INFO_PARAMS + [_output_param, _decrypt_param]


def add_params(params: list[click.Option]) -> Callable[[F], F]:
    def _add_params(func: F) -> F:
        params.reverse()
        func.__click_params__ = params  # type: ignore[attr-defined]
        return func

    return _add_params


class InfoCliParams(TypedDict):
    disc_nr: int
    input: Path | None
    minlength: int | None
    cache: int | None
    info_file: Path | None
    json: bool
    no_info: bool
    verbose: bool
    quiet: bool
    no_bar: bool


class MKVCliParams(InfoCliParams):
    output: Path
    title: str


class BackupCliParams(InfoCliParams):
    output: Path
    decrypt: bool
