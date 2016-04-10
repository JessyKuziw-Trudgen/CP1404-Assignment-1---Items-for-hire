"""
Jessy Kuziw-Trudgen
24-3-2016
https://github.com/JessyKuziw-Trudgen/CP1404-Assignment-1---Items-for-hire.git

this program opens a file called items.csv, reads it and creates a list from it and then depending on the users choice
it will either:
    1. List all items on the file
    2. Allow users to hire an item
    3. Allow users to return an item
    4. Allow users to add a new item
    5. Save all items to the file and quit the program
"""
import locale
locale.setlocale(locale.LC_ALL, '')

OUT = "out"
IN = "in"
COUNTER = 0
PADDING_1 = 12
PADDING_2 = 25

"""
function main
    items = open file
    print - Items for Hire -  by Jessy Kuziw
    for line in items
        append line to items_for_hire
        items_for_hire = replace "in" in line with ""
        items_for_hire = replace "out" in line with "*"
    print - length of items_for_hire "items loaded from items.csv"
    for item in items_for_hire
        if item not in items_available and "*" not in item
            append item to items_available
        else
            append item to items_not_available
    menu input = items_for_hire_main_menu()
    while menu_input not = to "Q"
        if menu_input = "L"
            count = 0
            print - All items on file (* indicates item is currently out):
            items_on_file = items_available + items_not_available
            for item in item_on_file
                item_for_hire = item
                print - count "-" item_for_hire[0] "(" item_for_hire[1] ")" =item_for_hire[2] item_for_hire[3]
                count + 1
            menu_input = items_for_hire_main_menu()
        else if menu_input = "H"
            item_hired = hiring_an_item(items_available)
            index_to_remove = item_hired[-1]
            items_available remove items_available[index_to_remove]
            item_holder = item_hired as string
            menu_input = items_for_hire_main_menu()
        else if menu_input = "R"
            item_returned = returning_item(items_not_available)
            index_to_remove = item_returned[-1]
            items_not_available remove  items_not_available[index_to_remove]
            item_holder = item_returned as a string
            items_available_again append item_holder
            items_available append items_available_again
            menu_input = items_for_hire_main_menu()
        else if menu_input = "A"
            new_item = adding_new_item()
            items_available append new_item[0] new_item[1] new_item[2] new_item[3]
            menu_input = items_for_hire_main_menu()
        else
            print - Invalid menu choice
            menu_input = items_for_hire_main_menu()
    return to start of file items
    count = 0
    for item in items_available
        write item + "in\n" to items
        count + 1
    for item in items_not_available
        write item + "out\n" to items
        count + 1
    print - count "items saved to items.csv"
    print - Have a nice day :)
"""


def main():
    items_available = []
    items_not_available = []
    items_no_longer_available = []
    items_available_again = []
    items_for_hire = []
    items = open("items.csv", "r+")  # opens file in read and write mode
    print("Items for Hire - by Jessy Kuziw")
    for line in items:
        items_for_hire.append("{0}".format(line).strip())
        items_for_hire = [w.replace(IN, "").strip() for w in items_for_hire]  # replaces "in" with ""
        items_for_hire = [w.replace(OUT, "*").strip() for w in items_for_hire]  # replaces "out" with "*"
    print("{} items loaded from items.csv".format(len(items_for_hire)), end='')
    for item in items_for_hire:
        if item not in items_available and "*" not in item:
            items_available.append(item)
        else:
            items_not_available.append(item)
    menu_input = items_for_hire_main_menu().upper()
    while menu_input != "Q":
        if menu_input == "L":
            count = COUNTER
            print("All items on file (* indicates item is currently out):")
            items_on_file = items_available[:] + items_not_available[:]
            for item in items_on_file:
                item_for_hire = item.split(",")
                print("{0} - {1} ({2})  ={3:>9} {4:>2}".format(count, item_for_hire[0].ljust(PADDING_1),
                                                               item_for_hire[1].ljust(PADDING_2),
                                                               locale.currency(float(item_for_hire[2])),
                                                               item_for_hire[3]))
                count += 1
            menu_input = items_for_hire_main_menu().upper()
        elif menu_input == "H":
            item_hired = hiring_an_item(items_available)
            index_to_remove = item_hired.pop(-1)
            items_available.remove(items_available[index_to_remove])
            item_holder = str(",".join(item_hired[:]))  # adds item_hired as a string to a temp holding variable
            items_no_longer_available.append(item_holder)
            items_not_available.append(','.join(items_no_longer_available[:]))
            items_no_longer_available = []
            menu_input = items_for_hire_main_menu().upper()
        elif menu_input == "R":
            item_returned = returning_item(items_not_available)
            index_to_remove = item_returned.pop(-1)
            items_not_available.remove(items_not_available[index_to_remove])
            item_holder = ",".join(item_returned[:])  # adds item_returned as a string to a temp holding variable
            items_available_again.append(item_holder)
            items_available.append(','.join(items_available_again[:]))
            menu_input = items_for_hire_main_menu().upper()
        elif menu_input == "A":
            new_item = adding_new_item()
            items_available.append('{},{},{},{}'.format(new_item[0], new_item[1], new_item[2], new_item[3]))
            menu_input = items_for_hire_main_menu().upper()
        else:
            print("Invalid menu choice")
            menu_input = items_for_hire_main_menu().upper()
    items.seek(0, 0)
    count = COUNTER
    for item in items_available:
        items.write(item + "in\n")
        count += 1
    for item in items_not_available:
        items.write(item[:-1] + "out\n")
        count += 1
    print("{} items saved to items.csv".format(count))
    print("Have a nice day :)")
    items.close()


