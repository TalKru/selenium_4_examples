
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

WEB_URL = 'https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(WEB_URL)

    # locate the moving elements
    min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[1]")
    max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[2]")

    # find slide bar positions (x, y)
    # NOTE w have horizontal slider that cannot move vertically, hence 'y' axis is FIXED
    min_pos = min_slider.location  # {'x': 59, 'y': 294}
    max_pos = max_slider.location  # {'x': 766, 'y': 294}
    print(f'sliders position BEFORE moving: \nmin:{min_pos} \nmax:{max_pos}')

    action_chains = ActionChains(driver)
    # move the min slider
    action_chains.drag_and_drop_by_offset(min_slider, 150, 0).perform()
    # move the max slider
    action_chains.drag_and_drop_by_offset(max_slider, -300, 0).perform()

    # note 1: the values of movement will not be exact as it depends on many factors such as window res, browser, ect
    # note 2: in this example the slider is horizontal so the movement is only on X-axis, while Y-axis remains 0

    min_pos = min_slider.location
    max_pos = max_slider.location
    print(f'sliders position AFTER moving: \nmin:{min_pos} \nmax:{max_pos}')

    time.sleep(5)
    driver.quit()
