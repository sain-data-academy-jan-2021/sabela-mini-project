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
order_columns = ["ID","customer_name", "customer_address", "customer_phone_number", "products", "courier_id", "order_status"]





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
            # return value_product

        else:
            break

    return value_product        
    print(f"{value_product} products have been added")


# def updating():
#     value = input("")
    




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



# update list - completish --------datahandling if possible
def update_item_in_database(list_type, key_1, key_2, key_3, columns):

    display_database(list_type, columns)

    item_index = int(input(f"What is the ID of the {list_type} you would like to update? Or press 0 to return to {list_type} menu. "))
    
    os.system("clear")

    if item_index == 0:
        pass

    else:

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from {list_type} where id={item_index}")
        cursor.close()

        if row_exists == 1:

            value_2 = input(f"Please enter the new name of the {key_2} or press enter to skip ").capitalize()
            
            if value_2 == "":
                pass

            else:

                cursor = connection.cursor()

                cursor.execute(f"UPDATE {list_type} SET {key_2} = '{value_2}' WHERE id = '{item_index}'")

                connection.commit()
                cursor.close()     


            value_3 = input(f"Please enter the {key_3} of the new {key_2} or press enter to skip ")
 
            if value_3 == "":
                pass
                os.system("clear")
                

            else:

                cursor = connection.cursor()

                cursor.execute(f"UPDATE {list_type} SET {key_3} = '{value_3}' WHERE id = '{item_index}'")

                connection.commit()
                cursor.close()
            
                os.system("clear")

                display_database(list_type, key_1, key_2, key_3)
                print(f"{list_type} has been updated")
            

        else:
            print(f"{key_2} {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            update_item_in_database(list_type, key_1, key_2, key_3)




# delete item off list ---- completish , see if it's possible to do data handling otherwise complete, improve confirmation part
# os.system("clear")
def delete_item_in_database(list_type, name, columns):


    display_database(list_type, columns)

    item_index = int(input(f"What is the ID of the {list_type} you would like to delete? Or press 0 to return to {list_type} menu."))
    os.system("clear")

    if item_index == 0:
        pass

    else:

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from {list_type} where {name}_id={item_index}")
        cursor.close()

        if row_exists == 1:

            confirmation = input(f"Are you sure you want to delete {list_type} {item_index}? Press 1 to confirm or 0 to go back to {list_type} menu.")

            if confirmation == "0":
                print(f"{list_type} {item_index} has not been deleted\n")
                pass

            else:
                print(row_exists)
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM {list_type} WHERE {name}_id ={item_index}")

                connection.commit()
                cursor.close()

                print(f"\n{list_type} {item_index} has been deleted")


        else:
            
            print(f"ID {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            delete_item_in_database(list_type, columns)
            
  


#Only Orders functionality
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#incomplete - data handling for couriers
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
    
    
    # cursor = connection.cursor()

    # cursor.execute(f'INSERT INTO orders ("order_columns") VALUES ("{value_product})')

    # connection.commit()
    # cursor.close()

    connecting_to_database(f"INSERT INTO orders ("customer_name", "customer_address", "customer_phone_number", "products", "courier_id", "order_status") VALUES ({value_customer_name}, {value_customer_address}, {value_customer_phone}, {value_product}, {value_courier}, {order_status})")





#LINES 283/284 AND DATA HANDLING FOR ORDER_STATUS NEEDS TO BE CHECKED
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
        #display the specific order
        #datahandling for item_index here

        status = ["Preparing", "Ready", "Out for delivery", "Delivered"]

        for item in status:
            print(item)

        new_order_status = input("\nWhat would you like to change the order status to? Please choose from the list above ").capitalize()

        if new_order_status in status:
            
            cursor = connection.cursor()

            cursor.execute(f"UPDATE orders SET order_status = '{new_order_status}' WHERE order_id = '{item_index}'")

            connection.commit()
            cursor.close()

        else:
            print("Status not recognised, please choose from the list.\n")
            pass




#database 
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def connecting_to_database(sql):

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()
    cursor.close()




