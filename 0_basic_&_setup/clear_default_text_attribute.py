from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

WEB_URL = 'https://admin-demo.nopcommerce.com/login'

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    email_box = driver.find_element(By.ID, 'Email')
    time.sleep(2)
    # ------------------------------------------------
    email_box.clear()  # clear the default text
    # ------------------------------------------------
    time.sleep(1)
    email_box.send_keys("tal.is.cool@mail.com")
    time.sleep(2)

    """
    NOTE:
    <button type="submit" class="button-1 login-button"> Log in </button>
                                                         ^^^^^^^
                                                         Log in
                                                  (this is inner-text)
                            and this inner-text is what we gen using element.text
    """

    """
    element.text
    returns inner text on the element
    """
    res1 = email_box.text

    """
    return value of any attribute the element have: 
    <button type="submit" class="button-1 login-button">Log in</button>
    element.get_attribute('type') ===> "submit"
    """
    res2 = email_box.get_attribute('value')

    print(f'result of email_box.text - {res1}')
    print(f'result of email_box.get_attribute(value) - {res2}')

    driver.quit()

