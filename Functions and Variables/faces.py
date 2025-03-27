# making faces
# implement a funciton called convert that accepts a str as input and returns the same input with any :) converted to smiley emoji
# all other text should be returned unchanged

# implement a function called main that prompts the user for input, calls convert on that input, and prints the result

def main():
    smiley = convert(input("How are you today? "))
    print(smiley)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()