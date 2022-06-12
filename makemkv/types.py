from typing import Literal, Protocol, Union

from typing_extensions import Required, TypedDict


class ProgressUpdateHandlerType(Protocol):
    """A callback function to parse progress updates.

    See :func:`makemkv.ProgressParser.parse_progress` for an example.
    """

    def __call__(  # noqa: D102
        self, task_description: str, progress: int, max: int
    ) -> None:
        ...  # pragma: no cover


class Drive(TypedDict, total=False):
    device_path: str
    disc_name: str
    drive_name: str


class Disc(TypedDict, total=False):
    comment: str
    information: str
    metadata_langcode: str  # two-letter ISO 639-1 code if it exists, eg. "en"
    metadata_language: str  # eg. "English"
    name: str
    type: Literal["DVD", "BD", "HDDVD", "MKV"]
    volume_name: str


class Stream(TypedDict, total=False):
    aspect_ratio: str  # eg. "16:9"
    bitrate: str  # eg. "384 Kb/s"
    codec_id: str  # eg. "V_MPEG2", "A_AC3", "S_VOBSUB"
    codec_long: str  # eg. "Mpeg4 AVC High@L4.1"
    codec_short: str  # eg. "Mpeg4"
    dimensions: str  # eg. "720x576",
    downmix: str  # eg. "Surround 5.1"
    framerate: Union[int, float]  # eg. 25 or 23.976
    information: str  # eg. "DD Surround 5.1 English"
    langcode: str  # two-letter ISO 639-1 code if it exists, eg. "en"
    language: str  # eg. "English"
    metadata_langcode: str  # two-letter ISO 639-1 code if it exists, eg. "en"
    metadata_language: str  # eg. "English"
    samplerate: int  # eg. 48000,
    type: Literal["video", "audio", "subtitles"]


class Title(TypedDict, total=False):
    chapter_count: int
    comment: str
    file_output: str  # eg. "title_t00.mkv"
    information: str
    length: str  # hh:mm:ss
    name: str  # eg. "title"
    metadata_langcode: str  # two-letter ISO 639-1 code if it exists, eg. "en"
    metadata_language: str  # eg. "English"
    original_title_id: int  # used on multi-angle discs, eg. 1
    segments_count: int  # eg. 5
    segments_map: str  # eg. "174,175,175,175,448" or "1,(2,4,6),11-22,23-44"
    source_filename: str  # eg. "00021.mpls"
    size_human: str  # eg. "5.9 GB"
    size: int  # bytes
    streams: Required[list[Stream]]
    video_angle: int  # eg. 1


class MakeMKVOutput(TypedDict, total=False):
    disc: Disc
    drives: Required[list[Drive]]
    title_count: int
    titles: Required[list[Title]]
