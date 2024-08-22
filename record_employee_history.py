import mysql.connector


def record_employee_history(connection, emp_id, change_type, change_description):
    try:
        cursor = connection.cursor()

        # Insert a new record into employee_history
        insert_query = "INSERT INTO employee_history (emp_id, change_type, change_description) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (emp_id, change_type, change_description))

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
