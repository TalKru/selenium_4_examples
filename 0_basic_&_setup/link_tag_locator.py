from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://demo.nopcommerce.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(WAIT_TIME_SEC)
    driver.get(WEB_URL)

    # click a normal link example
    # locator_tuple = (By.LINK_TEXT, 'Digital downloads')
    # link1 = wait.until(EC.element_to_be_clickable(locator_tuple))
    # link1.click()

    # find all the links in the page
    links = driver.find_elements(By.TAG_NAME, 'a')

    for link in links:
        print('---------------------------')
        print(f'link text: {link.text}')
        print(link.get_attribute('href'))


    time.sleep(5)
    driver.quit()
