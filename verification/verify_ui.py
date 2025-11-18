
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            # Go to the local HTML file served by the HTTP server
            await page.goto('http://localhost:8000/index.html', wait_until='networkidle')
            
            # Increased wait time to ensure all elements are loaded
            await page.wait_for_timeout(5000)

            # A more robust selector for leaflet vector features
            feature_selector = 'path.leaflet-interactive'
            await page.wait_for_selector(feature_selector, timeout=30000)
            
            # Take a screenshot
            screenshot_path = 'verification/ui_verification.png'
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
                
        except Exception as e:
            print(f"An error occurred: {e}")
            # Take a screenshot on error to debug
            await page.screenshot(path='verification/error_screenshot.png')
            print("Error screenshot saved to verification/error_screenshot.png")
            
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
