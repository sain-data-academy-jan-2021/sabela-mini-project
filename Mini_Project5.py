import os
import sys
import csv
from tabulate import tabulate





from miniproject5_func import display_dict
from miniproject5_func import add_item_to_dict
from miniproject5_func import update_item_in_dict
from miniproject5_func import delete_item_in_dict
from miniproject5_func import write_csv_file




products = []


with open("product.csv","r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        products.append(row)

# for product in products:
#     print(product)

couriers = []


with open("courier.csv","r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        couriers.append(row)

# for courier in couriers:
#     print(courier)


orders = []


with open("order.csv","r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        orders.append(row)

# for order in orders:
#     print(order)











os.system('clear')


def app():

    choice = input(
        "Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 3 to go to the order menu \nEnter 0 to save and leave the app \nWhich option would you like?"
    )
    print(choice)

    os.system("clear")

    #Products
    while choice == "1":

        choice_product = input(
            "Enter 1 to view products \nEnter 2 to add a new product \nEnter 3 to update product \nEnter 4 to delete a product \nEnter 5 to return to main menu \nWhich option would you like?"
        )

        #display products list
        if choice_product == "1":
            display_dict("product", products)

        #add item
        if choice_product == "2":
            add_item_to_dict("product",products, "ID", "Product" ,"Price")

        #update item
        # os.system("clear")
        if choice_product == "3":
            update_item_in_dict("product",products, "ID", "Product" ,"Price")

        #delete item   
        # os.system("clear")
        if choice_product == "4":
            delete_item_in_dict("product",products, "ID", "Product" ,"Price")

        #return to main menu
        if choice_product == "5":
            os.system("clear")
            app()


    #Couriers 
    while choice == "2":

        choice_product = input(
            "Enter 1 to view couriers \nEnter 2 to add a new courier \nEnter 3 to update courier \nEnter 4 to delete a courier \nEnter 5 to return to main menu \nWhich option would you like?"
        )

        #display products list
        if choice_product == "1":
            display_dict("courier", couriers)

        #add item
        if choice_product == "2":
            add_item_to_dict("courier",couriers, "ID", "Courier" ,"Phone_Number")

        #update item
        # os.system("clear")
        if choice_product == "3":
            update_item_in_dict("courier",couriers, "ID", "Courier" ,"Phone_Number")

        #delete item   
        # os.system("clear")
        if choice_product == "4":
            delete_item_in_dict("courier", couriers)

        #return to main menu
        if choice_product == "5":
            os.system("clear")
            app()



    #Orders
    while choice == "3":

        choice_product = input(
            "Enter 1 to view orders \nEnter 2 to create a new order \nEnter 3 to update order status \nEnter 4 to update an order \nEnter 5 to delete an order \nEnter 6 to return to main menu \nWhich option would you like?"
        )

        #display products list
        if choice_product == "1":
            display_dict("order", orders)

        #add item - completeish data handling for products and couriers -- data persistance
if choice_order == "2":
                os.system("clear")
                print("order list:")

                make_list_into_table(orders)

                value_Order_ID = list_ID(orders)
                value_Customer_Name = input(f"What is your name?").capitalize()
                value_Customer_Address = input(f"What is your address?")
                value_Customer_Phone = input(f"What is your phone number?")

                os.system("clear")
                
                make_list_into_table(products)

                value_Product = input("What products would you like to order? Please enter the product ID's from the list above to select product")
                
                os.system("clear")

                for item in couriers:
                    print(item)
                

                
                value_Courier = int(input(f"Please select a courier using the ID from the list above?"))
                if value_Courier < len(couriers)+1:
                    
                    my_dict = {
                        "Order_ID":value_Order_ID,
                        "Customer_Name":value_Customer_Name,
                        "Customer_Address":value_Customer_Address,
                        "Customer_Phone":value_Customer_Phone,
                        "Product":value_Product,
                        "Courier":value_Courier,
                        "Order_Status": "Preparing"
                        }

            
                    orders.append(my_dict)


                    os.system("clear")

                    make_list_into_table(orders)

                    print(f"\nOrder has been created!")


                else:
                    print(f"{value_Courier} is an invalid ID. Please choose again")
                    continue

            

                with open("order.csv","a") as file:
                    writer = csv.writer(file, delimiter = ",")
                    writer.writerow([value_Order_ID,value_Customer_Name,value_Customer_Address,value_Customer_Phone,value_Product,value_Courier,"Preparing"])












        #update order status -incomplete
        # os.system("clear")
        if choice_product == "3":
            os.system("clear")
            print("order list")
            for item in orders:
                print(item)

            current_item_index = int(input(
                "What is the Order ID of the order you would like to update the status of? Or press 0 to return to order menu."
            ))
            
            os.system("clear")

            if current_item_index == 0:
                pass

            else:
                index = current_item_index - 1
                print(orders[index])

                # status = ["Preparing", "Ready", "Out for delivery", "Delivered"]

                # for item in status:
                #     print(item)

                new_order_status = input("What would you like to change the order status to? Please choose from th list above ")

                # if new_order_status in status:
                #     print("yay")

                # else:
                #     print("oops")

                orders[0]["Order_Status"] = new_order_status

                for item in orders:
                    print(item)





        #update order  - incomplete
        # os.system("clear")
        if choice_product == "4":
            
            print("orders list")
            for item in orders:
                print(item)

            current_item_index = int(input(
                f"What is the order ID of the order you would like to update? Or press 0 to return to {dict_type} menu."
            ))
            
            os.system("clear")

            if current_item_index == 0:
                pass

            else:

                try:
                    index = current_item_index - 1
                    print(list[index])

                    value_2 = input(f"Please enter the new name of the {key_2} or press enter to skip").capitalize
                    
                    if value_2 == "":
                        pass

                    else:
                        list[index][key_2] = value_2
                        
                    value_3 = input(f"Please enter the {key_3} of the new {key_2} or press enter to skip")
        
                    if value_3 == "":
                        pass
                        os.system("clear")
                        print(list[index])
                    else:
                        list[index][key_3] = value_3
                        os.system("clear")
                        print(list[index])
                        print(f"{list} has been updated")
                    

                except:
                    print(f"ID {current_item_index} does not exist")
                    print("\nplease choose an ID from the list below")
                    update_item_in_dict(dict_type, list, key_1, key_2, key_3)




        #delete item 
        if choice_product == "5":
            delete_item_in_dict("order", orders)

        #return to main menu
        if choice_product == "6":
            os.system("clear")
            app()




 
app()


