
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