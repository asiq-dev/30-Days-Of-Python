movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0

for movie in movies:
    total_budget += movie[1]


avg_budget = total_budget/len(movies)
print("The average cost is: ",avg_budget)

high_budget_movies = []

for movie in movies:
    if movie[1]>avg_budget:
        high_budget_movies.append(movie)
        print(f" '{movie[0]}' cost ${movie[1]:,}: the over average cost: {movie[1] - avg_budget:,}")

print(f"There were {len(high_budget_movies)} movies with over average budget.")




#code for the add extra movies....


new_movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("Enter how many movie you want to add to the list: "))
for movie in range(new_movie_count):
    name = input("Enter movie name: ")
    budget = int(input("Enter the budget: "))
    new_movie = (name,budget)
    new_movies.append(new_movie)

print(new_movies)

new_total_budget = 0

for movie in new_movies:
    new_total_budget += movie[1]

new_avg_budget = new_total_budget/len(new_movies)
print("the avg budget is: ",new_avg_budget)
new_high_budget_movies = []
for movie in new_movies:
    if movie[1]>new_avg_budget:
        new_high_budget_movies.append(movie)
        print(f" '{movie[0]}' cost ${movie[1]:,}: the over average cost: {movie[1] - new_avg_budget:,}")

print(f"There were {len(new_high_budget_movies)} movies with over average budget.")
