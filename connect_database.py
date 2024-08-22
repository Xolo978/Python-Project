# connect_database.py
import mysql.connector
import time


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="PrithviB44", database="employee"
        )
        print("Connected to the database")
        time.sleep(2)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(2)
        return None
