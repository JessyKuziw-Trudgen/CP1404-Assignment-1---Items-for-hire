"""
Jessy Kuziw-Trudgen
24-3-2016
https://github.com/JessyKuziw-Trudgen/CP1404-Assignment-1---Items-for-hire.git


"""


def main():
    count = 0
    items_for_hire = []
    print("Items for Hire - by Jessy Kuziw")
    items = open("items.csv")
    for line in items:
        item = line.split(',')
        items_for_hire.append("{0} ({1})".format(item[0], item[1], item[2]))
    print("{} items loaded from items.csv".format(len(items_for_hire)), end='')
    menu_input = items_for_hire_menu()
    menu_input = menu_input.upper()
    if menu_input == "L":
        for item in items_for_hire:
            count += 1
            print("{} - {}".format(count, item))

    items.close()


def items_for_hire_menu():
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
