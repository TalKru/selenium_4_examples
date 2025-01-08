from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WEB_URL = 'https://testautomationpractice.blogspot.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1)

    driver.get(WEB_URL)

    # radio_check_box1 = wait.until(EC.element_to_be_clickable((By.ID, 'male')))
    #
    # time.sleep(2)
    # radio_check_box1.click()
    #
    # radio_check_box2 = wait.until(EC.element_to_be_clickable((By.ID, 'female')))
    #
    # time.sleep(2)
    # radio_check_box2.click()

    # Wait for the parent container to be present
    parent_container = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[text()='Days:']/following-sibling::div[@class='form-check form-check-inline']/.."))
    )

    # Find all checkbox elements within the parent container
    checkboxes = parent_container.find_elements(By.XPATH, ".//input[@type='checkbox']")
    # checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input']")

    # Interact with each checkbox
    for checkbox in checkboxes:
        checkbox_id = checkbox.get_attribute("id")
        is_displayed = checkbox.is_displayed()
        print(f"Checkbox ID: {checkbox_id}, Visible: {is_displayed}")

        if is_displayed:
            checkbox.click()
            print(f"Clicked checkbox with ID: {checkbox_id}")
    print('----------------------------------------------------------')

    for box in checkboxes:
        if box.is_selected():
            box.click()
            print(f'found clicked box: {box.get_attribute('id')}, cleared.')
    print('----------------------------------------------------------')

    time.sleep(2)
    driver.quit()
