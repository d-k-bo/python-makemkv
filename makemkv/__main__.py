from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, List, Mapping, TypedDict, Union, cast

try:
    import click
    from rich import print
    from rich.logging import RichHandler
    from rich.tree import Tree
except ImportError as exc:
    raise ImportError(
        "pymakemkv requires 'rich' and 'click' to be installed. You can "
        "install them with 'pip install rich click' or 'pip install makemkv[cli].'"
    ) from exc

from ._cli_params import (
    BACKUP_PARAMS,
    INFO_PARAMS,
    MKV_PARAMS,
    BackupCliParams,
    HelpfulGroup,
    InfoCliParams,
    MKVCliParams,
    add_params,
)
from .makemkv import MakeMKV, MakeMKVError
from .progress import ProgressParser
from .types import MakeMKVOutput, ProgressUpdateHandlerType


class MakeMKVArgs(TypedDict, total=False):
    input: int | Path
    progress_handler: ProgressUpdateHandlerType
    cache: int
    minlength: int


rich_handler = RichHandler(level=logging.INFO)
logging.basicConfig(
    format="%(message)s",
    handlers=[rich_handler],
    level=logging.NOTSET,
)
logger = logging.getLogger()


@click.group(cls=HelpfulGroup)
def cli() -> None:
    pass


@cli.command()
@add_params(INFO_PARAMS)
def info(**_params: Any) -> None:
    """Display information about a disc."""
    params = cast(InfoCliParams, _params)

    set_log_level(params)

    with ProgressParser() as bar:
        makemkv = MakeMKV(**extract_makemkv_args(params, bar))
        try:
            disc_info = makemkv.info()
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            raise
        except MakeMKVError:
            raise click.Abort from None
        except FileNotFoundError as exc:
            logger.critical(exc)
            raise click.Abort from None

    return_info(disc_info, params)


@cli.command()
@add_params(MKV_PARAMS)
def mkv(**_params: Any) -> None:
    """Copy titles from disc."""
    params = cast(MKVCliParams, _params)

    set_log_level(params)

    with ProgressParser() as bar:
        makemkv = MakeMKV(**extract_makemkv_args(params, bar))
        try:
            disc_info = makemkv.mkv(params["title"], params["output"])
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            raise
        except MakeMKVError:
            raise click.Abort from None
        except FileNotFoundError as exc:
            logger.critical(exc)
            raise click.Abort from None

    return_info(disc_info, params)


@cli.command()
@add_params(BACKUP_PARAMS)
def backup(**_params: Any) -> None:
    """Backup whole disc."""
    params = cast(BackupCliParams, _params)

    set_log_level(params)

    with ProgressParser() as bar:
        makemkv = MakeMKV(**extract_makemkv_args(params, bar))
        try:
            disc_info = makemkv.backup(params["output"], decrypt=params["decrypt"])
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            raise
        except MakeMKVError:
            raise click.Abort from None
        except FileNotFoundError as exc:
            logger.critical(exc)
            raise click.Abort from None

    return_info(disc_info, params)


def set_log_level(params: InfoCliParams) -> None:
    if params["verbose"]:
        logger.setLevel(logging.DEBUG)
    elif params["quiet"]:
        logger.setLevel(logging.CRITICAL)


def extract_makemkv_args(params: InfoCliParams, bar: ProgressParser) -> MakeMKVArgs:
    makemkv_args = MakeMKVArgs()
    input = makemkv_args["input"] = (
        params["input"] if params["input"] else params["disc_nr"]
    )
    logger.debug(
        f"input: {params['input']}, disc_nr: {params['disc_nr']} " f"-> {input}"
    )
    if not params["no_bar"] and not params["quiet"]:
        makemkv_args["progress_handler"] = bar.parse_progress
    if params["cache"]:
        makemkv_args["cache"] = params["cache"]
    if params["minlength"]:
        makemkv_args["minlength"] = params["minlength"]
    return makemkv_args


def return_info(output: MakeMKVOutput, params: InfoCliParams) -> None:
    if params["info_file"]:
        with open(params["info_file"], "w") as f:
            json.dump(output, f, indent=2, sort_keys=True)
    elif params["json"]:
        print(json.dumps(output, indent=2, sort_keys=True))
    elif params["no_info"]:
        pass
    else:
        print(MakeMKVOutputTree("Disc Info", output))
        pass


# see https://github.com/python/mypy/issues/731
NestedDictItem = Union[str, int, "NestedDict", List["NestedDictItem"]]  # type: ignore [misc] # noqa:E501
NestedDict = Mapping[str, NestedDictItem]  # type: ignore [misc]


class MakeMKVOutputTree:
    """A tree renderable generated from MakeMKVOutput."""

    def __init__(
        self,
        label: str,
        data: MakeMKVOutput,
    ) -> None:
        self.tree = Tree(
            label,
            style="tree",
            guide_style="tree.line",
            expanded=True,
            highlight=True,
        )
        self.walk_dict(cast(NestedDict, data), self.tree)

    def __rich__(self) -> Tree:
        return self.tree

    def add(
        self,
        label: str,
        parent_tree: Tree,
    ) -> Tree:
        return parent_tree.add(
            label,
            style="tree",
            guide_style="tree.line",
            expanded=True,
            highlight=True,
        )

    def walk_dict(
        self,
        data: NestedDict,
        parent_tree: Tree,
    ) -> None:
        data = {key: value for key, value in sorted(data.items(), key=lambda x: x[0])}
        for key, value in data.items():
            key = key.replace("_", " ").capitalize()
            if isinstance(value, str):
                parent_tree.add(f"{key}: {value}")
            elif isinstance(value, int):
                parent_tree.add(f"{key}: {value}")
            elif isinstance(value, list):
                child_tree = self.add(key, parent_tree)
                self.walk_list(value, child_tree, label=key[:-1])
            elif isinstance(value, dict):
                child_tree = self.add(key, parent_tree)
                self.walk_dict(value, child_tree)

    def walk_list(
        self,
        data: list[NestedDictItem],
        parent_tree: Tree,
        label: str = "",
    ) -> None:
        try:
            data.sort()  # pyright: reportGeneralTypeIssues=false
        except TypeError:
            pass
        for i, value in enumerate(data):
            if isinstance(value, str):
                parent_tree.add(f"{value.replace('_', ' ').capitalize()}")
            elif isinstance(value, int):
                parent_tree.add(f"{value}")
            elif isinstance(value, list):
                child_tree = self.add(f"{label} {str(i + 1)}", parent_tree)
                self.walk_list(value, child_tree)
            elif isinstance(value, dict):
                child_tree = self.add(f"{label} {str(i + 1)}", parent_tree)
                self.walk_dict(value, child_tree)
