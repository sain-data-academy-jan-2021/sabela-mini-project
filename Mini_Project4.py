import os
import sys
import csv


from miniproject_func import choice_1
from miniproject_func import choice_2
from miniproject_func import choice_3
from miniproject_func import choice_4


# products = ["Bread", "Milk", "Eggs"]
# Open file to get new products
products = []

products_file = open("product.txt", "r")
products = [line.strip() for line in products_file]
print(products)

# list of couriers
# couriers = ["John", "Sarah", "Andy", "Amy"]
# Open file to get new couriers
couriers = []

couriers_file = open("courier.txt", "r")
couriers = [line.strip() for line in couriers_file]
print(couriers)


orders = []


with open("order.csv", "r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        orders.append(row)


os.system("clear")


while True:
    choice = input(
        "Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 3 to go to the order menu \nEnter 0 to save and leave the app \nWhich option would you like?"
    )
    print(choice)

    # products
    os.system("clear")
    if choice == "1":
        choice = input(
            "Enter 1 to view products \nEnter 2 to add a new product \nEnter 3 to update product \nEnter 4 to delete a product \nEnter 5 to return to main menu \nWhich option would you like?"
        )
        print(choice)

        if choice == "1":
            display_list("product", products)

        elif choice == "2":
            add_item_to_list("product", products)

        elif choice == "3":
            update_item_in_list("product", products)

        elif choice == "4":
            delete_item_in_list("product", products)

        elif choice == "5":
            os.system("clear")

        else:
            os.system("clear")
            print("Invalid option, please choose again\n")

    # couriers
    elif choice == "2":
        choice = input(
            "Enter 1 to view courier \nEnter 2 to add a new courier \nEnter 3 to update courier \nEnter 4 to delete a courier \nEnter 5 to return to main menu \nWhich option would you like?"
        )
        print(choice)

        if choice == "1":
            display_list("courier", couriers)

        elif choice == "2":
            add_item_to_list("courier", couriers)

        elif choice == "3":
            update_item_in_list("courier", couriers)

        elif choice == "4":
            delete_item_in_list("courier", couriers)

        elif choice == "5":
            os.system("clear")
            continue

        else:
            print("Invalid option, please choose again")

    # orders
    elif choice == "3":
        choice = input(
            "Enter 1 to view your orders \nEnter 2 to create a new order \nEnter 3 to update order status \nEnter 4 to update your order \nEnter 5 to delete your order \nEnter 6 to return to main menu \nWhich option would you like?"
        )
        print(choice)

        if choice == "1":
            display_list("order", orders)

        if choice == "2":
            os.system("clear")
            print("Let's create your order\n")
            name = input("What's your name?").capitalize()
            address = input("What's your address?").capitalize()
            phone_number = input("What's your phone number?")
            print(couriers)
            courier = input("Please choose a courier from the list").capitalize()

            os.system("clear")

            # while True:
            #     if courier in couriers:
            #         print("Your order has been added succesfully!")
            #         pass

            #     else:
            #         print(couriers)
            #         courier = input(f"{courier} is not part of our courier team, please choose again").capitalize()

            try:

                with open("order.csv", "a") as file:
                    fields = [name, address, phone_number, courier, "Preparing"]
                    writer = csv.writer(file)
                    writer.writerow(fields)

                    with open("order.csv", "r") as file:
                        csv_file = csv.DictReader(file)
                        for row in csv_file:
                            print(row)

            except Exception as e:
                print("Sorry, something went wrong" + e)

        if choice == "3":
            os.system("clear")

            with open("order.csv", "r") as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    print(row)

            # order_number = input ("")
            # updated_status = input("What would you like to update the order status to?").capitalize()

            try:

                # with open("order.csv","r") as file:
                #     csv_file = csv.DictReader(file)
                #     for line in csv_file:
                #         line[1][1] = "30"

                r = csv.reader(open("order.csv"))  # Here your csv file
                lines = list(r)

                lines[1][1] = "30"

                writer = csv.writer(open("order.csv", "w"))
                writer.writerows(lines)

            except Exception as e:
                print("Sorry, something went wrong")
                print(e)

            os.system("clear")
            print("Order has been update successfully!")
            print(orders)

        if choice == "4":
            os.system("clear")

            with open("order.csv", "r") as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    print(row)

            name_change = input(
                "Would you like to change your name? Enter Y for yes or N for no"
            ).capitalize()
            if name_change == "Y":
                name = input("What is the new name?")

            else:
                continue

        if choice == "5":
            os.system("clear")
            updatedlist = []
            with open("order.csv") as file:
                reader = csv.reader(file)
                name = input(
                    "Enter the name of the order you wish to remove from file:"
                ).capitalize()

                for row in reader:  # for every row in the file

                    if (
                        row[0] != name
                    ):  # as long as the username is not in the row .......
                        updatedlist.append(
                            row
                        )  # add each row, line by line, into a list called 'udpatedlist'
                # print(updatedlist)

            def updatefile(updatedlist):
                with open("order.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerows(updatedlist)
                    print("Order has been deleted!")

            updatefile(updatedlist)

        if choice == "6":
            os.system("clear")
            continue

            # with open("order.csv","r") as file:
            #         writer = csv.writer(file, delimeter = ",")

            #         writer.writerow([])

    # leave the app
    elif choice == "0":
        print("See you soon!")
        break

    # invalid option
    else:
        print("Invalid option, please choose again")
