#### DWLD PDF ####

import asyncio
from playwright.async_api import async_playwright
import os

async def download_ugly_love_pdf():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        pdf_url = "https://www.junkybooks.com/administrator/thebooks/62fec2186328f-ugly-love.pdf"
        destination_path = os.path.join(os.getcwd(), "ugly_love.pdf")

        print("Navigating and downloading the PDF stream...")
        
        # Navigate directly to the URL and capture the network response
        response = await page.goto(pdf_url)
        
        if response and response.status == 200:
            # Read the binary data from the network response stream
            pdf_buffer = await response.body()
            
            # Write the binary data directly to your file
            with open(destination_path, "wb") as f:
                f.write(pdf_buffer)
            print(f"Success! File successfully saved to: {destination_path}")
        else:
            status = response.status if response else "No response received"
            print(f"Failed to download. Server returned: {status}")

        # Clean up and close the browser
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(download_ugly_love_pdf())