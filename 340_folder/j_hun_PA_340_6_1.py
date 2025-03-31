movies = {
    "The Shawshank Redemption": {
        "year": 1994,
        "genre": "Drama",
        "director": "Frank Darabont",
        "actors": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]
    },
    "The Godfather": {
        "year": 1972,
        "genre": "Crime, Drama",
        "director": "Francis Ford Coppola",
        "actors": ["Marlon Brando", "Al Pacino", "James Caan"]
    },
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action, Crime, Drama",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Forrest Gump": {
        "year": 1994,
        "genre": "Drama, Romance",
        "director": "Robert Zemeckis",
        "actors": ["Tom Hanks", "Robin Wright", "Gary Sinise"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Action, Adventure, Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Fight Club": {
        "year": 1999,
        "genre": "Drama",
        "director": "David Fincher",
        "actors": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]
    },
    "The Matrix": {
        "year": 1999,
        "genre": "Action, Sci-Fi",
        "director": "The Wachowskis",
        "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime, Drama",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
    },
    "Gladiator": {
        "year": 2000,
        "genre": "Action, Adventure, Drama",
        "director": "Ridley Scott",
        "actors": ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]
    },
    "The Social Network": {
        "year": 2010,
        "genre": "Biography, Drama",
        "director": "David Fincher",
        "actors": ["Jesse Eisenberg", "Andrew Garfield", "Justin Timberlake"]
    }
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
    for i in range(3):
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
