#### HANDILING ALERT ####

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    def handle_dialog(dialog):
        print("Alert Message:", dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.goto("https://vinothqaacademy.com/alert-and-popup/")

    page.get_by_role("button", name="Alert Box").click()

    page.wait_for_timeout(3000)

    browser.close()