# Agent Guidelines: FlipHTML5 Downloader

This repository contains **FlipHTML5 Downloader**, a client-side web application that downloads public FlipHTML5 books directly in the browser and packages them into Comic Book Zip (`.cbz`) files.

## Architecture & Project Structure

- **`index.html`**: The frontend markup and application controller (HTML5, vanilla JavaScript).
- **`style.css`**: Standalone stylesheet containing CSS design tokens, responsive layout, animations, and dark/light color-scheme theming.
  - External Dependencies:
    - [JSZip](https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js) loaded via CDN for generating `.cbz` archive in-memory.
    - [deString.js](https://static.fliphtml5.com/resourceFiles/html5_templates/js/deString.js) WebAssembly module loaded for decrypting modern FlipHTML5 book page manifests.
  - No build toolchain, bundler, or transpiler required.
- **`README.md`**: User-facing documentation and usage guide.
- **`CHANGELOG.md`**: Version history and log of changes.
- **`LICENSE`**: European Union Public Licence (EUPL-1.2).

## Core Application Logic

1. **URL Parsing & Normalization**:
   - Accepts FlipHTML5 URLs in multiple formats (`https://online.fliphtml5.com/<base>/<book>/`, `/index.html`, `#p=1`, etc.).
   - Extracts `<base>` and `<book>` identifiers to derive the book root path.
2. **Title Extraction**:
   - Fetches the book's `index.html` to extract the `<title>` element.
   - Decodes HTML entities and cleans illegal filename characters (`[\\/:*?"<>|]`) to name the `.cbz` archive.
3. **Page Discovery & Decryption**:
   - Fetches `javascript/config.js` to inspect `htmlConfig`.
   - If modern encrypted `fliphtml5_pages` manifest is present, decrypts it using the WASM `deString` module (`Module._DeString`).
   - Resolves page image paths (`files/large/`, `files/page/`, etc.).
   - Falls back gracefully to sequential probing (`files/large/` and `files/page/`) for legacy books without manifests.
4. **Image Fetching & Multi-Format Validation**:
   - Magic bytes check: validates binary file headers for JPEG (`0xff 0xd8`), PNG (`0x89 0x50 0x4e 0x47`), and WebP (`RIFF....WEBP`).
   - Rejects non-image error pages (404s, HTML error bodies).
5. **CBZ Packaging & Saving**:
   - Formats filenames zero-padded with detected image extension (e.g., `001.webp`, `001.jpg`).
   - Packages into a zip blob with MIME type `application/octet-stream`.
   - Generates an object URL and triggers native browser file download.

## Development & Testing Workflow

- **No compilation step**: Serve `index.html` directly using any local HTTP static file server:
  ```bash
  python3 -m http.server 8000
  ```
  Then navigate to `http://localhost:8000`.
- **Browser Compatibility**: Target modern standards-compliant browsers with support for `fetch`, async/await, and `Uint8Array`.
- **Pre-commit / CI**: Pre-commit hooks are intentionally omitted; maintain clean and consistent formatting directly in code.

## Coding Conventions & Mandates

- **Mandatory Changelog Updates**: Any meaningful code or structural change **MUST** be documented in [CHANGELOG.md](file:///Users/jbudz/Documents/FlipHTML/CHANGELOG.md) under the `[Unreleased]` section following the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`).
- Keep the application self-contained, light, and dependency-minimal. Avoid heavy UI frameworks or unnecessary NPM dependencies unless requested.
- Maintain responsive, accessible CSS supporting both desktop and mobile viewports.
- Keep UI feedback clear with accurate status updates in `#status`.
- Validate binary responses before archiving to avoid corrupted CBZ files.
