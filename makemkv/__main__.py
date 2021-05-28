from __future__ import annotations
import json
import logging
from typing import Union

import click
from rich import print
from rich.logging import RichHandler
from rich.tree import Tree

from . import MakeMKV, logger
from ._cli_params import add_params
from .progress import ProgressParser

rich_handler = RichHandler(level=logging.INFO)
logging.basicConfig(
    format="%(message)s",
    handlers=[rich_handler],
    level=logging.NOTSET,
)
logger = logging.getLogger("rich")


@click.group()
@add_params(
    [
        "disc_nr",
        "input",
        "output",
        "title",
        "decrypt",
        "minlength",
        "cache",
        "info_file",
        "json",
        "verbose",
        "quiet",
        "no_bar",
        "no_info",
    ]
)
@click.pass_context
def cli(ctx: click.Context, **params):
    pass


@cli.command(name="info")
@add_params(
    [
        "disc_nr",
        "input",
        "minlength",
        "cache",
        "info_file",
        "json",
        "verbose",
        "quiet",
        "no_bar",
        "no_info",
    ]
)
@click.pass_context
def info(ctx: click.Context, **params):
    """Display information about a disc."""
    params = dict(ctx.parent.params, **params)
    with ProgressParser() as bar:
        makemkv_args, info_args = {}, {}
        input = params["input"] if params["input"] else params["disc_nr"]
        print(
            "input:",
            params["input"],
            "disc_nr:",
            params["disc_nr"],
            "result:",
            input,
        )
        if params["verbose"]:
            rich_handler.setLevel(logging.DEBUG)
        elif params["quiet"]:
            rich_handler.setLevel(logging.CRITICAL)
        if not params["no_bar"] and not params["quiet"]:
            makemkv_args.update({"progress_handler": bar.parse_progress})
        if params["cache"]:
            info_args.update({"cache": params["cache"]})
        if params["minlength"]:
            info_args.update({"minlength": params["minlength"]})
        makemkv = MakeMKV(input, **makemkv_args)
        try:
            disc_info = makemkv.info(**info_args)
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            return
    return_info(disc_info, params)


@cli.command(name="mkv")
@add_params(
    [
        "disc_nr",
        "input",
        "output",
        "title",
        "minlength",
        "cache",
        "info_file",
        "json",
        "verbose",
        "quiet",
        "no_bar",
        "no_info",
    ]
)
@click.pass_context
def mkv(ctx: click.Context, **params):
    """Copy titles from disc."""
    params = dict(ctx.parent.params, **params)
    with ProgressParser() as bar:
        makemkv_args, mkv_args = {}, {}
        input = params["input"] if params["input"] else params["disc_nr"]
        if params["verbose"]:
            logger.setLevel(logging.DEBUG)
        elif params["quiet"]:
            logger.setLevel(logging.CRITICAL)
        if not params["no_bar"] and not params["quiet"]:
            makemkv_args.update({"progress_handler": bar.parse_progress})
        if params["cache"]:
            mkv_args.update({"cache": params["cache"]})
        if params["minlength"]:
            mkv_args.update({"minlength": params["minlength"]})
        makemkv = MakeMKV(input, **makemkv_args)
        try:
            disc_info = makemkv.mkv(
                params["title"],
                params["output"],
                **mkv_args,
            )
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            return
    return_info(disc_info, params)


