import csv
import database as db

def draw_lines():
    '''
    Function Used to draw lines
    '''
    print('-'*50, end='\n\n')

def read_data(filename):
    '''
    Function Used to read csv files
    '''
    with open(filename, 'r') as f:
        val = []
        data = csv.reader(f)
        for row in data:
            data = [i if i!='' else None for i in row]
            val.append(data)
        val.pop(0)
    
    return val 

def populate_tables(connection):

    mycursor = connection.cursor()    

    def users_data():

        '''
        Function used to create and insert multiple data for users table
        '''

        # create users table 
        mycursor.execute("CREATE TABLE USERS(USER_ID VARCHAR(10) PRIMARY KEY, USER_NAME VARCHAR(45), USER_EMAIL VARCHAR(45), USER_PASSWORD VARCHAR(45), USER_ADDRESS VARCHAR(45), IS_VENDOR TINYINT(1))")

        #read users data using read_data function
        users_data = read_data(r'../config/users.csv')

        users_sql = "INSERT INTO USERS (USER_ID, USER_NAME, USER_EMAIL, USER_PASSWORD, USER_ADDRESS, IS_VENDOR) VALUES (%s, %s, %s, %s, %s, %s)"

        #insert data into table 
        db.insert_many_data(connection,users_sql,users_data)

    def orders_data():

        '''
        Function used to create and insert multiple data for orders table
        '''
 
        # create orders table 
        mycursor.execute("CREATE TABLE ORDERS(ORDER_ID INT, CUSTOMER_ID VARCHAR(10),VENDOR_ID VARCHAR(10),TOTAL_VALUE DOUBLE(10,2),ORDER_QUANTITY INT,REWARD_POINT INT, PRIMARY KEY(ORDER_ID), FOREIGN KEY(CUSTOMER_ID) REFERENCES USERS(USER_ID), FOREIGN KEY(VENDOR_ID) REFERENCES USERS(USER_ID))")

        orders_sql = "INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, VENDOR_ID, TOTAL_VALUE, ORDER_QUANTITY, REWARD_POINT) VALUES (%s, %s, %s, %s, %s, %s)"

        #read orders data using read_data function
        orders_data = read_data(r'../config/orders.csv')

        #insert data into table 
        db.insert_many_data(connection,orders_sql,orders_data)

    def items_data():

        '''
        Function used to create and insert multiple data for items table
        '''
        # create items table 
        mycursor.execute("CREATE TABLE ITEMS(PRODUCT_ID VARCHAR(45),PRODUCT_NAME VARCHAR(45),PRODUCT_PRICE DOUBLE(10,2),PRODUCT_DESCRIPTION VARCHAR(100),VENDOR_ID VARCHAR(10),EMI_AVAILABLE VARCHAR(10), PRIMARY KEY(PRODUCT_ID), FOREIGN KEY(VENDOR_ID) REFERENCES USERS(USER_ID))")

        items_sql = "INSERT INTO ITEMS (PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_DESCRIPTION, VENDOR_ID, EMI_AVAILABLE) VALUES (%s, %s, %s, %s, %s, %s)"

        #read items data using read_data function
        items_data = read_data(r'../config/items.csv')

        #insert data into table 
        db.insert_many_data(connection,items_sql,items_data)

    #function calls
    users_data()
    orders_data()
    items_data()

def create_customer_leaderboard(connection,data):
        '''
        Function used to create and insert data into customer_leaderboard
        '''

        mycursor = connection.cursor()

        #create customer_leaderboard table 
        mycursor.execute("CREATE TABLE CUSTOMER_LEADERBOARD(CUSTOMER_ID VARCHAR(10), CUSTOMER_NAME VARCHAR(50), CUSTOMER_EMAIL VARCHAR(50),TOTAL_VALUE DOUBLE(10,2), PRIMARY KEY(CUSTOMER_ID))")

        insert_query = "INSERT INTO CUSTOMER_LEADERBOARD(CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_EMAIL,TOTAL_VALUE) VALUES (%s, %s, %s, %s)"

        #insert data into table 
        db.insert_many_data(connection,insert_query,data)

