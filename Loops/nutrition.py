# FDA fruits


x = input("What kind of fruit would you like?")

fruits = [
    {"fruit": "apple", "calories": "130"},
    {"fruit": "avocado", "calories": "50"}
]

for fruit in fruits:
    if fruit["fruit"] == x:
        print(fruit["calories"])
        break