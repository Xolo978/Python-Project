import time
from connect_database import connect_to_database
from create_tables import create_employee_table
from add_employee import add_employee
from delete_employee import delete_employee
from update_employee import update_employee
from display_employees import display_employees
from employee_stats import employee_stats
from export_employee_data import export_employee_data
from record_employee_history import record_employee_history
from display_employee_history import display_employee_history
from menu import menu
from search_employee import search_employee
from load_sample_data import load_sample_data


def main():
    connection = connect_to_database()

    if connection:
        create_employee_table(connection)
        load_sample_data(connection)

        while True:
            choice = menu()

            if choice == "1":
                # Add Employee
                name = input("Enter employee name: ")
                designation = input("Enter employee designation: ")
                salary = int(input("Enter employee salary: "))
                add_employee(connection, name, designation, salary)
                time.sleep(1)
            elif choice == "2":
                # Remove Employee
                identifier = input("Enter employee ID or name to remove: ")
                delete_employee(connection, identifier)
                time.sleep(1)
            elif choice == "3":
                # Update Employee
                emp_id = input("Enter employee ID to update: ")
                update_employee(connection, emp_id)
                time.sleep(1)
            elif choice == "4":
                # Display Employee Status
                display_employees(connection)
                time.sleep(1)
            elif choice == "5":
                # Employee Statistics
                employee_stats(connection)
                time.sleep(1)
            elif choice == "6":
                # Export Employee Data
                filename = input(
                    "Enter the filename to export (press Enter for default): "
                )
                export_employee_data(
                    connection, filename if filename else "employee_data.csv"
                )
                time.sleep(1)
            elif choice == "7":
                # Search Employee
                search_term = input("Enter search term (Name or ID): ")
                search_employee(connection, search_term)
                time.sleep(1)
            elif choice == "8":
                # Display Employee History
                emp_id = input("Enter employee ID to view history: ")
                display_employee_history(connection, emp_id)
                time.sleep(1)
            elif choice == "9":
                # Exit the program
                print("Exiting the program.")
                time.sleep(1)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
                time.sleep(1)

        connection.close()
        print("Connection closed")
        time.sleep(1)


if __name__ == "__main__":
    main()
