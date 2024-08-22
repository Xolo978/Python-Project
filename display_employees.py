# display_employees.py
import prettytable
import mysql.connector
import time

def display_employees(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        if employees:
            table = prettytable.PrettyTable()
            table.field_names = ["ID", "Name", "Designation", "Salary"]

            for employee in employees:
                table.add_row(employee)

            print("Employee List:")
            print(table)
            print("")
        else:
            print("No employees found")
            time.sleep(1)

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
