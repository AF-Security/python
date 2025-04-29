# adieu

# implement a program that prompts the user for names, one per line, until the user inputs control-d. 
# Assume that the user will input at least one name. 
# Then bid adieu to those names, separating two names with one and, three names with two commas and one and
# and n names with n-1 commas and one and

import inflect

def main():
    while True:
        try:
            name = input("Enter a name: ").strip()
            names = storage(name)
        except EOFError:
            print("\n")
            break
    print(f"Adieu, adieu {names}")

def storage(name):
    names = []
    p = inflect.engine()
    for name in names:
        names.append(name)
    return p.join((names))


# join words into a list
# https://pypi.org/project/inflect/

main()