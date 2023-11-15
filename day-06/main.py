movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
      print(f"{movie[0]} ({movie[2]}), by {movie[1]}")


# break statement
for movie in movies:
      # Check the title of the current movie is Memento
      if movie[0] == "Memento":
            # If the title is Memento, inform the user that the movie exists and break the loop
            print("Memento is in the movie library!")
            break



# Range

numbers = list(range(10))
immutable_numbers = tuple(range(10))

print(numbers)
print(immutable_numbers)

for number in range(10):
    print(number)

for number in range(10):
    print("Hello!")