
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time
import excel_utils

WEB_URL = ('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI'
           '-BSB001.html')
FILE_PATH = r'D:\data\calc-data.xlsx'
WAIT_TIME_SEC = 10


def app_init():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")  # will mess up file downloads
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])
    return driver, wait


def main_test(driver: webdriver, wait: WebDriverWait):
    driver.get(WEB_URL)

    # optional for visuals
    driver.execute_script(f"document.body.style.zoom='125%'")  # zoom in 150%
    ActionChains(driver).move_to_element(driver.find_element(By.ID, 'frequency'))

    # ---------------------------------------------------------------------------------------------------
    # in case pop-up msg opens
    elements = driver.find_elements(By.ID, 'wzrk-cancel')
    if elements:  # If the list is not empty
        wait.until(EC.element_to_be_clickable((By.ID, 'wzrk-cancel'))).click()
    # ---------------------------------------------------------------------------------------------------

    # get only the data test rows from the file
    r = excel_utils.get_row_count(FILE_PATH, 'Sheet1')
    excel_data_rows = range(2, r + 1)

    for i in excel_data_rows:
        print(f'-------------------(test row number: {i})-------------------')

        value1 = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 1)  # get data from excel
        field1 = driver.find_element(By.ID, 'principal')                        # find element
        field1.clear()                                                          # clear old data
        field1.send_keys(value1)                                                # pass data to element
        # ---------------------------------------------------------------------------------------------------
        value2 = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 2)
        field2 = driver.find_element(By.ID, 'interest')
        field2.clear()
        field2.send_keys(value2)
        # ---------------------------------------------------------------------------------------------------
        value3 = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 3)
        field3 = driver.find_element(By.ID, 'tenure')
        field3.clear()
        field3.send_keys(value3)
        # ---------------------------------------------------------------------------------------------------
        value4 = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 4)

        dropdown1 = driver.find_element(By.ID, 'tenurePeriod')
        Select(dropdown1).select_by_visible_text(value4)
        # ---------------------------------------------------------------------------------------------------
        value5 = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 5)

        dropdown2 = driver.find_element(By.ID, 'frequency')
        Select(dropdown2).select_by_visible_text(value5)
        # ---------------------------------------------------------------------------------------------------
        xpath = "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']"
        calc_btn = driver.find_element(By.XPATH, xpath)
        calc_btn.click()
        # ---------------------------------------------------------------------------------------------------
        xlsx_value = excel_utils.read_data(FILE_PATH, 'Sheet1', i, 6)
        xlsx_value = float(xlsx_value)
        url_value = driver.find_element(By.ID, 'resp_matval').text
        url_value = float(url_value)

        print(f'xlsx_value: {xlsx_value}')
        print(f'url_value: {url_value}')

        # mark the test result cell
        if xlsx_value == url_value:
            excel_utils.write_to_cell(FILE_PATH, 'Sheet1', i, 8, "PASS")
            excel_utils.fill_cell_color(FILE_PATH, 'Sheet1', i, 8, 'green')
            print("[v][PASS]")
        else:
            excel_utils.write_to_cell(FILE_PATH, 'Sheet1', i, 8, "FAIL")
            excel_utils.fill_cell_color(FILE_PATH, 'Sheet1', i, 8, 'red')
            print("[x][FAIL]")

        time.sleep(1)

    driver.quit()


if __name__ == '__main__':
    driver, wait = app_init()
    main_test(driver, wait)





