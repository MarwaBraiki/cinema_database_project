from utils.csv_loader import load_csv_to_mongodb
from utils.mongo_connection import connect_mongo
import os

# Import aggregation functions
from aggregations.movie_aggregation import (
    top_rated_directors,
    longest_average_duration_directors,
    most_movies_directors,
    top_actors,
)

def run():
    """Main function to execute database operations."""
    # Connect to the MongoDB database and create collections if necessary
    db, movie_count, director_count = connect_mongo()

    # Check if the connection was successful
    if db is None:
        print("Failed to connect to MongoDB.")
        return  # Exit the function if connection fails

    # Path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'movies.csv')

    # Load data from the CSV file into MongoDB
    movies_inserted = load_csv_to_mongodb(csv_file_path, db)

    # Count the number of movies and directors in the database
    movie_count += db.movies.count_documents({})  # Update the count with the current number
    director_count = db.directors.count_documents({})

    # Display insertion results
    if movies_inserted > 0:
        print(f"Success: {movie_count} movies and {director_count} directors have been inserted into the database.")
    else:
        print(f"No new records to insert. {movie_count} records already exist in the 'movies' collection.")

    # Call aggregation functions
    print("\nAggregation results:")
    aggregation_functions = [
        top_rated_directors,
        longest_average_duration_directors,
        most_movies_directors,
        top_actors,
    ]

    # Execute each aggregation function
    for aggregation_function in aggregation_functions:
        results = aggregation_function(db)  # These functions already handle the display
