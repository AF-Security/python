# math interpreter
# prompt user for an arithmetic expression and then calculates and outputs the result as a floating point value
# formatted to one decimal place
# assume user's input will be formatted as x, y, z with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer
# assume that if y is /, z will not be 0


def main():
    response = input("Expression: ").strip()
    x, y, z = response.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        return None
    print(f"{result:.1f}")

main()
