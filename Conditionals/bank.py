# bank

# prompt the user for a greeting
# if greeting starts with 'hello, output $0
# if greeting starts with an 'h', but not 'hello', output $20
# otherwise output $100
# ignore any leading whitespace in the user's greeting, and treat the users greeting case insensitively


def main():
    greeting = input("Greeting:")
    greeting = greeting.casefold().lstrip()
    is_matching(greeting)

def is_matching(answer):
    if answer.startswith("hello"):
        print("$0")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$100")


main()