
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://www.browserstack.com/guide/mouse-hover-in-selenium'
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

    # locate elements to hover on
    step0 = driver.find_element(By.XPATH, "//button[@id='developers-dd-toggle']")
    step1 = driver.find_element(By.XPATH, "//button[@id='products-dd-toggle']")
    step2 = driver.find_element(By.XPATH, "//button[@id='products-dd-tab-2']")
    xpath = ("//div[@id='products-dd-tabpanel-2-inner-1']//div[contains(@class,"
             "'bstack-mm-sub-nav-tabcol')]//div//a[@title='App Percy']")
    step3 = driver.find_element(By.XPATH, xpath)

    # mouse hover action - setup action chains
    action_chains = ActionChains(driver)  # create special class object

    # create desired actions, will not execute them without .perform()
    # action_chains_obj.action(element).action(element).action(element)...action(element).click
    action_chains.move_to_element(step0).move_to_element(step1).move_to_element(step3).click().perform()

    time.sleep(4)
    driver.quit()
