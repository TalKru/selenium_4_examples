"""
https://www.selenium.dev/documentation/webdriver/interactions/cookies/
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://demo.nopcommerce.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    # ------------------------------------------------------------------------------------ #
    cookies = driver.get_cookies()
    print(f'Number of cookies: {len(cookies)}')

    # Add new user defined cookie - in the list[dict] format
    driver.add_cookie({'name': 'super-sweet-cookie', 'value': 'chocolate', 'ID': '007'})
    print('just added a cookie...')

    cookies = driver.get_cookies()  # UPDATE the list
    print(f'Number of cookies: {len(cookies)}')

    # delete specific cookie - BY NAME attribute
    driver.delete_cookie('super-sweet-cookie')
    print('Deleted my cookie...')

    cookies = driver.get_cookies()  # UPDATE the list
    print(f'Number of cookies: {len(cookies)}')

    # delete ALL the cookies
    driver.delete_all_cookies()
    print('deleting all the cookies...')

    cookies = driver.get_cookies()  # UPDATE the list
    print(f'Number of cookies: {len(cookies)}')
    # ------------------------------------------------------------------------------------ #

    time.sleep(1)
    driver.quit()
