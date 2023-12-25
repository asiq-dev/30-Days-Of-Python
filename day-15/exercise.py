#1 Convert the following for loop into a comprehension:
#   numbers = [1, 2, 3, 4, 5]
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

# solution
numbers = [1, 2, 3, 4, 5]
numbers = [number ** 2 for number in numbers]
print(numbers)


#2  Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = {
    key:value.title() for key,value in movie.items()
}

print(movie)