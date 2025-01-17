"""
QA special websites for sample testing automation
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
https://demo.nopcommerce.com/
https://admin-demo.nopcommerce.com/login
https://testautomationpractice.blogspot.com/
https://testautomationpractice.blogspot.com/
http://www.deadlinkcity.com/
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

WEB_URL = 'https://formstone.it/components/dropdown/demo/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WEB_URL)

    """
    IMPORTANT NOTE:
    the element we interact here is from a 'select' tag:
    
    <select name="demo_basic_2" id="demo_basic_2" ... </select>
    
    if the tag is not 'select' then Select(...) instantiation will throw exception!
    choose fearfully the locator of the element.
    """
    dropdown_menu_element = driver.find_element(By.ID, 'demo_basic_2')

    # "Select(...)" - for drop-down elements there is a special module that help's with their handling
    select_obj = Select(dropdown_menu_element)
    # -----------------------------------------------------------------------------------------------------
    # select any option from drop-down menu using instance of "Select()" class
    # By visible text
    select_obj.select_by_visible_text('Mississippi')
    # -----------------------------------------------------------------------------------------------------
    # By value: <option value="DE">Delaware</option>
    select_obj.select_by_value('DE')
    # -----------------------------------------------------------------------------------------------------
    # By index
    select_obj.select_by_index(5)
    # -----------------------------------------------------------------------------------------------------
    # in case of multiple select options, where we can select several things at once, also can remove selection
    # select_obj.deselect_by_visible_text('Mississippi')
    # -----------------------------------------------------------------------------------------------------

    # get a list of all options, from type of element! not text!
    options_list = select_obj.options

    print(f'Amount of drop-down options: {len(options_list)}')

    # print all options from the drop-down menu
    for option in options_list:
        print(option.text)  # note the dot.text
    # -----------------------------------------------------------------------------------------------------
    driver.quit()
