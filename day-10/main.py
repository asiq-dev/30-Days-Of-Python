# #1
# student = {
#     "name": "John Smith",
#     "grades": [88, 76, 92, 85, 69]
# }

# print(student["grades"])

# #2
# student = {
#     "name": "John Smith",
#     "grades": [88, 76, 92, 85, 69]
# }

# print(student.get("grade"))  # None
# print(student.get("grade", []))  # []




# #3 Some opearation with dictionary

# # Adding items to a dictionary
# student = {
#     "name": "John Smith",
#     "grades": [88, 76, 92, 85, 69]
# }
# student["age"] = 17
# print(student)





# # Updating items to a dictionary
# movie = {
#     "title": "Avengers: Endgame",
#     "directors": ["Anthony Russo", "Joe Russo"],
#     "year": 2019
# }

# meta_info = {
#     "runtime": 181,
#     "budget": "$356 million",
#     "earnings": "$2.798 billion",
#     "producer": "Kevin Feige"
# }
# movie.update(meta_info)
# # movie.update({
# #     "runtime": 181,
# #     "budget": "$356 million",     #another way of update a dictonary
# #     "earnings": "$2.798 billion",
# #     "producer": "Kevin Feige"})
# print(movie)



# #Modifying existing items in a dictionary
# student = {
#     'name': 'John Smith',
#     'grades': [88, 76, 92, 85, 69],
#     'age': 17
# }
# student["age"] = 18
# print(student)



# #Deleting items from a dictionary
# movie = {
#     "title": "Avengers: Endgame",
#     "directors": ["Anthony Russo", "Joe Russo"],
#     "year": 2019,
#     "runtime": 181
# }
# del movie["runtime"]
# # movie.pop('runtime') #another technique to remove value from dictonary
# # movie.clear()
# print(movie)



# #4 Iterating over dictionaries

# movie = {
#     "title": "Avengers: Endgame",
#     "directors": ["Anthony Russo", "Joe Russo"],
#     "year": 2019
# }

# for attribute in movie:
#     print(attribute)



# get the key and value at the same time using items() function
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

for key, value in movie.items():
    print(f"{key}: {value}")


