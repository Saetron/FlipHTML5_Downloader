# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Streamlined repository configuration by removing pre-commit checks and workflows.
- Added `AGENTS.md` guidelines for AI coding agents and automated contributors.
- Updated documentation and project structure.

## [2.0.0] - 2026-10-22

### Added
- Complete client-side web application in `index.html` replacing the Python CLI downloader.
- In-browser CBZ generation using JSZip.
- Automatic extraction of the book title from HTML metadata for naming downloaded CBZ files.
- Support for URLs with page hash/anchor identifiers.
- JPEG magic byte validation (`0xff 0xd8`) to detect corrupt or non-image responses.
- Responsive, Material-inspired dark user interface optimized for mobile and desktop screens.
- GitHub Pages live deployment support.

### Changed
- Replaced backend Python script dependencies (`requests`, `beautifulsoup4`) with native browser `fetch` and client-side processing.
- Updated project license to European Union Public Licence (EUPL-1.2).

### Removed
- Python script `download.py` and `requirements.txt`.

## [1.0.0] - 2026-07-15

### Added
- Initial release with Python CLI downloader script (`download.py`).
- Download FlipHTML5 book pages sequentially.
- Packaging of downloaded images into CBZ archive format.
- Basic `.gitignore` and `README.md`.
