# load_sample_data.py
import mysql.connector
import random
import time


def load_sample_data(connection):
    try:
        cursor = connection.cursor()

        # Check if sample data has already been loaded
        cursor.execute("SELECT COUNT(*) FROM employees")
        existing_count = cursor.fetchone()[0]

        if existing_count > 0:
            print("Sample data has already been loaded. Skipping.")
            time.sleep(1)
            return

        # Sample employee data (unchanged)
        sample_data = [
            ("John Doe", "Software Engineer", 80000),
            ("Jane Smith", "Data Scientist", 90000),
            ("Bob Johnson", "Product Manager", 95000),
            ("Alice Williams", "UX Designer", 85000),
            ("Charlie Brown", "QA Engineer", 75000),
            ("Diana Davis", "Frontend Developer", 82000),
            ("Ethan Evans", "Backend Developer", 83000),
            ("Fiona Fisher", "Database Administrator", 88000),
            ("George Green", "Network Engineer", 78000),
            ("Helen Harris", "Business Analyst", 92000),
            ("Ian Ingram", "Project Manager", 97000),
            ("Jenna Jackson", "DevOps Engineer", 86000),
            ("Kevin King", "UI Designer", 79000),
            ("Laura Lee", "System Administrator", 93000),
            ("Mike Miller", "Mobile App Developer", 94000),
            ("Nina Nguyen", "Security Analyst", 87000),
            ("Oscar Olson", "Technical Writer", 80000),
            ("Pam Parker", "IT Support Specialist", 77000),
            ("Quincy Quinn", "Full Stack Developer", 91000),
            ("Rita Rodriguez", "Software Tester", 76000),
        ]

        # Insert sample data into the 'employees' table
        insert_query = (
            "INSERT INTO employees (name, designation, salary) VALUES (%s, %s, %s)"
        )
        cursor.executemany(insert_query, sample_data)

        print("Sample data loaded successfully.")
        time.sleep(1)

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(1)
