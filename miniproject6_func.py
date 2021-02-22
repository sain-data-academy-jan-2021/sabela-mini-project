import os
import sys
import csv
from tabulate import tabulate

import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
  host,
  user,
  password,
  database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()


product_columns = ["ID","product", "price"]
courier_columns = ["ID","courier", "phone_number"]
order_columns = ["ID","customer_name", "customer_address", "customer_phone_number", "courier_id", "order_status"]





# make list into table 
def make_list_into_table(list_type):
    header = list_type[0].keys()
    rows =  [x.values() for x in list_type]
    print(tabulate(rows, header))
    


#add products to orders---------figure out how to not make the question repeat
def add_products_to_order():

    value_product = []

    while True:
        
        products = int(input("What products would you like to order? Please enter the product IDs from the list above to select product and 0 to stop choosing "))

        if products != 0:
            value_product.append(products)

        else:
            break

    return value_product


#the updating functionality
def updating(list_type, name, question, key, item_index):

    value = input(f"Please enter the new {question} or press enter to skip ").capitalize()
            
    if value == "":
        pass

    else:

        connecting_to_database(f"UPDATE {list_type} SET {key} = '{value}' WHERE {name}_id = '{item_index}'")

    
# tabulate the display of current products, WORK ON THIS FIRST
def updating_products_in_orders():

    cursor = connection.cursor()
    # cursor.execute(f"SELECT * FROM orders_products WHERE order_id = {order_id}")
    cursor.execute(f"SELECT p.product_id, p.product FROM orders_products o INNER JOIN products p ON o.product_id = p.product_id AND o.order_id = 12")
    current_products = cursor.fetchall()
    cursor.close()

    print("These are your current products:")
    
    for x in current_products:
        print(f"{x[0]}:{x[1]}") 
   
  
    value = input("\nPress 1 to update your products or press enter to skip")

    if value == "":
        pass

    else:
        os.system("clear")
        product_choice = input("Please choose \n1 to add more products to your basket \n2 to change a specific product in your basket \n3 to delete your basket and choose again")



#Main functionality
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# view database
def display_database(list_type, columns):
    
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {list_type}")
    
    rows = cursor.fetchall()
    header = columns
    print(tabulate(rows,header))

    cursor.close()
    
    print("\n")




# insert into database
def add_item_to_database(list_type, key_1, key_2, key_3, columns):
    os.system("clear")

    display_database(list_type, columns)
    print("\n")

    value_2 = input(f"What is the name of the {key_2} to add?").capitalize()
    value_3 = input(f"What is the price of the {key_3} to add?")


    connecting_to_database(f'INSERT INTO {list_type} ({key_2}, {key_3}) VALUES ("{value_2}", {value_3})')

    print(f"\nUpdated {list_type} list\n")
    display_database(list_type, columns)



# update list
def update_item_in_database(list_type, key_1, key_2, key_3, columns):

    display_database(list_type, columns)

    item_index = int(input(f"What is the ID of the {key_2} you would like to update? Or press 0 to return to {list_type} menu. "))
    
    os.system("clear")

    if item_index == 0:
        pass

    else:

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from {list_type} where {key_2}_id={item_index}")
        cursor.close()

        if row_exists == 1:

            updating(list_type, key_2, f"name of the {key_2}", key_2, item_index)

            updating(list_type, key_2, key_3, key_3, item_index)

                
            os.system("clear")

            display_database(list_type, columns)
            print(f"{list_type} has been updated")
            

        else:
            print(f"{key_2} {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            update_item_in_database(list_type, key_1, key_2, key_3, columns)




# delete item off list 
def delete_item_in_database(list_type, name, columns):


    display_database(list_type, columns)

    item_index = int(input(f"What is the ID of the {name} you would like to delete? Or press 0 to return to {list_type} menu."))
    os.system("clear")

    if item_index == 0:
        pass

    else:

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from {list_type} where {name}_id={item_index}")
        cursor.close()

        if row_exists == 1:

            confirmation = input(f"Are you sure you want to delete {name} {item_index}? Press 1 to confirm or 0 to go back to {list_type} menu.")

            if confirmation == "0":
                print(f"{list_type} {item_index} has not been deleted\n")
                pass

            else:

                connecting_to_database(f"DELETE FROM {list_type} WHERE {name}_id ={item_index}")

                print(f"\n{list_type} {item_index} has been deleted")


        else:
            
            print(f"ID {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            delete_item_in_database(list_type, name, columns)
            
  


#Only Orders functionality
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#complete but incorporate orders_products table into th products section
def create_order():

    os.system("clear")
    
    
    value_customer_name = input("What is your name?").capitalize()
    value_customer_address = input("What is your address?")
    value_customer_phone = input("What is your phone number?")

    os.system("clear")
    
    display_database("products", product_columns)
    value_product = add_products_to_order()

    os.system("clear")

    display_database("couriers", courier_columns)
    value_courier = int(input(f"Please select a courier using the ID from the list above?"))

    order_status = "Preparing"
    

    connecting_to_database(f"INSERT INTO orders (customer_name, customer_address, customer_phone_number, courier_id, order_status) VALUES ('{value_customer_name}', '{value_customer_address}', '{value_customer_phone}', {value_courier}, '{order_status}')")
    
    order_id = last_order_id()
    
    for product in value_product:
        connecting_to_database(f"INSERT INTO orders_products (order_id, product_id) VALUES ({order_id}, {product})")




#TABULATE THE STATUS LINE 290
def update_order_status():
    print("order list")
    display_database("orders", order_columns)

    item_index = int(input(
        "What is the order ID of the order you would like to update the status of? Or press 0 to return to order menu."
    ))
    
    os.system("clear")

    if item_index == 0:
        pass

    else:
        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from orders where order_id={item_index}")
        cursor.close()

        if row_exists == 1:

            status = {
            1:"Preparing", 
            2:"Ready", 
            3:"Out for delivery", 
            4:"Delivered"
            }

            
            print(status)

            status_index = int(input("Please choose a status from the list above. "))

            new_order_status = status[status_index]
            print(new_order_status)
    
            connecting_to_database(f"UPDATE order SET order_status = '{new_order_status}' WHERE order_id = '{item_index}'")


        else:
            print(f"order {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            update_order()
          
update_order_status()

#complete - NEED TO CALL THE UPDATE PRODUCTS FUNCTION AFTER ITS FINISHED
def update_order():

    print("orders list")
    display_database("orders", order_columns)

    item_index = int(input(
        f"What is the order ID of the order you would like to update? Or press 0 to return to order menu. "
    ))
    
    os.system("clear")

    if item_index == 0:
        pass

    else:

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from orders where order_id={item_index}")
        cursor.close()

        if row_exists == 1:
            
            updating("orders", "order", "customer name", "customer_name", item_index)

            updating("orders", "order", "customer address", "customer_address", item_index)

            updating("orders", "order", "customer phone number", "customer_phone_number", item_index)

            # display_database("products", product_columns)
            # updating("orders", "order", "products", "products", item_index)

            display_database("couriers", courier_columns)
            updating("orders", "order", "courier id", "courier_id", item_index)
            
            
        else:
            print(f"order {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            update_order()
          

     

    





#database 
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def connecting_to_database(sql):

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()
    cursor.close()


def last_order_id():

    cursor = connection.cursor()

    cursor.execute("SELECT MAX(order_id) from orders")
    order_id = cursor.fetchall()
    

    cursor.close()
    return order_id[0][0]

