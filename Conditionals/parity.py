# parity 

def main ():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("The number is even.")
    else:
        print("The number is odd.")     

def is_even(n):
    return True if n % 2 == 0 else False    

# the result of n % 2 == 0: is a boolean value, so we can return it directly
#   return n % 2 == 0

main()