# 1  Use map to call the strip method on each string in the following list:

import operator
from operator import methodcaller

def line_stripper(line):
    return line.strip()


humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]

print(*map(line_stripper,humpty_dumpty), sep="\n")


#2  Below you'll find a tuple containing several names: Use a list comprehension with a filtering condition so that only names
#  with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
new_names = [name.title() for name in names if len(name) < 8]
print(new_names)

#  another solution
new_names = map(methodcaller('title'), filter(lambda name: len(name) < 8,names))
print(new_names)



# 3 Use filter to remove all negative numbers from the following range: range(-5, 11). 
# Print the remaining numbers to the console.

def is_positive(number):
    return number >=0

print(*filter(is_positive,range(-5, 11)))