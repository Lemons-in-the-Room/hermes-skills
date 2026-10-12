#!/usr/bin/env python3
"""
Lemons proposal renderer — A4 portrait PDF via Playwright/Chromium.
Usage: python render_proposal.py INPUT.html OUTPUT.pdf
"""
import sys, os, threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

def render(html_path, pdf_path):
    html_path = os.path.abspath(html_path)
    serve_dir = os.path.dirname(html_path)
    html_file = os.path.basename(html_path)

    server = HTTPServer(("127.0.0.1", 0), lambda *a: SimpleHTTPRequestHandler(*a, directory=serve_dir))
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    url = f"http://127.0.0.1:{port}/{html_file}"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox", "--font-render-hinting=none"])
            page = browser.new_page(device_scale_factor=2)
            page.goto(url, wait_until="networkidle")
            page.emulate_media(media="print")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(800)
            page.pdf(
                path=pdf_path,
                format="A4",
                landscape=False,
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                prefer_css_page_size=False,
            )
            browser.close()
    finally:
        server.shutdown()

    print(f"OK -> {pdf_path}  ({os.path.getsize(pdf_path)//1024} KB)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: python render_proposal.py INPUT.html OUTPUT.pdf")
    render(sys.argv[1], sys.argv[2])
