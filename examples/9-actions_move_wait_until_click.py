from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

WEB_URL = 'https://demos.jquerymobile.com/1.4.5/checkboxradio-radio/'

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    title = driver.title
    page_source = driver.page_source
    driver_name = driver.name

    print(f'Website URL: {WEB_URL}')
    print(f'Title: {title}')
    #print(f'Page source: {page_source}')
    print(f'Driver Name: {driver_name}')
    ############################################################################## [WAIT Until]
    radio_box_one = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'radio-choice-0a'))
    )

    radio_box_two = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'radio-choice-0b'))
    )
    ############################################################################## [WAIT Until]
    print(f'radio_box_one is displayed? - {radio_box_one.is_displayed()}')
    print(f'radio_box_one is enabled? - {radio_box_one.is_enabled()}')
    print('----------------------------------------------')
    print(f'radio_box_one is selected? - {radio_box_one.is_selected()}')
    print(f'radio_box_two is selected? - {radio_box_two.is_selected()}')
    print('----------------------------------------------')

    time.sleep(1)
    ActionChains(driver).move_to_element(radio_box_one).click().perform()
    print('clicked radio_box_one...')

    print(f'radio_box_one is selected? - {radio_box_one.is_selected()}')
    print(f'radio_box_two is selected? - {radio_box_two.is_selected()}')
    print('----------------------------------------------')

    time.sleep(1)
    ActionChains(driver).move_to_element(radio_box_two).click().perform()
    print('clicked radio_box_two...')

    print(f'radio_box_one is selected? - {radio_box_one.is_selected()}')
    print(f'radio_box_two is selected? - {radio_box_two.is_selected()}')
    print('----------------------------------------------')

    ##############################################################################

    ### TODO - DO MORE OPTIONS IN THE WEB PAGE some elements are not enabled, test them....
    driver.quit()

