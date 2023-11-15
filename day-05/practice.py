#1 Try to approximate the behaviour of the is operator using ==.
a = 5
b = 6

print(a==b)
print(a is b)
print(id(a)==id(b))

a = b
print(a==b)
print(a is b)
print(id(a)==id(b))

#2 Try to use the is operator or the id function to investigate the difference between this:
print("exercise 2")
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(numbers is new_numbers)

number = [1, 2, 3, 4]
print(id(f"numbers memory: {number}"))
number.append(5)
print(id(f"numbers memory: {number}"))
print(number)

#3 Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
    print(f"the number {num} is positive")
elif num < 0:
    print(f"the number {num} is negative")
else:
    print(f"the number {num} is Zero")



#4) Write a program to determine whether an employee is owed any overtime
emp_name = "Enter Employee name:"
worked_hours = float(input(f"How many hours {emp_name} worked: "))
hourly_wage = float(input(f"What is {emp_name} hourly wage rate: "))

if worked_hours > 40:
    regular_pay = 40 * hourly_wage
    overtime = (worked_hours - 40) * (hourly_wage * 1.1)
    amount = regular_pay + overtime
    print(f" {emp_name} is owed ${amount}")
else:
    amount = hourly_wage * worked_hours
    print(f"{emp_name} is owed ${amount}")    