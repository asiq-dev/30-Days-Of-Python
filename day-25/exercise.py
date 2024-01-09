# 1) Write a function that prompts the user for their name and then greets them. You should process the string by removing any whitespace
# and converting the string to title case.

def greets():
    name = input("Enter your name: ").strip().title()
    print(f"hello! i am {name or 'john'}.")

print(greets())


# 2) Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).
from string import ascii_letters

def is_ascii_letters(test_string):
    return all(character in ascii_letters for character in test_string)

print(is_ascii_letters("munna5351"))


# 3) Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). 
# Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.


import random
population_range = range(1, 101)

numbers = [random.sample(population_range,15) for _ in range(3)]
# num = [random.sample(range(1, 100),15)]
print(numbers)
for number_set in numbers:
    number_set.sort(reverse=True)
    del number_set[5:]
    print(number_set)
