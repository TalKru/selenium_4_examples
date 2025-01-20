from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://lazyinvestor.co.il/monetary-fund/')

    """
    note the syntax of the XPATH:
    first we copy the relational path of a value of a table
    then we go up by hierarchy to the parent
    then from the parent we take all it's children
    """
    elements = driver.find_elements(By.XPATH, "//td[contains(text(),'244,000 יחידות')]/ancestor::tr/child::td")

    print(f'amount of children elements of the ancestor: {len(elements)}')

    for i, elm in enumerate(elements):
        print(f'{i}: {elm.text}')
    print('#'*100)

    """
    now we will find single element
    and then print it's text, such that entire row will be printed 
    since the element itself does not have and text but it's children do
    so we get the text from ALL the children
    """
    parent = driver.find_element(By.XPATH, "//td[contains(text(),'244,000 יחידות')]/ancestor::tr")

    print(parent.text)

    driver.quit()


