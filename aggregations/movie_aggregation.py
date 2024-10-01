from utils.mongo_connection import connect_mongo

# Connect to MongoDB
db = connect_mongo()

# Check the number of movies in the collection
movie_count = db.movies.count_documents({})
print(f"Number of movies in the collection: {movie_count}")

# Function to get the top-rated directors
def top_rated_directors(db):
    pipeline_top_rated_directors = [
        {
            "$match": {"rating": {"$exists": True, "$ne": None}}  # Ensure the rating field exists and is not null
        },
        {
            "$group": {
                "_id": {"$toLower": {"$ifNull": ["$director", "Unknown"]}},  # Normalize director name (lowercase)
                "average_rating": {"$avg": "$rating"},  # Calculate the average rating per director
            }
        },
        {
            "$sort": {"average_rating": -1},  # Sort directors by average rating in descending order
        },
        {
            "$limit": 5  # Limit to 5 directors
        }
    ]
    # Execute aggregation for top-rated directors
    return list(db.movies.aggregate(pipeline_top_rated_directors))

# Function to get directors with the highest average runtime
def longest_average_duration_directors(db):
    pipeline_longest_average_duration_directors = [
        {
            "$match": {"runtime": {"$exists": True, "$ne": None}}  # Ensure the runtime field exists and is not null
        },
        {
            "$group": {
                "_id": {"$toLower": {"$ifNull": ["$director", "Unknown"]}},  # Normalize director name (lowercase)
                "average_runtime": {"$avg": "$runtime"},  # Calculate the average runtime per director
            }
        },
        {
            "$sort": {"average_runtime": -1},  # Sort directors by average runtime in descending order
        },
        {
            "$limit": 5  # Limit to 5 directors
        }
    ]
    # Execute aggregation for longest average runtime directors
    return list(db.movies.aggregate(pipeline_longest_average_duration_directors))

# Function to get directors with the most films
def most_movies_directors(db):
    pipeline_most_movies_directors = [
        {
            "$group": {
                "_id": {"$toLower": {"$ifNull": ["$director", "Unknown"]}},  # Normalize director name (lowercase)
                "film_count": {"$sum": 1},  # Count the number of films per director
            }
        },
        {
            "$sort": {"film_count": -1},  # Sort directors by film count in descending order
        },
        {
            "$limit": 5  # Limit to 5 directors
        }
    ]
    # Execute aggregation for most films directors
    return list(db.movies.aggregate(pipeline_most_movies_directors))

# Function to get the most featured actors with their films
def top_actors(db):
    pipeline_top_actors = [
        {
            "$unwind": "$cast"  # Unwind the cast array to separate each actor
        },
        {
            "$match": {"cast": {"$exists": True, "$ne": None}}  # Ensure the cast field exists and is not null
        },
        {
            "$project": {
                "cast": {
                    "$split": ["$cast", "|"]  # Split actor names if they are separated by a '|'
                },
                "title": 1
            }
        },
        {
            "$unwind": "$cast"  # Unwind again if actors are combined in the string
        },
        {
            "$group": {
                "_id": "$cast",  # Group by actor
                "film_count": {"$sum": 1},  # Count the number of films per actor
                "films": {"$addToSet": "$title"}  # Add movie titles to the list without duplicates
            }
        },
        {
            "$sort": {"film_count": -1},  # Sort actors by number of films in descending order
        },
        {
            "$limit": 15  # Limit to 15 actors
        }
    ]
    # Execute the aggregation for the most featured actors
    return list(db.movies.aggregate(pipeline_top_actors))

# Get and print results from the functions
top_rated_directors_list = top_rated_directors(db)
print("\nTop 5 highest-rated directors:")
if not top_rated_directors_list:
    print("No results found for the highest-rated directors.")
else:
    for director in top_rated_directors_list:
        print(f"Director: {director['_id'].title()}, Average Rating: {director['average_rating']:.2f}")

longest_average_duration_directors_list = longest_average_duration_directors(db)
print("\nTop 5 directors with the longest average runtime:")
if not longest_average_duration_directors_list:
    print("No results found for directors with the longest average runtime.")
else:
    for director in longest_average_duration_directors_list:
        print(f"Director: {director['_id'].title()}, Average Runtime: {director['average_runtime']:.2f} minutes")

most_movies_directors_list = most_movies_directors(db)
print("\nTop 5 directors with the most films:")
if not most_movies_directors_list:
    print("No results found for directors with the most films.")
else:
    for director in most_movies_directors_list:
        print(f"Director: {director['_id'].title()}, Number of Films: {director['film_count']}")

top_actors_list = top_actors(db)
print("\nTop 15 most featured actors with their films:")
if not top_actors_list:
    print("No results found for the most featured actors.")
else:
    for actor in top_actors_list:
        print(f"Actor: {actor['_id']}, Number of Films: {actor['film_count']}")
        for i, film in enumerate(actor['films'], start=1):
            print(f"   {i}. {film}")  # List each movie with a number

