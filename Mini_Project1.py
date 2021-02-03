import os
import sys


products = ["Bread","Milk","Eggs"]
#list of products

os.system('clear')

print("Hello User \nEnter 0 to leave the app \nEnter 1 to return to main menu \nEnter 2 to view products \nEnter 3 to add a new product ")
#main menu



choice = input("What option do you want?")

os.system('clear')

if choice == "0":
    print("You have chosen to leave")
    sys.exit()
    #leave app
elif choice == "1":
    print("Hello User \nEnter 0 to leave the app \nEnter 1 to return to main menu \nEnter 2 to view products \nEnter 3 to add a new product ")
    #main menu
elif choice =="2":
    print(products)
    #Display list of products
    print("Enter 0 to leave the app \nEnter 1 to return to main menu")
    choice = input("What option do you want?")
    #what the customer wants to do next
    if choice == "0":
        sys.exit()
    else:
        os.system("clear")
        #clear previous screen
        print("Hello User \nEnter 0 to leave the app \nEnter 1 to return to main menu \nEnter 2 to view products \nEnter 3 to add a new product ")
elif choice =="3":
    new_product = input("What product would you like to add?")
    #name of the new product
    products.append(new_product)
    #add new product to original list
    print(products)
    #print products with new addition
    print("Enter 0 to leave the app \nEnter 1 to return to main menu")
    #what the customer wants to do next
    choice = input("What option do you want?")
    if choice == "0":
        sys.exit()
    else:
        os.system("clear")
        #clear previous screen
        print("Hello User \nEnter 0 to leave the app \nEnter 1 to return to main menu \nEnter 2 to view products \nEnter 3 to add a new product ")
else:
    print("Invalid Option")
#option not recognised