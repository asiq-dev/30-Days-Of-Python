# *args 
# def mul(*args):
#     print(args[0] * args[1])

# mul(5, 10)


# def multigreet(*names):      #multigreet (other,*args)
#     for name in names:
#         print(f"Hello, {name}!")

# multigreet("Rolf", "Bob", "Anne")






# print(dict(name="Phil", age=29, city="Budapest", nationality="British")) dict is dictionary

# kwargs
def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

pretty_print(title="The Matrix", director="Wachowski", year=1999)



# in the below code, args and kwargs both used 
def pretty_print(*args , **kwargs):
     for obj in args:
        print(obj)
    
     for key, value in kwargs.items():
        print(f"{key}: {value}")
   
pretty_print("watch","yes",title="The Matrix", director="Wachowski", year=1999)



# Other uses for * and **

numbers = [1, 2, 3, 4, 5]
print(*numbers, sep=" | ")
#output = 1 | 2 | 3 | 4 | 5
#In the avobe code shown 'sep' function used for separet value by symbol 



# 1
def print_movie(*args):
    for value in args:
        print(value)

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(movie.values())


# 2
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(**movie)



# 3
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(studio="Warner Bros", **movie)

