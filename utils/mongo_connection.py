# mongo_connection.py

from pymongo import MongoClient, errors  # Import the necessary classes from pymongo

def connect_mongo(uri='mongodb://localhost:27017/', db_name='cinema_benyahia'):
    """
    Connects to the MongoDB database and returns the database object.

    Args:
        uri (str): The connection string to MongoDB.
        db_name (str): The name of the database to connect to.

    Returns:
        db (MongoClient.database): The connected MongoDB database object, or None if the connection fails.
    """
    try:
        print("Connecting to MongoDB...")
        client = MongoClient(uri)  # Create a MongoDB client
        db = client[db_name]  # Access the specified database
        print(f"Successfully connected to MongoDB database: {db_name}")

        # Create collections if they do not exist
        create_movies_collection(db)
        create_directors_collection(db)

        return db  # Return the database object
    except errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")  # Print error message if connection fails
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Capture unexpected errors
        return None

def create_movies_collection(db):
    """Creates the 'movies' collection if it doesn't already exist."""
    if 'movies' not in db.list_collection_names():
        db.create_collection('movies')
        print("Successfully created collection: movies")
    else:
        print("Collection 'movies' already exists.")

def create_directors_collection(db):
    """Creates the 'directors' collection if it doesn't already exist."""
    if 'directors' not in db.list_collection_names():
        db.create_collection('directors')
        print("Successfully created collection: directors")
    else:
        print("Collection 'directors' already exists.")

if __name__ == "__main__":
    db = connect_mongo()
    if db is not None:  # Check if the db object is valid
        print("Connected to database successfully!")
    else:
        print("Failed to connect to the database.")
