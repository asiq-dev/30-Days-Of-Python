#lists
names = ["John", "Alice", "Sarah", 24, 25, 30]
print(names)

#print by specificly
print(names[0])
print(names[-1])

#adding items to a list
names.append("Mike") #append add only one argumet
print(names)

names = names + ["Rock", 23] # + add only multiple argumet
print(names)

new_names = ["Jack", 26]
names.extend(new_names) #add new list to the existing list
print(names)

#insert item in the middle
numbers = [1, 2, 4, 5]
numbers.insert(2, 3) #2 means index, 3 means value
print(numbers)



#Removing items from the lists
names.remove("Mike") #delete only the matching value
print(names)

del names[2]  #delete given index value
print(names)
deleted_value = names.pop(2) #delete given index value but it can store delted value
print(names)
print(deleted_value)

#clear lists full value
names.clear()
print("the list value are:" + str(names))



#Tuples
movies = "memento",2000
print(movies)
movies = [("memento", 2000), ("requim for a dream", 2000)]
print(movies)
print(movies[0][0], movies[0][1])