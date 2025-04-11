# vanity plates

# All vanity plates must start with at least two letters
# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
# Numbers cannot be used in the middle of a plate; they must come at the end. AAA222 would be acceptable; AAA22A would not be acceptable. 
# The first number used cannot be a ‘0’
# No periods, spaces, or punctuation marks are allowed
# Assume that any letters in the user’s input will be uppercase



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length_check(s):
        if alpha_num_check(s):
            if start_check(s):
                if num_check1(s):
                    if num_check2(s):
                        return True
                    else:
                        return False
            

def alpha_num_check(s):
    for c in s:
        if c.isalnum():
          continue 
        else:
          return False
    return True


def length_check(s):
     if 2 <= len(s) <= 6:
          return True
     else:
          return False 

def start_check(s):
    start = s[0:2]
    for c in start:
        if c.isalpha():
            continue
        else:
            return False
    return True
        

def num_check1(s):
    for c in s[2]:
        if c.isdigit():
            if c == "0":
                return False
            elif s[3:].isalpha():
                return False
        elif c.isalpha():
            continue
    return True

def num_check2(s):
    for c in s[3]:
        if c.isdigit():
            if c == "0" and s[2].isalpha():
                return False
            elif s[4:].isalpha():
                return False
        elif c.isalpha():
            continue
    return True


    
        
        
main()
