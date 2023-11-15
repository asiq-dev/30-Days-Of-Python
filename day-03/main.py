#concatinate two string in one line
# hourly_wage = input("Please enter your hourly wage: ")
# hours_worked = input("How many hours did you work this week? ")

# print("Hourly wage: " + hourly_wage)
# print("Hours worked: " + hours_worked)

#convert int/float into string
age = str(28)
age = "28"  #both are same
print(age)


#convert string into int/float
intage = int("25")
fltage = float("25.5")
print(intage,fltage)


#format interpolation 
mname = "munna"
mage = 25
profession = "Software Engineer"
print("{} is {} years old!".format(mname,mage))
#another ways of using format
output = "{} is {} years old, and {} works as a {}."
print(output.format(mname,mage,mname,profession))

output = "{name} is {age} years old, and {name} works as a {profession}."
print(output.format(name=mname,age=mage,profession=profession))


#f-strings interpolation
name = "John"
age = 24
print(f"{name} is {age} years old!")
print(f"{name} is {age*12} months old!")


#Strings cases
"Hello, World!".lower()       # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"


#removing white space from the strings
"  Hello, World!  ".strip()  # "Hello, World!"

#processing multiple things in one line
user_name = " ROLF SMITH  ".strip().title()





#Excercise written from here.................

name = input("please enter your name: ").strip().title()
greeting = f"Hello {name}"
print(greeting)

#Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
myAge = "i am " + str(25)
print(myAge)

#Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}), directed by {director}")