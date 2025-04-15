# say

import sys

from saying import hello

def main():

    if len(sys.argv) == 2:
        hello(sys.argv[1])

# while importing other files, we need to be mindful of main or other functions being called
# the proper way of defining a main function and appropriately calling it, rather than unconditionally

# referece saying.py
# 
# if __name__ == "__main__":
    # main()

# __name__ in python is a variable whose value is automatically set to be "__main__" when you run a file from the command line
# by the definition of the __name__ value, if we import a file main will not get set to "main" and therefore called

main() 