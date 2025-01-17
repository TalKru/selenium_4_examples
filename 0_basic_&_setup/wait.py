from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WEB_URL = 'www.google.com'
TIMEOUT_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    ######################################################################################################[implicit]
    """
    implicit wait:
    driver.implicitly_wait(TIME IN SEC)
    that will allow every driver action in the following code to wait the configured amount of time
    before it throw exception.
    you should use it ONCE in the beginning of the setup
    after creation of the driver instance
    """
    driver.implicitly_wait(10)
    ######################################################################################################[implicit]


    driver.get(WEB_URL)


    ######################################################################################################[explicit]
    """
    explicit wait:
    WebDriverWait is defined once on the start with driver instance
    then it is used with .until(EC.wait_function((By.XXX, "locator")))
    
    if ignored_exceptions=[] is empty or omitted then each wait.until(...) 
    will throw specific exception based on the condition, 
    for example: NoSuchElementException
    
    poll_frequency=2
    sleep interval between calls, default if not specified is 0.5
    time interval between it try to test the condition, if not met the first time,
    it will "ping" again after 2 seconds, and so long until the time-out hits (10)
    """
    wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

    # returns bool
    bool_var1 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'lnXdpd')))
    bool_var2 = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'lnXdpd')))
    bool_var3 = wait.until(EC.new_window_is_opened((By.CLASS_NAME, 'lnXdpd')))

    # returns driver element
    element1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lnXdpd')))
    element2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'lnXdpd')))
    element3 = wait.until(EC.visibility_of(element2))
    ######################################################################################################[explicit]

    driver.quit()
