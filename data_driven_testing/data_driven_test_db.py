import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
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
        raise


def fetch_data_from_db(connection, query: str):
    """
    Executes a SELECT query and fetches the data.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data

    except Error as e:
        logging.error(f"Error fetching data from database: {e}")
        raise


def setup_webdriver():
    """
    Initializes and returns a Selenium WebDriver instance.
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")

        driver = webdriver.Chrome(options=chrome_options)
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
    try:
        driver.find_element(By.ID, "principal").clear()
        driver.find_element(By.ID, "principal").send_keys(principal)

        driver.find_element(By.ID, "interest").clear()
        driver.find_element(By.ID, "interest").send_keys(interest_rate)

        driver.find_element(By.ID, "tenure").clear()
        driver.find_element(By.ID, "tenure").send_keys(tenure)

        Select(driver.find_element(By.ID, "tenurePeriod")).select_by_visible_text(tenure_period)
        Select(driver.find_element(By.ID, "frequency")).select_by_visible_text(frequency)

    except Exception as e:
        logging.error(f"Error filling the form: {e}")
        raise


def validate_results(driver, expected_value):
    """
    Validates the calculated maturity value against the expected value.
    """
    try:
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # Calculate button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='resp_matval']/strong"))
        )
        actual_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        try:
            expected = float(expected_value)
            actual = float(actual_value)
        except ValueError:
            logging.error(f"Validation failed. Non-numeric values encountered: {expected_value}, {actual_value}")
            return

        if expected == actual:
            logging.info(f"Test passed. Expected: {expected}, Actual: {actual}")
        else:
            logging.warning(f"Test failed. Expected: {expected}, Actual: {actual}")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # Clear button
    except Exception as e:
        logging.error(f"Error validating results: {e}")
        raise


def main():
    """
    Main function to execute the Selenium + MySQL workflow.
    """
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database": "mydb",
    }
    query = "SELECT principal, interest_rate, tenure, tenure_period, frequency, expected_maturity FROM caldata"

    connection = None
    driver = None

    try:
        # Connect to the database
        connection = create_db_connection(**db_config)
        data = fetch_data_from_db(connection, query)

        # Set up and initialize WebDriver
        driver = setup_webdriver()
        driver.get(
            "https://www.moneycontrol.com/fixed-income/calculator/"
            "state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
        )

        # Process data and validate results
        for row in data:
            logging.debug(f"Processing row: {row}")
            fill_fd_form(driver, *row[:-1])
            validate_results(driver, row[-1])

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        if driver:
            driver.quit()
        if connection and connection.is_connected():
            try:
                connection.close()
            except Error as e:
                logging.error(f"Error closing database connection: {e}")
        logging.info("Resources cleaned up.")


if __name__ == "__main__":
    main()
