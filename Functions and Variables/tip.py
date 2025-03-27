# tip calculator, just the tip!

def main ():
    dollars = dollars_to_float(input("Enter the amount of the bill: "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.lstrip("$")
    d = float(d)
    return d

# accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. 
# For instance, given $50.00 as input, it should return 50.0.

def percent_to_float(p):
    p = p.rstrip("%")
    p = float(p)
    p = p / 100
    return p

main()