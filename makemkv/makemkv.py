"""Main module of python-makemkv that provides the `MakeMKV` class."""

from __future__ import annotations

import logging
import platform
import re
import shutil
from os import PathLike
from pathlib import Path, WindowsPath
from subprocess import PIPE, STDOUT, Popen
from typing import Any, Literal

from iso639 import Lang  # type: ignore [import]
from typing_extensions import TypedDict, get_args, get_origin, get_type_hints

from .output_codes import KEY_CODES, MESSAGE_CODES, SPECIAL_VALUES
from .types import Disc, Drive, MakeMKVOutput, ProgressUpdateHandlerType, Stream, Title

if platform.system() == "Windows":
    MAKEMKVCON_BINARIES = [
        "makemkvcon",
        str(WindowsPath("C:/Program Files/MakeMKV/makemkvcon.exe")),
        str(WindowsPath("C:/Program Files (x86)/MakeMKV/makemkvcon.exe")),
    ]
else:
    MAKEMKVCON_BINARIES = ["makemkvcon"]

logger = logging.getLogger(__package__)
makemkvcon_logger = logger.getChild("makemkvcon")
_split_msg_exp = re.compile(r'[A-Z]+(?=:)|(?<=,")[^"]*(?=")|(?!:)[^,"]+|(?<=,)(?=,)')


def _do_nothing(*args: Any, **kwargs: Any) -> None:
    return


