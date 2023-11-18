#1 Define four functions: add, subtract, divide, and multiply. Each function should take two arguments,
# and they should print the result of the arithmetic operation indicated by the function name.

def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def multi(a, b):
    print(a * b)

def div(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

a, b = input("Enter two number : ").split()

add(int(a), int(b))
sub(int(a), int(b))
multi(int(a), int(b))
div(int(a), int(b))


#2 Define a function called print_show_info that has a single parameter. 
# The argument passed to it will be a dictionary with some information about a T.V. show. For example:

def print_show_info(show):
    print(f"{ show['title'] } ({show['initial_release']}) - {show['seasons']} seasons")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
 }

print_show_info(tv_show)


#3 Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration,
#  passing in each dictionary. You should end up with each series printed in the appropriate format.

def print_show_info(show):
    for series in show:
        print(f"{ series['title'] } ({series['initial_release']}) - {series['seasons']} seasons")

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

print_show_info(series)


#4 Create a function to test if a word is a palindrome. 
# A palindrome is a string of characters that are identical whether read forwards or backwards.


def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)

    if list(word) == list(reversed_word):
        print(True)
    else:
        print(False)

is_palindrome("Hannah") 
is_palindrome("Fred")