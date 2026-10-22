# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2026-10-22

### Added
- Complete client-side web application in `index.html` replacing the Python CLI downloader.
- In-browser CBZ generation using JSZip.
- Dedicated standalone stylesheet [`style.css`](style.css) with modern design tokens, typography, and dark/light color-scheme support.
- Modernized user interface: clean header, subtle icons, active progress bar, dynamic status indicators, and keyboard shortcut support (Enter key to submit).
- Support for modern FlipHTML5 books with encrypted page manifests using FlipHTML5's WASM-based `deString` decryption module.
- Multi-format image support: automatically detects and validates WebP (`RIFF....WEBP`), PNG, and JPEG formats via binary magic bytes.
- Dynamic path resolution across `files/large/`, `files/page/`, and `files/thumb/`.
- Download button state handling (disabled during active downloading to avoid redundant requests).
- Automatic extraction of the book title from HTML metadata for naming downloaded CBZ files.
- Robust URL parsing supporting page hash/anchor identifiers, trailing slashes, and omitted `index.html`.
- Added `AGENTS.md` guidelines for AI coding agents and automated contributors.
- GitHub Pages live deployment support.

### Changed
- Replaced backend Python script dependencies (`requests`, `beautifulsoup4`) with native browser `fetch` and client-side processing.
- Refactored frontend styling out of inline `<style>` tags into `style.css`.
- Updated project license to European Union Public Licence (EUPL-1.2).
- Streamlined repository configuration by removing pre-commit checks and workflows.
- Updated documentation and project structure.

### Removed
- Python script `download.py` and `requirements.txt`.

## [1.0.0] - 2026-07-15

### Added
- Initial release with Python CLI downloader script (`download.py`).
- Download FlipHTML5 book pages sequentially.
- Packaging of downloaded images into CBZ archive format.
- Basic `.gitignore` and `README.md`.
