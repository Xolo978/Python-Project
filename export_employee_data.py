import time
import mysql.connector


def export_employee_data(connection, filename="employee_data.csv"):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        if employees:
            with open(filename, "w") as file:
                # Write header
                header = ["ID", "Name", "Designation", "Salary"]
                file.write(",".join(header) + "\n")

                # Write data
                for employee in employees:
                    file.write(",".join(map(str, employee)) + "\n")

            print(f"Employee data exported to {filename} successfully.")
            time.sleep(1)
        else:
            print("No employees found for export.")

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
