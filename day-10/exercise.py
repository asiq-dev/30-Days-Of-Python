#1 Inside the tuple we have the album name, the artist (in this case, the band), the year of release, 
#and then another tuple containing the track list.
#Convert this outer tuple to a dictionary with four keys.

album = {

    "title" : "The Dark Side of the Moon",
    "artist" : "Pink Floyd",
    "year" : 1973,
    "track" : (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

# print(album)



#2 Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, 
# you should print the name of the key, and then the value alongside it.

# for key,value in album.items():
#     print(f"{key} : {value}")



#3 Delete the track list and year of release from the dictionary you created. Once you've done this, 
# add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon
# was March 1st, 1973.

del album["year"]
del album["track"]
# print(album)
# delete = {'year','title'}
# def to_remove(delete,album):
#     for key in delete:         # delete multiple key
#         if key in album:
#             del album[key]
album['release_date'] = "March 1st, 1973"
# print(album)


# Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. 
# Once you've tried this, repeat the step using the get method to prevent the exception being raised.
print(album.get('track',[]))