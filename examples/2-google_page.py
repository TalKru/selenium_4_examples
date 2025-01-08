
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")


    driver = webdriver.Chrome(options=chrome_options)
    #driver.maximize_window()  # included in init options

    driver.get("https://www.google.com")

    assert 'APjFqb' in driver.page_source

    search_box = driver.find_element(By.ID, 'APjFqb')
    time.sleep(0.7)
    search_box.send_keys('blablabla')
    time.sleep(0.7)
    search_box.clear()

    time.sleep(0.7)

    search_box.send_keys('funny cat')
    time.sleep(0.7)

    driver.implicitly_wait(3)
    #search_box.send_keys(Keys.ENTER)
    search_button = driver.find_element(By.NAME, "btnK")
    driver.implicitly_wait(3)
    search_button.click()

    text_bar = driver.find_element(By.ID, 'APjFqb')

    for _ in range(0, 8):
        text_bar.send_keys(Keys.PAGE_DOWN)  # Scroll down
        time.sleep(0.7)

    time.sleep(1)
    driver.quit()
















