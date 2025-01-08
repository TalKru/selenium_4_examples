from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import requests

WEB_URL = 'http://www.deadlinkcity.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, WAIT_TIME_SEC)
    driver.get(WEB_URL)

    # click the proceed-button to go to the site
    proceed_button_tup = (By.XPATH, '//*[@id="proceed-button"]')
    proceed_button = wait.until(EC.element_to_be_clickable(proceed_button_tup))
    time.sleep(2)  # dumb web, no other wait works here!
    proceed_button.click()


    # find all the links in the page
    links = driver.find_elements(By.TAG_NAME, 'a')

    for link in links:
        link_str = link.get_attribute('href')

        print('---------------------------')
        print(f'link text: {link.text}')
        print(link_str)

        try:
            response = requests.head(link_str)
            print(f'response: {response.status_code}')
        except:
            pass

    time.sleep(2)
    driver.quit()
