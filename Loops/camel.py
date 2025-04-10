# camel
# prompts a user for the name of a variable in camel case
# outputs the corresponding name in snake case
# assume users input will be camel case

def main():
    camel_case = input("Enter a variable name: ")
    snake_case = convert(camel_case)
    print(snake_case)

def convert(string):
    snake = ""
    # defining a new variable, snake, as an empty string that we can build on 
    for c in string:
        # for c in string iterates through each character in the string just like a list 
        if c.isupper():
            # if a character, c, is uppercase, we convert it to lowercase
            c = c.casefold()
            # we then begin to build our string, snake, starting with the empty string defined above
            snake = snake + ("_" + c)  # Equivalent to snake += "_" + c
        else:
            snake = snake + c  # Equivalent to snake += c
    return snake

main()
