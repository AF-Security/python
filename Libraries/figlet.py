# figlet 

# Expects zero or two command-line arguments:
    # Zero if the user would like to output text in a random font.
    # Two if the user would like to output text in a specific font,
    # in which case the first of the two should be -f or --font, 
    # and the second of the two should be the name of the font.
   
# Prompts the user for a str of text.
# Outputs that text in the desired font.

# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.



if sys.argv() == 1 or sys.argv() == 3:
    if sys.argv() == 1:
        # output random

    else sys.argv() == 3:
        while True:
            if cli_1 == -f or cli_1 == --font:
                continue
            elif font in figlet.getFonts():
                continue
            else:
                sys.exit("Invalid font or font type input ")




else:
    sys.exit("Invalid CLI input ")
