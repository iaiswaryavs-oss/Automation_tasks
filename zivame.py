#### LAUNCH BROWSER ####
#### OPEN PAGE ####
#### CLICK ####
#### AUTO WAITS ####
#### ASSERTIONS ####

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)

    page = browser.new_page()
    page.goto("https://www.zivame.com/")

    expect(page).to_have_title("Zivame")

    page.locator("a.fit-container").click()

    page.wait_for_timeout(5000)
    browser.close()