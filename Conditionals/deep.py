# deep

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").casefold()
# we use the casefold() method to convert the string to lowercase
    if is_42(answer):
        print("Yes")
    else:  
        print("No")

def is_42(response):
    if response == "42" or response == "forty-two" or response == "forty two":    
        return True 
    else:
        return False
    
# we could also define this function in a single line such as:
    # return True if response == "42" or response == "forty-two" or response == "forty two" else False






main ()