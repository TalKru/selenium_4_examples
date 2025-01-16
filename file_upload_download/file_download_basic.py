"""
The "Save As" dialog was skipped by configuring Chrome preferences through the add_experimental_option method. Specifically:

"download.prompt_for_download": False

This setting disables the "Save As" dialog, allowing files to be automatically downloaded to the specified directory.
"download.directory_upgrade": True

Ensures the browser uses the directory defined by "download.default_directory" instead of defaulting to the standard downloads folder.
"download.default_directory": current_location

Specifies the target directory for downloaded files, here set to the directory where the script is located.
These changes ensure that downloads proceed automatically and are saved directly to the specified location without user interaction.
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEB_URL = 'https://demo.automationtesting.in/FileDownload.html'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--incognito")  # will mess up file downloads

    # Set the current working directory as the download folder
    current_location = os.getcwd()

    preferences = {
        "download.default_directory": current_location,  # Set download directory
        "download.prompt_for_download": False,          # Disable Save As dialog
    }
    # preferences = {
    #     "download.default_directory": current_location,
    #     "download.prompt_for_download": False,
    #     "plugins.always_open_pdf_externally": True  # in case PDF file will auto-open in the browser instead downloading
    # }

    chrome_options.add_experimental_option("prefs", preferences)

    # Initialize the WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, WAIT_TIME_SEC)

    try:
        # Navigate to the website
        driver.get(WEB_URL)

        # Locate the 'Generate File' button for text file download and click it
        generate_text_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@type='button']")))
        generate_text_btn.click()

        # Wait to ensure the file is downloaded
        time.sleep(4)

        # Verify if the file exists in the current directory
        downloaded_file = os.path.join(current_location, 'samplefile.pdf')  # Adjust based on the actual file name

        if os.path.exists(downloaded_file):
            print(f"File successfully downloaded: {downloaded_file}")
        else:
            print("File was not downloaded. Please check the setup or website behavior.")

    finally:
        driver.quit()
