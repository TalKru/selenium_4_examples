
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://support.orangehrm.com/portal/en/signin'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    # open a link that pops up new window
    link_element = driver.find_element(By.CLASS_NAME, "Footer__footerLink")
    link_element.click()  # open new tab
    link_element.click()  # open new tab
    link_element.click()  # open new tab

    # the focus of the driver is not switching automatically to the new window that was opened
    # we must give a command to the driver to switch focus on the new window
    # each time we open a new window/tab a random ID is generated for this window
    # save the window ID
    tab_ID = driver.current_window_handle

    print(f'new window_ID: {tab_ID}')

    # we opened multiple tabs (windows) and each got a unique ID
    # we can get all the ID's of the open windows
    all_tabs_ID = driver.window_handles

    print('All tabs IDs')
    for i, tab_id in enumerate(all_tabs_ID):
        print(f'[{i}] window ID:  [{tab_id}]')

    # switch focus to a specific tab (window) --> driver.switch_to.window(tab-ID)
    # all_tabs_ID[0] is the parent tab and all_tabs_ID[1] is the second we clicked
    driver.switch_to.window(all_tabs_ID[1])

    time.sleep(3)  # title takes time to load...?

    print(f'child tab title: {driver.title}')

    # switch back to parent tab
    driver.switch_to.window(all_tabs_ID[0])

    print(f'parent tab title: {driver.title}')

    # for example, we can loop over the tabs have
    # and perform same operations on each tab
    for tab in all_tabs_ID:
        time.sleep(1)

        # 1. switch driver focus on the current tab
        driver.switch_to.window(tab)

        # 2. perform actions...
        print(f'working on window: {driver.title}')

        if 'Zoho' in driver.title:
            driver.close()  # closing specific tab based on a condition

    time.sleep(3)
    driver.quit()
