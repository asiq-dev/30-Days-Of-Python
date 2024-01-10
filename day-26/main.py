# The namedtuple function

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