#1
# num = input("Enter a number for check even: ")
# while int(num) % 2 != 0:
#     print(f" {num} is not even ")
#     num = input("Enter enother number: ")

# print(f"{num} is even")



#2
# while True:
#     guess_number = int(input("Enter the guess number: ")) 

#     if guess_number == 1:
#         print('you enter one')  

#     elif guess_number == 2:
#         print("you enter two")

#     elif guess_number == 3:
#         print("you enter three")

#     elif guess_number == 4:
#         print("you enter four")

#     elif guess_number == 5:
#         print("you enter five")

#     elif guess_number == 6:
#         print("you enter six")

#     elif guess_number == 8:
#         print("you enter eight")
    
#     elif guess_number == 9:
#         print("you enter nine")

#     elif guess_number == 10:
#         print("you enter ten")
    
#     elif guess_number == 7:
#         print("You guess the right number")
#         break
    
#     else:
#         print('You enter invalid number!')


#3
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)