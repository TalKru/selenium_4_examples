import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def configure_driver() -> webdriver.Chrome:
    """
    Configures the Chrome WebDriver with desired options for the session.
    :return: A configured instance of the Chrome WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start in maximized mode
    chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
    chrome_options.add_argument("--incognito")  # Enable incognito mode for privacy
    return webdriver.Chrome(options=chrome_options)


def is_email_loaded(driver) -> bool:
    """
    Checks if the email input field contains a value matching the email pattern.
    :param driver: The WebDriver instance.
    :return: True if a valid email address is detected, False otherwise.
    """
    email_box_element = driver.find_element(By.ID, 'mail')
    extrct_mail = email_box_element.get_attribute("value")

    # return bool(re.match(r".+@.+\.com", extrct_mail))
    # return re.match(r".+@.+\.com", extrct_mail) is not None

    if re.match(r".+@.+\.com", extrct_mail) is not None:
        return True
    else:
        return False


def wait_for_email_to_load(driver, timeout=30) -> str:
    """
    Waits for the temporary email address to load and match the specified pattern.
    :param driver: The WebDriver instance.
    :param timeout: Maximum time to wait for the email to appear (in seconds).
    :return: The temporary email address as a string.
    :raises: TimeoutException if the email doesn't load within the specified time.
    """
    WebDriverWait(driver, timeout).until(is_email_loaded)  # Explicitly pass the helper function
    email_input = driver.find_element(By.ID, 'mail')
    return email_input.get_attribute("value")


def main():
    """
    Main function to initialize the WebDriver, navigate to the site,
    fetch the temp mail, and perform post-retrieval actions.
    """
    driver = configure_driver()  # Initialize the WebDriver

    try:
        driver.get("https://temp-mail.org/en/")

        # Wait for the email to load and retrieve it
        temp_email = wait_for_email_to_load(driver)
        print(f"Generated Temporary Email: {temp_email}")

        # Optionally save a screenshot of the page
        driver.save_screenshot("temp_mail_screenshot.png")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
