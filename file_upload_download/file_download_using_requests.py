"""
DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), "downloads"):

Sets the download directory to a folder named downloads inside the current working directory of the script.
os.getcwd() retrieves the current directory where the script is being executed.
os.path.join() constructs the full path.
os.makedirs(DOWNLOAD_DIRECTORY, exist_ok=True):

Ensures the downloads folder exists. If it doesn't, it creates it.
exist_ok=True prevents an error if the folder already exists.
Selenium and Web Interaction
chrome_options = Options():

Configures Chrome browser options.
For example, --start-maximized ensures the browser starts in full-screen mode.
driver.get(WEB_URL):

Navigates to the target website.
download_btn.get_attribute("href"):

Extracts the direct file download URL from the href attribute of the download button.
File Download Using requests
os.path.basename(download_link):

Extracts the file name (e.g., samplefile.pdf) from the download URL.
file_path = os.path.join(DOWNLOAD_DIRECTORY, file_name):

Combines the DOWNLOAD_DIRECTORY and the file name to determine where the file will be saved.
requests.get(download_link):

Sends a GET request to the download URL.
with open(file_path, 'wb') as file::

Opens the file in binary write mode (wb) and writes the content from the GET request response.
How to Change the Download Location
Modify the DOWNLOAD_DIRECTORY variable to any path you like. For example:
python
Copy code
DOWNLOAD_DIRECTORY = "C:\\Users\\YourName\\Downloads\\AutomationFiles"
The directory will automatically be created if it doesn't exist.
Benefits of This Approach:
No Dialog Box: Directly downloads the file without triggering the browser's "Save As" dialog.
Control Over File Location: Allows precise control over where the file is stored.
"""

import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEB_URL = 'https://demo.automationtesting.in/FileDownload.html'
WAIT_TIME_SEC = 10

# Set the desired download directory
DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), "downloads")  # Default is "./downloads" in the script's directory

# Ensure the download directory exists
os.makedirs(DOWNLOAD_DIRECTORY, exist_ok=True)

if __name__ == '__main__':
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start Chrome in maximized mode
    #chrome_options.add_argument("--headless=new")

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Create an explicit wait object
    wait = WebDriverWait(driver, WAIT_TIME_SEC)

    # Open the target URL
    driver.get(WEB_URL)

    # Wait for the download button to be clickable
    locator_tuple = (By.XPATH, "//a[@type='button']")  # XPath to locate the download button
    download_btn = wait.until(EC.element_to_be_clickable(locator_tuple))

    download_btn.click()

    # Retrieve the direct download URL from the button's "href" attribute
    download_link = download_btn.get_attribute("href")
    print(f"Download link: {download_link}")

    # Download the file using the requests library
    if download_link:
        # Extract the file name from the URL
        file_name = os.path.basename(download_link)

        # Define the full path to save the downloaded file
        file_path = os.path.join(DOWNLOAD_DIRECTORY, file_name)

        # Make a GET request to download the file
        response = requests.get(download_link)

        # Save the file to the specified directory
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded: {file_path}")
    else:
        print("Failed to retrieve the download link.")

    driver.quit()

