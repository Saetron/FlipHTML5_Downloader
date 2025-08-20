import os
import re
import sys
import requests
import zipfile
from urllib.parse import urlparse

def get_flipbook_info(url):
    # Extract the base path and flipbook id from the URL
    m = re.match(r'https://online\.fliphtml5\.com/([^/]+)/([^/]+)/index\.html', url)
    if not m:
        print("Invalid FlipHTML5 URL format.")
        sys.exit(1)
    return m.group(1), m.group(2)

def get_max_page(url):
    # Try to fetch the index.html and guess the max page number
    resp = requests.get(url)
    if resp.status_code != 200:
        print("Failed to fetch flipbook index page.")
        sys.exit(1)
    # Look for page count in the HTML
    m = re.search(r'#p=(\d+)', url)
    if m:
        start_page = int(m.group(1))
    else:
        start_page = 1
    # Try to find the max page from the HTML
    pages = re.findall(r'#p=(\d+)', resp.text)
    if pages:
        max_page = max(map(int, pages))
    else:
        # Fallback: try up to 200 pages
        max_page = 200
    return start_page, max_page

def download_images(base_url, book_id, start_page, max_page, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    downloaded = []
    for page in range(start_page, max_page + 1):
        img_url = f"https://online.fliphtml5.com/{base_url}/{book_id}/files/page/{page}.jpg"
        img_path = os.path.join(out_dir, f"{page:03}.jpg")
        resp = requests.get(img_url)
        if resp.status_code == 200:
            with open(img_path, "wb") as f:
                f.write(resp.content)
            downloaded.append(img_path)
            print(f"Downloaded page {page}")
        else:
            print(f"Stopped at page {page} (image not found).")
            break
    return downloaded

def create_cbz(image_files, cbz_name):
    with zipfile.ZipFile(cbz_name, 'w') as cbz:
        for img in image_files:
            cbz.write(img, os.path.basename(img))
    print(f"CBZ file created: {cbz_name}")

def main():
    urls_file = "urls.txt"
    finished_file = "finished.txt"
    downloads_dir = "downloads"
    os.makedirs(downloads_dir, exist_ok=True)
    # Create urls.txt if it does not exist
    if not os.path.exists(urls_file):
        with open(urls_file, "w") as f:
            f.write("# Put one FlipHTML5 URL per line in this file.\n")
        print(f"{urls_file} created. Please add URLs to it and rerun the script.")
        sys.exit(1)
    # Read finished URLs
    finished = set()
    if os.path.exists(finished_file):
        with open(finished_file, "r") as f:
            finished = set(line.strip() for line in f if line.strip())
    # Read URLs to process
    with open(urls_file, "r") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    if not urls:
        print("No URLs found in urls.txt. Please add URLs and rerun the script.")
        sys.exit(1)
    for url in urls:
        if url in finished:
            print(f"Already finished: {url}")
            continue
        if not url.startswith("https://online.fliphtml5.com/"):
            print(f"Skipping invalid URL: {url}")
            continue
        base_url, book_id = get_flipbook_info(url)
        start_page, max_page = get_max_page(url)
        out_dir = f"{book_id}_images"
        images = download_images(base_url, book_id, start_page, max_page, out_dir)
        if images:
            cbz_name = os.path.join(downloads_dir, f"{book_id}.cbz")
            create_cbz(images, cbz_name)
            for img in images:
                os.remove(img)
            os.rmdir(out_dir)
            print(f"Downloaded {len(images)} images and created {cbz_name} for {url}.")
            # Mark as finished
            with open(finished_file, "a") as f:
                f.write(url + "\n")
        else:
            print(f"No images downloaded for {url}.")

if __name__ == "__main__":
    main()