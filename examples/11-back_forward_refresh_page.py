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

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)
    driver.get("https://www.google.com")
    time.sleep(2)

    driver.refresh()  # refresh page
    time.sleep(1)
    driver.refresh()  # refresh page
    time.sleep(1)

    driver.back()  # go to prev page
    time.sleep(3)

    driver.forward()   # go to forward page
    time.sleep(3)

    driver.quit()


