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

    # --------------------------------------------------------------------------- #
    # get all the cookies created by the browser
    # will return a list[dict] of all cookies, [{...}, {...}, {...}]
    cookies = driver.get_cookies()

    print(f'Number of cookies: {len(cookies)}')

    for i, cook in enumerate(cookies):
        # print the full cookie data
        print(f'{i}) [full cookie]-> {cook}')

        # print single value from the cookie - 'name'
        print(f'{i}) [\'value\']-> {cook['value']}')
        print(f'{i}) [\'secure\']-> {cook.get('secure')}')
    # --------------------------------------------------------------------------- #
    driver.quit()
