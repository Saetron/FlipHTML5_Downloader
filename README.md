# FlipHTML5 Downloader

Downloads FlipHTML5 Flipbooks as a CBZ file.

## Try it Online

👉 **[Use FlipHTML5 Downloader in your browser](https://saetron.github.io/FlipHTML5_Downloader/)**

## Requirements

- Python 3.8 or newer
- [requests](https://pypi.org/project/requests/) library

## Installation

1. Clone or download this repository.
2. Install dependencies using pip:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script once to generate a `urls.txt` file:

    ```sh
    python download.py
    ```

2. Open `urls.txt` and add one FlipHTML5 URL per line (e.g., `https://online.fliphtml5.com/abcd/efgh/index.html`).

3. Run the script again:

    ```sh
    python download.py
    ```

4. The script will download each flipbook as a `.cbz` file into the `downloads/` folder. Finished URLs are tracked in `finished.txt`.

## Notes

- Only Public Flipbooks are supported.
