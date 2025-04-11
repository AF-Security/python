


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
     num_check1(s)
    

def num_check1(s):
    for c in s[3:6]:
        if c.isnumeric() and c == 0:
            return False
        elif c.isalnum():
            continue
    return True



main()


def num_check(s):
    number_started = False
    for c in s[2:]:
        if c.isdigit():
            if not number_started:
                if c == "0":  # First number cannot be 0
                    return False
                number_started = True
        elif number_started and c.isalpha():  # Numbers cannot be followed by letters
            return False
    return True