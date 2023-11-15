# movies = [
#     (
#         "Eternal Sunshine of the Spotless Mind",
#         "Michel Gondry",
#         2004
#     ),
#     (
#         "Memento",
#         "Christopher Nolan",
#         2000
#     ),
#     (
#         "Requiem for a Dream",
#         "Darren Aronofsky",
#         2000
#     )
# ]

# counter = 1
# for title,director,year in movies:
#     print(f" {counter}. {title} ({year}), by {director}")
#     counter += 1


# for counter, (title,director,year) in enumerate(movies, start=1):
#     print(f" {counter}. {title} ({year}), by {director}")




#Zip part

# movie_titles = [
#     "Forrest Gump",
#     "Howl's Moving Castle",
#     "No Country for Old Men"
# ]

# movie_directors = [
#     "Robert Zemeckis",
#     "Hayao Miyazaki",
#     "Joel and Ethan Coen"
# ]

# movies = list(zip(movie_titles, movie_directors))

# for title, director in movies:
#     print(f"{title} by {director}.")

# movies_list = movies

# print(f"There are {len(movies_list)} movies in the collection.")
# print(f"These are our movies: {movies_list}.")


pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")