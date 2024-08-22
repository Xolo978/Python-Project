import mysql.connector
import prettytable


def display_employee_history(connection, emp_id):
    try:
        cursor = connection.cursor()

        # Check if the employee with the given emp_id exists
        cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
        existing_employee = cursor.fetchone()

        if existing_employee:
            print(f"Employee History for ID {emp_id}:")

            # Display history for the employee
            cursor.execute(
                "SELECT * FROM employee_history WHERE emp_id = %s", (emp_id,)
            )
            history_entries = cursor.fetchall()
            if history_entries:
                table = prettytable.PrettyTable()
                table.field_names = ["Change Type", "Description", "Timestamp"]
                for entry in history_entries:
                    table.add_row([entry[2], entry[3], entry[4]])
                print(table)
                print("")
            else:
                print("No history entries found for this employee.")
                print("")
        else:
            print(f"Employee with ID {emp_id} not found.")
            print("")

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
