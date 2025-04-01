import csv

#############################################################################################
movies = {}
# Reading from CSV
with open('340_folder/movies.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Process each row and convert it into the required dictionary format
    for row in csv_reader:
        title = row['Title'] 
        movies[title] = {
            "year": int(row['Year']), 
            "genre": row['Genre'],
            "director": row['Director'],
            "actors": [actor.strip() for actor in row['Actors'].split(',')]  # Split actors and strip any extra spaces
        }

#############################################################################################

def edit_movie_obj(movies: dict, selection: str) -> None:
    if selection == "1":
        print("To add a new movie simply fill out the prompt below.")
    elif selection == "2":
        print("To edit an existing movie simply fill out the prompts below. Please make sure the name matches and existing movie.")
        print(f"Here are the current movies we have to choose from: {movies}")

    categories = ["name", "year", "genre", "director"]
    movie = []
    actors = []
    for category in categories:
        movie.append(input(f"Enter the {category}: "))
    for _ in range(3):
        actors.append(input("Enter in an actor from your film: "))

    movies.update(
        {movie[0] : {
            "year": movie[1],
            "genre" : movie[2],
            "director" : movie[3],
            "actors" : actors
    }})

#############################################################################################

def search_by_anything(movies: dict) -> None:
    value_to_find = input("Enter the value you wish to find: ")
    if value_to_find in movies:
        print(movies[value_to_find])
    else:
        for title, details in movies.items():
            if value_to_find in details["genre"] or str(details["year"]) == value_to_find or details["director"] == value_to_find or value_to_find in details["actors"]:
                print(movies[title])
    
#############################################################################################

response = input("""
--------Please make a selection--------
                 1) Add a new movie
                 2) Edit a movie
                 3) Delete a movie
                 4) View all movies
                 5) Search movies
                 0) EXIT
""")

while response is not "0":
    match response : 
        case "1" : 
            edit_movie_obj(movies, response)
        case "2" :
            edit_movie_obj(movies, response)
        case "3" : 
            key_to_del = input("Enter the movie you want to delete: ")
            del movies[key_to_del]
        case "4" :
            print("Here is our current selection of movies: ")
            for movie, info in movies.items():
                print(f"{movie}:------------------------------ \n Year -> {info["year"]} \n Genre -> {info["genre"]} \n Director -> {info["director"]} \n Actors -> {info["actors"]}")
        case "5" :
            search_by_anything(movies)
        case _ : 
            print("Invalid Response")
    response = input("""
--------Please make a selection--------
                 1) Add a new movie
                 2) Edit a movie
                 3) Delete a movie
                 4) View all movies
                 5) Search movies
                 0) EXIT
""")

#############################################################################################

# Reading and Writing to CSV
# Updates to the original set of data will save after the changes have been made after the user exits the program ( while loop )
data_in_rows_format = [] # init the empty list that will contain objects for each row.
for title, details in movies.items():
    data_set = {
        "Title" : title,
        "Year" : details["year"],
        "Genre" : details["genre"],
        "Director" : details["director"],
        "Actors": ", ".join(details["actors"])
    }
    data_in_rows_format.append(data_set)

header_for_csv = ["Title", "Year", "Genre", "Director", "Actors"]

# Writing to CSV

with open('340_folder/movies.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header_for_csv)

    writer.writeheader()

    writer.writerows(data_in_rows_format)
