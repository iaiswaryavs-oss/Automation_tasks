#### FRAMES ####


from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.hyrtutorials.com/p/frames-practice.html")

    print("Main Page URL:")
    print(page.url)

    print("\nIframe Details:")

    for index, frame in enumerate(page.frames[1:], start=1):
        print("Iframe", index)
        print("URL:", frame.url)
        print("----------------")

    browser.close()