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

WEB_URL = 'https://practice-automation.com/iframes/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WEB_URL)
    """
    NOTE:
    Frames/Iframes: These are HTML documents embedded within another HTML document. 
    Selenium cannot directly interact with elements inside a frame or iframe 
    because it operates on the main DOM by default.

    Issue: Trying to interact with elements inside a frame or iframe will result in NoSuchElementException.

    Solution: Switch to the frame first using driver.switch_to.frame()
    
    3 option to find the frame:
    -----------------------------
    1. .switch_to.frame(name of the frame)
    <iframe ...name="top-iframe" ...</iframe>
    
    2. .switch_to.frame(ID of the frame)
    <iframe id="iframe-1"...</iframe>
    
    3. .switch_to.frame(web-element) - Switching using a WebElement is the most flexible option. 
    You can find the frame using your preferred selector and switch to it.
    
    4. .switch_to.frame(index of the frame) - if we have only one frame on the page, we use by index of zero.
    """
    #---------------------------------------------------------------------------------------(1)
    # find and switch to the iframe by name
    driver.switch_to.frame("top-iframe")

    # perform all the operation same as on any page
    xpath = "//a[@class='getStarted_Sjon' and @href='/docs/intro' and text()='Get started']"
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    time.sleep(2)
    driver.back()  # [<-] page back, but inside the frame

    # Leaving a frame: switch focus back to the main page
    driver.switch_to.default_content()

    # ---------------------------------------------------------------------------------------(2)
    # find and switch to the iframe by ID
    driver.switch_to.frame('iframe-1')

    xpath = "//a[@class='getStarted_Sjon' and @href='/docs/intro' and text()='Get started']"
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    time.sleep(2)
    driver.back()

    driver.switch_to.default_content()

    # -------------------------------------------------------------------------------------------------------------(3)
    # find the frame using your preferred selector
    iframe = driver.find_element(By.XPATH, "//iframe[@src='https://www.selenium.dev/' and @title='Selenium']")

    driver.switch_to.frame(iframe)

    xpath = "//a[@class='nav-link' and @href='/downloads']/span[text()='Downloads']"
    button = driver.find_element(By.XPATH, xpath)
    ActionChains(driver).move_to_element(button).click().perform()
    time.sleep(2)
    driver.back()

    driver.switch_to.default_content()

    # -----------------------------------(4)
    # switch to the iframe by index
    # driver.switch_to.frame(0)
    # ...
    # driver.switch_to.default_content()

    time.sleep(1)
    driver.quit()
