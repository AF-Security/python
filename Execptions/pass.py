# pass



def main():
    x = get_int("What is x? ")
    print(f"x is equal to {x}")
   


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # if we are immediately declaring a variable and returning it,
            # may not always be necessary to even define it direclty 
        except ValueError:
            pass
            # rather than continually printing error messages, we can pass
            # rather than handling it further or specifically 
            # print("Sorry, x is not an integer")
        

main()