# Initialize the running total
total = 0

while True:
    try:
        # Take input from the user
        x = int(input("Enter Coin (or type 0 to stop): "))
        
        # Break the loop if the user enters 0
        if x == 0:
            break
        
        # Add the input to the running total
        total += x
        print(f"Running Total: {total}")
    except ValueError:
        print("Please enter a valid integer.")

# Print the final total
print(f"Final Total: {total}")



def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n
main()


total = 0 
while True:
    n = int(input("Instert Coin: "))
    if n == 5 or n == 10 or n == 25:
        total = total + n
        amount_due = 50 - total
        print(f"Amount Due: {amount_due}")


