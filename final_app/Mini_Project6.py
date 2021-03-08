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


connection = pymysql.connect(
  host,
  user,
  password,
  database
)


cursor = connection.cursor()





from miniproject6_func import *






product_columns = ["ID","product", "price"]
courier_columns = ["ID","courier", "phone_number"]
order_columns = ["ID","customer_name", "customer_address", "customer_phone_number", "courier_id", "order_status"]
orders_products_column = ["order_id", "product_id"]









os.system('clear')


def app():

    logo()

    while True:
        choice = input(
            "Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 3 to go to the order menu \nEnter 0 to save and leave the app \nWhich option would you like?"
        )
        print(choice)

        os.system("clear")


        #Products
        while choice == "1":
            
            choice_product = input(
                "Enter 1 to view products \nEnter 2 to add a new product \nEnter 3 to update product \nEnter 4 to delete a product \nEnter 5 to return to main menu \nWhich option would you like? "
            )

            #display products list
            if choice_product == "1":
                os.system("clear")
                display_database("products", product_columns)
                
            #add item
            elif choice_product == "2":
                add_item_to_database("products", "ID", "product", "price", product_columns)
        
            #update item
            elif choice_product == "3":
                update_item_in_database("products", "ID", "product", "price", product_columns)

        
            #delete item   
            elif choice_product == "4":
                delete_item_in_database("products", "product", product_columns)

            #return to main menu
            elif choice_product == "5":
                os.system("clear")
                app()


            #Invalid option
            else:
                os.system("clear")                
                print(f"{choice_product} is not a valid option, please choose an option from the list below \n")




        #Couriers 
        while choice == "2":

            choice_courier = input(
                "Enter 1 to view couriers \nEnter 2 to add a new courier \nEnter 3 to update courier \nEnter 4 to delete a courier \nEnter 5 to return to main menu \nWhich option would you like? "
            )
       
            # display couriers list
            if choice_courier == "1":
                os.system("clear")
                display_database("couriers", courier_columns)

            #add item
            elif choice_courier == "2":
                add_item_to_database("couriers", "ID", "courier", "phone_number", courier_columns)
        
            #update item
            elif choice_courier == "3":
                os.system("clear")
                update_item_in_database("couriers", "ID", "courier", "phone_number", courier_columns)

        
            #delete item   
            elif choice_courier == "4":
                os.system("clear")
                delete_item_in_database("couriers", "courier", courier_columns)

            #return to main menu
            elif choice_courier == "5":
                os.system("clear")
                app()

            #Invalid option
            else:
                os.system("clear")
                print(f"{choice_courier} is not a valid option, please choose an option from the list below \n")
                


        #Orders
        while choice == "3":

            choice_order = input(
                "Enter 1 to view orders \nEnter 2 to create a new order \nEnter 3 to update order status \nEnter 4 to update an order \nEnter 5 to delete an order \nEnter 6 to view your order details \nEnter 7 to return to main menu \nWhich option would you like? "
            )


            #display products list 
            if choice_order == "1":
                os.system("clear")
                display_database("orders", order_columns)

            #add item 
            elif choice_order == "2":
                create_order()

            #update order status 
            elif choice_order == "3":
                os.system("clear")
                update_order_status()


            #update order  
            elif choice_order == "4":
                os.system("clear")
                update_order()

    

            #delete item  
            elif choice_order == "5":
                delete_item_in_database("orders", "order", order_columns)

            
            elif choice_order == "6":
                order_details()



            #return to main menu
            elif choice_order == "7":
                os.system("clear")
                app()

            
            #Invalid option
            else:
                os.system("clear")
                print(f"{choice_order} is not a valid option, please choose an option from the list below \n")
              



        #Exit app
        while choice == "0":
            print("Thank you, bye!")
            connection.close()
            sys.exit()
            


        # invalid option
        else:
            print(f"{choice} is not a valid option, please choose an option from the list below \n")









if __name__ == "__main__":
    app()
