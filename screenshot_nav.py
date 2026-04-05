from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Light mode
    page = browser.new_page(color_scheme="light")
    page.goto('http://localhost:8000')
    page.screenshot(path="light_nav.png", full_page=True)

    # Dark mode
    page_dark = browser.new_page(color_scheme="dark")
    page_dark.goto('http://localhost:8000')
    page_dark.screenshot(path="dark_nav.png", full_page=True)

    browser.close()
