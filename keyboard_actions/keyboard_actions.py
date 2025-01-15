
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

WEB_URL = 'https://text-compare.com/'
WAIT_TIME_SEC = 10


def set_zoom(driver, zoom_percentage):
    driver.execute_script(f"document.body.style.zoom='{zoom_percentage}%'")


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

    wait = WebDriverWait(driver, WAIT_TIME_SEC, poll_frequency=1, ignored_exceptions=[])

    driver.get(WEB_URL)
    #--------------------------------------------------------------
    # zoom in 150%
    set_zoom(driver, 150)
    # --------------------------------------------------------------

    # click on the left side text box
    left_txt_box = driver.find_element(By.ID, "inputText1")
    left_txt_box.click()
    left_txt_box.send_keys('The message was sent by a robot automation!')

    # create ActionChains obj for mouse operations
    act = ActionChains(driver)

    # press Enter
    act.send_keys(Keys.ENTER).perform()

    left_txt_box.send_keys('The judgment day is coming...')

    # to select the full text that was typed in the text box press ctrl+A
    # NOTE: after key_down() always release the key with key_up() or it will remain pressed
    act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    # copy selected text using ctrl+C
    act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

    # chose the right side text box
    # driver.find_element(By.ID, "inputText2").click()  # same result, different way
    act.send_keys(Keys.TAB).perform()

    # paste the copied text in there using ctrl+v
    act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # click the compare text button on the web
    compare_button = driver.find_element(By.ID, 'compareButton')
    compare_button.click()

    # check if the message received: "The two texts are identical!"
    locate_tup = (By.CLASS_NAME, 'messageForUser')
    text = 'The two texts are identical!'
    wait.until(EC.text_to_be_present_in_element(locate_tup, text))

    text_element = driver.find_element(By.CLASS_NAME, 'messageForUser').text

    print(f'action message: {text_element}')
    assert text_element == text

    time.sleep(5)
    driver.quit()
