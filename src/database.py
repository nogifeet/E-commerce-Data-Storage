import mysql.connector
import random
import time
import datetime

# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):

    # Implement the logic to create the server connection
    cursor = mysql.connector.connect(host = host_name, user = user_name, password = user_password)

    return cursor

# This method will create the database
def create_switch_database(connection, db_name, switch_db):
    # For database creation use this method
    # If you have created your databse using UI, no need to implement anything
    connection.execute(f"CREATE DATABASE {db_name}")

    print(f"Database {db_name} created!")



# This method will establish the connection with the newly created DB 
def create_db_connection(host_name, user_name, user_password, db_name):

    cursor = mysql.connector.connect(host = host_name, user = user_name, password = user_password, database=db_name)

    print(f"Database {db_name} connected!")

    return cursor

# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, data, query):

    cursor = connection.cursor()
    cursor.execute(query,data)

    connection.commit()
    print("Record Inserted!")


    
# retrieving the data from the table based on the given query
def select_query(connection, query):

    mycursor = connection.cursor()

    mycursor.execute(query)

    results = mycursor.fetchall()

    return results

# performing the execute many query over the table, 
# this method will help us to inert multiple records using a single instance
def insert_many_data(connection, sql, val):

    # to perform multiple insert operation in the database
    cursor = connection.cursor()

    cursor.executemany(sql,list(val))

    connection.commit()

    print(cursor.rowcount, "rows inserted.")
