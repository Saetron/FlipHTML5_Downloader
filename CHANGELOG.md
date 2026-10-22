# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Support for modern FlipHTML5 books with encrypted page manifests using FlipHTML5's WASM-based `deString` decryption module.
- Multi-format image support: automatically detects and validates WebP (`RIFF....WEBP`), PNG, and JPEG formats via binary magic bytes.
- Dynamic path resolution across `files/large/`, `files/page/`, and `files/thumb/`.
- Download button state handling (disabled during active downloading to avoid redundant requests).

### Fixed
- Fixed downloading for modern FlipHTML5 books where pages are stored as hashed filenames or WebP images instead of sequential numbers.
- Improved URL parsing to handle trailing slashes, missing `index.html`, and hash fragments robustly.
- Decoded HTML entities in book titles before sanitizing CBZ archive names.

### Changed
- Streamlined repository configuration by removing pre-commit checks and workflows.
- Added and updated `AGENTS.md` guidelines for AI coding agents and automated contributors.
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
