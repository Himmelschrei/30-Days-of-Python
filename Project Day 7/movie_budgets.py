movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

avbudget = 0.0

for movie in movies:
    avbudget += movie[1]

avbudget /= len(movies)

expmovies = 0

for movie in movies:
    if movie[1] > avbudget:
        print(f"{movie[0]} cost ${movie[1]} and was ${movie[1] - avbudget} more expensive than the average.")
        expmovies += 1

print(f"A total of {expmovies} movies were more expensive than the average.")