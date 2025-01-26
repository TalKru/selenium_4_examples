import mysql.connector
from mysql.connector import Error


def create_connection(host: str, port: int, user: str, password: str, database: str):
    """
    Creates and returns a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connection to the database was successful.")
        return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database.")
        return None


def execute_query(connection, query: str, params: tuple = None):
    """
    Executes an INSERT, UPDATE, or DELETE query.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            print("Query executed successfully.")
    except Error as e:
        print(f"Error: '{e}' occurred while executing the query.")


def fetch_query_results(connection, query: str, params: tuple = None):
    """
    Executes a SELECT query and fetches the results.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
    except Error as e:
        print(f"Error: '{e}' occurred while fetching data.")
        return None


# Main function to demonstrate database operations.
def main():
    # Connection configuration
    connection = create_connection(
        host="localhost",
        port=3307,  # Change to your MySQL port
        user="root",
        password="root",
        database="mydb"
    )

    if connection is None:
        print("Exiting due to connection failure.")
        return

    # INSERT example
    insert_query = "INSERT INTO student (sid, sname) VALUES (%s, %s)"
    execute_query(connection, insert_query, (104, 'Kim'))

    # UPDATE example
    update_query = "UPDATE student SET sname = %s WHERE sid = %s"
    execute_query(connection, update_query, ('Mary', 104))

    # DELETE example
    delete_query = "DELETE FROM student WHERE sid = %s"
    execute_query(connection, delete_query, (104,))

    # SELECT example
    select_query = "SELECT * FROM orders"
    results = fetch_query_results(connection, select_query)

    if results:
        print("Orders table data:")
        for row in results:
            print(row)

    # Close connection
    if connection.is_connected():
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
