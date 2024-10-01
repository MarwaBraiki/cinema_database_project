import os
import csv
from pymongo import errors
from pymongo import MongoClient
from utils.config import CSV_COLUMNS  # Assurez-vous que le fichier config.py contient la définition de CSV_COLUMNS

def load_csv_to_mongodb(csv_file, db):
    """
    Loads movie data from a CSV file into the MongoDB database.

    Args:
        csv_file (str): The path to the CSV file.
        db (MongoClient.database): The MongoDB database object.

    Returns:
        bool: True if the loading was successful, False otherwise.
    """
    if not os.path.exists(csv_file):
        print(f"Error: The file '{csv_file}' does not exist.")
        return False

    records = []
    existing_movies_count = 0
    directors_movies = {}

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                record = {
                    'title': row['Title'],
                    'year': int(row['Year']) if row['Year'] else None,
                    'summary': row['Summary'],
                    'short_summary': row['Short Summary'],
                    'imdb_id': row['IMDB ID'],
                    'runtime': int(row['Runtime']) if row['Runtime'] else None,
                    'youtube_trailer': row['YouTube Trailer'],
                    'rating': float(row['Rating']) if row['Rating'] else None,
                    'movie_poster': row['Movie Poster'],
                    'director': row['Director'],
                    'writers': row['Writers'],
                    'cast': row['Cast']
                }

                if db.movies.find_one({"title": record['title'], "director": record['director']}):
                    existing_movies_count += 1
                else:
                    records.append(record)
                    director = record['director']
                    if director not in directors_movies:
                        directors_movies[director] = []
                    directors_movies[director].append(record['title'])

            except ValueError as ve:
                print(f"Value error while processing row {row}: {ve}")
                continue
            except Exception as e:
                print(f"Error processing row {row}: {e}")
                continue

    if records:
        try:
            result = db.movies.insert_many(records)
            print(f"Inserted {len(result.inserted_ids)} records into the 'movies' collection.")

            for director, movies in directors_movies.items():
                director_entry = db.directors.find_one({"name": director})
                if director_entry:
                    db.directors.update_one(
                        {"_id": director_entry["_id"]},
                        {"$addToSet": {"movies": {"$each": movies}}}
                    )
                else:
                    db.directors.insert_one({"name": director, "movies": movies})
                    print(f"Inserted director: {director} with movies: {movies}")

            return True
        except errors.PyMongoError as e:
            print(f"Error inserting records: {e}")
            return False
    else:
        if existing_movies_count > 0:
            print(f"No new records to insert. {existing_movies_count} records already exist.")
        else:
            print("No valid records to insert.")
        return False


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client['cinema_benyahia']
    csv_file = r'C:\Users\NEW.PC\PycharmProjects\cinema_project\data\movies.csv'

    load_csv_to_mongodb(csv_file, db)
