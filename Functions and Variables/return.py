# return 
def main():
    x = int(input("Enter a value for x: "))
    print("x squared = ", square(x))

def square(n):
    return n * n
# we are using return to explicitly return the value of the operation done to our parameter 
# return n ** 2 would return n to the power of 2
# return pow(n,2) would accomplish the same thing

main()