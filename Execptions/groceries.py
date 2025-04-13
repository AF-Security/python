# groceries

# implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item
# No need to pluralize the items
# Treat the user’s input case-insensitively



def main():
    grocery_list = []
    # defining an empty list for which we can update with user inputs
    while True:
        try:
            item = input("").casefold()
            grocery_list.append(item)
        except EOFError:
             print("\n")
             break
    print_grocery_list(grocery_list)

def print_grocery_list(list):
    count_dict = {}
    for item in list:
        count_dict[item] = count_dict.get(item, )
            # we need to sort the list alphabetically

    # print the list, prefixed with number of times item is in list
    print(f"{list}")

# we need to prompt input, store it as a list(?)













main()    