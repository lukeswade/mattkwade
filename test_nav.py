from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(color_scheme="light")
    page.goto('http://localhost:8000')
    logo_color = page.locator('.logo').first.evaluate('el => window.getComputedStyle(el).color')
    nav_link_color = page.locator('.nav a').first.evaluate('el => window.getComputedStyle(el).color')
    nav_bg = page.locator('.nav').evaluate('el => window.getComputedStyle(el).backgroundColor')
    print("LIGHT MODE:")
    print("Logo color:", logo_color)
    print("Nav link color:", nav_link_color)
    print("Nav bg:", nav_bg)

    page_dark = browser.new_page(color_scheme="dark")
    page_dark.goto('http://localhost:8000')
    logo_color_d = page_dark.locator('.logo').first.evaluate('el => window.getComputedStyle(el).color')
    nav_link_color_d = page_dark.locator('.nav a').first.evaluate('el => window.getComputedStyle(el).color')
    nav_bg_d = page_dark.locator('.nav').evaluate('el => window.getComputedStyle(el).backgroundColor')
    print("\nDARK MODE:")
    print("Logo color:", logo_color_d)
    print("Nav link color:", nav_link_color_d)
    print("Nav bg:", nav_bg_d)

    browser.close()
