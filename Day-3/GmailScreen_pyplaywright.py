from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.wait_for_load_state("networkidle")

    # Navigate to Gmail
    page.goto("https://www.gmail.com")

    # Wait for page to load
    page.wait_for_load_state("networkidle")

    # Take screenshot
    page.screenshot(path="gmail.png")

    print("Screenshot saved as gmail.png")

    browser.close()

