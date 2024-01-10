# The namedtuple function


from collections import namedtuple
Book = namedtuple("Book", ["title", "author", "year"])
book = Book(title="The Colour of Magic", author="Terry Pratchett", year=1983)
print(f"{book.title} ({book.year}), by {book.author}")



# project of iris file with namedtuple


from collections import namedtuple
Iris = namedtuple("Iris",["sepal_length", "sepal_width", "petal_lengtth", "petal_width", "species"])

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

    irises = []

    for row in iris_data[1:]:
        iris = Iris._make(row.strip().split(","))
        # iris = Iris(*row.strip().split(","))
        irises.append(iris)
    
print(irises)


# The partial function

from functools import partial

def exponentiate(base, exponent):
    return base ** exponent

square = partial(exponentiate, exponent = 2)
qube = partial(exponentiate, exponent = 3)
print(qube(5))


# The defaultdict type


from collections import namedtuple, defaultdict

User = namedtuple("User", 'name, username, location')
users = defaultdict(
    lambda: "Couldn't find a user matching that user id.",
    {
        "001" : User("phil", "pbest", "hungary"),
        "002" : User("jose", "jslvtr", "uk")
    }
)

user_id = input("Enter a user id: ")
print(users[user_id])