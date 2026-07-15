#### FORM ####
#### UPLOAD ####
#### SCREENSHOT ####

import os
from playwright.sync_api import sync_playwright

# Absolute path to your real local file
FILE_TO_UPLOAD = "/home/aiswarya/Aiswarya Sibin/REPORT DOC-1.pdf"
actual_file_path = os.path.abspath(FILE_TO_UPLOAD)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto("https://demoqa.com/automation-practice-form")
    page.wait_for_load_state("domcontentloaded")

    # 1. Fill out Names
    page.locator("#firstName").fill("Aiswarya")
    page.locator("#lastName").fill("Sibin")

    # 2. Fill Email
    page.locator("#userEmail").fill("iaiswaryavs@gmail.com")
    
    # 3. Select Gender
    page.locator("label[for='gender-radio-2']").click()
    
    # 4. Fill Mobile Number
    page.locator("#userNumber").fill("9876543210")

    # 5. Date of birth 
    dob_input = page.locator("#dateOfBirthInput")
    dob_input.click()
    page.keyboard.press("Control+A")
    page.keyboard.type("01 NOV 2004")
    
    # Press Escape to close the calendar popup safely!
    page.keyboard.press("Escape")

    # 6. Subjects (Must use a valid site-supported category)
    subjects_input = page.locator("#subjectsInput")
    subjects_input.fill("Computer Science")
    page.keyboard.press("Enter")

    # 7. Hobbies
    page.locator("label[for='hobbies-checkbox-1']").click()

    # 8. File Upload
    if os.path.exists(actual_file_path):
        page.locator("#uploadPicture").set_input_files(actual_file_path)
    else:
        print(f"\n[WARNING] File not found: {actual_file_path}")
        print("Continuing with the rest of the script...\n")

    # 9. Address
    page.locator("#currentAddress").fill("Mills Lane, Kochi, Kerala")

    # 10. State and City dropdowns
    page.locator("#state").click()
    page.locator("#react-select-3-option-2").click()
    page.locator("#city").click()
    page.locator("#react-select-4-option-1").click()

    # 11. Submit
    page.locator("#submit").click(force=True)

    # 12. Wait for the confirmation modal overlay to appear on screen
    page.locator(".modal-content").wait_for(state="visible")

    # 13. Take the screenshot and save it in your project folder
    page.screenshot(path="screenshot_image.png")
    print("Screenshot saved successfully as 'screenshot_image.png'")

    # Keep browser open for 5 seconds to inspect results
    page.wait_for_timeout(5000)
    browser.close()