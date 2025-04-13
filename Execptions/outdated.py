# outdated 
# prompt user for date in month-day-year order, formatted 9/9/1998 or september 9, 1998
# return date in year-month-day order, formatted 1998-09-09
# if the user's input is not a valid date in either format, prompt user again
# assume every month has no more than 31 days



def main():
    while True:
        try:
            date = input("Enter a date please: ")
            convert(date)
            
        except NameError:
            pass


def convert(date):
    months = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December:":12
        }
    month, day, year = date.split("/")
    for text_month in months:
        if month in months.values():
            print(f"{year} - {text_month} - {day}")

    # month, day, year = date.split("")




main()