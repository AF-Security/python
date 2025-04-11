# twitter
# prompt user for a string of text
# output same string, but with all vowels omitted, whether input in lowercase or uppercase


def main():
    user_input = input("Enter a string: ")
    user_input = convert(user_input)
    print(user_input)

def convert(input):
    twttr = ""
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for c in input:
        if c in vowels:
            twttr = twttr
        else:
            twttr = twttr + c
    return twttr



main()