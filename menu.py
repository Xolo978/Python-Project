# menu.py
def menu():
    print("*" * 30)
    print("        Employee Management")
    print("*" * 30)
    print("Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Display Employees")
    print("5. Employee Statistics")
    print("6. Export Employee Data")
    print("7. Search Employee")
    print("8. Display Employee History")
    print("9. Exit")
    print("*" * 30)

    choice = input("Enter your choice (1-9): ")
    print("")
    return choice
