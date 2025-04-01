# meal time



def main():
    reply = input("What time is it? ").strip()
    convert(reply)

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    if 7 <= hours + minutes < 8:
        print("Breakfast time")
    elif 12 <= hours + minutes < 13:
        print("Lunch time")
    elif 18 <= hours + minutes < 19:
        print("Dinner time")
    else:
        None

   


# if __name__ == "__main__":
main()



# meal time

def main():
    reply = input("What time is it? ").strip()
    time_in_24hr = convert(reply)
    if 7 <= time_in_24hr < 8:
        print("Breakfast time")
    elif 12 <= time_in_24hr < 13:
        print("Lunch time")
    elif 18 <= time_in_24hr < 19:
        print("Dinner time")

def convert(time):
# Use .casefold() to make the input case-insensitive
    time = time.casefold()
    
# Split the time into hours, minutes, and period (a.m./p.m.)
    if "a.m." in time or "p.m." in time:
        time, period = time.split(" ")
# here we have now split the time and period from our input string
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        # Convert to 24-hour format
        if period == "p.m." and hours != 12:
            hours += 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:
        # Assume input is already in 24-hour format
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
    
    # Convert hours and minutes to a float representing the time
    return hours + minutes / 60

# if __name__ == "__main__":
main()