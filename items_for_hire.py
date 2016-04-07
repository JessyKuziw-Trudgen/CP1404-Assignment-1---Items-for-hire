"""
Jessy Kuziw-Trudgen
24-3-2016
https://github.com/JessyKuziw-Trudgen/CP1404-Assignment-1---Items-for-hire.git


"""
import locale
locale.setlocale(locale.LC_ALL, '')

OUT = "out"
IN = "in"
COUNTER = 0
PADDING_1 = 12
PADDING_2 = 25


def main():
    items_available = []
    items_not_available = []
    items_no_longer_available = []
    items_available_again = []
    items_for_hire = []
    items = open("items.csv")
    print("Items for Hire - by Jessy Kuziw")
    # count = COUNTER
    # item_holder = ""
    # with open('items.csv', 'r') as f:
    #     data = f.readlines()
    #     items_for_hire = []
    #     for i in range(0, len(data)):
    #         items_for_hire.append(data[i:i + 1])
    #     print(items_for_hire)
    for line in items:
        items_for_hire.append("{0}".format(line).strip())
        items_for_hire = [w.replace(IN, "").strip() for w in items_for_hire]
        items_for_hire = [w.replace(OUT, "*").strip() for w in items_for_hire]
    # print(items_for_hire)
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
            for item in items_available:
                item_for_hire = item.split(",")
                # print(item_for_hire)
                print("{0} - {1} ({2})  ={3:>9} {4:>2}".format(count, item_for_hire[0].ljust(PADDING_1),
                                                               item_for_hire[1].ljust(PADDING_2),
                                                               locale.currency(float(item_for_hire[2])),
                                                               item_for_hire[3]))
                count += 1
            # print(items_for_hire)
            menu_input = items_for_hire_main_menu().upper()
        elif menu_input == "H":
            item_hired = hiring_an_item(items_available)
            index_to_remove = item_hired.pop(-1)
            items_available.remove(items_available[index_to_remove])
            item_holder = str(",".join(item_hired[:]))
            items_no_longer_available.append(item_holder)
            items_not_available.append(','.join(items_no_longer_available[:]))
            items_no_longer_available = []
            menu_input = items_for_hire_main_menu().upper()
            # for item in items_not_available:
            #     if "*" not in item:
            #         if item not in items_available:
            #             items_available.append(item)
            #     elif "*" in item:
            #         if item not in items_not_available:
            #             items_not_available.append(item)
            # print(item_holder)
            # item_holder = ''
            # print(index_to_remove)
            # print(item_hired)
            # print(items_no_longer_available)
            # print(item_holder)

        elif menu_input == "R":
            item_returned = returning_item(items_not_available)
            index_to_remove = item_returned.pop(-1)
            items_not_available.remove(items_not_available[index_to_remove])
            item_holder = ",".join(item_returned[:])
            items_available_again.append(item_holder)
            items_available.append(','.join(items_available_again[:]))
            menu_input = items_for_hire_main_menu().upper()
            # print(items_available)
            # for item in items_not_available:
            #     if "*" in item:
            #         if item not in items_not_available:
            #             items_not_available.append(item)
            #     elif "*" not in item:
            #         if item not in items_not_available:
            #             items_available.append(item)
            # item_hired = hiring_an_item(items_available)
            # index_to_remove = item_hired.pop(-1)
            # items_available.remove(items_available[index_to_remove])
            # item_holder = ",".join(item_hired[0:])
            # items_no_longer_available.append(item_holder)
            # items_not_available.append(','.join(items_no_longer_available[:]))
            # item_hired = returning_an_item(items_not_available)
            # for item in item_hired:
            #     hired_item.append(item)
            #     if item in items_for_hire:
            #     print(items_for_hire)
            #     menu_input = items_for_hire_main_menu().upper()
        elif menu_input == "A":
            new_item = adding_new_item()
            items_available.append('{},{},{},{}'.format(new_item[0], new_item[1], new_item[2], new_item[3]))
            menu_input = items_for_hire_main_menu().upper()
        else:
            print("Invalid menu choice")
            menu_input = items_for_hire_main_menu().upper()

    # for item in items_available
    #     items_for_hire
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
    print("{} ({}), {:>7} now available for hire".format(new_item[0].ljust(PADDING_1), new_item[1].ljust(PADDING_2), locale.currency(float(new_item[2]))))
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
                # print(return_item)
                valid_choice = True
                return_item = return_item + [item_to_return]
    return return_item


def hiring_an_item(items_available):
    # print(items_available)
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
                    # print(hire_item)
                    valid_choice = True
                    hire_item = hire_item + [item_to_hire]
    # print(hire_item)
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
