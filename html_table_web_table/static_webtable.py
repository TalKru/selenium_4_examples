
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

WEB_URL = 'https://testautomationpractice.blogspot.com/'
WAIT_TIME_SEC = 10

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless=new")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEB_URL)

    """
    HTML table (or web table) is a matrix of rows and cols with data
    
    +--------------------------------------------+
    |   X    |   Y    |    Z   |   M    |   R    |
    +--------------------------------------------+
    |   12   |   75   |   83   |   10   |   5    |
    +--------------------------------------------+
    |        |        |        |        |        |
    +--------------------------------------------+

    Everything between <td> and </td> are the content of the table cell.
    Each table row starts with a <tr> and ends with a </tr> tag.
    
    <table>
      <tr>
        <td>Emil</td>
        <td>Tobias</td>
        <td>Linus</td>
      </tr>
      <tr>
        <td>16</td>
        <td>14</td>
        <td>10</td>
      </tr>
    </table>
    
    
    <table>	Defines a table
    <th>	Defines a header cell in a table
    <tr>	Defines a row in a table
    <td>	Defines a cell in a table
    <caption>	Defines a table caption
    <colgroup>	Specifies a group of one or more columns in a table for formatting
    <col>	Specifies column properties for each column within a <colgroup> element
    <thead>	Groups the header content in a table
    <tbody>	Groups the body content in a table
    <tfoot>	Groups the footer content in a table
    """

    # locate the table element
    # table_element = driver.find_element(By.XPATH, "//table[@name='BookTable']")

    # -------------------------------------------------------------------------------------------------
    # Count number of rows & columns (including headers)
    count_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
    count_cols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))

    print(f'Number of rows in the table: {count_rows}')
    print(f'Number of columns in the table: {count_cols}')

    # -------------------------------------------------------------------------------------------------
    # Read specific row & Column data  - Master In Selenium
    # similar to a matrix, we can pass row and col index, but inside XPATH locator ...tr[5]/td[1]
    cell_data1 = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
    cell_data2 = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[7]/td[3]").text
    cell_data3 = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[6]/td[4]").text

    print(f'data from cells: {cell_data1},  {cell_data2},  {cell_data3}')

    # -------------------------------------------------------------------------------------------------
    # Read all the rows & Columns data
    print("...............printing all the rows and columns data...............")

    for r in range(2, count_rows + 1):       # 2 because we skip the header row
        for c in range(1, count_cols + 1):

            cell_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
            print(f'[ {cell_data} ]', end='\t\t\t')
        print(end='\n')

    # -------------------------------------------------------------------------------------------------
    # Read data based on condition (List books name whose author is Amit)
    author_name = 'Amit'

    for row in range(2, count_rows + 1):

        author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[2]").text

        if author == author_name:  # print book names by Amit
            book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[1]").text
            price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[4]").text
            print(f'Book name: {book_name}, by: {author_name}, price: {price}')

    driver.quit()
