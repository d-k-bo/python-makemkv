from typing import Union
import click

_params = {
    "disc_nr": click.option(
        "-n",
        "--disc-nr",
        default=0,
        type=click.INT,
        metavar="NR",
        help="Specify disc number. "
        "Alternatively you can specify an input with -i/--input. "
        "Defaults to 0.",
    ),
    "input": click.option(
        "-i",
        "--input",
        type=click.Path(exists=True, resolve_path=True),
        metavar="PATH",
        help="Specify input, can be either a device, "
        "a .IFO file or a VIDEO_TS folder.",
    ),
    "output": click.option(
        "-o",
        "--output",
        default=".",
        type=click.Path(
            exists=True,
            file_okay=False,
            writable=True,
            resolve_path=True,
        ),
        metavar="DIR",
        help="Specify output directory for created mkv files. "
        "Defaults to current directory.",
    ),
    "title": click.option(
        "-t",
        "--title",
        default="0",
        type=click.STRING,
        metavar="NR",
        help="Select title to be ripped, can be either "
        'an integer starting with 0 or the keyword "all". '
        "Defaults to 0.",
    ),
    "decrypt": click.option(
        "-d",
        "--decrypt",
        is_flag=True,
        help="Decrypt stream files during backup.",
    ),
    "minlength": click.option(
        "-l",
        "--minlength",
        type=click.INT,
        metavar="SECS",
        help="Specify minimum title length in seconds.",
    ),
    "cache": click.option(
        "-c",
        "--cache",
        type=click.INT,
        metavar="MB",
        help="Specify size of read cache in megabytes.",
    ),
    "info_file": click.option(
        "-f",
        "--info-file",
        type=click.Path(dir_okay=False, writable=True, resolve_path=True),
        metavar="FILE",
        help="Write disc info to file.",
    ),
    "json": click.option(
        "-j",
        "--json",
        is_flag=True,
        help="show disc info in JSON format.",
    ),
    "no_info": click.option(
        "--no-info",
        is_flag=True,
        help="Dont' show disc info.",
    ),
    "verbose": click.option(
        "-v",
        "--verbose",
        is_flag=True,
        help="Show more detailed logs.",
    ),
    "quiet": click.option(
        "-q",
        "--quiet",
        is_flag=True,
        help="Don't show logs.",
    ),
    "no_bar": click.option(
        "--no-bar",
        is_flag=True,
        help="Don't show progress bars.",
    ),
}


def add_params(param_names: list[str]):
    def _add_params(
        func: Union[click.Group, click.Command]
    ) -> Union[click.Group, click.Command]:
        for param_name in reversed(param_names):
            param = _params[param_name]
            func = param(func)
        return func

    return _add_params