class MakeMKV:
    """Wraps makemkvcon and exposes makemkvcon's commands as methods."""

    def __init__(
        self,
        input: int | str | PathLike[str],
        cache: int | str | None = None,
        minlength: int | str | None = None,
        progress_handler: ProgressUpdateHandlerType = _do_nothing,
    ) -> None:
        """Initialize MakeMKV with input.

        Args:
            input: Can be either a disc number starting with 0, a device,
                a .IFO file or a VIDEO_TS folder.
            cache: Size of read cache in megabytes.
            minlength: Minimum title length in seconds.
            progress_handler: A callback function to parse progress updates.
                See :func:`makemkv.ProgressParser.parse_progress`
                for an example.
        """
        self._input = self._parse_input(input)
        self.cache = cache
        self.minlength = minlength
        self.progress_handler = progress_handler
        self.process: Popen | None = None

    def info(
        self,
        cache: int | str | None = None,
        minlength: int | str | None = None,
    ) -> MakeMKVOutput:
        """Display information about a disc.

        Args:
            cache: Size of read cache in megabytes.
            minlength: Minimum title length in seconds.

        Returns:
            MakeMKVOutput: A dict containing some information about drives,
                discs, titles and streams.

        Raises:
            MakeMKVError: MakeMKV encountered a critical problem.
            FileNotFoundError: Couldn't find `makemkvcon`.
        """
        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            _find_makemkvcon_binary(),
            "info",
            self._input,
            "--robot",
            "--progress=-same",
            "--noscan",
        ]
        if cache:
            cmd.extend(["--cache", str(cache)])
        if minlength:
            cmd.extend(["--minlength", str(minlength)])

        return self._run(cmd)

    def mkv(
        self,
        title: int | str,
        output_dir: str | Path,
        cache: int | str | None = None,
        minlength: int | str | None = None,
    ) -> MakeMKVOutput:
        """Copy titles from disc.

        Args:
            title: Title to be ripped, can be either an integer starting
                with 0 or the keyword "all".
            output_dir: Output directory for created mkv files.
            cache: Size of read cache in megabytes.
            minlength: Minimum title length in seconds.

        Returns:
            MakeMKVOutput: A dict containing some information about drives,
                discs, titles and streams.

        Raises:
            MakeMKVError: MakeMKV encountered a critical problem.
            FileNotFoundError: Couldn't find `makemkvcon`.
        """
        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            _find_makemkvcon_binary(),
            "mkv",
            self._input,
            str(title),
            str(output_dir),
            "--robot",
            "--progress=-same",
            "--noscan",
        ]
        if cache:
            cmd.extend(["--cache", str(cache)])
        if minlength:
            cmd.extend(["--minlength", str(minlength)])

        return self._run(cmd)

    def backup(
        self,
        output_dir: str | Path,
        cache: int | str | None = None,
        minlength: int | str | None = None,
        decrypt: bool = False,
    ) -> MakeMKVOutput:
        """Backup whole disc.

        Args:
            output_dir: Output directory for created backup files.
            cache: Size of read cache in megabytes.
            minlength: Minimum title length in seconds.
            decrypt: Decrypt stream files during backup.

        Returns:
            MakeMKVOutput: A dict containing some information about drives,
                discs, titles and streams.

        Raises:
            MakeMKVError: MakeMKV encountered a critical problem.
            FileNotFoundError: Couldn't find `makemkvcon`.
        """
        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            _find_makemkvcon_binary(),
            "backup",
            self._input,
            str(output_dir),
            "--robot",
            "--progress=-same",
            "--noscan",
        ]
        if cache:
            cmd.extend(["--cache", str(cache)])
        if minlength:
            cmd.extend(["--minlength", str(minlength)])
        if decrypt:
            cmd.append("--decrypt")

        return self._run(cmd)

    def kill(self) -> None:
        """Terminate the `makemkvcon` progress."""
        if self.process:
            self.process.kill()

    def _parse_input(self, input: int | str | PathLike[str]) -> str:
        """Autodetect suitable input type and reformat it for makemkvcon."""
        if isinstance(input, int):
            return f"disc:{input}"

        input_path = Path(input)

        def is_video_ts_folder(path: Path) -> bool:
            return (
                path.is_dir()
                and re.match(r"video[-_ ]?ts", path.name.lower()) is not None
            )

        if (
            input_path.is_block_device()
            or isinstance(input_path, WindowsPath)
            and str(input_path) in (input_path.drive, input_path.anchor)
        ):
            return f"dev:{input_path}"
        if input_path.suffix.lower() == ".iso":
            return f"iso:{input_path}"
        if input_path.suffix.lower() == ".ifo":
            return f"file:{input_path.parent}"
        if not is_video_ts_folder(input_path):
            for path in input_path.iterdir():
                if is_video_ts_folder(path):
                    return f"file:{path}"
        return f"file:{input_path}"

    def _translate_codes(
        self, flag: str, id: int, value: str, code: int
    ) -> tuple[str, str | int]:
        """Translate makemkvcon's codes into something useful.

        Raises:
            KeyError: if `id` is unknown or irrelevant
        """
        return_value: int | str
        key = KEY_CODES[id]
        if flag == "SINFO":
            if id == 2:
                # "downmix" seems to be more suitable
                # for audiostreams than "name"
                key = "downmix"
            elif id == 3:
                # convert 3-letter language codes to 2-letter codes
                value = Lang(value).pt1

        if code:
            return_value = SPECIAL_VALUES.get(code, value)
        elif value.strip('"').isdecimal():
            return_value = int(value.strip('"'))
        else:
            return_value = value.strip()

        return key, return_value

    def _run(self, cmd: list[str]) -> MakeMKVOutput:
        """Run makemkvcon and parse its output."""
        p = self.process = Popen(cmd, stderr=STDOUT, stdout=PIPE, bufsize=1, text=True)
        logger.info('Running "%s"', " ".join(cmd))
        output = MakeMKVOutput(drives=[], titles=[])
        progress_title = ""
        assert p.stdout is not None
        for line in p.stdout:
            # flag, msg = line.strip().split(':', 1)
            # msg_values = _split_values_exp.findall(msg)
            # msg_values = [v.strip('"').strip() for v in msg_values]
            flag: str
            msg_values: list[str]
            flag, *msg_values = _split_msg_exp.findall(line.strip())

            if flag in "MSG":
                # MSG:code,flags,count,message,format,param0,param1,...
                #   code - unique message code, should be used to identify
                #          particular string in language-neutral way.
                #   flags - message flags, see AP_UIMSG_xxx flags in apdefs.h
                #   count - number of parameters
                #   message - raw message string suitable for output
                #   format - format string used for message. This string is
                #            localized and subject to change, unlike message
                #            code.
                #   paramX - parameter for message

                try:
                    code = int(msg_values[0])
                    message = msg_values[3]
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                loglevel = MESSAGE_CODES.get(code, 10)
                makemkvcon_logger.log(loglevel, "%s (%s)", message, code)

                if loglevel == logging.CRITICAL:
                    p.kill()
                    raise MakeMKVError(message)

            elif flag == "PRGT":
                # PRGT:code,id,name
                # code - unique message code
                # id - operation sub-id
                # name - name string

                try:
                    code = int(msg_values[0])
                    message = msg_values[2]
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                loglevel = MESSAGE_CODES.get(code, 10)
                makemkvcon_logger.log(loglevel, "%s (%s)", message, code)

            elif flag == "PRGC":
                # PRGC:code,id,name
                #   code - unique message code
                #   id - operation sub-id
                #   name - name string

                try:
                    progress_title = msg_values[2]
                except IndexError:
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

            elif flag == "PRGV":
                # PRGV:current,total,max
                #   current - current progress value
                #   total - total progress value
                #   max - maximum possible value for a progress bar, constant

                try:
                    current = int(msg_values[0])
                    max = int(msg_values[2])
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                self.progress_handler(progress_title, current, max)

            elif flag == "DRV":
                # DRV:index,visible,enabled,flags,drive name,disc name,
                # device path (wrong documented)
                #   index - drive index
                #   visible - set to 1 if drive is present
                #   enabled - set to 1 if drive is accessible
                #   flags - media flags, see AP_DskFsFlagXXX in apdefs.h
                #   drive name - drive name string
                #   disc name - disc name string
                #   device path - device path string (not documented)

                try:
                    _, _, _, _, drive_name, disc_name, device_path = msg_values
                except ValueError:
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                if drive_name or disc_name or device_path:
                    drive = Drive()
                    if drive_name:
                        drive["drive_name"] = drive_name
                    if disc_name:
                        drive["disc_name"] = disc_name
                    if device_path:
                        drive["device_path"] = device_path
                    output["drives"].append(drive)

            elif flag == "TCOUNT":
                # TCOUNT:count
                #   count - titles count
                try:
                    count = int(msg_values[0])
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                output["title_count"] = count

            elif flag == "CINFO":
                # CINFO:id,code,value
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value
                try:
                    id = int(msg_values[0])
                    code = int(msg_values[1])
                    value = msg_values[2]
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                if "disc" not in output:
                    output["disc"] = Disc()
                    assert "disc" in output

                try:
                    key, d_value = self._translate_codes(flag, id, value, code)
                except KeyError:
                    continue
                if not _is_valid_typeddict_item(Disc, key, d_value):
                    logger.error(f"Error while parsing '{line.strip()}'")
                    continue

                output["disc"][key] = d_value  # type: ignore[literal-required] # noqa:E501

            elif flag == "TINFO":
                # TINFO:disc_nr,title_nr,id,code,value (wrong documented)
                #   title_nr - title number
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value

                try:
                    title_nr = int(msg_values[0])
                    id = int(msg_values[1])
                    code = int(msg_values[2])
                    value = msg_values[3]
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                while title_nr >= len(output["titles"]):
                    output["titles"].append(Title(streams=[]))

                try:
                    key, d_value = self._translate_codes(flag, id, value, code)
                except KeyError:
                    continue

                if not _is_valid_typeddict_item(Title, key, d_value):
                    logger.error(f"Error while parsing '{line.strip()}'")
                    continue

                output["titles"][title_nr][key] = d_value  # type: ignore[literal-required] # noqa:E501

            elif flag == "SINFO":
                # SINFO:disc_nr,title_nr,stream_nr,id,code,value
                # (wrong documented)
                #   title_nr - title number
                #   stream_nr - stream number
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value

                try:
                    title_nr = int(msg_values[0])
                    stream_nr = int(msg_values[1])
                    id = int(msg_values[2])
                    code = int(msg_values[3])
                    value = msg_values[4]
                except (ValueError, IndexError):
                    logger.exception(f"Error while parsing '{line.strip()}'")
                    continue

                while stream_nr >= len(output["titles"][title_nr]["streams"]):
                    output["titles"][title_nr]["streams"].append(Stream())

                try:
                    key, d_value = self._translate_codes(flag, id, value, code)
                except KeyError:
                    continue

                if not _is_valid_typeddict_item(Stream, key, d_value):
                    logger.error(f"Error while parsing '{line.strip()}'")
                    continue

                output["titles"][title_nr]["streams"][stream_nr][key] = d_value  # type: ignore[literal-required] # noqa:E501
            else:
                logger.error(f"Error while parsing '{line.strip()}'")

        if (return_code := p.wait()) != 0:
            raise MakeMKVError(
                f"makemkvcon exited with non-zero return code {return_code}"
            )
        return output


def _is_valid_typeddict_item(
    td: type[TypedDict], key: str, value: Any  # type: ignore [valid-type]
) -> bool:
    """Check if `key` and `value` form a valid item for the TypedDict `td`."""
    annotations = get_type_hints(td)
    if key not in annotations:
        return False
    if get_origin(annotations[key]) is Literal:
        return value in get_args(annotations[key])
    return isinstance(value, annotations[key])


def _find_makemkvcon_binary() -> str:
    for bin_path in MAKEMKVCON_BINARIES:
        if shutil.which(bin_path) is not None:
            return bin_path
    else:
        raise FileNotFoundError(
            "Couldn't find makemkvcon. Make sure it is installed and in your PATH."
        )


class MakeMKVError(Exception):
    """Raised if MakeMKV encounters a critical problem."""
