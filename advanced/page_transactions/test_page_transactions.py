import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from guara.transaction import AbstractTransaction, Application
from guara import it
from guara import setup
from selenium.webdriver.support import expected_conditions as EC


# Transaction for configuring Chrome WebDriver
class ConfigureDriverTransaction(AbstractTransaction):
    def do(self, **kwargs):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        return driver


# Transaction to check if email has been loaded
class IsEmailLoadedTransaction(AbstractTransaction):
    def do(self, **kwargs):
        driver = self._driver
        email_box_element = driver.find_element(By.ID, "mail")
        email_value = email_box_element.get_attribute("value")
        return bool(re.match(r".+@.+\.com", email_value))


# Transaction to wait until the email is loaded
class WaitForEmailToLoadTransaction(AbstractTransaction):
    def __init__(self, driver, timeout=30):
        super().__init__(driver)
        self.timeout = timeout

    def do(self):
        driver = self._driver
        WebDriverWait(driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, "mail"))
        )
        email_input = driver.find_element(By.ID, "mail")
        return email_input.get_attribute("value")


# Transaction to take a screenshot
class TakeScreenshotTransaction(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, filename):
        driver = self._driver
        self.filename = filename
        driver.save_screenshot(self.filename)
        return f"Screenshot saved as {self.filename}"


# Example test flow
def test_temp_email_task():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    app = Application(driver)
    app.at(setup.OpenApp, url="https://temp-mail.org/en/")
    app.at(WaitForEmailToLoadTransaction).asserts(it.MatchesRegex, ".+@.+\.com")
    email = app.at(TakeScreenshotTransaction, filename="temp_mail_screenshot.png")

    print(f"Generated Temporary Email: {email}")
