from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) 

    page = browser.new_page()
    page.goto('https://www.youtube.com/watch?v=MfISy9zei90')
    page.goto('https://www.facebook.com/playwrightvietnam')
    page.wait_for_timeout(10_000)