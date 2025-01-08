from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

WEB_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    # open link in the page in a new tab
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc"))
    )
    time.sleep(2)
    link.click()

    time.sleep(3)
    driver.close()  # will close the parent tab, the first tab opened
    print('closed only the parent tab...')

    time.sleep(3)
    driver.quit()  # will close the browser
    print('closed the browser')

