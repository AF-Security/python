# ask user for input
name = input("what is your name?")
# say hello back to the user by printing out the input
name = name.strip()
# strip() method removes any whitespace from the beginning or the end
name = name.capitalize()
# capitalize() method returns a string where the first character is upper case 
# title() method returns a string where the first character in every word is upper case
# upper() method returns a string where all characters are in upper case
# name = name.strip().title()  - chaining methods together 


#print("hello,", name)
# print will automatically introduct a new line after the output 

print ("hello, ", end="")
# overriding the default new line (\n) with an empty string
print(f'{name}')

# print(f"hello, {name}")



