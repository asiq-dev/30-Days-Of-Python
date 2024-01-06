# One interesting question is, what happens when we call iter on the list_iterator?

numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)

print(numbers_iter is iter(numbers_iter)) 

# Replicating for loops with iter

numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)

while True:
    try:
        number = next(numbers_iter)
    except StopIteration:
        break
    else:
        print(number)


# Generators
        
def first_hundred():
    for number in range(1, 101):
        yield number

g = first_hundred()
print(next(g))
print(next(g))
print(next(g))



# Example of The yield keyword
def first_hundred():
    print("First value requested\n")

    for number in range(1, 101):
        print("Starting new iteration")
        yield number
        print("Ending this iteration\n")

g = first_hundred()

print(next(g))
print(next(g))



# Generator Expressions

# 1
squares = (number ** 2 for number in range(1, 11))
for square in squares:
    print(square)

# 2
squares = (number ** 2 for number in range(1, 11))
print(*squares, sep=", ")

# 3
squares = (number ** 2 for number in range(1, 11))

print(next(squares)) 
print(next(squares))  
print(next(squares))  

# 4
total = sum(number ** 2  for number in  range(1,  11))
print(total)