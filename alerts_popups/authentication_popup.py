from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    ##################################################################################################
    """
    Login alerts or popups that appear before accessing a webpage are often implemented for security reasons. 
    They act as a gate to ensure only authorized users can access sensitive or restricted content, 
    protecting against unauthorized access or data breaches. 
    These are commonly seen in corporate, financial, or admin portals.
    
    To handle login popups (basic authentication dialogs) in Selenium, 
    include the username and password directly in the URL using the format http://username:password@website.com
    
    This bypasses the popup and allows Selenium to proceed with automation. 
    Note: This works for basic authentication dialogs, not custom login modals.
    """
    #           http://usern:pswrd@...
    driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

    xpath = "//div[@class='example' and p[contains(text(), 'Congratulations!')]]"
    auth_element = driver.find_element(By.XPATH, xpath)

    auth_txt = auth_element.text
    print(auth_txt)

    assert 'Congratulations!' in auth_txt
    ##################################################################################################

    driver.quit()
