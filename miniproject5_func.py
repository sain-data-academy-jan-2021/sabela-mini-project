import os
import sys
import csv
from tabulate import tabulate

# products = []


# with open("product.csv","r") as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         products.append(row)


# make list into table 
def make_list_into_table(list_type):
    header = list_type[0].keys()
    rows =  [x.values() for x in list_type]
    print(tabulate(rows, header))
    

# make ID for number 
#cannot be used in an empty list since you need to add from the previous ID
def list_ID(list_type):
    firstkey =list(list_type[0].keys())[0]
    last_num = int((list_type[-1][firstkey]))
    last_num += 1
    return str(last_num)





#Main functionality
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# view list -- unit test done!
def display_dict(dict_type, list_type):
    os.system("clear")
    # logo()
    print(f"{dict_type} list_type")
    make_list_into_table(list_type)
    


# append onto list 
def add_item_to_dict(dict_type, list_type, key_1, key_2, key_3):
    os.system("clear")
    print(f"{dict_type} list:")

    make_list_into_table(list_type)

    value_1 = list_ID(list_type)
    value_2 = input(f"What is the name of the {dict_type} would you like to add?").capitalize()
    value_3 = input(f"What is the {key_3} of the new {dict_type}?")

    my_dict = {
        key_1:value_1,
        key_2:value_2,
        key_3:value_3
        }

    list_type.append(my_dict)


    os.system("clear")

    make_list_into_table(list_type)

    print(f"\n{value_2} has been added to your {dict_type} list")

    appending_to_csv_file(dict_type,value_1,value_2,value_3)


# update list - data persistance  
def update_item_in_dict(dict_type, list_type, key_1, key_2, key_3):

    print(f"{dict_type} list")
    make_list_into_table(list_type)

    current_item_index = int(input(
        f"What is the ID of the {dict_type} you would like to update? Or press 0 to return to {dict_type} menu."
    ))
    
    os.system("clear")

    if current_item_index == 0:
        pass

    else:

        try:
            index = current_item_index - 1
            print(list_type[index])

            value_2 = input(f"Please enter the new name of the {key_2} or press enter to skip").capitalize()
            
            if value_2 == "":
                pass

            else:
                list_type[index][key_2] = value_2
                
            value_3 = input(f"Please enter the {key_3} of the new {key_2} or press enter to skip")
 
            if value_3 == "":
                pass
                os.system("clear")
                print(list_type[index])
            else:
                list_type[index][key_3] = value_3
                os.system("clear")
                make_list_into_table(list_type)
                print(f"{list_type} has been updated")
            

        except:
            print(f"ID {current_item_index} does not exist")
            print("\nplease choose an ID from the list below")
            update_item_in_dict(dict_type, list_type, key_1, key_2, key_3)

    write_csv_file(dict_type,list_type,key_1,key_2,key_3)





# delete item off list 
os.system("clear")
def delete_item_in_dict(dict_type, list_type, key_1, key_2, key_3):


    print(f"{dict_type} list")

    make_list_into_table(list_type)

    current_item_index = int(input(f"What is the ID of the {dict_type} you would like to delete? Or press 0 to return to {dict_type} menu."))
    os.system("clear")

    if current_item_index == 0:
        pass

    else:
    
        try:
            index = current_item_index - 1
            print(list_type[index])
            confirmation = input(f"Are you sure you want to delete this {dict_type}? Press 1 to confirm or 0 to go back to {dict_type} menu.")

            if confirmation == "0":
                pass

            else:
                list_type.remove(list_type[index])
                make_list_into_table(list_type)

                print(f"\n{dict_type} {current_item_index} has been deleted")


        except:
            print(f"ID {current_item_index} does not exist")
            print("\nplease choose an ID from the list below")
            delete_item_in_dict(dict_type, list_type)

    write_csv_file(dict_type,list_type,key_1,key_2,key_3)


  

#data persistance
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#append to a csv file
def appending_to_csv_file(dict_type,value_1,value_2,value_3):
    with open(dict_type + ".csv","a") as file:
        writer = csv.writer(file, delimiter = ",")
        writer.writerow([value_1,value_2,value_3])


   
def read_csv_file(dict_type,list_type):
     with open(dict_type + "csv", "r") as file:
        csv.file = csv.DictReader(file)
        for row in csv.file:
            list_type.append(row)



def write_csv_file(dict_type,list_type,key_1,key_2,key_3):
    with open(dict_type + ".csv", "w") as file:
        writer = csv.DictWriter(file,fieldnames = [key_1, key_2, key_3])
        writer.writeheader()
        for row in list_type:
            writer.writerow(row)



