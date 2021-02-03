import os
import sys


def logo():
    print(
        """
        *****************************
        *****************************
                JAMSBURY\'S          
        *****************************
        *****************************
        """
    )


# view list
def display_list(list_type, list):
    os.system("clear")
    # logo()
    print(f"{list_type} list")
    for item in list:
        print(item)
    # sub_menu()


# append onto list Complete the end of the code!!!!!!!!
def add_item_to_list(list_type, list):
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

    print(f"\n{new_item} has been added to your {list_type}")

    # another = input(f"Would you like to add another {list_type} to the list? /nPress Y for yes or for No").capitalize()
    # if another == "Y":
    #     choice(2)

    # elif another == "N":

    # sub_menu()


# update list
def update_item_in_list(list_type, list):
    os.system("clear")
    print(f"{list_type} list")

    for item in list:
        print(item)

    current_item = input(
        f"Which {list_type} would you like to update? Or press 0 to return to product menu."
    ).capitalize()
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
            with open(list_type + ".txt", "w") as item_file:
                for item in list:
                    item_file.write(item + "\n")

        except Exception as e:
            print("Sorry, something went wrong")
        # saving it as a text file by replacing the whole list and relisting again

    # sub_menu()


# delete item off list
def delete_item_in_list(list_type, list):
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
