# fuel gauge 

# prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer
# outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty
# if 99% or more remains, output F instead to indicate that the tank is essentially full


def main():
    fraction = input("Enter a fraction: ")
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    z = x / y
    z = z * 100
    z = round(z)
    z = gas(z)

def gas(z):
    if z <= 1:
        print("E ")
    elif z >= 99:
        print("F ")
    else:
        print(f"{z}%")





main()