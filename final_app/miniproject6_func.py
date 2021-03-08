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
orders_products_column = ["order_id", "product_id"]




def logo():
    print(
        """
        *****************************
        *****************************
              JAMS FRUITS STALL        
        *****************************
        *****************************
        """
    )


def fetching_data(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    output = cursor.fetchall()
    cursor.close()

    return output


def check_if_data_exists(sql):
    cursor = connection.cursor()
    row_exists = cursor.execute(f"select * from orders_products where product_id={item_index}")
    cursor.close()


#add products to orders---------DATA HANDLING FOR PRODCUTS REQUIRED
def add_products_to_order():

    value_product = []

    display_database("products", product_columns)

   

    while True:

        try:
            
            products = int(input("What products would you like to order? Please enter the product IDs from the list above to select product and 0 to stop choosing "))

            if products != 0:
                value_product.append(products)

            else:
                break

        except ValueError:
            os.system("clear")
            print("Invalid entry, please choose again")
            

    return value_product
    




#the updating functionality
def updating(list_type, name, question, key, item_index):

    value = input(f"Please enter the new {question} or press enter to skip ").capitalize()
            
    if value == "":
        pass

    else:

        connecting_to_database(f"UPDATE {list_type} SET {key} = '{value}' WHERE {name}_id = '{item_index}'")



#ERROR AND DATA HANDLING DONE
def delete_product_from_orders(order_id):

    current_products = fetching_data(f"SELECT p.product_id, p.product FROM orders_products o INNER JOIN products p ON o.product_id = p.product_id AND o.order_id = {order_id}")

    print("These are your current products:")

    for x in current_products:
        print(f"{x[0]}:{x[1]}") 

    try: 

        item_index = int(input(f"What is the ID of the product you would like to delete? ."))
        os.system("clear")


        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from orders_products where product_id={item_index}")
        cursor.close()



        if row_exists == 1:

            confirmation = input(f"Are you sure you want to delete product {item_index}? Press 1 to confirm or 0 to return.")

            if confirmation == "0":
                print(f"product {item_index} has not been deleted\n")
                pass

            else:

                connecting_to_database(f"DELETE FROM orders_products WHERE product_id ={item_index} and order_id = {order_id}")
                print(f"\n{list_type} {item_index} has been deleted")


        else:
            
            print(f"ID {item_index} does not exist")
            print("\nplease choose an ID from the list below")
            delete_product_from_orders()

    except:
        os.system("clear")
        print("Invalid entry, please choose again.")
        




# complete
def updating_products_in_orders(order_id):

    cursor = connection.cursor()
    cursor.execute(f"SELECT p.product_id, p.product FROM orders_products o INNER JOIN products p ON o.product_id = p.product_id AND o.order_id = {order_id}")
    current_products = cursor.fetchall()
    cursor.close()

    print("These are your current products:")
    
    for x in current_products:
        print(f"{x[0]}:{x[1]}") 
   
  
    value = input("\nPress 1 to update your products or press enter to skip ")

    if value == "":
        pass

    else:
        os.system("clear")
        product_choice = input("Please choose \n1 to add more products to your basket \n2 to delete a specific product in your basket \n0 to return to the updating your order ")

        if product_choice == "1":
            os.system("clear")

            value_product = add_products_to_order()
            
            for product in value_product:
                connecting_to_database(f"INSERT INTO orders_products (order_id, product_id) VALUES ({order_id}, {product})")
            

        if product_choice == "2":
            os.system("clear")
            delete_product_from_orders(order_id)

        if product_choice =="0":
            pass

            

def choose_courier():

    try:
        
        display_database("couriers", courier_columns)
        item_index = int(input(f"Please select a courier using the ID from the list above?"))

        cursor = connection.cursor()
        row_exists = cursor.execute(f"select * from couriers where courier_id={item_index}")
        cursor.close()

        if row_exists == 1:
            return item_index

        else:
            print("Invalid ID, please choose again")
            choose_courier()

    except ValueError:
        os.system("clear")
        print("Invalid entry. Please try again") 
        choose_courier()





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


# add_products_to_order()

# insert into database - DATA HANDLING DONE
def add_item_to_database(list_type, key_1, key_2, key_3, columns):
    os.system("clear")

    display_database(list_type, columns)

    value_2 = input(f"What is the name of the new {key_2}? ").capitalize()

    if list_type == "products":
    
        while True:
            try:
                price = float(input("What is the price of the new product? "))

                if isinstance(price,float) == True:
                    value_3 = "{:.2f}".format(price)
                    break
                
                else:
                    os.system("clear")
                    print("Invalid price, please enter again")

            except ValueError:
                os.system("clear")
                print("Invalid price, please enter again")

    
            

    if list_type == "couriers":
        
        while True:
            try:
                value_3 = str(input("What is the phone number of the new courier? "))

                if len(str(value_3)) == 11 and isinstance(int(value_3), int) == True:
                    break
                
                else:
                    os.system("clear")
                    print("Invalid phone number, please enter again")

            except ValueError:
                os.system("clear")
                print("Invalid phone number, please enter again")


    connecting_to_database(f'INSERT INTO {list_type} ({key_2}, {key_3}) VALUES ("{value_2}", {value_3})')

    os.system("clear")
    print(f"\nUpdated {list_type} list\n")
    display_database(list_type, columns)



# update list - ERROR HANDLING DONE 
def update_item_in_database(list_type, key_1, key_2, key_3, columns):

    display_database(list_type, columns)

    try:
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

        

    except ValueError:
        os.system("clear")
        print("Invalid entry. Please try again")   
        update_item_in_database(list_type, key_1, key_2, key_3, columns)


# delete item off list -----ERROR HANDLING DONE
def delete_item_in_database(list_type, name, columns):


    display_database(list_type, columns)

    try:

        item_index = int(input(f"What is the ID of the {name} you would like to delete? Or press 0 to return to {name} menu."))
        os.system("clear")

        if item_index == "0":
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

                    if list_type == "orders":

                        connecting_to_database(f"DELETE FROM orders_products WHERE order_id ={item_index}")
                        connecting_to_database(f"DELETE FROM {list_type} WHERE {name}_id ={item_index}")

                    else:
                        connecting_to_database(f"DELETE FROM {list_type} WHERE {name}_id ={item_index}")

                    print(f"\n{list_type} {item_index} has been deleted")


            else:
                
                print(f"ID {item_index} does not exist")
                print("\nplease choose an ID from the list below")
                delete_item_in_database(list_type, name, columns)

   
    except ValueError:
        os.system("clear")
        print("Invalid entry. Please try again") 
        delete_item_in_database(list_type, name, columns)
    
  


#Only Orders functionality
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#complete -DATA HANDLING AND ERROR DONE
def create_order():

    os.system("clear")
    
    
    value_customer_name = input("What is your name?").capitalize()
    value_customer_address = input("What is your address?")


    while True:
        try:
            value_customer_phone = str(input("What is your phone number?"))

            if len(str(value_customer_phone)) == 11 and isinstance(int(value_customer_phone), int) == True:
                break
            
            else:
                os.system("clear")
                print("Invalid phone number, please enter again")

        except ValueError:
            os.system("clear")
            print("Invalid phone number, please enter again")

    os.system("clear")

    value_product = add_products_to_order()

    os.system("clear")

    value_courier = choose_courier()
    print(value_courier)


    order_status = "Preparing"
    

    connecting_to_database(f"INSERT INTO orders (customer_name, customer_address, customer_phone_number, courier_id, order_status) VALUES ('{value_customer_name}', '{value_customer_address}', '{value_customer_phone}', {value_courier}, '{order_status}')")
    
    order_id = last_order_id()
    
    for product in value_product:
        connecting_to_database(f"INSERT INTO orders_products (order_id, product_id) VALUES ({order_id}, {product})")




#TABULATE THE STATUS LINE 290, DATA HANDLING DONE
def update_order_status():
    print("order list")
    display_database("orders", order_columns)

    try:

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

                while True:

                    status_index = int(input("Please choose a status from the list above. "))

                    if status_index in status:

                        new_order_status = status[status_index]
                        print("Status updated successfuly")
                        connecting_to_database(f"UPDATE orders SET order_status = '{new_order_status}' WHERE order_id = {item_index}")

                        break

                    else:
                        print("Invalid entry, please choose again")


            else:
                print(f"order {item_index} does not exist \nplease choose an ID from the list below")
                update_order_status()

    except ValueError:
        os.system("clear")
        print("Invalid entry, please choose again")
        update_order_status()  


#complete DATA AND ERROR HANDLING DONE
def update_order():

    print("orders list")
    display_database("orders", order_columns)

    try:

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

                updating_products_in_orders(item_index)

                display_database("couriers", courier_columns)
                updating("orders", "order", "courier id", "courier_id", item_index)

                
            else:
                print(f"order {item_index} does not exist")
                print("\nplease choose an ID from the list below")
                update_order()
            
    except ValueError:
        os.system("clear")
        print("Invalid entry, please try again")
        update_order()
     

    


#order history
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


def order_details():

    os.system("clear")

    display_database("orders", order_columns)

    order_id = input("Which order would you like to view the basket of ")

    os.system("clear")

    cursor = connection.cursor()
    cursor.execute(f"SELECT p.product_id, p.product FROM orders_products o INNER JOIN products p ON o.product_id = p.product_id AND o.order_id = {order_id}")
    current_products = cursor.fetchall()
    cursor.close()

    print("These are the products from your order:")
    product_details = []
    for x in current_products:
        product_details.append(x) 

    print(tabulate(product_details, headers=["product_id","product"]))
    print("\n")


# still need to work on this
def price_of_transaction():

    cursor = connection.cursor()
    cursor.execute(f"SELECT price FROM products WHERE product_id = 8")
    current_products = cursor.fetchall()[0][0]
    cursor.close()

    print(float(current_products))




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



# price_of_transaction()
# # view_basket()
# cursor = connection.cursor()
# cursor.execute(f"SELECT p.product_id, p.product FROM orders_products o INNER JOIN products p ON o.product_id = p.product_id AND o.order_id = 13")
# current_products = cursor.fetchall()
# cursor.close()

# product_list = []

# for product in current_products:
#     product_list.append(product[0])

# price_list = []

# for item in product_list:
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT price FROM products WHERE product_id = {item}")
#     price_product = cursor.fetchall()[0][0]
#     cursor.close()

#     price_list.append(price_product)

    



# print(price_list)
