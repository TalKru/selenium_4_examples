
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://www.worldometers.info/geography/flags-of-the-world/'
WAIT_TIME_SEC = 10


def setup() -> (webdriver, WebDriverWait):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    return driver, wait


def scroll_to_element_1(webdriver, WebDriverWait):
    driver, wait = webdriver, WebDriverWait

    locator_tup = (By.XPATH, "//img[@src='/img/flags/small/tn_is-flag.gif']")
    israel_flag = wait.until(EC.visibility_of_element_located(locator_tup))

    # create ActionChains obj for mouse operations
    ac = ActionChains(driver)

    # simple option: will scroll until given element in bottom of the page
    ac.scroll_to_element(israel_flag).perform()


def scroll_by_amount_1(webdriver, WebDriverWait):
    driver, wait = webdriver, WebDriverWait

    locator_tup = (By.XPATH, "//img[@src='/img/flags/small/tn_is-flag.gif']")
    israel_flag = wait.until(EC.visibility_of_element_located(locator_tup))

    # create ActionChains obj for mouse operations
    ac = ActionChains(driver)

    # more accurate option, to position the element in the center (more or less) of te page
    # get the Y-axis position (vertical) of the element
    delta_y = israel_flag.rect['y']
    # adjust to position, scroll_by_amount(int_X, int_Y)
    offset_element_pos = int(delta_y - 400)
    ac.scroll_by_amount(0, offset_element_pos).perform()


def scroll_with_keyboard(webdriver, WebDriverWait):
    driver, wait = webdriver, WebDriverWait

    locator_tup = (By.XPATH, "//img[@src='/img/flags/small/tn_is-flag.gif']")
    israel_flag = wait.until(EC.visibility_of_element_located(locator_tup))

    # create ActionChains obj for mouse operations
    ac = ActionChains(driver)

    # use the keyboard arrows
    for _ in range(200):
        ac.send_keys(Keys.ARROW_DOWN).perform()  # down

    for _ in range(50):
        ac.send_keys(Keys.ARROW_UP).perform()  # up


if __name__ == '__main__':
    driver, wait = setup()

    scroll_to_element_1(driver, wait)
    scroll_by_amount_1(driver, wait)
    scroll_with_keyboard(driver, wait)

    time.sleep(3)
    driver.quit()

    """
    NOTE: there is also additional way, by using:
    driver.execute_script(...)
    and passing a javascript code 
    """
