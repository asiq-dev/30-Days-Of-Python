#1 The data contains the character name, the voice actor or actress who plays them, 
#and the species of the character.
#Write a for loop that uses destructuring so that you can print each tuple in the following format:
#change the species information to lowercase when you print it.

# main_characters = [
#     ("BoJack Horseman", "Will Arnett", "Horse"),
#     ("Princess Carolyn", "Amy Sedaris", "Cat"),
#     ("Diane Nguyen", "Alison Brie", "Human"),
#     ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
#     ("Todd Chavez", "Aaron Paul", "Human")
# ]

# for character,actor,species in main_characters:
#     print(f"{character} is a {species.lower()} voiced by {actor}.")



#2 Unpack the following tuple into 4 variables:

# name,id,(major,minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

# print(f"Name = {name},Id = {id}, Major = {major}, Minor = {minor}")




#3 Investigate what happens when you try to zip two iterables of different lengths.

name = ['munna','ashik','islam']
id = (18,19,32,30,35)

info = zip(name,id)
print(list(info))