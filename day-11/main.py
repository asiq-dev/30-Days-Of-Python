# Defining a set

vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}




# for empty set
set()

# Modifying sets

# Adding items to a set
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.add("potato")
print(vegetables)


# update method
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin"])
print(vegetables)


# Deleting items from a set
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.remove("lettuce")
# vegetables.discard("lettuce")   #another technique for remove
# vegetables.pop()
print(vegetables)
# vegetables.clear()



# Set operations

# Union -> We can find the union of two sets with the union method.
letters = {"a", "b", "c"}
numbers = {1, 2, 3}
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)


# Intersection-> When we find the intersection of two sets, we get a new set containing the elements common to both sets.
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}
mod_6 = mod_2.intersection(mod_3)
print(mod_6)


# Difference
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2)) 
print(bundle_2.difference(bundle_1))


# Symmetric difference
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.symmetric_difference(bundle_2))



# Set operations with other collections
letters = {"a", "b", "c"}
numbers = [1, 2, 3]
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)




# Checking if items are in collections

numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # True
print(7 in numbers)  # False

print("j" in "Python")  # False
print("n" in "Python")  # True



student = {
    "name": "Eric Cartman",
    "age": 10,
    "school": "South Park Elementary"
}
print(10 in student.values())  # True