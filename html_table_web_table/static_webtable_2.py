from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

WEB_URL = 'https://cosmocode.io/automation-practice-webtable/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    # Count number of rows & columns (WITHOUT headers)
    count_rows = len(driver.find_elements(By.XPATH, "//tbody/tr/td[2]")) - 1  # (WITHOUT headers)
    count_cols = len(driver.find_elements(By.XPATH, "//tbody/tr[1]/td"))

    print(f'Number of rows in the table: {count_rows}')
    print(f'Number of columns in the table: {count_cols}')
    print('---------------------------------------------------')

    # Read specific cell data
    israel_info_list: list[str] = []
    israel_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[83]/td[2]").text )
    israel_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[83]/td[3]").text )
    israel_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[83]/td[4]").text )
    israel_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[83]/td[5]").text )
    print(israel_info_list)

    japan_info_list: list[str] = []
    japan_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[86]/td[2]").text )
    japan_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[86]/td[3]").text )
    japan_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[86]/td[4]").text )
    japan_info_list.append( driver.find_element(By.XPATH, "//tbody/tr[86]/td[5]").text )
    print(japan_info_list)
    print('---------------------------------------------------')

    # find countries that speak English
    # XPATH -->  //tbody/tr[ROW_INDEX]/td[COLUMN_INDEX]
    # Primary Language on COLUMN = 5
    # Row is dynamic to loop over each one
    counter: int = 0
    for row in range(2, count_rows + 2):  # +2 since the header row was subtracted but the number of each row didn't changed
        lang_str = driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[5]").text

        # if English detected print the country (col 2)
        if "English" in lang_str:
            counter += 1
            country_str = driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[2]").text
            print(f'Country: [{country_str}]')

    print(f'English speaking countries: {counter}')

    driver.quit()
