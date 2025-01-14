
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WEB_URL)

    # switch to iframe
    driver.switch_to.frame("iframeResult")
    #------------------------------------------------------------------------------------------------------------
    # DOUBLE CLICK MOUSE

    button = driver.find_element(By.XPATH, "//button[normalize-space()='Double-click me']")

    action_chains = ActionChains(driver)
    action_chains.double_click(button).perform()
    # ------------------------------------------------------------------------------------------------------------

    time.sleep(3)
    driver.quit()
