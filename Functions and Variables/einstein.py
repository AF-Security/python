# Einstein 
# prompt the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
# Assume that the user will input an integer

def main():
    joules = energy(float(input("Enter mass in kg: ")))
    # allowing for decimal input
    joules = round(joules)
    # outputting the result rounded to an integer 
    print("energy in Joules: ", joules)

def energy(mass):
    mass = (mass) * 9.0 * 10**16
    return mass
    # E = mc^2
    # c =~ 3.0 x 10^8 m/s, c*c= = 9.0 x 10^16 m^2/s^2


main()