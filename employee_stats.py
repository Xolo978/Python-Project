import prettytable
import mysql.connector


def employee_stats(connection):
    try:
        cursor = connection.cursor()

        # Get the total number of employees
        cursor.execute("SELECT COUNT(*) FROM employees")
        total_employees = cursor.fetchone()[0]

        # Get the highest salary
        cursor.execute("SELECT MAX(salary) FROM employees")
        highest_salary = cursor.fetchone()[0]

        # Get the lowest salary
        cursor.execute("SELECT MIN(salary) FROM employees")
        lowest_salary = cursor.fetchone()[0]

        # Get the average salary
        cursor.execute("SELECT AVG(salary) FROM employees")
        average_salary = cursor.fetchone()[0]

        # Display the statistics
        # Create a PrettyTable object
        table = prettytable.PrettyTable()
        table.field_names = ["Statistic", "Value"]

        # Add data to the table
        table.add_row(["Total Employees", total_employees])
        table.add_row(["Highest Salary", highest_salary])
        table.add_row(["Lowest Salary", lowest_salary])
        table.add_row(["Average Salary", f"{average_salary:.2f}"])

        # Display the table
        print("Employee Statistics:")
        print(table)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
