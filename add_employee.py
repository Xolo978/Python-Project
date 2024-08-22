# add_employee.py
import time
import mysql.connector


def add_employee(connection, name, designation, salary):
    try:
        cursor = connection.cursor()

        # Check if the employee with the given name already exists
        cursor.execute("SELECT id FROM employees WHERE name = %s", (name,))
        existing_employee = cursor.fetchone()

        if existing_employee:
            print(f"Employee with name '{name}' already exists. Skipping insertion.")
            time.sleep(2)
        else:
            # If the employee does not exist, generate and increment emp_id
            cursor.execute("SELECT MAX(id) FROM employees")
            max_id = cursor.fetchone()[0]
            emp_id = 1 if max_id is None else max_id + 1

            # Insert the new employee
            cursor.execute(
                """
                INSERT INTO employees (id, name, designation, salary)
                VALUES (%s, %s, %s, %s)
            """,
                (emp_id, name, designation, salary),
            )

            print(f"Employee added successfully with ID: {emp_id}")
            time.sleep(2)

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(2)
