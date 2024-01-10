# 1) Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user to provide information for each of these fields and create an instance of the Movie tuple you defined.

from collections import namedtuple

Movie = namedtuple("Movie",'title, director, year, budget')

title = input("Enter Movie Title: ").title()
director = input("Enter Movie Director name: ")
year = int(input("Enter Release Year: "))
budget = input("Enter Movie budget: ")

movie = Movie(title, director, year, budget)
print(f"{movie.title} ({movie.year}), by {movie.director} and budget is: {movie.budget}")