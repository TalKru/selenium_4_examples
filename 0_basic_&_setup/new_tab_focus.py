
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://www.orangehrm.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")  # will mess up file downloads
    # chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    locate_tup = (By.XPATH, "//input[@id='Form_submitForm_action_request']")
    button = wait.until(EC.presence_of_element_located(locate_tup))

    # ---------------------------------------------------------------------
    # print which window ID the driver is focused on
    print(f'ID of current_window_handle = {driver.current_window_handle}')

    # old way
    # open a link in a new tab (window) and switch focus on it
    # create keyboard keys combo that will open the link in a new page
    keys_combo = Keys.CONTROL + Keys.ENTER
    button.send_keys(keys_combo)

    # switch driver focus on the new tab
    driver.switch_to.window(driver.window_handles[1])
    print(f'ID of current_window_handle = {driver.current_window_handle}')
    # ---------------------------------------------------------------------

    """
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # New Window, Selenium4: Opens a new browser tab + switches to new tab
    driver.get("URL_1")
    driver.switch_to.new_window('tab')     # will open a new TAB, then driver.get() will open there the new page
    driver.switch_to.new_window('window')  # will open a new WINDOW, then driver.get() will open there the new page
    driver.get("URL_2")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    driver.switch_to.new_window('tab')
    time.sleep(5)
    driver.quit()
