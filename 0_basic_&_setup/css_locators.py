
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.solomycar.co.il/')

    text_box = driver.find_element(By.CSS_SELECTOR, 'input.js-license-number')
    text_box.send_keys('1234567')

    # button = WebDriverWait(driver, 15).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='submit_btn'].submit_btn.js-license-submit"))
    # )

    btn_xpath = '/html/body/main/header/div[3]/div/div[8]/div/form/div/div[2]/button'
    button = driver.find_element(By.XPATH, btn_xpath)
    
    button.click()

    time.sleep(5)
    driver.quit()


