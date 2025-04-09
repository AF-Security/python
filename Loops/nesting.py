# square, length x width


def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print a brick
            print("#", end="")
        # print with no arguments will print a new, blank line    
        print()

main()


def print_square(size):
    for i in range(size):
        print("#" * size)
        


        # print_row(size):

# def print_row(width):
    # print("#" * width)


