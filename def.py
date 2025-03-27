# definition of custom functions 

def main ():    
    name = input("What is your name?")

    hello(name)
# scope is where a variable only exists within the confines of the function where it has been defined 

def hello(to):
    print("hello,", to)
# all indented lines after def "___" : will define the meaning of the function
# we define what hello(to) will do on the indented line, print () where 'to' is our parameter
# below we will replace this with an argument, containing the specific value of name
# def hello(to="world"): would define the hello function to literally print world

# def is how we define functions in python

# print(name)

main()

# general notes, you always need to define a function in line before calling it
# organize the main part of your code into the main(): function 