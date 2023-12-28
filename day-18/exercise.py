#1) Import the fractions module and create a Fraction from the float 2.25. 
# You can find information on how to create fractions

import fractions
print(fractions.Fraction(2.25))


#2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:

from math import fsum

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
summation = fsum(numbers)
print(summation)


#3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function.

import random as rnd
rnd_num = (rnd.randint(1,100))
print(rnd_num)

# 4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. 
# This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

target_num = (rnd.randint(1,100))
guess_num = int(input("Enter a guess number: "))

while guess_num != target_num:
    if guess_num > target_num:
        print("guess number is big!")
    elif guess_num < target_num:
        print("guess number is small")
    guess_num = int(input("Enter a guess number: "))

print("guess number is right")
