# The map function

def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

for number in cubed_numbers:
    print(number)

print(*cubed_numbers, sep = ",")


# map with multiple iterables
def add(a, b):
    return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")

# map with lambda expressions

numbers = [1,2,3,4,5]
cubed_numbers = map(lambda number: number **3 , numbers)

print(cubed_numbers)



# The operator module

from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")


# operator methodcaller

from operator import methodcaller

names = ["tom","michel","holland"]
title_names = map(methodcaller('title'),names)

# Conditional comprehensions   
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [number for number in numbers if number % 2 == 0]


# The filter function
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)