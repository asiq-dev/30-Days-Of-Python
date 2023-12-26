#** function as variable
def add(a,b):
    print(a + b)

def multi(a,b):
    print(a*b)

adder = add     #assign  'add'functions to 'adder' variable
multier = multi
del add    #delete the function,
del multi
adder(5,6)     #adder work as function
multier(20,30)
print(adder)
print(multier)



#** Functions as arguments

def get_grade_average(student):
    return student["grade_average"]

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

highest = max(students,key = get_grade_average)
print(highest)


#** returning functions from other functions

def add(a,b):
    print(a+b)

def substruct(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    if b==0:
        print("You can't divide by 0!")
    else:
        print(a/b)

operations = {
    "a" : add,
    "s" : substruct,
    "m" : multiply,
    "d" : divide
}

selected_options = input("""Please select one of the following options: 
                         
a: add
s: substruct
m: multiply
d: divide

what would you like to do?""")

operation = operations.get(selected_options)


if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a,b)

else:
    print("invalid Selection!")


#lambda expressions
    
lambda_add = lambda a,b: a+b
print(lambda_add(5,6))



