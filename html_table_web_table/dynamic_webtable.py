from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WEB_URL = 'https://opensource-demo.orangehrmlive.com'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)

    # steps to pass the login page
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    username_input.send_keys('Admin')

    pass_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    pass_input.send_keys('admin123')

    locator_tuple = (By.XPATH, "//button[@type='submit']")
    wait.until(EC.element_to_be_clickable(locator_tuple)).click()

    locator_tuple_2 = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
    wait.until(EC.element_to_be_clickable(locator_tuple_2)).click()

    locator_tuple_3 = (By.XPATH, "//span[normalize-space()='User Management']")
    wait.until(EC.element_to_be_clickable(locator_tuple_3)).click()

    locator_tuple_4 = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//li")
    wait.until(EC.element_to_be_clickable(locator_tuple_4)).click()

    #------------------------------------------------------------------------------------------------------------
    # get all the Employee Names
    rows_xpath = "(//div[@class='oxd-table-row oxd-table-row--with-border'])//div[@class='oxd-table-cell oxd-padding-cell'][5]"

    # rows = len(driver.find_elements(By.XPATH, rows_xpath))
    rows = len(wait.until(EC.visibility_of_all_elements_located((By.XPATH, rows_xpath))))
    print(f'Number of data rows detected: {rows - 1}')  # -1 since first element is headline, non-data

    for row in range(2, rows + 1):  # from 2 since first row is header and also will error - no such element

        xpath = ("(//div[@class='oxd-table-row oxd-table-row--with-border'])["
                 + str(row) + "]//div[@class='oxd-table-cell oxd-padding-cell'][4]")

        cell_data = driver.find_element(By.XPATH, xpath).text
        print(cell_data)

    driver.quit()
