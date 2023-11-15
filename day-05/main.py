#booleans value

print(bool("Hello World"))
print(bool(""))
print(bool(5))
print(bool(0))
print(bool(True))
print(bool(False))
print(bool([1,2,3]))
print(bool([]))

#comparing operators
print('comparing oparations')
print(5>10) 
print(5<10) 
print(10>10) 
print(10<=10) 
print('a'< 'A') 
print(50!=60) 
print("hello" != 'hi') 

#comparing between 'is' and ==
print('compare between is and ==')
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)

print(id(a))
print(id(b))

x = [1,2,3]
y = x
print(x==y)
print(x is y)

print(id(x))
print(id(y))

#condition statements
print('conditional statements')
age = int(input('Enter your age: '))
if age < 16:
    print("youre the eligable for child rate of 80p.")
elif age >= 60:
    print("youre eligable for OAP rate of $1.")
else:
    print("You must pay standard rate $1.50.")


# Truth values and conditional statements

name = input("Enter your name: ")

if name:
    print(f"Your name is: {name}")
else:
    print("you enterd nothing")