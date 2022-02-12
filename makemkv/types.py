from typing import Literal, Protocol

from typing_extensions import Required, TypedDict


class ProgressUpdateHandlerType(Protocol):
    """A callback function to parse progress updates.

    See :func:`makemkv.ProgressParser.parse_progress` for an example.
    """

    def __call__(  # noqa: D102
        self, task_description: str, progress: int, max: int
    ) -> None:
        ...


class Drive(TypedDict, total=False):
    device_path: str
    disc_name: str
    drive_name: str


class Disc(TypedDict, total=False):
    information: str
    name: str
    type: Literal["DVD", "BD", "HDDVD", "MKV"]


class Stream(TypedDict, total=False):
    aspect_ratio: str  # eg. "16:9"
    bitrate: str  # eg. "384 Kb/s"
    codec: str  # eg. "V_MPEG2", "A_AC3", "S_VOBSUB"
    dimensions: str  # eg. "720x576",
    downmix: str  # eg. "Surround 5.1"
    framerate: int  # eg. 25
    information: str  # eg. "DD Surround 5.1 English"
    langcode: str  # two-letter ISO 639-1 code if it exists, eg. "en"
    language: str  # eg. "English"
    samplerate: int  # eg. 48000,
    type: Literal["video", "audio", "subtitles"]
    video_angle: int  # eg. 1


class Title(TypedDict, total=False):
    chapter_count: int
    file_output: str  # eg. "title_t00.mkv"
    information: str
    length: str  # hh:mm:ss
    size_human: str  # eg. "5.9 GB"
    size: int  # bytes
    streams: Required[list[Stream]]


class MakeMKVOutput(TypedDict, total=False):
    disc: Disc
    drives: Required[list[Drive]]
    title_count: int
    titles: Required[list[Title]]