@cli.command(name="backup")
@add_params(
    [
        "disc_nr",
        "input",
        "output",
        "decrypt",
        "minlength",
        "cache",
        "info_file",
        "json",
        "verbose",
        "quiet",
        "no_bar",
        "no_info",
    ]
)
@click.pass_context
def backup(ctx: click.Context, **params):
    """Backup whole disc."""
    params = dict(ctx.parent.params, **params)
    with ProgressParser() as bar:
        makemkv_args, backup_args = {}, {}
        input = params["input"] if params["input"] else params["disc_nr"]
        if params["verbose"]:
            logger.setLevel(logging.DEBUG)
        elif params["quiet"]:
            logger.setLevel(logging.CRITICAL)
        if not params["no_bar"] and not params["quiet"]:
            makemkv_args.update({"progress_handler": bar.parse_progress})
        if params["cache"]:
            backup_args.update({"cache": params["cache"]})
        if params["minlength"]:
            backup_args.update({"minlength": params["minlength"]})
        if params["decrypt"]:
            backup_args.update({"decrypt": params["decrypt"]})
        makemkv = MakeMKV(input, **makemkv_args)
        try:
            disc_info = makemkv.backup(
                params["output"],
                **backup_args,
            )
        except KeyboardInterrupt:
            logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
            makemkv.kill()
            return
    return_info(disc_info, params)


@cli.command(name="f", context_settings={"ignore_unknown_options": True})
@add_params(
    [
        "info_file",
        "json",
        "verbose",
        "quiet",
        "no_bar",
        "no_info",
    ]
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def f(ctx: click.Context, args: tuple[str], **params):
    """Run universal firmware tool."""
    params = dict(ctx.parent.params, **params)
    makemkv = MakeMKV("")
    try:
        makemkv.f(*args)
    except KeyboardInterrupt:
        logger.warning("Received CTRL-C signal. Terminating makemkvcon.")
        makemkv.kill()
        return


def return_info(output: dict[str, Union[str, int, dict, list]], params: dict):
    if params["info_file"]:
        with open(params["info_file"], "w") as f:
            json.dump(output, f, indent=2, sort_keys=True)
    if params["json"]:
        print(json.dumps(output, indent=2, sort_keys=True))
    if params["no_info"]:
        pass
    else:
        print(DictTree("Disc Info", output))
        pass


class DictTree(Tree):
    """A tree renderable generated from a dict"""

    def __init__(
        self,
        label: str,
        data: dict[str, Union[str, int, dict, list]],
        sort_keys: bool = True,
        style: str = "tree",
        guide_style: str = "tree.line",
        expanded: bool = True,
        highlight: bool = True,
    ):
        self.config = {
            "style": style,
            "guide_style": guide_style,
            "expanded": expanded,
            "highlight": highlight,
        }
        super().__init__(label, **self.config)
        self.sort_keys = sort_keys
        self.walk_dict(data, self)

    def walk_dict(
        self,
        data: dict[str, Union[str, int, dict, list]],
        parent_tree: DictTree,
    ):
        if self.sort_keys:
            data = (
                (key, value)
                for key, value in sorted(data.items(), key=lambda x: x[0])
            )
        else:
            data = data.items()
        for key, value in data:
            key = key.replace("_", " ").capitalize()
            if isinstance(value, str):
                parent_tree.add(f"{key}: {value}", **self.config)
                continue
            if isinstance(value, int):
                parent_tree.add(f"{key}: {value}", **self.config)
                continue
            if isinstance(value, list):
                child_tree = parent_tree.add(key, **self.config)
                self.walk_list(value, child_tree, label=key[:-1])
                continue
            if isinstance(value, dict):
                child_tree = parent_tree.add(key, **self.config)
                self.walk_dict(value, child_tree)
                continue

    def walk_list(
        self,
        data: list[Union[str, int, dict, list]],
        parent_tree: DictTree,
        label: str = "",
    ):
        if self.sort_keys:
            try:
                data.sort()
            except TypeError:
                pass
        for i, value in enumerate(data):
            if isinstance(value, str):
                parent_tree.add(
                    f"{value.replace('_', ' ').capitalize()}", **self.config
                )
                continue
            if isinstance(value, int):
                parent_tree.add(f"{value}", **self.config)
                continue
            if isinstance(value, list):
                child_tree = parent_tree.add(
                    f"{label} {str(i + 1)}", **self.config
                )
                self.walk_list(value, child_tree)
                continue
            if isinstance(value, dict):
                child_tree = parent_tree.add(
                    f"{label} {str(i + 1)}", **self.config
                )
                self.walk_dict(value, child_tree)
                continue
