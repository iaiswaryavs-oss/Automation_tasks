#### TABS ####

from playwright.sync_api import sync_playwright

urls = [
    "https://www.google.com/aclk?sa=L&pf=1&ai=DChsSEwjJ79jwi9SVAxXAhmYCHcZ2Gc8YACICCAEQABoCc20&co=1&ase=2&gclid=CjwKCAjwvNfSBhBiEiwAyaGMCd5kKKqDL8FmRduCheKE5SE9CE6URxuQ633hGXvZ134YqkQZ3qE7XhoCiMoQAvD_BwE&ei=xC1XarfCAqaiseMPqODbqQc&cid=CAASugHkaNtiR6knlca7YDpLJyyRW_wCb6GafqubtZ39SPR8jeVLZTSQVYycuw6sKg_MZ0X44CnYXfHOHk9dUYuIDuzmSfuO5gXeQvoP0op9ZX12UIBIfUr7YRHf3fFq1ONIv1gza6iLQL1i-r4EjgR7LJxfEmOY_n-py_b6C9C6dBE7A_4k45QUqR3q26cg0z5U_eeJqAIiH9quGD9Gt23z7BoegodB5GPRhvjSKaUmc1Db4kHHHhT3h0-obpI&cce=2&category=acrcp_v1_32&sig=AOD64_2U0btjFk6K45nvY0eFklIAsTYqhg&q&sqi=2&nis=4&adurl=https://www.dotandkey.com/?utm_source%3Dadmitad%26utm_medium%3Daffiliate%26utm_campaign%3D1808514_368_6a56e5126ffee4cff13648d5%26irclid%3DwaftqjkRbHsY%26utm_term%3Dhttps%253A%252F%252Fdotandkey.com%26gad_source%3D1%26gad_campaignid%3D24021809005%26gbraid%3D0AAAABEG9Nl8UKXXyzmwOROgBClARbjcXd%26gclid%3DCjwKCAjwvNfSBhBiEiwAyaGMCd5kKKqDL8FmRduCheKE5SE9CE6URxuQ633hGXvZ134YqkQZ3qE7XhoCiMoQAvD_BwE&ved=2ahUKEwi3tNLwi9SVAxUmUWwGHSjwNnUQ0Qx6BAgNEAE",
    "https://www.g3r.co/",
    "https://foxtale.in/?srsltid=AfmBOoqfBMOJ4L0tU4IvhdJxFAInCE8LNz6p0-CJqx7Q1zHoU5v7V0sb",
    "https://aqualogica.in/?srsltid=AfmBOopkAOPrCqEeGE4S1vZbigBZj6BxcsVT-i6HS8QAmzZ-kL60QlHN",
    "https://www.drsheths.com/?srsltid=AfmBOop6ZYpWnz_KKKnOs-8KvPbRUbmtPAC8WpuT91zx-TW0AUU3DuOi"
]

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="chrome",
        headless=False
    )

    context = browser.new_context()

    for url in urls:
        page = context.new_page()
        page.goto(url)

    input("Press Enter to close...")
    browser.close()