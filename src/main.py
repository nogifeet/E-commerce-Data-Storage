import database as db
from setup import populate_tables,create_customer_leaderboard,draw_lines
from SLL import LinkedList

# Driver code
if __name__ == "__main__":

    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    
    PW = "567894" 
    ROOT = "root"
    DB = "ecommerce_record" 
    LOCALHOST = "localhost"
    
    #create connection with mysql
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    #get cursor 
    mycursor = connection.cursor()

    try:
        #if ecommerce_record schema is present drop it 
        mycursor.execute("DROP DATABASE ECOMMERCE_RECORD")
    except: 
        print("Database ecommerce_record not present")

    #create ecommerce_record schema 
    db.create_switch_database(mycursor, DB, DB)

    #connect with ecommerce_record schemma (this is will be used as connection through the rest of code)
    ecommerce_connection = db.create_db_connection(LOCALHOST,ROOT,PW,DB)

    #insert method to perform insert operation on the user, items and orders tables with the data available in the relevant csv file
    populate_tables(ecommerce_connection)

    #Write logic to perform at least 5 insert operations in the orders table. These insert operations should be for different customers.
    orders_sql = "INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, VENDOR_ID, TOTAL_VALUE, ORDER_QUANTITY, REWARD_POINT) VALUES (%s, %s, %s, %s, %s, %s)"

    #order_id,customer_id,vendor_id,total_value,order_qunatity,reward_point
    db.create_insert_query(ecommerce_connection,(101,7,3,8100,3,200),orders_sql)
    db.create_insert_query(ecommerce_connection,(102,9,1,3290,1,100),orders_sql)
    db.create_insert_query(ecommerce_connection,(103,11,1,1100,4,100),orders_sql)
    db.create_insert_query(ecommerce_connection,(104,13,4,2000,3,200),orders_sql)
    db.create_insert_query(ecommerce_connection,(105,6,2,7905,5,300),orders_sql)


    #Write a read method that should fetch all the records that are available in the orders table and print it on the console.

    select_query = "SELECT * FROM ORDERS"

    result = db.select_query(ecommerce_connection,select_query)

    LL = LinkedList()

    if result:
        for row in result:
            LL.addElement_Ending(row)
    else:
        print("No records to display")

    LL.print_all()
    draw_lines()

    #Use the data fetched in the previous task to find the maximum and minimum value order from the orders table 

    print(f'Minimum Value {LL.find_minimum()} Maximum Value:{LL.find_maximum()} from orders table.')
    draw_lines()

    #print all the order details with total_value more than the average order value ordered from all users

    select_query_2 = "SELECT * FROM ORDERS WHERE TOTAL_VALUE > (SELECT AVG(TOTAL_VALUE) FROM ORDERS)"

    result_2 = db.select_query(ecommerce_connection,select_query_2)

    LL2 = LinkedList()

    if result_2:
        for row in result_2:
            LL2.addElement_Ending(row)
    
    else:
        print("No records to display")

    LL2.print_all()
    draw_lines()

    # Create a new table named customer_leaderboard(customer_id, total_value, customer_name,customer_email) and insert the highest ordered purchase for each of the registered customers.If there are no orders you can ignore that customer.

    select_query_3 = "(SELECT CUSTOMER_ID, USER_NAME, USER_EMAIL, MAX(TOTAL_VALUE) FROM ORDERS INNER JOIN USERS ON USERS.USER_ID = ORDERS.CUSTOMER_ID WHERE CUSTOMER_ID IN (SELECT DISTINCT(USER_ID) FROM USERS WHERE IS_VENDOR=0) GROUP BY CUSTOMER_ID) ORDER BY USER_NAME ASC"

    result_3 = db.select_query(ecommerce_connection, select_query_3)

    create_customer_leaderboard(ecommerce_connection,result_3)
    draw_lines()

    select_query_4 = "SELECT * FROM CUSTOMER_LEADERBOARD"

    result_4 = db.select_query(ecommerce_connection,select_query_4)

    print("Printing Rows from Customer_Leaderboard Table", end='\n\n')
    for row in result_4:
        print(row)