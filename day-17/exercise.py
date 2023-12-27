#1 Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. 
# Remember that we can use the sum function to add the values in an iterable.
def multi_add(*numbers):
    print(sum(numbers))

multi_add(1,2,3,4,5)


#2 Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. 
# Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def show(*args, **kwargs):

    print(f"Positional arguments are {args}")

    print(f"Keyword arguments are {kwargs}")

    

show (3, "blue",[5,7,3], name="munna",id = 18193203003, key = lambda a: a**2)


#3 Print the following dictionary using the format method and ** unpacking.

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
 }

country_template = """
Name:{name},
Population:{population},
Capital:{capital},
Currency:{currency}
"""

print(country_template.format(**country))
# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for 
# print function's sep parameter for this exercise.

print(*range(1, 21), sep=", ")

# 5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call

print(*range(1, 21), sep="\n")
