import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    """
    A class to manage database operations.
    """
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Establish a database connection.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to the database was successful.")
        except Error as e:
            print(f"Error: '{e}' occurred while connecting to the database.")

    def disconnect(self):
        """
        Close the database connection.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query: str, params: tuple = None):
        """
        Execute INSERT, UPDATE, or DELETE queries.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                print("Query executed successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while executing the query.")

    def fetch_query_results(self, query: str, params: tuple = None):
        """
        Execute SELECT queries and return results.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Error as e:
            print(f"Error: '{e}' occurred while fetching data.")
            return None


def main():
    """
    Main function to demonstrate database operations using the DatabaseManager class.
    """
    db_manager = DatabaseManager(
        host="localhost",
        port=3307,
        user="root",
        password="root",
        database="mydb"
    )

    db_manager.connect()

    # INSERT example
    insert_query = "INSERT INTO student (sid, sname) VALUES (%s, %s)"
    db_manager.execute_query(insert_query, (104, 'Kim'))

    # UPDATE example
    update_query = "UPDATE student SET sname = %s WHERE sid = %s"
    db_manager.execute_query(update_query, ('Mary', 104))

    # DELETE example
    delete_query = "DELETE FROM student WHERE sid = %s"
    db_manager.execute_query(delete_query, (104,))

    # SELECT example
    select_query = "SELECT * FROM orders"
    results = db_manager.fetch_query_results(select_query)

    if results:
        print("Orders table data:")
        for row in results:
            print(row)

    db_manager.disconnect()


if __name__ == "__main__":
    main()
