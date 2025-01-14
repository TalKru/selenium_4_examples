
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://demo.automationtesting.in/Static.html'
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

    # locate the elements
    source1 = driver.find_element(By.XPATH, "//img[@id='node']")  # drag this element
    source2 = driver.find_element(By.XPATH, "//img[@id='mongo']")  # drag this element
    box_area = driver.find_element(By.XPATH, "//div[@id='droparea']")  # drop area

    action_chains = ActionChains(driver)

    # drag the element and drop in the box area
    action_chains.drag_and_drop(source1, box_area).perform()
    action_chains.drag_and_drop(source2, box_area).perform()

    for _ in range(5):
        action_chains.drag_and_drop(source1, box_area).perform()

    time.sleep(3)
    driver.quit()
