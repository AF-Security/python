# python calculator and interactive mode (running code directly in terminal)

x = input("enter a value for x: ").strip()
# function nesting: x = int(input("enter a value for x: "))
y = input("enter a value for y: ").strip()  

z = int(x) + int(y)
# int is converting the string variable 'x' to an integer, so we can perform arithmetic operations on it

print(f"integer sum = {z}")    
# if we wouldn't be using 'z' again, it is not necessary to store it in a variable, we can directly print the result
# print(x + y) - if we used funciton nesting above to already convert strings to integer values 