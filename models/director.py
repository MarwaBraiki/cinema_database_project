from utils.mongo_connection import connect_mongo
from utils.movie_utils import add_director_if_not_exists, add_film_if_not_exists

class Director:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def add_director(self):
        """Adds the director to the database if they do not already exist."""
        add_director_if_not_exists(self.db, self.name)

    def add_film(self, film_data):
        """Adds a film to the director."""
        add_film_if_not_exists(self.db, film_data)

    def remove_film(self, film_title):
        """Removes a film from the director's list and the database."""
        result = self.db.movies.delete_one({"title": film_title, "director": self.name})
        if result.deleted_count > 0:
            self.db.directors.update_one(
                {"name": self.name},
                {"$pull": {"movies": film_title}}  # Remove the film title from the director's movies list
            )
            print(f"The film '{film_title}' has been removed from the database.")
        else:
            print(f"The film '{film_title}' was not found.")

    def list_films(self):
        """Returns the list of films associated with this director."""
        return list(self.db.movies.find({"director": self.name}))  # Returns a list of films

    def average_rating(self):
        """Calculates the average rating of the director's films."""
        films = self.list_films()
        if films:
            total_rating = sum(film['rating'] for film in films if 'rating' in film)
            return total_rating / len(films) if total_rating > 0 else 0
        return 0


if __name__ == "__main__":
    # Example of using the Director class
    db = connect_mongo()

    # Create a director
    director = Director("Antonio Morabito", db)
    director.add_director()

    # Add a film for this director
    film_data = {
        "title": "Film Example",
        "year": 2023,
        "summary": "This is a summary of the film.",
        "short_summary": "Short summary.",
        "imdb_id": "tt1234567",
        "runtime": 120,
        "youtube_trailer": "https://youtube.com/example",
        "rating": 8.5,
        "movie_poster": "https://example.com/poster.jpg",
        "director": "Antonio Morabito",  # Ensure the director's name is included
        "writers": "Writer Name",
        "cast": "Actor 1, Actor 2"
    }
    director.add_film(film_data)

    # List films directed by the director
    films = director.list_films()
    film_titles = [film["title"] for film in films]
    print(f"Films directed by {director.name}: {film_titles}")

    # Calculate the average rating of the films
    average_rating = director.average_rating()
    print(f"Average rating of films directed by {director.name}: {average_rating}")

    # Remove a film
    director.remove_film("Film Example")  # Replace with the title of the film you want to remove

    # List films again to verify removal
    films_after_removal = director.list_films()
    film_titles_after_removal = [film["title"] for film in films_after_removal]
    print(f"Films directed by {director.name} after removal: {film_titles_after_removal}")
