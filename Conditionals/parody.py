# parody
# addition, subtraction, multiplication, division, and exponentiation (%) of two numbers

def main():
    x = int(input("Enter any number, x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:
# if our argument, n, is divisible by 2 and has a remainder of 0, then it is even (true)
        return True
    else:
        return False


main()