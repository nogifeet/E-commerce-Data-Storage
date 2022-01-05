setup.py 

---- Function draw_lines()
--------- Used to draw lines between console outputs

---- Function read_data(filename) 
--------- Accepts the path+filename.csv as argument
--------- Used to read data from csv files (orders,items,users)

---- Function populate_tables(connection)
--------- Accepts ecommerce_connection as argument 
--------- Generates cursor 
--------- Contains three nested functions

-------------- users_data()
--------------------- Function used to create users table 
--------------------- Calls read_data() function 
--------------------- defines insert query 
--------------------- inserts data into users table 

-------------- orders_data()
--------------------- Function used to create orders table 
--------------------- Calls read_data() function 
--------------------- defines insert query 
--------------------- inserts data into orders table 

-------------- items_data()
--------------------- Function used to create items table 
--------------------- Calls read_data() function 
--------------------- defines insert query 
--------------------- inserts data into items table 


---- Function create_customer_leaderboard(connection,data)
--------- Accepts ecommerce_connection and data(list of tuples) as argument
--------- creates customer_leaderboard table
--------- defines insert query 
--------- inserts data into customer_leaderboard table 

database.py 

No changes made in this python file 

SLL.py - Contains blueprint for Single Linked List to store data 

--------- class Node 
------------- Used to store Node data and next node pointer 

--------- class Linked List 
------------ contains four instance methods 

------------ addElement_Ending(data)
------------------ Accepts data in form of tuple/list 
------------------ inserts data at the end of the node 

------------ find_maximum()
------------------ return the maximum value order 

------------ find_minimum()
------------------ returns the minimum value order 

------------ print_all()
------------------ prints all linked list values 

main.py 

task descriptions are used as comments