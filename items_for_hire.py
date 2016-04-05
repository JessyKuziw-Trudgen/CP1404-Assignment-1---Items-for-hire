"""
Jessy Kuziw-Trudgen
24-3-2016
https://github.com/JessyKuziw-Trudgen/CP1404-Assignment-1---Items-for-hire.git


"""
import locale
locale.setlocale(locale.LC_ALL, '')

OUT = "out"
IN = "in"


def main():
    items_available = []
    count = 0
    items_for_hire = []
    print("Items for Hire - by Jessy Kuziw")
    items = open("items.csv")
    for line in items:
        items_for_hire.append("{0}".format(line).strip())
        items_for_hire = [w.replace("in", "").strip() for w in items_for_hire]
        items_for_hire = [w.replace("out", "*").strip() for w in items_for_hire]
    print(items_for_hire)
    print("{} items loaded from items.csv".format(len(items_for_hire)), end='')
    menu_input = items_for_hire_menu().upper()
    while menu_input != "Q":
        if menu_input == "L":
            print("All items on file (* indicates item is currently out):")
            for item in items_for_hire:
                padding_1 = 12
                padding_2 = 25
                items_for_hire = item.split(",")
                print("{0} - {1} ({2})  ={3:>9} {4:>2}".format(count, items_for_hire[0].ljust(padding_1), items_for_hire[1].ljust(padding_2), locale.currency(float(items_for_hire[2])), items_for_hire[3]))
                count += 1
            menu_input = items_for_hire_menu().upper()
        # print(items_for_hire)
        if menu_input == "H":
            for item in items_for_hire:
                if "*" not in item:
                    items_available.append(item)
                    print(items_available)
                    hiring_an_item(items_available)
    items.close()


def hiring_an_item(items_available):

    return


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
