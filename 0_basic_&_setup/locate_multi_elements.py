from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

WEB_URL = 'https://demo.nopcommerce.com/'

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    # get a list of elements that match the locator
    element_list = driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")

    print(f'amount of elements found: {len(element_list)}')
    print('=======================================')
    for i, elem in enumerate(element_list):
        print(f'{i}: -> {elem.text}')
    print('=======================================')

    driver.quit()

