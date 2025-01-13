from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")  # <--- ignore

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://whatmylocation.com/')

    """
    +====================================+
    |          www.x.com wants to        |
    |                                    |
    |          know your location        |
    |                                    |
    |     [ allow ]      [ block ]       |
    +====================================+
    
    we can disable this notification on the browser level
    """

    time.sleep(7)
    driver.quit()
