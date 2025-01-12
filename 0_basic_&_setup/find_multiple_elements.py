from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://ali-buy.com/')

    class_ident = 'col_item offer_grid rehub-sec-smooth offer_grid_com mobile_compact_grid no_btn_enabled'

    # find all the classes:
    class_list = driver.find_elements(By.CLASS_NAME, class_ident)

    print(f'amount of classes found: {len(class_list)}')
    for classes in class_list:
        print(classes.text)

    # find all the links:
    links_list = driver.find_elements(By.TAG_NAME, 'a')

    print(f'amount of links found: {len(links_list)}')
    print('links:')
    for link in links_list:
        print(link.text)

    driver.quit()


