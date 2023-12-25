#open a different file and read data
# text_file = open("read_example.txt")
# text_file = open(".read_example.txt")
# print(text_file.read())

# text_file.close()




#Opening files in different modes
 
 # read mode 
# read_file = open("read_example.txt", mode = 'r')
# read_file = open("read_example.txt", 'r')
# print(read_file.read())
# read_file.close()

 # write mode
# write_file = open("write_example.txt", 'w')
# write_file.write("hello World! I am in write_example file")
# write_file.close()


 #append mode
# write_file = open("write_example.txt", 'a')
# write_file.write("\nNow you have two lines! You're growing up so fast!")
# write_file.close()


# also files read and write in diifferent way where not need to close function
# with open("read_example.txt", 'r') as read_file:
#     print(read_file.read())

# with open("write_example.txt", 'w') as write_file:
#     write_file.write("Hello i am new")

# with open("write_example.txt", 'a') as write_file:
#     write_file.write("\nhello i am second new")






# working with iris-data 
# with open("iris.csv", 'r') as iris_file:
#     # iris_data = iris_file.read().split("\n")
#     iris_data = iris_file.readlines()  #that readlines is going to preserve this "\n" character, so we're going to need to remember to trim it off
#     print(iris_data)


# irises = []

# for row in iris_data[1:]:
#     sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

#     irises.append({
#         "sepal_length":sepal_length,
#         "sepal_width": sepal_width,
#         "petal_length": petal_length,
#         "petal_width": petal_width,
#         "species": species
#     })

# print(irises)


# Using the dict function -another way to enter value in dictionary

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers,iris))

    irises.append(iris_dict)

print(irises)


