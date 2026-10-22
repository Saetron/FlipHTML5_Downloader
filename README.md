# FlipHTML5 Downloader

Download FlipHTML5 Flipbooks as a CBZ (Comic Book Zip) file directly in your browser — zero installation or server required!

## Try it Online

👉 **[Launch FlipHTML5 Downloader Web App](https://saetron.github.io/FlipHTML5_Downloader/)**

---

## Features

- **100% Client-Side**: All downloading, page validation, and archive generation happen entirely within your browser.
- **Zero Dependencies/Installation**: No Python, command line, or runtime installations needed.
- **Automatic Book Naming**: Fetches book title from FlipHTML5 metadata to name the output `.cbz` file automatically.
- **Smart Validation**: Validates JPEG magic bytes (`0xff 0xd8`) to ensure only actual page images are bundled.
- **Responsive Dark UI**: Clean, Material-inspired dark theme designed for mobile and desktop screens.
- **Standard CBZ Output**: Generates `.cbz` archives compatible with all standard comic and ebook readers.

---

## How to Use

1. Visit the [web application](https://saetron.github.io/FlipHTML5_Downloader/).
2. Paste any public FlipHTML5 book link (e.g., `https://online.fliphtml5.com/abcd/efgh/index.html`).
3. Click **Download as CBZ**.
4. The tool downloads pages sequentially and automatically triggers a download of the finished `.cbz` file once complete.

---

## Running Locally

To run the web app locally on your machine:

```bash
# Clone the repository
git clone https://github.com/Saetron/FlipHTML5_Downloader.git
cd FlipHTML5_Downloader

# Start a local static file server
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your web browser.

---

## Notes & Limitations

- **Public Books Only**: Flipbooks must be publicly accessible.
- **Sequential Termination**: The downloader stops when it encounters the first missing page or non-JPEG response.
- **CORS Requirements**: Browsers must have network access to `online.fliphtml5.com`.

---

## License

This project is licensed under the [European Union Public Licence (EUPL-1.2)](LICENSE).
