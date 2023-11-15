#Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [("3 idiots", "Rajkumar Hirani", 2009, "$4,000,000")]

title = input("Enter the title of a movie: ")
director = input("Enter the director name: ")
release_year = int(input("Enter the realease year: "))
budget = input("Enter the budget of the movie: ")

#Use an f-string to print the movie name and release year by accessing your new movie tuple.
new_movie =title, director, release_year, budget
print( f"{new_movie[0]} ({(new_movie[2])})" )

#Add the new movie tuple to the movies collection using append.
movies.append(new_movie)
print(movies)

#Remove the first movie from movies. Use any method you like.
movies.pop(0)
print(movies)