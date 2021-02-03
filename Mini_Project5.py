import os
import sys
import csv




from miniproject5_func import display_dict
from miniproject5_func import add_item_to_dict
from miniproject5_func import update_item_in_dict
from miniproject5_func import delete_item_in_dict




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
        print(choice)
        #display products list-complete
        if choice_product == "1":
            display_dict("product", products)

        #add item- still need to do data persistance add £ to price
        if choice_product == "2":
            add_item_to_dict("product",products, "ID", "Product" ,"Price")

        #incomplete
        if choice_product == "3":
            update_item_in_dict("product", products)

        #incomplete
        if choice_product == "4":
            print("hi")

        #return to main menu-complete
        if choice_product == "5":
            os.system("clear")
            app()








app()


