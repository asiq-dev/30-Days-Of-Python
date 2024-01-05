#Iterator examples

from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

for word in a_words:
    print(word)

# printed second time to see values are consumed or not
for word in a_words:
    print(word)


# Changes to mutable collections can affect an iterator
from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

words.append("apple")

for word in a_words:
    print(word)


#Manual iteration with the next function
from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

first_word = next(a_words)
second_word = next(a_words)
print(first_word)
print(second_word)


# used an approach like the one below to get the file data and extract the headers.

irises = []

with open("iris.csv", "r") as iris_file:
    headers = next(iris_file).strip().split(",")

    for row in iris_file:
        iris = row.strip().split(",")
        iris_dict = dict(zip(headers, iris))

        irises.append(iris_dict)
print(irises)