# search_employee.py
import mysql.connector
import prettytable
import time


def search_employee(connection, search_term):
    try:
        cursor = connection.cursor()

        # Check if the search term is numeric, indicating an ID search
        if search_term.isdigit():
            cursor.execute("SELECT * FROM employees WHERE id = %s", (int(search_term),))
        else:
            # Search for employees based on the given term in name
            cursor.execute(
                "SELECT * FROM employees WHERE name LIKE %s", (f"%{search_term}%",)
            )

        search_results = cursor.fetchall()

        if search_results:
            table = prettytable.PrettyTable()
            table.field_names = ["ID", "Name", "Designation", "Salary"]

            for result in search_results:
                table.add_row(result)

            print("Search Results:")
            print(table)
            print("")
        else:
            print(f"No employees found matching the search term: {search_term}")
            print("")

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(1)
