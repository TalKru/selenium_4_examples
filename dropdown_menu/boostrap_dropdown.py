
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://www.dummyticket.com/dummy-ticket-for-visa-application/'
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

    """
    NOTE: this dropdown menu is not a select tag, its span tag:
    <span ....</span>
    
    <span> dropdowns (Bootstrap): These are custom dropdowns styled with JavaScript/CSS. 
    this element appears dynamically on the HTML, only after a click
    """

    locate_tup = (By.ID, "select2-billing_country-container")
    dropdown_menu = wait.until(EC.presence_of_element_located(locate_tup))

    # step 1: click on the element to reveal the menu options
    dropdown_menu.click()

    # step 2: capture all options from the dropdown
    # all options are inside <li> tag, and all of them under <ul> tag, note the custom XPath
    options = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

    print(f'found {len(options)} options in the dropdown menu.')

    # print all options
    for i, country in enumerate(options):
        print(f'{i}) country: {country.text}')

        # select an option
        if country.text == 'Costa Rica':
            country.click()
            driver.save_screenshot('selected_country.png')
            break  # or else the "country.text" will throw exception on the next iteration

    time.sleep(4)
    driver.quit()
