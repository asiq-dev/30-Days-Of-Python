# 1) Create an empty set and assign it to a variable.

name = set()
print(name)


#2 Add three items to your empty set using either several add calls, or a single call to update.
name.update(["munna","ashiq","ashik"])
print(name)


# 3) Create a second set which includes at least one common element with the first set.
name_2 = {"islam","munna"}


# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
print(name.union(name_2))
print(name.intersection(name_2))
print(name.symmetric_difference(name_2))

# Create a sequence of numbers using range, then ask the user to enter a number. 
# Inform the user whether or not their number was within the range you specified.

numbers = range(20, 70)
usr_num = int(input("Enter a number: "))
print(numbers)
if usr_num in numbers:
    print('your number is in the range')
else:
    if usr_num < numbers[0]:
        print("your number is too low!")
    else:
        print("your number is too high!")
