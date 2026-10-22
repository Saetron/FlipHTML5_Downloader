# FlipHTML5 Downloader

Download public FlipHTML5 books directly in your browser as Comic Book Zip (`.cbz`) files — 100% client-side, zero installations or servers required.

## Try it Online

👉 **[Launch FlipHTML5 Downloader Web App](https://saetron.github.io/FlipHTML5_Downloader/)**

---

## Features

- **100% Client-Side**: All downloading, page decryption, and CBZ archive packaging occur directly inside your browser.
- **Modern Manifest & Encryption Support**: Seamlessly decrypts modern FlipHTML5 page manifests and hashed assets via the official WASM module (`deString`).
- **Multi-Format Image Detection**: Automatically detects and validates **WebP**, **JPEG**, and **PNG** images using binary magic bytes to prevent corrupted downloads.
- **Flexible URL Parsing**: Accepts FlipHTML5 URLs in any format — including direct book roots, `/index.html`, and `#p=1` page hash anchors.
- **Auto Book Naming**: Fetches book titles from HTML metadata and sanitizes them for clean `.cbz` archive naming.
- **Live Progress & Clean UI**: Real-time progress bar, status indicators, keyboard shortcuts (`Enter` to submit), and responsive dark/light adaptive theming.
- **Legacy Fallback**: Gracefully probes sequential page paths (`files/large/` and `files/page/`) for older flipbooks without manifests.

---

## How to Use

1. Open the **[Web App](https://saetron.github.io/FlipHTML5_Downloader/)**.
2. Paste any public FlipHTML5 book link (e.g. `https://online.fliphtml5.com/abcd/efgh/` or with `#p=1`).
3. Press **Enter** or click **Download CBZ**.
4. Watch the progress bar as pages are fetched and packaged into a `.cbz` file, which is saved automatically to your device.

---

## Running Locally

Serve `index.html` with any local static HTTP file server:

```bash
# Clone the repository
git clone https://github.com/Saetron/FlipHTML5_Downloader.git
cd FlipHTML5_Downloader

# Start a local static file server
python3 -m http.server 8000
```

Then navigate to `http://localhost:8000` in your web browser.

---

## Project Structure

```text
FlipHTML5_Downloader/
├── index.html       # Application controller & markup (HTML5, vanilla JS)
├── style.css        # Standalone CSS design system & adaptive theming
├── AGENTS.md        # Guidelines and architecture for automated agents
├── CHANGELOG.md     # Semantic version history (Keep a Changelog)
├── LICENSE          # European Union Public Licence (EUPL-1.2)
└── README.md        # User documentation
```

### Dependencies
- **[JSZip](https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js)**: In-memory `.cbz` archive generation.
- **[deString.js](https://static.fliphtml5.com/resourceFiles/html5_templates/js/deString.js)**: WebAssembly decryption module for modern FlipHTML5 manifests.

---

## Notes & Limitations

- **Public Books Only**: Flipbooks must be publicly accessible without requiring credentials.
- **CORS Requirements**: Browsers must have network access to `online.fliphtml5.com` and `static.fliphtml5.com`.

---

## License

This project is licensed under the [European Union Public Licence (EUPL-1.2)](LICENSE).
