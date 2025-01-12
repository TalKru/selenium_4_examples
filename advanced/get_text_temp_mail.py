from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import re


def email_loaded(driver):
    mail_text_box = driver.find_element(By.ID, 'mail')
    email_value = mail_text_box.get_attribute("value")
    # Check if the email matches the pattern xxx@xxxx.com
    return re.match(r".+@.+\.com", email_value)


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://temp-mail.org/en/")

    # Wait until the email is loaded and matches the pattern
    try:
        WebDriverWait(driver, 30).until(email_loaded)
        mail_text_box = driver.find_element(By.ID, 'mail')
        temp_mail_str = mail_text_box.get_attribute("value")
        print(f"Generated Temp Mail: {temp_mail_str}")
        driver.save_screenshot('del.png')

    except Exception as e:
        print(f"Failed to load temp mail: {e}")

    driver.quit()

