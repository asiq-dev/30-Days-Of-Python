# List comprehensions
names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]
print(names)

# another example

names = ["mary", "Richard", "Noah", "KATE"]
ages = [40,25,37,50]

people = [(name.title(), age) for name,age in zip(names,ages)]
# people = [
#     (name.title(),age)
#     for name,age in zip(names, ages)
# ]
print(people)

# set comprehensions
names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}
print(names)

# dictionary comprehensions
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {
    student_id: name.title()
    for student_id, name in zip(student_ids, names)
}
print(students)