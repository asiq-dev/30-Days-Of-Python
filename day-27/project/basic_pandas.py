import pandas as pd

movies = {
    "title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
    "director": ("Christopher Nolan", "Gore Verbinski"),
    "year": (2010, 2003)
}

df = pd.DataFrame(movies)
print(df)

df = pd.DataFrame(movies)
df.rename(columns={"year": "release_year"}, inplace=True)
print(df)

df.drop(columns="release_year",  inplace=True)
print(df)

# Filtering by values
latest_movies = df.query("release_year == 2020")
print(latest_movies)

nolan_movies = df.query("director == 'Christopher Nolan'")
print(nolan_movies)