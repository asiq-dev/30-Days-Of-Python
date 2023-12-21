#1 Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to.
# The function should return the result of this operation

def power(a,b):
    return a**b

print(power(2,3))




#2 Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, 
# and has had any excess whitespace removed.

def process_string(str):
    return str.strip().lower()

print(process_string("MunNa"))




#3 Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. 
# The data should be in the following format: ("Tom Hardy", "English", 42)  # name, nationality, age


# def actor(info):
#     name, nationality, age = info

#     return{
#         name: name,
#         nationality: nationality,
#         age: age
#     }
# actor("Tom Hardy", "English", 42)




#4 Write a function that takes in a single number and returns True or False depending on whether or not the number is prime.

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
        else:
            return True

print(is_prime(10))