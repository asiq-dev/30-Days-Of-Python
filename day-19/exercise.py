#1) Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual
# grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user 
# when the values they entered cannot be converted.

grades = input("please enter your grades, separated by commas: ").split(",")

try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("The grades you entered were in an invalid format.")



#2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.
    
def func():
    try:
        return "its return from try clause!"
    finally:
        return "its return from finally clause!"
    
print(func())



# 3 Imagine you have a file named data.txt with this content:
# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't 
# exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.
# When files don't exist when you try to open them, the exception raised is FileNotFoundError.

try:
     with open("data.txt" , 'r') as datafile:
         print(datafile.read())

except FileNotFoundError:
    print("Data.txt file not found! ")