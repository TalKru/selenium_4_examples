

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time
import os

WEB_URL = 'https://the-internet.herokuapp.com/upload'
WAIT_TIME_SEC = 10
FILENAME = 'image_file_test.jpg'

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    try:
        driver.get(WEB_URL)

        # --------------------------------------------------------------------------------
        """
        # Relative path
        path = os.path.join("..", "folder", "file.txt")
        print(path)  # ../folder/file.txt
        
        # Absolute path
        absolute_path = os.path.abspath(os.path.join("..", "folder", "file.txt"))
        print(absolute_path)  # /home/user/folder/file.txt (on Linux)
        
        __file__ refers to the location of the current script file.
        """
        # create path for the file to upload
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), FILENAME))
        print(f'file path of the file to upload: {file_path}')
        # --------------------------------------------------------------------------------

        # Send the file path to the file input element to "upload" the file
        choose_file_btn = wait.until(EC.element_to_be_clickable((By.ID, 'file-upload')))
        choose_file_btn.send_keys(file_path)

        upload_btn = driver.find_element(By.ID, 'file-submit')
        upload_btn.click()

        # bool
        is_uploaded = (
            wait.until(EC.text_to_be_present_in_element((By.ID, "uploaded-files"), FILENAME))
        )
        print(f'is the web showing uploaded file name -> {is_uploaded}')
        time.sleep(4)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except TimeoutError as e:
        print(f"Timeout occurred: {e}")
    except NoSuchElementException as e:
        print(f"No such element found: {e}")
    except WebDriverException as e:
        print(f"WebDriver error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        driver.quit()
