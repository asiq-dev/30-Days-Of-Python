# join a list into string / make a list into string

project_authors = ["Mike", "Sofia", "Helen"]
print(f"The people who worked on this project are: {','.join(project_authors)}.")

# join technique for numbers because join() not working with numbers
numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(', '.join(stringified_numbers))


# split the numbers
user_numbers = input("Please enter 5 numbers separated by space: ") # 1-2-3-4-5
numbers_tuple = user_numbers.split(" ")
print(numbers_tuple) 

#split() won't strip white space. Sometimes this isn’t really an issue,
#but sometimes you may need to go through the collection with a for loop and clear things up using strip.

user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
user_numbers = user_numbers.split(",")
numbers_list = []
for number in user_numbers:
    numbers_list.append(number.strip())
print(numbers_list) # ['1', '2', '3', '4', '5']


# new line \n
print("Super Special Mega Awesome Program\n\nBy Phillip Best")