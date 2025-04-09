# super mario

print("#")
print("#")
print("#")


for _ in range(3):
    print("#")



def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

# an equivalent function to print_column(height) is:
# def print_column(height):
#     print("#\n" * height, end="")

main()


# printing horizontal rows
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()