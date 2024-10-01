# utils/movie_utils.py

# Function to add a director to the collection if they do not already exist
def add_director_if_not_exists(db, director_name):
    """Adds a director to the collection if they do not already exist."""
    try:
        # Check if the director already exists
        existing_director = db.directors.find_one({"name": director_name})

        if existing_director is None:
            # If the director does not exist, add them
            director = {
                "name": director_name,
                "movies": []  # Initialize with an empty list of movies
            }
            db.directors.insert_one(director)
            print(f"Added director: {director_name}")
        else:
            print(f"The director '{director_name}' already exists.")
    except Exception as e:
        print(f"Error while adding the director: {e}")


# Function to add a film to the database if it does not already exist
def add_film_if_not_exists(db, film_data):
    """Adds a film to the database if it does not already exist."""
    try:
        existing_film = db.movies.find_one({"imdb_id": film_data["imdb_id"]})

        if existing_film:
            print(f"The film '{film_data['title']}' already exists in the database.")
        else:
            # Add the film data to the movies collection
            db.movies.insert_one(film_data)

            # Update the director's movie list
            db.directors.update_one(
                {"name": film_data["director"]},
                {"$addToSet": {"movies": film_data["title"]}}  # Add film title to the director's movies list
            )

            print(f"The film '{film_data['title']}' has been added to the database.")
    except Exception as e:
        print(f"Error while adding the film: {e}")


# Function to list directors associated with a given film
def list_directors_for_film(db, film_title):
    """Returns the list of directors for a given film."""
    film = db.movies.find_one({"title": film_title})

    if film and "director" in film:
        return film["director"]  # Assuming director is a single value; could change to a list
    else:
        print(f"No director found for the film '{film_title}'.")
        return None  # Return None if no director is found for the film


# Adding new methods to manage films in relation to directors

def add_film_to_director(db, director_name, film_data):
    """Adds a film to a director."""
    try:
        director = db.directors.find_one({"name": director_name})  # Find the director by name
        if director:
            # Update the director's document to add the film
            db.directors.update_one(
                {"_id": director["_id"]},
                {"$addToSet": {"films": film_data}}  # Using $addToSet to avoid duplicates
            )
            print(f"Film '{film_data['title']}' added for director '{director_name}'.")
        else:
            print(f"Director '{director_name}' does not exist.")
    except Exception as e:
        print(f"Error while adding film to director: {e}")

def list_films_for_director(db, director_name):
    """Returns the list of films for a director."""
    try:
        director = db.directors.find_one({"name": director_name})  # Find the director
        if director:
            return director.get('films', [])  # Return the list of films if found
        else:
            print(f"Director '{director_name}' not found.")
            return []
    except Exception as e:
        print(f"Error while listing films for director: {e}")
        return []
