
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time
import calendar

WEB_URL = 'https://jqueryui.com/datepicker/'
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

    """
    NOTE: the element we need to interact is within iframe!
    <iframe src="..." class="demo-frame" ></iframe>
    
    We cannot interact with it directly before we switch to this iframe
    The iframe don't have a NAME or ID attributes so the only way 
    to find it is by index of 0, since it's the only iframe on the page
    """
    driver.switch_to.frame(0)

    datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")

    # date format in this date picker: MM/DD/YYYY
    # datepicker.send_keys("09/28/2025")  # simple way but not always available

    datepicker.click()  # open the datepicker

    # locate the navigation buttons
    # next_btn = driver.find_element(By.XPATH, "//a[@title='Next']")
    # prev_btn = driver.find_element(By.XPATH, "//a[@title='Prev']")

    # define the date of choice
    year = 2026
    month = 'September'
    day = '13'
    # ------------------------------------------------------------------------------------------------------
    # choose YEAR

    # get the currently selected month
    curr_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    curr_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    # click BACK id selected year > desired year
    while int(curr_year) > year:
        prev_btn = driver.find_element(By.XPATH, "//a[@title='Prev']")
        prev_btn.click()
        curr_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

        print(f'desired year: {year} | current year: {curr_year}')

    # click NEXT id selected year < desired year
    while int(curr_year) < year:
        next_btn = driver.find_element(By.XPATH, "//a[@title='Next']")
        next_btn.click()
        curr_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

        print(f'desired year: {year} | current year: {curr_year}')

    # ------------------------------------------------------------------------------------------------------
    # choose MONTH
    # same trick with the months, but we need a clever way to compare months as strings

    # {'January': 1, 'February': 2, ... 'November': 11, 'December': 12}
    month_order = {month: index for index, month in enumerate(calendar.month_name) if month}

    # must update the month var since it's changed with every click
    curr_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    #while             curr_month > month
    while month_order[curr_month] > month_order[month]:
        prev_btn = driver.find_element(By.XPATH, "//a[@title='Prev']")
        prev_btn.click()
        curr_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

        print(f'desired month: {month} | current month: {curr_month}')

    while month_order[curr_month] < month_order[month]:
        next_btn = driver.find_element(By.XPATH, "//a[@title='Next']")
        next_btn.click()
        curr_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

        print(f'desired month: {month} | current month: {curr_month}')

    #------------------------------------------------------------------------------------------------------
    # choose DAY

    # capture all the day elements, with special Xpath
    days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

    for curr_day in days:
        if curr_day.text == day:
            curr_day.click()
            print(f'Clicked the {curr_day.text} day!')
            break

    time.sleep(5)
    driver.quit()
