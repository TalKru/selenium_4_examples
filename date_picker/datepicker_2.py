from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    # click to open the date picker
    datepicker = driver.find_element(By.XPATH, "//input[@id='dob']")
    datepicker.click()

    # open 'month selecter'
    #driver.find_element(By.XPATH, "//select[@aria-label='Select month']").click()

    """
    <select class="ui-datepicker-month" data-handler="selectMonth" ...>
        <option value="0" selected="selected">Jan</option>
        <option value="1">Feb</option><option value="2">Mar</option>
        <option value="3">Apr</option><option value="4">May</option>
        <option value="5">Jun</option><option value="6">Jul</option>
        <option value="7">Aug</option><option value="8">Sep</option>
        <option value="9">Oct</option><option value="10">Nov</option>
        <option value="11">Dec</option></select>
    
    we have a select class so we can use the special class
    """
    # select month
    dropdown_menu_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
    dropdown_menu_month.select_by_visible_text('Oct')
    #dropdown_menu_month.select_by_index(9)  # start from index 0, not 1

    # select year 1999
    dropdown_menu_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
    dropdown_menu_year.select_by_value("1999")

    # select day 13
    days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

    for day in days:
        if day.text == '13':
            day.click()

    time.sleep(5)
    driver.quit()
