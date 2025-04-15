# oudated 1
# prompt user for date in month-day-year order, formatted 9/9/1998 or september 9, 1998
# return date in year-month-day order, formatted 1998-09-09
# if the user's input is not a valid date in either format, prompt user again
# assume every month has no more than 31 days


def main():
    while True:
        try:
            date = input("Enter a date please: ").title()
            formatted_date = convert(date)
            if formatted_date:
            # a truthy value (a non-empty string, a non-zero number, or a populated list)
                print(formatted_date)
                break
        except ValueError:   
            print("Invalid date format. Please try again.")
        except EOFError:
            print("\n")
            break


def convert(date):
    # Dictionary to map month names to numbers
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    # Check for "Month Day, Year" format
    if "," in date:
        try:
            month, day, year = date.split(" ")
            day = day.strip(",")
            # month = months[month]  # Convert month name to number
            if month in months:
                return f"{int(year):04d}-{int(months[month]):02d}-{int(day):02d}"
        except:
            raise ValueError

    # Check for "MM/DD/YYYY" format
    elif "/" in date:
        try:
            month, day, year = date.split("/")
            return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
        except:
            raise ValueError

    # If neither format matches, raise an error
    else:
        raise ValueError


main()