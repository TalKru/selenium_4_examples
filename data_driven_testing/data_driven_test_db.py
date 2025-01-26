import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import mysql.connector
from mysql.connector import Error


# Setup logging for better traceability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)


def create_db_connection(host: str, port: int, user: str, password: str, database: str):
    """
    Creates and returns a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=host, port=port, user=user, passwd=password, database=database
        )
        if connection.is_connected():
            logging.info("Connected to the database successfully.")
        return connection
    except Error as e:
        logging.error(f"Error connecting to the database: {e}")
        return None


def fetch_data_from_db(connection, query: str):
    """
    Executes a SELECT query and fetches the data.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except Error as e:
        logging.error(f"Error fetching data: {e}")
        return None


def setup_webdriver(chromedriver_path: str):
    """
    Initializes and returns a Selenium WebDriver instance.
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        logging.info("WebDriver initialized successfully.")
        return driver
    except Exception as e:
        logging.error(f"Error initializing WebDriver: {e}")
        raise


def fill_fd_form(driver, principal, interest_rate, tenure, tenure_period, frequency):
    """
    Fills in the Fixed Deposit form on the webpage.
    """
    driver.find_element(By.XPATH, "//input[@id='principal']").clear()
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)

    driver.find_element(By.XPATH, "//input[@id='interest']").clear()
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(interest_rate)

    driver.find_element(By.XPATH, "//input[@id='tenure']").clear()
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(tenure)

    period_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    period_dropdown.select_by_visible_text(tenure_period)

    frequency_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)


def validate_results(driver, expected_value):
    """
    Validates the calculated maturity value against the expected value.
    """
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # Calculate button
    time.sleep(2)

    actual_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    if float(expected_value) == float(actual_value):
        logging.info(f"Test passed. Expected: {expected_value}, Actual: {actual_value}")
    else:
        logging.warning(f"Test failed. Expected: {expected_value}, Actual: {actual_value}")

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # Clear button


def main():
    """
    Main function to execute the Selenium + MySQL workflow.
    """
    # Database and WebDriver configuration
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database": "mydb",
    }
    chromedriver_path = "C:/Drivers/chromedriver_win32/chromedriver.exe"
    query = "SELECT principal, interest_rate, tenure, tenure_period, frequency, expected_maturity FROM caldata"

    # Initialize database connection
    connection = create_db_connection(**db_config)
    if not connection:
        logging.error("Exiting due to database connection failure.")
        return

    # Fetch data from database
    data = fetch_data_from_db(connection, query)
    if not data:
        logging.error("No data retrieved. Exiting...")
        connection.close()
        return

    # Initialize WebDriver
    driver = setup_webdriver(chromedriver_path)

    try:
        # Open the target webpage
        driver.get(
            "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
        )

        # Process each row from the database
        for row in data:
            principal, interest_rate, tenure, tenure_period, frequency, expected_maturity = row
            fill_fd_form(driver, principal, interest_rate, tenure, tenure_period, frequency)
            validate_results(driver, expected_maturity)

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

    finally:
        # Cleanup resources
        driver.quit()
        connection.close()
        logging.info("Execution completed. Resources cleaned up.")


if __name__ == "__main__":
    main()
