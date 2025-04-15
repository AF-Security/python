# libraries and modules

# when you install python, you get a lot of libraries built into the interpreter
# random.py is one of these such files, https://docs.python.org/3/library/random.html

# we use keyword import to import the contents, the functions from, some module

# random.choice(seq), seq=sequence

# program to simulate a coin flip

import random
# importing random module to access all of the functions within it

coin = random.choice(["heads", "tails"])
# this will randomly select either heads or tails

print(coin)

# from is a keyword in python that allows us to import a specific function from a module
# import random imports everything from the random module







from random import choice
# using from, this imports the choice function from the random module into our namespace
# this means we can use the function without prefixing it with the module name
# this also allows us to make sure there aren't other conflicting functions or variables
# this is a good practice to use when importing functions from modules


