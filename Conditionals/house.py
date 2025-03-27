# house matching


def main():
    name = input("What is your name? ")
    
    match name:
        case "Harry":
            print("Welcome to Gryffindor!")
        case "Hermione":        
            print("Welcome to Gryffindor!")
        case "Draco":
            print("Welcome to Slytherin!")
        case "Luna":
            print("Welcome to Ravenclaw!")
            


main()