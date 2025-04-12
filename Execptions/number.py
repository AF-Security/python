# error handling 

def main():
    x = get_int()
    print(f"x is equal to {x}")
   


def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            # return = int(input("What is x? "))
            # if we are immediately declaring a variable and returning it,
            # may not always be necessary to even define it direclty 
        except ValueError:
            print("Sorry, x is not an integer")
        else:
            break
    return x

# return is used to return values from a function
# break is used to break out of a loop
# return, while returning a value, will also break out of a loop
# rewriting the last few lines
        # else:
        # return x


main()
    
