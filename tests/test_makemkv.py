from typing import Iterable

import pytest
from trycast import isassignable  # type: ignore[import]

from makemkv import MakeMKV, MakeMKVOutput
from makemkv.types import Disc, Drive, Stream, Title


class TestParser:
    parse = staticmethod(MakeMKV(0)._parse_makemkv_log)

    @pytest.mark.parametrize(
        argnames=["log", "expected_output"],
        argvalues=[
            (
                ['DRV:0,0,999,0,"Drive name","Disc name","/dev/sr0"'],
                MakeMKVOutput(
                    drives=[
                        Drive(
                            device_path="/dev/sr0",
                            disc_name="Disc name",
                            drive_name="Drive name",
                        )
                    ],
                    titles=[],
                ),
            ),
            (['DRV:1,256,999,0,"","",""'], MakeMKVOutput(drives=[], titles=[])),
        ],
    )
    def test_drv(self, log: Iterable[str], expected_output: MakeMKVOutput):
        output = self.parse(log)
        assert output == expected_output
        assert isassignable(output, MakeMKVOutput)

    @pytest.mark.parametrize(
        argnames=["log", "title_count"], argvalues=[(["TCOUNT:42"], 42)]
    )
    def test_tcount(self, log: Iterable[str], title_count: int):
        output = self.parse(log)
        expected_output = MakeMKVOutput(drives=[], titles=[], title_count=title_count)
        assert output == expected_output
        assert isassignable(output, MakeMKVOutput)

    @pytest.mark.parametrize(
        argnames=["log", "disc"],
        argvalues=[
            (['CINFO:1,6206,"DVD disc"'], Disc(type="DVD")),
            (['CINFO:1,6209,"Blu-ray disc"'], Disc(type="BD")),
            (['CINFO:1,6212,"HDDVD disc"'], Disc(type="HDDVD")),
            (['CINFO:1,6213,"MKV file"'], Disc(type="MKV")),
            (['CINFO:2,0,"Foo Bar"'], Disc(name="Foo Bar")),
            (['CINFO:28,0,"eng"'], Disc(metadata_langcode="en")),
            (['CINFO:29,0,"English"'], Disc(metadata_language="English")),
            (['CINFO:30,0,"Foo Bar"'], Disc(information="Foo Bar")),
            (['CINFO:32,0,"FOO_BAR"'], Disc(volume_name="FOO_BAR")),
            (
                ['CINFO:49,0,"BD-123456_FooBar_ABC1"'],
                Disc(comment="BD-123456_FooBar_ABC1"),
            ),
            (
                [
                    'CINFO:1,6209,"Blu-ray disc"',
                    'CINFO:2,0,"Foo Bar"',
                    'CINFO:28,0,"eng"',
                    'CINFO:29,0,"English"',
                    'CINFO:30,0,"Foo Bar"',
                    'CINFO:31,6119,"<b>Source information</b><br>"',
                    'CINFO:32,0,"FOO_BAR"',
                    'CINFO:33,0,"0"',
                    'CINFO:49,0,"BD-123456_FooBar_ABC1"',
                ],
                Disc(
                    comment="BD-123456_FooBar_ABC1",
                    information="Foo Bar",
                    metadata_langcode="en",
                    metadata_language="English",
                    name="Foo Bar",
                    type="BD",
                    volume_name="FOO_BAR",
                ),
            ),
        ],
    )
    def test_cinfo(self, log: Iterable[str], disc: Disc):
        output = self.parse(log)
        expected_output = MakeMKVOutput(drives=[], titles=[], disc=disc)
        assert output == expected_output
        assert isassignable(output, MakeMKVOutput)

    @pytest.mark.parametrize(
        argnames=["log", "title"],
        argvalues=[
            (['TINFO:0,2,0,"Foo Bar"'], Title(name="Foo Bar", streams=[])),
            (['TINFO:0,8,0,"42"'], Title(chapter_count=42, streams=[])),
            (['TINFO:0,9,0,"1:23:45"'], Title(length="1:23:45", streams=[])),
            (['TINFO:0,10,0,"12.3 MB"'], Title(size_human="12.3 MB", streams=[])),
            (['TINFO:0,11,0,"12300000"'], Title(size=12300000, streams=[])),
            (['TINFO:0,15,0,"1"'], Title(video_angle=1, streams=[])),
            (
                ['TINFO:0,16,0,"00001.mpls"'],
                Title(source_filename="00001.mpls", streams=[]),
            ),
            (['TINFO:0,24,0,"01"'], Title(original_title_id=1, streams=[])),
            (['TINFO:0,25,0,"1"'], Title(segments_count=1, streams=[])),
            (['TINFO:0,26,0,"123"'], Title(segments_map="123", streams=[])),
            (
                ['TINFO:0,26,0,"1,(2,4,6),11-22,23-44"'],
                Title(segments_map="1,(2,4,6),11-22,23-44", streams=[]),
            ),
            (
                ['TINFO:0,27,0,"title_t00.mkv"'],
                Title(file_output="title_t00.mkv", streams=[]),
            ),
            (['TINFO:0,28,0,"eng"'], Title(metadata_langcode="en", streams=[])),
            (
                ['TINFO:0,29,0,"English"'],
                Title(metadata_language="English", streams=[]),
            ),
            (
                ['TINFO:0,30,0,"Foo Bar - 42 chapter(s) , 12.3 MB"'],
                Title(information="Foo Bar - 42 chapter(s) , 12.3 MB", streams=[]),
            ),
            (
                ['TINFO:0,49,0,"Comment text"'],
                Title(comment="Comment text", streams=[]),
            ),
            (
                [
                    'TINFO:0,2,0,"Foo Bar"',
                    'TINFO:0,8,0,"42"',
                    'TINFO:0,9,0,"1:23:45"',
                    'TINFO:0,10,0,"12.3 MB"',
                    'TINFO:0,11,0,"12300000"',
                    'TINFO:0,16,0,"00001.mpls"',
                    'TINFO:0,25,0,"1"',
                    'TINFO:0,26,0,"123"',
                    'TINFO:0,27,0,"title_t00.mkv"',
                    'TINFO:0,28,0,"eng"',
                    'TINFO:0,29,0,"English"',
                    'TINFO:0,30,0,"Foo Bar - 42 chapter(s) , 12.3 MB"',
                    'TINFO:0,49,0,"Comment text"',
                ],
                Title(
                    chapter_count=42,
                    comment="Comment text",
                    file_output="title_t00.mkv",
                    information="Foo Bar - 42 chapter(s) , 12.3 MB",
                    length="1:23:45",
                    name="Foo Bar",
                    metadata_langcode="en",
                    metadata_language="English",
                    segments_count=1,
                    segments_map="123",
                    size=12300000,
                    size_human="12.3 MB",
                    source_filename="00001.mpls",
                    streams=[],
                ),
            ),
        ],
    )
    def test_tinfo(self, log: Iterable[str], title: Title):
        output = self.parse(log)
        expected_output = MakeMKVOutput(drives=[], titles=[title])
        assert output == expected_output
        assert isassignable(output, MakeMKVOutput)

    @pytest.mark.parametrize(
        argnames=["log", "stream"],
        argvalues=[
            (['SINFO:0,0,1,6201,"Video"'], Stream(type="video")),
            (['SINFO:0,0,1,6202,"Audio"'], Stream(type="audio")),
            (['SINFO:0,0,1,6203,"Subtitles"'], Stream(type="subtitles")),
            (['SINFO:0,0,2,0,"Surround 7.1"'], Stream(downmix="Surround 7.1")),
            (['SINFO:0,0,3,0,"eng"'], Stream(langcode="en")),
            (['SINFO:0,0,4,0,"English"'], Stream(language="English")),
            (['SINFO:0,0,5,0,"V_MPEG4/ISO/AVC"'], Stream(codec_id="V_MPEG4/ISO/AVC")),
            (['SINFO:0,0,6,0,"Mpeg4"'], Stream(codec_short="Mpeg4")),
            (
                ['SINFO:0,0,7,0,"Mpeg4 AVC High@L4.0"'],
                Stream(codec_long="Mpeg4 AVC High@L4.0"),
            ),
            (['SINFO:0,0,13,0,"128 Kb/s"'], Stream(bitrate="128 Kb/s")),
            (['SINFO:0,0,17,0,"48000"'], Stream(samplerate=48000)),
            (['SINFO:0,0,19,0,"1920x1080"'], Stream(dimensions="1920x1080")),
            (['SINFO:0,0,20,0,"16:9"'], Stream(aspect_ratio="16:9")),
            (['SINFO:0,0,21,0,"25"'], Stream(framerate=25)),
            (
                ['SINFO:0,0,21,0,"23.976 (120000/5005)"'],
                Stream(framerate=23.976),
            ),
            (
                ['SINFO:0,0,30,0,"TrueHD Surround 7.1 English"'],
                Stream(information="TrueHD Surround 7.1 English"),
            ),
        ],
    )
    def test_sinfo(self, log: Iterable[str], stream: Stream):
        output = self.parse(('TINFO:0,2,0,"Dummy title"', *log))
        expected_output = MakeMKVOutput(
            drives=[], titles=[Title(name="Dummy title", streams=[stream])]
        )
        assert output == expected_output
        assert isassignable(output, MakeMKVOutput)
