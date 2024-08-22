# create_tables.py
import time
import mysql.connector


def create_employee_table(connection):
    try:
        cursor = connection.cursor()

        # Create the employee table if it does not exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                designation VARCHAR(255),
                salary INT
            )
        """
        )

        # Create the employee_history table if it does not exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employee_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                emp_id INT,
                change_type VARCHAR(255),
                change_description VARCHAR(255),
                change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (emp_id) REFERENCES employees(id)
            )
        """
        )

        print("Employee tables created successfully.")

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(1)
