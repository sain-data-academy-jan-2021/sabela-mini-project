import os
import sys



# for friend in ['Margot', 'Kathryn', 'Prisila']:
#     invitation = "Hi " + friend + ".  Please come to my party on Saturday!"
#     print(invitation)

# name = 'Harrison'
# guess = input("So I'm thinking of person's name. Try to guess it: ")
# pos = 0

# while guess != name and pos < len(name):
#     print("Nope, that's not it! Hint: letter ", end='')
#     print(pos + 1, "is", name[pos] + ". ", end='')
#     guess = input("Guess again: ")
#     pos = pos + 1

# if pos == len(name) and name != guess:
#     print("Too bad, you couldn't get it.  The name was", name + ".")
# else:
#     print("\nGreat, you got it in", pos + 1,  "guesses!")

#input_string = input("Enter a list elements separated by space ")

# print("\n")
# userList = input_string.split()
# print("user list is ", userList)
# # Calculating the sum of input list elements
# sum1 =9
# for num in userList:
#     sum1 += int(num)
# print("Sum = ", sum1)

# list_num = []
# list_num.extend([1, 2])  # extending list elements
# print(list_num)
# list_num.extend((3, 4))  # extending tuple elements
# print(list_num)
# list_num.extend("ABC")  # extending string elements
# print(list_num)



# while True:
#     eingabe = input ('Please enter a name: ')
#     print (eingabe)
#     if eingabe == '':
#         break






# def main_menu():
#     choice = input("Hello User! \nEnter 1 to go to the product menu \nEnter 2 to go to the courier menu \nEnter 0 to save and leave the app")
#     if choice == "1":
#         product_menu
#     else:
#         sys.exit()
    
# main_menu()

# try:  x = 1 / 0
# except:
#       print("You can't do that!")  
#       print("We can still run the program after this though")



# def logo():
#     print ("""
#         *****************************
#         *****************************
#                 JAMSBURY\'S          
#         *****************************
#         *****************************
#         """)

# logo()
# a = "6"
# b = 5

# def add_two_numbers(a, b):
#     if (a.isnumeric()) and (b.isnumeric()):
#        return a + b

#     else:
#         print("error")


# add_two_numbers(a, b)

# print(a.isnumeric())

import csv

r = csv.reader(open('order.csv')) # Here your csv file
lines = list(r)

lines[1][1] = '30'

writer = csv.writer(open('order.csv', 'w'))
writer.writerows(lines)

# text = open("order.csv", "r")
# text = ''.join([i for i in text]).replace("3", "e")
# x = open("order.csv","w")
# x.writelines(text)
# x.close()



    #1. This code snippet asks the user for a username and deletes the user's record from file.
#     updatedlist=[]
#     with open("order.csv",delimeter=",") as file:
#       reader=csv.reader(f)
#       name=input("Enter the name of the order you wish to remove from file:")
      
#       for row in reader: #for every row in the file
            
#                 if row[0]!=name: #as long as the username is not in the row .......
#                     updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
#       print(updatedlist)
#       updatefile(updatedlist)
        
# def updatefile(updatedlist):
#     with open("order.csv","w") as file:
#         Writer=csv.writer(file)
#         Writer.writerows(updatedlist)
#         print("Order has been deleted!")