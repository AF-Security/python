# groceries 1
# implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item
# No need to pluralize the items
# Treat the user’s input case-insensitively



def main():
    count_dict = {}
    # defining an empty dictionary for which we can update with user inputs
    while True:
        try:
            item = input("").casefold()
            count_dict = sort_count(item, count_dict)
        except EOFError:
             print("\n")
             break
    for item in sorted(count_dict):
        # item = item.capitalize()
        print(count_dict[item], item.upper(), sep=", ")

    # print_grocery_list(grocery_list)

def sort_count(item, count_dict):
    # count_dict = {}
    # for item in count_dict:
    if item in count_dict:
        count_dict[item] = count_dict.get(item) + 1
    # then update its value by +1
    else:
        count_dict[item] = 1
        # add key to dictionary
    # sorted(count_dict)
    return count_dict
    # print(count_dict[item], item, sep=", ")


def print_grocery_list(list):
    count_dict = {}
    for item in list:
        count_dict[item] = count_dict.get(item, )
            # we need to sort the list alphabetically

    # print the list, prefixed with number of times item is in list
    print(f"{list}")

# we need to prompt input, store it as a list(?)

main()