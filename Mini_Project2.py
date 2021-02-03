import os
import sys

def logo():
    print ("""
        *****************************
        *****************************
                JAMSBURY\'S          
        *****************************
        *****************************
        """)
     



# products = ["Bread", "Milk", "Eggs"]
# Open file to get new products
products = []

products_file = open("products.txt","r")
products = [line.strip() for line in products_file]
print(products)

# list of couriers
# couriers = ["John", "Sarah", "Andy", "Amy"]
# Open file to get new couriers
couriers = []

couriers_file = open("couriers.txt","r")
couriers = [line.strip() for line in couriers_file]
print(couriers)

os.system('clear')

def main_menu():
    logo()
    choice = input("Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 0 to save and leave the app \nWhich option would you like?")
    if choice == "1":
        product_menu()
    elif choice == "2":
        courier_menu()
    elif choice == "0":
        sys.exit
    else:
        os.system("clear")
        print("Invalid option. Please choose again.")
        main_menu()
#main menu for whole app


def sub_menu():

    choice = input("\nWhat would you like to do now? \nEnter 1 for main menu \nEnter 2 for product menu \nEnter 3 for courier menu \nEnter 0 to quit app \nWhich option would you like? ")
    if choice == "1":
        os.system("clear")
        main_menu()
    
    elif choice == "2":
        os.system("clear")
        product_menu()

    elif choice == "3":
        os.system("clear")
        courier_menu()

    elif choice == "0":
        sys.exit

    else:
        os.system("clear")
        print("Invalid option. Please choose again.")
        sub_menu()
#submenu for whole app


def product_menu():
    os.system("clear")
    logo()
    choice = input("Hello User \nEnter 1 to view products \nEnter 2 to add a new product \nEnter 3 to update product \nEnter 4 to delete a product \nEnter 5 to return to main menu \nWhich option would you like?")
    
    if choice =="1":
        os.system("clear")
        logo()
        for product in products:
            print(product)
        sub_menu()
        #Display list of products
        
    elif choice =="2":
        os.system("clear")
        print("Current products:")
        for product in products:
            print(product)
        new_product = input("What product would you like to add?").capitalize()
        products.append(new_product)
        # update the file
        try:
             products_file = open("products.txt", "a")
             products_file.write("\n" + new_product)
             products_file.close()
        
        except Exception as e:
            print("Sorry, something went wrong")

        os.system("clear")

        for product in products:
            print(product)
        print (f"\n{new_product} has been added to your list")
        sub_menu()
        #print products with new addition

    elif choice =="3":
        os.system("clear")
        print("Current products:")
        for product in products:
            print(product)
        current_product = input("Which product would you like to update? Or press 0 to return to product menu.").capitalize()
        os.system("clear")
        if current_product == "0":
            product_menu()
        else:
            new_product = input("What's the new name of the product?").capitalize()
            os.system("clear")
            try:
                if current_product in products:
                    index = products.index(current_product)
                    products[index] = new_product
                    for product in products:
                        print(product)
                print(f"\n{current_product} has been updated to {new_product}")

            except ValueError:
                print(f"{current_product} does not exist")
                print("\nplease choose from the list below")
                for product in products:
                    print(product)

            try:
                with open("products.txt","w") as products_file:
                    for product in products:
                        products_file.write(product + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")
            #saving it as a text file by replacing the whole list and relisting again

        sub_menu()
    #update products

    elif choice =="4":
        os.system("clear")
        print("Current products")
        for product in products:
            print(product)

        delete_product = input("Which product would you like to delete? Or press 0 to return to product menu.").capitalize()
        os.system("clear")
        if delete_product == "0":
            product_menu()
        else:
            try:
                products.remove(delete_product)
                for product in products:
                    print(product)

                print(f"\n{delete_product} has been deleted")
            except ValueError:
                print(f"{delete_product} does not exist")
                print("\nplease choose from the list below")
                for product in products:
                    print(product)

            try:
                with open("products.txt","w") as products_file:
                    for product in products:
                        products_file.write(product + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")
        sub_menu()

        #delete a product from the list

    elif choice == "5":
        os.system("clear")
        main_menu()

    else:
        print("Invalid Option. Please choose a valid option")
        #product_menu()
    #option not recognised
#product menu


def courier_menu():
    os.system("clear")
    choice = input("Hello User \nEnter 1 to view all the courier drivers \nEnter 2 to add a new courier driver \nEnter 3 to update the name of a courier driver \nEnter 4 to delete a courier driver \nEnter 5 to return to main menu \nWhich option would you like?")

    if choice =="1":
        os.system("clear")
        for courier in couriers:
            print(courier)
        sub_menu()
        #Display list of products
        
    elif choice =="2":
        os.system("clear")
        print("Available Couriers:")
        for courier in couriers:
            print(courier)
        new_courier = input("What's the name of the courier you would like to add'?").capitalize()
        #name of the new product
        couriers.append(new_courier)
        #add new product to original list
        os.system("clear")
        for courier in couriers:
            print(courier)
        print (f"\n{new_courier} has been added to your list")

        try:
             couriers_file = open("couriers.txt", "a")
             couriers_file.write("\n" + new_courier)
             couriers_file.close()
        
        except Exception as e:
            print("Sorry, something went wrong")
        sub_menu()
        #print products with new addition

    elif choice =="3":
        os.system("clear")
        print("Available Couriers:")
        for courier in couriers:
            print(courier)
        current_courier = input("Which courier would you like to update? Or press 0 to return to product menu.").capitalize()
        os.system("clear")
        if current_courier == "0":
            product_menu()
        else:
            new_courier = input("What's the new name of the courier?").capitalize()
            os.system("clear")
            try:
                if current_courier in couriers:
                    index = couriers.index(current_courier)
                    couriers[index] = new_courier
                    for courier in couriers:
                        print(courier)

                print(f"\n{current_courier} has been updated to {new_courier}")
            except ValueError:
                print(f"{current_courier} does not exist")
                print("\nplease choose from the list below")
                for product in products:
                    print(product)

            try:
                with open("couriers.txt","w") as couriers_file:
                    for courier in couriers:
                        couriers_file.write(courier + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")

        sub_menu()


 
    elif choice =="4":
        os.system("clear")
        print("Available Couriers")
        for courier in couriers:
            print(courier)

        delete_courier = input("Which courier would you like to delete? Or press 0 to return to product menu.").capitalize()
        os.system("clear")
        if delete_courier == "0":
            courier_menu()
        else:
            try:
                couriers.remove(delete_courier)
                for courier in couriers:
                    print(courier)

                print(f"\n{delete_courier} has been deleted")
            except ValueError:
                print(f"{delete_courier} does not exist")
                print("\nplease choose from the list below")
                for courier in couriers:
                    print(courier)

            try:
                with open("couriers.txt","w") as couriers_file:
                    for courier in couriers:
                        couriers_file.write(courier + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")
        sub_menu()

        #delete a product from the list

    elif choice == "5":
        os.system("clear")
        main_menu()

    else:
        os.system("clear")
        print("Invalid option. Please choose again.")
        courier_menu()
    #option not recognised
#product menu






main_menu()
