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
    #driver.maximize_window()  # included in init options

    driver.get("https://pyinstaller.org/en/v6.3.0/usage.html")
    time.sleep(3)

    link_btn = driver.find_element(By.LINK_TEXT, 'What PyInstaller Does and How It Does It')
    print('-'*80)
    print(link_btn)
    print('-' * 80)
    link_btn.click()

    time.sleep(5)
    driver.quit()


