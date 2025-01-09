
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WEB_URL = 'https://the-internet.herokuapp.com/javascript_alerts'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    locator_tuple = (By.XPATH, "//button[@onclick='jsPrompt()']")
    alert_btn_3 = wait.until(EC.element_to_be_clickable(locator_tuple))
    alert_btn_3.click()  # open alert window

    """
    NOTE: Alert window is NOT a web element so when it pops you 
    cannot handle it the usual way (click ok or cancel).
    we cannot inspect it and identify element on it.
    
    what we must do instead?
    the driver is focused on the page we are on, so we need to switch focus on the alert
    with the command -> driver.switch_to.alert
    """
    alert_window = driver.switch_to.alert

    # how to capture the text from the popup/alert window
    txt = alert_window.text
    print(f'alert window says: [{txt}]')

    # how to pass value in the input box of the alert window (if such exist)
    alert_window.send_keys("I don't like alerts!")  # note: in automation the text inserted will not be visible

    # how to click on the popup/alert window options: OK / Cancel
    # NOTE: choose one option! comment out the other
    alert_window.accept()   # to choose OK
    alert_window.dismiss()  # to choose Cancel

    # locate the element that displays on the page the text we sent to the alert
    result_txt = driver.find_element(By.ID, 'result').text

    print(f'Text that sent to the popup window: [{result_txt}]')
    assert result_txt == "You entered: I don't like alerts!"

    driver.quit()
