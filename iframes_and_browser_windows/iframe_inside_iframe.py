"""
https://www.selenium.dev/documentation/webdriver/interactions/frames/
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://demo.automationtesting.in/Frames.html'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WEB_URL)
    driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

    # locate the outer iframe
    outer_iframe = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
    # switch to outer iframe
    driver.switch_to.frame(outer_iframe)

    # then, within outer iframe, locate inner iframe
    inner_iframe = driver.find_element(By.XPATH, "//div[@class='iframe-container']//iframe")
    # switch to inner iframe
    driver.switch_to.frame(inner_iframe)

    # now we can interact with the text input element
    text_box = driver.find_element(By.XPATH, "//input[@type='text']")
    text_box.send_keys("Found the inner frame! :)")

    # optional example, switch focus back to outer frame (parent element)
    driver.switch_to.parent_frame()

    # optional example, switch focus back to main webpage
    driver.switch_to.default_content()
    time.sleep(3)

    driver.quit()
