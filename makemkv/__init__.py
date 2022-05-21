"""python-makemkv is a simple python wrapper for MakeMKV."""

from .makemkv import MakeMKV, MakeMKVError
from .types import Disc, Drive, MakeMKVOutput, ProgressUpdateHandlerType, Stream, Title

__all__ = [
    "Disc",
    "Drive",
    "MakeMKV",
    "MakeMKVError",
    "MakeMKVOutput",
    "ProgressUpdateHandlerType",
    "Stream",
    "Title",
]

try:
    from .progress import ProgressParser  # noqa: F401
except ImportError:
    pass
else:
    __all__.extend(["ProgressParser"])
