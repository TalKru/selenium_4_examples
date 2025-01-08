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

    driver.get('https://www.solomycar.co.il/')

    # txt_box_xpath = '/html/body/main/header/div[3]/div/div[8]/div/form/div/div[2]/div/input' # Absolute XPATH -> unstable!
    txt_box_xpath = '//input[@placeholder=\'11-222-33\']' # Relative XPATH -> more stable!

    text_box = driver.find_element(By.XPATH, txt_box_xpath)
    car_plate = '50950101'
    text_box.send_keys(car_plate)

    # btn_xpath = '/html/body/main/header/div[3]/div/div[8]/div/form/div/div[2]/button'  # Absolute XPATH -> unstable!
    btn_xpath = '//button[@class=\'submit_btn js-license-submit\']'  # Relative XPATH -> more stable!

    button = driver.find_element(By.XPATH, btn_xpath)
    button.click()

    # car_model_rslt_txt_xpath = '/html/body/main/header/div[3]/div/div[3]/div[2]/span'  # Absolute XPATH -> unstable!
    car_model_rslt_txt_xpath = '//span[@class=\'selected_car_text\']' # Relative XPATH -> more stable!

    # Pass an empty string '' to wait until any text is present.
    # Wait for the text to be non-empty
    txt_element = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, car_model_rslt_txt_xpath), '')
    )

    print(txt_element)
    car_model_str = driver.find_element(By.XPATH, car_model_rslt_txt_xpath).text

    print(f'selected car model for plate: {car_plate} \nis: {car_model_str}')

    time.sleep(2)
    driver.quit()


