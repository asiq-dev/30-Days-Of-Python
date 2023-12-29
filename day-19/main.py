
# take a integer number with valid format
while  True:
    user_number = input("Please enter a whole number: ")

    if  user_number.lstrip("-").isnumeric():
        number = int(user_number)
        break
    else:
        print("You didn't enter a valid integer!")


#take a number with valid format using try and exception clause
    
while True:
    try:
        number = int(input("please enter a whole number : "))
        break
    except ValueError:
        print("you didn't enter a valid integer!")


# Handling multiple possible exceptions
        
import math

def averag(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    
    except (ZeroDivisionError, TypeError):
        print("An average cannot be calculated for the values you provided.")

averag(numbers = [5,4,78,48,5])


# The finally clause

def finally_flex():
    try:
        return
    finally:
        print("You return when I say you can return...")

finally_flex()