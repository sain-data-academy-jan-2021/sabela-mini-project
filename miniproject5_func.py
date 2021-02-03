import os
import sys


# def logo():
#     print(
#         """
#         *****************************
#         *****************************
#                 JAMSBURY\'S          
#         *****************************
#         *****************************
#         """
#     )


# view list
def display_dict(dict_type, list):
    os.system("clear")
    # logo()
    print(f"{dict_type} list")
    for item in list:
        print(item)
    


# append onto list - work on data persistance
def add_item_to_dict(dict_type, list, key_1, key_2, key_3):
    os.system("clear")
    print(f"{dict_type} list:")

    for item in list:
        print(item)

    value_1 = len(list)+1
    value_2 = input(f"What {dict_type} would you like to add?").capitalize()
    value_3 = input(f"What is the {key_3} of the new {dict_type}?")

    my_dict = {
        key_1:[],
        key_2:[],
        key_3:[]
        }

    my_dict[key_1].append(value_1)
    my_dict[key_2].append(value_2)
    my_dict[key_3].append(value_3)	
    # print(my_dict)
    list.append(my_dict)

    # update the file
    # try:

    #     with open("product.csv","a") as file:
    #         writer = csv.writer(file, delimiter = ",")

    #         writer.writerow(key_1,key_2,key_3)


    # except Exception as e:
    #     print(e)

    os.system("clear")

    for item in list:
        print(item)

    print(f"\n{value_2} has been added to your {dict_type} list")




# update list
def update_item_in_dict(dict_type, list, key_1, key_2, key_3):
    os.system("clear")
    print(f"{dict_type} list")

    for item in list:
        print(item)

    current_item_index = input(
        f"What is the ID of the {dict_type} you would like to update? Or press 0 to return to {dict_type} menu."
    ).capitalize()
    os.system("clear")

    if current_item == "0":
        pass

    else:

        

        print("update or press enter to skip")
        new_value_2 = input(f"What's the new {value_2} of the {list_type}?").capitalize()

        if new_value_2 = "" :
            pass

        else:
            new_value_3 = input(f"What's the new {value_3} of the {list_type}")

        os.system("clear")

       
       


        



# delete item off list
def delete_item_in_dict(list_type, list):
    os.system("clear")
    print(f"{list_type} list")
    for item in list:
        print(item)

    delete_item = input(
        f"Which {list_type} would you like to delete? Or press 0 to return to {list_type} menu."
    ).capitalize()
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
            with open(list_type + ".txt", "w") as item_file:
                for item in list:
                    item_file.write(item + "\n")

        except Exception as e:
            print("Sorry, something went wrong")
    # sub_menu()


# main menu
# def choice_5():
#         os.system("clear")
#         main_menu()
