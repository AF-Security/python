# playback speed
# prompt a user for input and then outputs the same input, replacing each space with ...

x = input("Enter a string: ").replace(" ", "...")
# .replace() is a method to return a copy of the string with all occurrences of a substring replaced with a new one
# in this case, we are replacing all spaces with '...'

print(x)
