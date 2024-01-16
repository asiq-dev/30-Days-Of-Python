
# using any type.
from typing import Any

name: str = "Munna"
age: int = 26
height: Any = 1.67
loves_python: bool = True



# using union type
from typing import Union

name: str = "Munna"
age: int = 26
height: Union[int, float] = 1.67
loves_python: bool = True


# Annotating collections
from typing import Union
names: list[str] =  ["Rick", "Morty", "Summer", "Beth", "Jerry"]
random_values: list[Union[str, int]] =  ["x", 13, "camel", 0]

#tuple
movie: tuple[str, str, int] = ("Toy Story 3", "Lee Unkrich", 2010)



#Creating type aliases

Movie = tuple[str, str, int]

movies: list[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]



# Annotating functions

Movie = tuple[str, str, int]

def show_movies(movies: list[Movie]):
    for title, director, year in movies:
        print(f"{title} ({year}), by {director}")

movies: list[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)


# Annotating return values

from typing import Union

Movie = tuple[str, str, int]

def find_movie(search_term: str, movies: list[Movie]) -> Union[Movie,None]:
    for title, director, year in movies:
        if title == search_term:
            return (title, director, year)
    return None

def show_movies(movies: list[Movie]):
    for movie in movies:
        print_movie(movie)

def print_movie(movie: Movie):
    title, director, year = movie
    print(f"{title} ({year}), by {director}")

movies: list[Movie] = [
    ("Finding Nemo", "Andrew Stanton", 2005),
    ("Inside Out", "Pete Docter", 2015),
    ("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)

search_result: Union[Movie, None] = find_movie("Finding Nemo", movies)

if search_result:
    print_movie(search_result)
else:
    print("Couldn't find movie.")


# Do you need from typing import List?

def double_values(items: list[int]) -> list[int]:
    return [x * 2 for x in items]