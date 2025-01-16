import os
import traceback
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT_SEC = 20
WEB_URL = 'https://the-internet.herokuapp.com/upload'
FILENAME = 'image_file_test.jpg'


def get_driver():
    """
    Set up and return a Selenium WebDriver with predefined options.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    return webdriver.Chrome(options=chrome_options)


def get_file_path(file_name: str) -> str:
    """
    Construct and validate the absolute path of the file to upload.
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Resolved file path: {file_path}")

    return file_path


def upload_file(driver, file_path: str):
    """
    Perform the file upload operation on the target web page.
    """
    driver.get(WEB_URL)

    upload_btn_locator = (By.ID, "file-upload")
    choose_file_btn = WebDriverWait(driver, TIMEOUT_SEC).until(
        EC.element_to_be_clickable(upload_btn_locator)
    )
    choose_file_btn.send_keys(file_path)

    upload_btn = WebDriverWait(driver, TIMEOUT_SEC).until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    upload_btn.click()


def validate_upload(driver, expected_file_name: str):
    """
    Validate the uploaded file name on the web page.
    """
    WebDriverWait(driver, TIMEOUT_SEC).until(
        EC.text_to_be_present_in_element((By.ID, "uploaded-files"), expected_file_name)
    )
    file_name = driver.find_element(By.ID, "uploaded-files").text
    print(f"Uploaded file name displayed on page: {file_name}")
    assert file_name == expected_file_name, f"Expected {expected_file_name}, but got {file_name}"
    print("File upload validation successful!")


def main():
    file_path = get_file_path(FILENAME)
    driver = get_driver()

    try:
        upload_file(driver, file_path)
        validate_upload(driver, FILENAME)
        time.sleep(4)

    except Exception as e:
        # Log the exception details
        print("An error occurred during execution:")
        print(traceback.format_exc())  # Print the full traceback

        # Capture a screenshot for debugging
        screenshot_path = os.path.join(os.path.dirname(__file__), "error_screenshot.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
