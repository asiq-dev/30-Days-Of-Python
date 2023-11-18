#1 Write a short guessing game program using a while loop. The user should be prompted to guess a 
# number between 1 and 100, and you should tell them whether their guess was too high 
# or too low after each guess. The loop should keeping running until the user guesses the number correctly.


# import random

# actual_num = random.randint(1,100)
# print(actual_num)
# guess_num = int(input('Enter guess number between 1 to 100: '))

# while guess_num != actual_num:
    
#     if guess_num > actual_num:
#         print("your guess number is larger!")

#     else:
#         print("your guess number is less!")

#     guess_num = int(input("guess another number: "))
    
   
# print("You guess the correct number!!")




#2 Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield 
# one character at a time.

# name = "python"

# for i in name:
#     if i == 'o':
#         continue
#     print(i)



#3 Using one of the examples from earlier—or a solution entirely 
# of your own—create a program that prints out every prime number between 1 and 100.

for i in range(2,101):
    for j in range(2, i):
     if i % j == 0:
        break
    else:
        print(f"the number {i} is prime")