def adding_new_item():
    new_item = []
    valid_input = False
    item_name = input("Item Name: ")
    while item_name == '':
        print("Input cannot be blank")
        item_name = input("Item Name: ")
    item_description = input("Description: ")
    while item_description == '':
        print("Input cannot be blank")
        item_description = input("Description: ")
    while not valid_input:
        try:
            item_price = float(input("Price per day: $"))
        except ValueError:
            print("Invalid input: Enter a valid number")
        else:
            if item_price >= 0:
                new_item.append("{},{},{},{}".format(item_name, item_description, item_price, ""))
                new_item = new_item[0].split(",")
                valid_input = True
            else:
                print("Price must be >= 0")
    print("{} ({}), {:>7} now available for hire".format(new_item[0].ljust(PADDING_1), new_item[1].ljust(PADDING_2),
                                                         locale.currency(float(new_item[2]))))
    return new_item


def returning_item(items_to_return):
    count = COUNTER
    return_item = ""
    valid_choice = False
    for item in items_to_return:
        item_to_return = item.split(",")
        print("{0} - {1} ({2})  ={3:>9} {4:>2}".format(count, item_to_return[0].ljust(PADDING_1),
                                                       item_to_return[1].ljust(PADDING_2),
                                                       locale.currency(float(item_to_return[2])), item_to_return[3]))
        count += 1
    while not valid_choice:
        try:
            item_to_return = int(input("Enter a number of an item to hire: "))
        except ValueError:
            print("Enter a number")
        else:
            if item_to_return < 0 or item_to_return >= count:
                print("wrong number entered")
            else:
                return_item = items_to_return[item_to_return].split(",")
                print("{} returned".format(return_item[0]))
                return_item[-1] = ""
                valid_choice = True
                return_item = return_item + [item_to_return]
    return return_item


"""
function hiring_an_item
    count = 0
    valid_choice = False
    for item in items_available
        print  count "-" items_available[0] items_available[1] "(" items_available[2] ")  =" items_available[3]
        count + 1
    while valid_choice = False
        item_to_hire = input - Enter a number of an item to hire:
        if item_to_hire < 0 or >= count
            print - Wrong number entered
        else
            hire_item = items_available[item_to_hire]
            print - hire_item[0] "hired for" hire_item[2]
            hire_item[-1] = "*"
            valid_choice = True
            hire_item = hire_item + item_to_hire
    return hire_item
"""


def hiring_an_item(items_available):
    count = COUNTER
    hire_item = ""
    valid_choice = False
    for item in items_available:
        item_available = item.split(",")
        print("{0} - {1} ({2})  ={3:>9} {4:>2}".format(count, item_available[0].ljust(PADDING_1),
                                                       item_available[1].ljust(PADDING_2),
                                                       locale.currency(float(item_available[2])), item_available[3]))
        count += 1
    while not valid_choice:
            try:
                item_to_hire = int(input("Enter a number of an item to hire: "))
            except ValueError:
                print("Enter a number")
            else:
                if item_to_hire < 0 or item_to_hire >= count:
                    print("wrong number entered")
                else:
                    hire_item = items_available[item_to_hire].split(",")
                    print("{} hired for {}".format(hire_item[0], hire_item[2]))
                    hire_item[-1] = "*"
                    valid_choice = True
                    hire_item = hire_item + [item_to_hire]
    return hire_item


def items_for_hire_main_menu():
    print("\nMenu:")
    print("(L)ist all items")
    print("(H)ire an item")
    print("(R)eturn an item")
    print("(A)dd new item to stock")
    print("(Q)uit")
    menu_input = input("")
    return menu_input

if __name__ == "__main__":
    main()
