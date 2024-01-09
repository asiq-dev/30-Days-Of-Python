#calculator using python dictonary

from operator import add, sub, mul, truediv

operations = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div':truediv
}

selected_option = input("select opearation for perform: ").strip().lower()

operation = operations.get(selected_option)

if operation:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The result is for {selected_option} opearation: {operation(a, b)}")

else:
    print("Invalid operation!")




#Boolean operators for control flow

# and operation
x = int(input("Please enter a number between 1 and 10: "))

if x > 0 and x < 11:
    print(x)
else:
    print("Invalid selection")


# OR opearation
x = int(input("Please enter a number between 1 and 10: "))

if x > 1 or x > 10:
    print(x)
else:
    print("Invalid selection")


# Using or to replace falsy values
    
name = input("Please enter your name: ").strip().title() or "John Doe"

# Using and to change how we handle return values

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return

a = 6
b = 0

result = divide(a, b)

if result and result.is_integer():
    print(f"{a} / {b} produces an integer result.")


# Truncation over slicing
    
numbers = [1, 54, 2, -4, -65, 23, 97, 45, 14, 19, 73, -6, 31, 92, 3]

positive_numbers = sorted(number for number in numbers if number > 0)
del positive_numbers[10:]

print(positive_numbers)

# Check for multiple values using in

proceed = input("Would you like to continue? ").strip().lower()

if proceed in ("y", "yes", "continue"):
    print(proceed)