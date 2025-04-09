# dictionaires, dict
# data structures that allow to store data in key-value pairs, associate a value to a key


students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
}

print(students["Hermione"])
# lists use locations that are numeric, 0, 1, 2, 3, etc.
# dictionaries use keys, which can be strings or numbers, to access the values
# the print function will return the value associated with the dictionary index or key "Hermione"


for student in students:
    print(student, students[student], sep=", ")
# a for loop in python will iterate through the keys of a dictionary, in this case the names of the students
# students[student] will return the value associated with the key, in this case the house of the student


# dictionaries with many values
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
# for student in students is iterating over the list of dictionaries
# student["name"] is accessing the value associated with the key "name" in each dictionary
# this will print the name of each student in the list
                                          