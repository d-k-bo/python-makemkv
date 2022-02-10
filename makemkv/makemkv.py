import logging
from pathlib import Path
import re
from subprocess import PIPE, STDOUT, Popen
from typing import Callable, Optional, Union

from iso639 import Lang

from .output_codes import KEY_CODES, MESSAGE_CODES, SPECIAL_VALUES
from .progress import ProgressParser

logger = logging.getLogger(__name__)
_split_msg_exp = re.compile(
    r'[A-Z]+(?=:)|(?<=,")[^"]*(?=")|(?!:)[^,"]+|(?<=,)(?=,)'
)


class MakeMKV:
    """Wrapper class for makemkvcon

    Args:
        input (pathlib.Path or int or str): Can be either a disc number
            starting with 0, a device, a .IFO file or a VIDEO_TS folder.
        cache (int or str, optional): Size of read cache in megabytes.
        minlength (int or str, optional): Minimum title length in
            seconds.
        progress_handler (Callable, optional): A callback function to parse
            progress updates. See :func:`makemkv.ProgressParser.parse_progress`
            for details.
    """

    def __init__(
        self,
        input: Union[int, str, Path],
        cache: Optional[Union[int, str]] = None,
        minlength: Optional[Union[int, str]] = None,
        progress_handler: Callable[[str, int, int], None] = lambda *a: None,
    ):
        self.input = self._parse_input(input)
        self.cache = cache
        self.minlength = minlength
        self.progress_handler: Callable[
            [str, int, int], None
        ] = progress_handler
        self.process: Optional[Popen] = None

    def info(
        self,
        cache: Optional[Union[int, str]] = None,
        minlength: Optional[Union[int, str]] = None,
    ) -> dict[str, Union[str, int, dict, list]]:
        """Display information about a disc.

        Args:
            cache (int or str, optional): Size of read cache in megabytes.
            minlength (int or str, optional): Minimum title length in seconds.

        Returns:
            dict: A dict containing detailed information about drives, discs,
            titles and streams.
        """

        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            "makemkvcon",
            "info",
            self.input,
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
        title: Union[int, str],
        output_dir: Union[str, Path],
        cache: Optional[Union[int, str]] = None,
        minlength: Optional[Union[int, str]] = None,
    ) -> dict[str, Union[str, int, dict, list]]:
        """Copy titles from disc.

        Args:
            title (int or str): Title to be ripped, can be either an integer
                starting with 0 or the keyword "all".
            output_dir (pathlib.Path or str): Output directory for created
                mkv files.
            cache (int or str, optional): Size of read cache in megabytes.
            minlength (int or str, optional): Minimum title length in seconds.

        Returns:
            dict: A dict containing some information about drives, discs,
            titles and streams.
        """

        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            "makemkvcon",
            "mkv",
            self.input,
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
        output_dir: Union[str, Path],
        cache: Optional[Union[int, str]] = None,
        minlength: Optional[Union[int, str]] = None,
        decrypt: bool = False,
    ) -> dict[str, Union[str, int, dict, list]]:
        """Backup whole disc.

        Args:
            output_dir (pathlib.Path or str): Output directory for created
                backup files.
            cache (int or str, optional): Size of read cache in megabytes.
            minlength (int or str, optional): Minimum title length in seconds.
            decrypt (bool, optional): Decrypt stream files during backup.

        Returns:
            dict: A dict containing some information about drives, discs,
            titles and streams.
        """

        cache = self.cache if cache is None else cache
        minlength = self.minlength if minlength is None else minlength
        cmd = [
            "makemkvcon",
            "backup",
            self.input,
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

    def f(self, *args) -> dict[str, Union[str, int, dict, list]]:
        """Run universal firmware tool.

        Args:
            args: Anything you want to append to the command.

        Returns:
            dict: A dict containing some information about drives, discs,
            titles and streams.
        """
        cmd = ["makemkvcon", "f", *args]

        return self._run(cmd)

    def kill(self) -> None:
        """Terminate the ``makemkvcon`` progress."""
        if self.process:
            self.process.kill()

    def _parse_input(self, input: Union[int, str, Path]) -> str:
        """Autodetect suitable input type and reformat it for makemkvcon."""
        if str(input).isdecimal():
            return f"disc:{input}"
        is_windows_drive = (
            re.match(r"[A-Z]:(?:\\|/)?$", str(input)) is not None
        )
        input = Path(input)

        def is_video_ts_folder(path: Path) -> bool:
            return (
                path.is_dir()
                and re.match(r"video[-_ ]?ts", path.name.lower()) is not None
            )

        if input.is_block_device() or is_windows_drive:
            return f"dev:{input}"
        if input.suffix.lower() == ".iso":
            return f"iso:{input}"
        if input.suffix.lower() == ".ifo":
            return f"file:{input.parent}"
        if not is_video_ts_folder(input):
            for path in input.iterdir():
                if is_video_ts_folder(path):
                    return f"file:{path}"
        return f"file:{input}"

    def _translate_codes(
        self, flag: str, id: int, value: str, code: Optional[int] = None
    ) -> dict[str, str]:
        """Translate makemkvcon's message ids and special codes
        to human readable strings"""
        key = KEY_CODES.get(id)
        if key:
            if flag == "SINFO":
                if id == 2:
                    # "downmix" seems to be more suitable
                    # for audiostreams than "name"
                    key = "downmix"
                elif id == 3:
                    # convert 3-letter language codes to 2-letter codes
                    value = Lang(value).pt1

            if code:
                value = SPECIAL_VALUES.get(code)
            elif value.isdecimal():
                value = int(value)
            else:
                value = value.strip()

            return {key: value}
        else:
            return {}

    def _run(self, cmd: list[str]) -> dict[str, Union[str, int, dict, list]]:
        """Run makemkvcon and parse its output."""
        try:
            p = Popen(cmd, stderr=STDOUT, stdout=PIPE, bufsize=1, text=True)
        except FileNotFoundError:
            logger.critical(
                "Couldn't find makemkvcon."
                "Make sure it is installed and in your PATH."
            )
            return {}
        self.progress = p
        logger.info('Running "%s"', " ".join(cmd))
        output: dict[str, Union[str, int, dict, list]] = {
            "drives": [],
            "title_count": None,
            "disc": {},
            "titles": [],
        }
        progress_title = ""
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

                code = int(msg_values[0])
                message = msg_values[3]

                loglevel = MESSAGE_CODES.get(code, 10)
                logger.log(loglevel, "%s (%s)", message, code)

            elif flag == "PRGT":
                # PRGT:code,id,name
                # code - unique message code
                # id - operation sub-id
                # name - name string

                code = int(msg_values[0])
                message = msg_values[2]

                loglevel = MESSAGE_CODES.get(code, 10)
                logger.log(loglevel, "%s (%s)", message, code)

            elif flag == "PRGC":
                # PRGC:code,id,name
                #   code - unique message code
                #   id - operation sub-id
                #   name - name string

                progress_title = msg_values[2]

            elif flag == "PRGV":
                # PRGV:current,total,max
                #   current - current progress value
                #   total - total progress value
                #   max - maximum possible value for a progress bar, constant

                current = int(msg_values[0])
                max = int(msg_values[2])

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

                _, _, _, _, drive_name, disc_name, device_path = msg_values

                if drive_name or disc_name or device_path:
                    drive = {}
                    if drive_name:
                        drive.update(
                            {
                                "drive_name": drive_name,
                            }
                        )
                    if disc_name:
                        drive.update(
                            {
                                "disc_name": disc_name,
                            }
                        )
                    if device_path:
                        drive.update(
                            {
                                "device_path": device_path,
                            }
                        )
                    output["drives"].append(drive)

            elif flag == "TCOUNT":
                # TCOUNT:count
                #   count - titles count

                count = int(msg_values[0])

                output.update({"title_count": count})

            elif flag == "CINFO":
                # CINFO:id,code,value
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value

                id = int(msg_values[0])
                code = int(msg_values[1])
                value = msg_values[2]

                output["disc"].update(
                    self._translate_codes(flag, id, value, code=code)
                )

            elif flag == "TINFO":
                # TINFO:disc_nr,title_nr,id,code,value (wrong documented)
                #   title_nr - title number
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value

                title_nr = int(msg_values[0])
                id = int(msg_values[1])
                code = int(msg_values[2])
                value = msg_values[3]

                if title_nr >= len(output["titles"]):
                    output["titles"].append({"streams": []})
                output["titles"][title_nr].update(
                    self._translate_codes(flag, id, value, code=code)
                )

            elif flag == "SINFO":
                # SINFO:disc_nr,title_nr,stream_nr,id,code,value
                # (wrong documented)
                #   title_nr - title number
                #   stream_nr - stream number
                #   id - attribute id, see AP_ItemAttributeId in apdefs.h
                #   code - message code if attribute value is a constant string
                #   value - attribute value

                title_nr = int(msg_values[0])
                stream_nr = int(msg_values[1])
                id = int(msg_values[2])
                code = int(msg_values[3])
                value = msg_values[4]

                if stream_nr >= len(output["titles"][title_nr]["streams"]):
                    output["titles"][title_nr]["streams"].append({})
                output["titles"][title_nr]["streams"][stream_nr].update(
                    self._translate_codes(flag, id, value, code=code)
                )
            else:
                # Usage Errors etc.

                logger.error(line.strip())

        p.wait()
        return output
