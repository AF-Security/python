# command line arguments

# the sys module, system, contains functions and variables specific to the system itself
# docs.python.org/3/library/sys.html
# this module allows us to access command line arguments

# within the sys module, there is a variable called argv, argument vector
# this variable is a list, of command line arguments
# the first element in the list is the name of the script itself
# sys.argv

import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# we don't always have to handle exceptions, if we can be smarter about what are taking as input
# checking for specific cases that we are worried about, providing feedback to the user for appropriate input

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])



# here, we can use sys.exit to exit the program and print the error messages

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# this is a more elegant way to handle the error, rather than using try/except
# this will then print the program message, and we can be sure sys.argv[1] is valid
print("Hello, my name is", sys.argv[1])



# get rid of the elif statement if we don't want to limit the number of arguments at the prompt
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# here we are using a for loop to iterate through all of the arguments entered at the prompt
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
    # so we aren't printing the name of the function, we use a slice to start at 1, the second element
    # this will print all of the arguments entered at the prompt- i.e. through the end of the list