import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://www.google.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    # basic screenshot of the full page
    # takes argument of the full path or just name of the file:
    # 'image1.png'
    # OR
    # 'D:\dev\selenium_4_examples\0_basic_&_setup\image1.png'
    driver.save_screenshot('image_1.png')
    driver.save_screenshot(os.path.abspath(os.path.join(os.path.dirname(__file__), 'image_2.png')))

    time.sleep(2)
    driver.quit()
