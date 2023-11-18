#print out the first ten even numbers, starting with 2

for number in range(1, 11):
    print(number * 2)
    

for number in range(2, 21, 2):
    print(number)




#make a funtion for get even numbers

def get_even_numbers():
    for number in range(1,11):
        print(number * 2)
get_even_numbers()




# Function parameters and arguments

def get_even_numbers(amount):
    for number in range(1, amount+1):
        print(number * 2)

get_even_numbers(20)




# Specifying multiple parameters - note that: always sent argument in right order

def x_print(request_output,quantity):
    for _ in range(quantity):
        print(request_output)
x_print('hello',5)


#Keyword arguments
def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)

x_print(requested_output="Hello", quantity=5)
x_print(quantity=5, requested_output="Hello")
