import os
import sys

     



# products = ["Bread", "Milk", "Eggs"]
# Open file to get new products
products = []

products_file = open("product.txt","r")
products = [line.strip() for line in products_file]
print(products)

# list of couriers
# couriers = ["John", "Sarah", "Andy", "Amy"]
# Open file to get new couriers
couriers = []

couriers_file = open("courier.txt","r")
couriers = [line.strip() for line in couriers_file]
print(couriers)


# orders = []
# orders_file = open("order.txt","r")
# orders = [line.strip() for line in orders_file]
# print(orders)

os.system('clear')



def logo():
    print ("""
        *****************************
        *****************************
                JAMSBURY\'S          
        *****************************
        *****************************
        """)


#view list
def choice_1(list_type, list):
    os.system("clear")
            # logo()
    print(f"{list_type} list" )
    for item in list:
        print(item)
    #sub_menu()

#append onto list Complete the end of the code!!!!!!!!
def choice_2(list_type, list):
        os.system("clear")
        print(f"{list_type} list:")
        
        for value in list:
            print(value)

        new_item = input(f"What {list_type} would you like to add?").capitalize()
        list.append(new_item)

        # update the file
        try:
             item_file = open(list_type + ".txt", "a")
             item_file.write("\n" + new_item)
             item_file.close()
        
        except Exception as e:
            print("Sorry, something went wrong")

        os.system("clear")

        for item in list:
            print(item)

        print (f"\n{new_item} has been added to your {list_type}")

        another = input(f"Would you like to add another {list_type} to the list? /nPress Y for yes and N for No").capitalize()
        os.system("clear")

    

        #sub_menu()

#update list
def choice_3(list_type, list):
        os.system("clear")
        print(f"{list_type} list")

        for item in list:
            print(item)

        current_item = input(f"Which {list_type} would you like to update? Or press 0 to return to product menu.").capitalize()
        os.system("clear")

        if current_item == "0":
            print("hello")
            # product_menu()
        else:
            new_item = input(f"What's the new name of the {list_type}?").capitalize()
            os.system("clear")
            try:
                if current_item in list:
                    index = list.index(current_item)
                    list[index] = new_item
                    for item in list:
                        print(item)
                print(f"\n{current_item} has been updated to {new_item}")

            except ValueError:
                print(f"{current_item} does not exist")
                print("\nplease choose from the list below")
                for item in list:
                    print(item)

            try:
                with open(list_type + ".txt","w") as item_file:
                    for item in list:
                        item_file.write(item + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")
            #saving it as a text file by replacing the whole list and relisting again

        #sub_menu()

#delete item off list
def choice_4(list_type, list):
        os.system("clear")
        print(f"{list_type} list")
        for item in list:
            print(item)

        delete_item = input(f"Which {list_type} would you like to delete? Or press 0 to return to {list_type} menu.").capitalize()
        os.system("clear")
        if delete_item == "0":
            # product_menu()
            print("hello")
        else:
            try:
                list.remove(delete_item)
                for item in list:
                    print(item)

                print(f"\n{delete_item} has been deleted")
            except ValueError:
                print(f"{delete_item} does not exist")
                print("\nplease choose from the list below")
                for item in list:
                    print(item)

            try:
                with open(list_type + ".txt","w") as item_file:
                    for item in list:
                        item_file.write(item + '\n')
        
            except Exception as e:
                print("Sorry, something went wrong")
        # sub_menu()

#main menu
# def choice_5():
#         os.system("clear")
#         main_menu()



while True:
    choice = input("Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 3 to go to the order menu \nEnter 0 to save and leave the app \nWhich option would you like?")
    print(choice)

    
#products
    os.system("clear")
    if choice == "1":
        choice = input("Enter 1 to view products \nEnter 2 to add a new product \nEnter 3 to update product \nEnter 4 to delete a product \nEnter 5 to return to main menu \nWhich option would you like?")
        print(choice)

        if choice == "1":
            choice_1("product", products)
        
        elif choice == "2":
            choice_2("product", products)

        elif choice == "3":
            choice_3("product", products)

        elif choice == "4":
            choice_4("product", products)

        elif choice == "5":
            os.system("clear")
        
        else:
            os.system("clear")
            print("Invalid option, please choose again\n")
        

 
 #couriers
    elif choice == "2":
        choice = input("Enter 1 to view courier \nEnter 2 to add a new courier \nEnter 3 to update courier \nEnter 4 to delete a courier \nEnter 5 to return to main menu \nWhich option would you like?")
        print(choice)

        if choice == "1":
            choice_1("courier", couriers)
        
        elif choice == "2":
            choice_2("courier", couriers)

        elif choice == "3":
            choice_3("courier", couriers)

        elif choice == "4":
            choice_4("courier", couriers)

        elif choice == "5":
            os.system("clear")
        
        else:
            print("Invalid option, please choose again")
            print(choice)

#orders
    elif choice == "3":
         choice = input("Enter 1 to view your orders \nEnter 2 to create a new order \nEnter 3 to update order status \nEnter 4 to update your order \nEnter 5 to delete your order \nEnter 6 to return to main menu \nWhich option would you like?")
         print(choice)

         if choice == "1":
             choice_1("order", orders)



 #leave the app   
    elif choice == "0":
        print("See you soon!")
        break
    


#invalid option
    else:
        print("Invalid option, please choose again")
        
    







