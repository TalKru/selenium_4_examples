from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # only for chrome


def headless_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def headless_edge():
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--headless=new")
    driver = webdriver.Edge(options=edge_options)
    return driver


def headless_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless=new")
    driver = webdriver.Edge(options=firefox_options)
    return driver


if __name__ == '__main__':
    #driver = headless_chrome()
    driver = headless_edge()
    #driver = headless_firefox()

    driver.get("https://demo.nopcommerce.com/")
    print(driver.title)
    print(driver.current_url)
    driver.close()
