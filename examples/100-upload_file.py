import os  # Importing the os module to work with file paths
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

TIMEOUT_SEC = 10
WEB_URL = 'https://the-internet.herokuapp.com/upload'
FILENAME = 'selenium-snapshot.png'


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    #driver.implicitly_wait(10)
    wait = WebDriverWait(driver, TIMEOUT_SEC)

    # Step 1: Navigate to the file upload page
    driver.get(WEB_URL)

    """
    Step 2: Create an absolute path for the file to be uploaded
    __file__ is a special variable in Python that represents the path to the current script file.
    os.path.dirname(__file__) gets the directory of the script.
    
    Example: If your script is at   D:/dev/udemy/Selenium/test_script.py, 
    then, os.path.dirname(__file__) will return D:/dev/udemy/Selenium.
    
    os.path.join():
    Joins multiple path components together in a way that works across different operating systems.
    combines  D:/dev/udemy/Selenium  with the file name "selenium-snapshot.png"
    os.path.join("D:/dev/udemy/Selenium", "selenium-snapshot.png")
    
    os.path.abspath():
    Converts a relative path into an absolute path.
    Example:
    os.path.abspath("selenium-snapshot.png")
    If the current working directory is D:/dev/udemy/Selenium, the result will be D:/dev/udemy/Selenium/selenium-snapshot.png.
    """
    upload_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), FILENAME)
    )
    print(f'file path of the file to upload: {upload_file_path}')

    # Step 3: Locate the file input and wait to_be_clickable
    upload_btn_locator = (By.ID, "file-upload")

    choose_file_btn = wait.until(EC.element_to_be_clickable(upload_btn_locator))
    # older version code where WebDriverWait wasn't defined on the start
    # choose_file_btn = WebDriverWait(driver, TIMEOUT_SEC).until(
    #     EC.element_to_be_clickable(upload_btn_locator)
    # )

    # Step 4: Send the file path to the file input element to "upload" the file
    choose_file_btn.send_keys(upload_file_path)

    # Step 5: Click the "upload" button to complete the file upload
    upload_btn = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    # older version code where WebDriverWait wasn't defined on the start
    # upload_btn = WebDriverWait(driver, TIMEOUT_SEC).until(
    #     EC.element_to_be_clickable((By.ID, "file-submit"))
    # )
    upload_btn.click()

    # Step 6: wait until the element is presenting the given text = our filename
    is_filename_presented = (
        wait.until(EC.text_to_be_present_in_element((By.ID, "uploaded-files"), FILENAME))
    )
    print(f'is the web showing uploaded file name -> {is_filename_presented}')

    time.sleep(5)
    driver.quit()




