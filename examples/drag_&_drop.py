
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
    #chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()  # included in init options

    driver.get('https://www.w3schools.com/html/html5_draganddrop.asp')

    assert 'HTML Drag and Drop API' == driver.title

    assert 'drag1' in driver.page_source
    assert 'div1' in driver.page_source
    assert 'div2' in driver.page_source

    element_to_drag = driver.find_element(By.ID, 'drag1')
    box1 = driver.find_element(By.ID, 'div1')
    box2 = driver.find_element(By.ID, 'div2')

    act = ActionChains(driver)

    for _ in range(1, 5):
        act.drag_and_drop(box1, box2).perform()
        time.sleep(0.7)
        act.drag_and_drop(box2, box1).perform()
        time.sleep(0.7)

    driver.quit()





