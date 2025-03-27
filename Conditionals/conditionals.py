# conditionals 
# python has many built in conditional statements and syntax
# if, elif, else, and, or, not, in, is, ==, !=, <, >, <=, >=

# comparing integer values input from a user

x = int(input("Enter any number, x: "))
y = int(input("Enter any number, y: "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
# we can use multiple if statements to compare multiple conditions
# however, this is not the most efficient way to compare multiple conditions- elif (else if)     