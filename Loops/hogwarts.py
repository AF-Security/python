# hogwarts

students = ["Hermoine", "Harry", "Ron"]
# to 'index' into the list and call a specific variable, or student by their name we use more square brackets

# print(students[0])
# print(students[1])
# print(students[2])

for student in students:
    print(student)
# this will print each student in the list  




# we can use len or length in python to tell us the length of a list 
for i in range(len(students)):
    print(i+1, students[i])
# this will print each student in the list
