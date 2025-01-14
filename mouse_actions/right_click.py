
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'http://swisnl.github.io/jQuery-contextMenu/demo.html'
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

    # ---------------------------------------------------------------------------------------------------------------
    # RIGHT CLICK

    button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

    # mouse right click - setup action chains
    action_chains = ActionChains(driver)

    # perform the right click with function .context_click(-)
    action_chains.context_click(button).perform()
    # ---------------------------------------------------------------------------------------------------------------

    # MOUSE HOVER: a special menu will pop up, lets hover over several and select the last one - exit
    option1 = driver.find_element(By.XPATH, "//span[normalize-space()='Edit']")
    option2 = driver.find_element(By.XPATH, "//span[normalize-space()='Cut']")
    option3 = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
    option_exit = driver.find_element(By.XPATH, "//span[normalize-space()='Quit']")

    action_chains.move_to_element(option1).move_to_element(option2).move_to_element(option3).move_to_element(option_exit).click().perform()

    # close the alert
    driver.switch_to.alert.dismiss()

    time.sleep(3)
    driver.quit()
