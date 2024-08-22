# update_employee.py
from record_employee_history import record_employee_history
import time
import mysql.connector
import prettytable


def update_employee(connection, emp_id):
    try:
        cursor = connection.cursor()

        # Check if the employee with the given emp_id exists
        cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
        existing_employee = cursor.fetchone()

        if existing_employee:
            print("Existing Employee Details:")
            table = prettytable.PrettyTable()
            table.field_names = ["ID", "Name", "Designation", "Salary"]
            table.add_row(existing_employee)
            print(table)
            # Get updated information from the user
            new_name = input("Enter new name (press Enter to keep the current name): ")
            new_designation = input(
                "Enter new designation (press Enter to keep the current designation): "
            )
            new_salary = input(
                "Enter new salary (press Enter to keep the current salary): "
            )
            if new_name == "" and new_salary == "" and new_designation == "":
                print("Updation cancelled")
                time.sleep(1)
                return

            # Record changes in history
            if new_name:
                record_employee_history(
                    connection, emp_id, "Name Change", f"Changed name to {new_name}"
                )
            if new_designation:
                record_employee_history(
                    connection,
                    emp_id,
                    "Designation Change",
                    f"Changed designation to {new_designation}",
                )
            if new_salary:
                record_employee_history(
                    connection,
                    emp_id,
                    "Salary Change",
                    f"Changed salary to {new_salary}",
                )

            # Update the employee details
            update_query = "UPDATE employees SET"
            update_values = []

            if new_name:
                update_query += " name = %s,"
                update_values.append(new_name)
            if new_designation:
                update_query += " designation = %s,"
                update_values.append(new_designation)
            if new_salary:
                update_query += " salary = %s,"
                update_values.append(new_salary)

            # Remove the trailing comma and add the WHERE clause
            update_query = update_query.rstrip(",") + " WHERE id = %s"
            update_values.append(emp_id)

            # Execute the update query
            cursor.execute(update_query, tuple(update_values))

            print(f"Employee with ID {emp_id} updated successfully")
            time.sleep(1)
        else:
            print(f"Employee with ID {emp_id} not found. Unable to update.")
            time.sleep(1)

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(1)
