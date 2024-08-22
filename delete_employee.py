# delete_employee.py
import time
import mysql.connector


def delete_employee(connection, identifier):
    try:
        cursor = connection.cursor()

        # Check if the identifier is numeric, indicating emp_id
        if identifier.isdigit():
            emp_id = int(identifier)
            # Check if the employee with the given emp_id exists
            cursor.execute("SELECT id FROM employees WHERE id = %s", (emp_id,))
        else:
            # Assume the identifier is a name, check if the employee with the given name exists
            cursor.execute("SELECT id FROM employees WHERE name = %s", (identifier,))

        existing_employee = cursor.fetchone()

        if existing_employee:
            # If the employee exists, delete them
            cursor.execute(
                "DELETE FROM employees WHERE id = %s", (existing_employee[0],)
            )
            print(
                f"Employee with {'ID' if identifier.isdigit() else 'Name'} {identifier} deleted successfully"
            )
            time.sleep(2)
        else:
            print(
                f"Employee with {'ID' if identifier.isdigit() else 'Name'} {identifier} not found. Unable to delete."
            )
            time.sleep(2)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(2)
