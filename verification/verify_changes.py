
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:8000")
    time.sleep(3)
    page.screenshot(path="verification/screenshot.png")
    browser.close()
