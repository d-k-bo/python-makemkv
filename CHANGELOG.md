# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> :warning: Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.

## [unreleased]

## [0.3.0]

### Added

- Basic test suite for known and accepted parts of makemkv log

### Changed

- Split parsing logic into separate internal method (by [@slick-nick-90](https://github.com/slick-nick-90))
- Extend parser and fix common parsing issues (by [@slick-nick-90](https://github.com/slick-nick-90))
  - Added: `codec_id`, `codec_short`, `codec_long`, `source_filename`, `segments_count`, `segments_map`, `metadata_langcode`, `metadata_language`, `volume_name`, `comment`
  - Changed: `framerate` accepts floating point values
  - Removed: `codec`

### Fixed

- `video_angle` is now a key in the `Title` dictionary (instead of `Stream`)

## [0.2.2]

### Changed

- Windows: find `makemkvcon.exe` if it's installed at its default location
- CLI: Hide exception traceback

## [0.2.1]

### Added

- CLI: except `MakeMKVError` and raise `click.Abort`

## [0.2.0]

### Added

- Support for static type checking
  - Disc info is now structured using TypedDicts
- Better error detection
- Use [black](https://github.com/psf/black),
  [isort](https://github.com/PyCQA/isort),
  [flakeheaven](https://github.com/flakeheaven/flakeheaven),
  [flake8-annotations](https://github.com/sco1/flake8-annotations),
  [flake8-docstrings](https://github.com/PyCQA/flake8-docstrings) and
  [mypy](https://github.com/python/mypy) to enforce code style and quality

### Changed

- Lots of refactoring
- Move main module to `makemkv/makemkv.py`
- Messages of `makemkvcon` are now logged by a child logger
- Improved output reliability for `pymakemkv`
- Use [flit](https://github.com/pypa/flit) for packaging
- Use `pyproject.toml` for packaging and tool configuration
- [click](https://github.com/pallets/click) and
  [rich](https://github.com/Textualize/rich) are now optional dependencies,
  use `pip install makemkv[cli]` to install them
- Use markdown and [mkdocs](https://github.com/mkdocs/mkdocs) for documentation

### Removed

- `MakeMKV.f()` / universal firmware tool support

[unreleased]: https://github.com/d-k-bo/python-makemkv/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/d-k-bo/python-makemkv/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/d-k-bo/python-makemkv/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/d-k-bo/python-makemkv/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/d-k-bo/python-makemkv/releases/tag/v0.2.0
