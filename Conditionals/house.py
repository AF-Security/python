# house matching


def main():
    name = input("What is your name? ")
    
# match is a keyword that we can use to match a value against a pattern
# we use the keyword case to define that we to match string values
    match name:
        case "Harry" | "Hermione" | "Ron":
# we use the vertical bars to match multiple values
            print("Welcome to Gryffindor!")
        # case "Hermione":        
        #     print("Welcome to Gryffindor!")
        case "Draco":
            print("Welcome to Slytherin!")
        case "Luna":
            print("Welcome to Ravenclaw!")
        case _:
            print("Who?")
            


main()