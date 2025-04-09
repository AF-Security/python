# for loops
# for is used to define a variable, in this case i, and then iterate through a list or range of numbers
# the defined variable will be iterated, or assigned to each value in the list or range of numbers

for i in [0, 1, 2]:
# square brackets are used to create a list
    print("meow")


for i in range(3):
# range(3) creates a list of numbers from 0 to 2, up to but not including 3
# using a single underscore as the variable name is a convention to indicate that the variable is not used
    print("meow")   


print("meow\n" * 3, end=" ")
# the string "meow" followed by a newline character is repeated 3 times)
# the string "meow" is repeated 3 times


# in python, when you want to define a specific type of input, start with while True:
while True:
# this creates an infinite loop
    n = int(input("Enter a number: "))
    if n < 0:
        continue 
    else:
        break
# the loop will continue until a non-negative number is entered
# if n > 0:
#     break
# the loop will break if a negative number is entered   

def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n
main()


