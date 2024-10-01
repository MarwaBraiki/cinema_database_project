Cinema Database Project
Objective

The goal of this project is to apply MongoDB and Python concepts learned in class to manage and manipulate a movie dataset.
Project Description

We are working with a movie dataset and using Python and MongoDB to build a system that allows us to store, query, and manipulate movie-related data. The project is structured into several steps:
Step 1: Import Data

    We create a MongoDB database called cinema and a collection named movies.
    A schema validator is used to ensure data integrity.
    Using Python and the pymongo library, we import movie data from a .csv file into the movies collection.

Step 2: Declare Classes

    Director Class: This class ensures that every director added to the database is validated and meets the necessary data integrity rules.
    Movie Class: Similarly, this class ensures that each movie added to the database is validated and structured properly.

Step 3: Create the Director Collection

Using pymongo, we will implement the following features:

    Store a list of directors and their corresponding movies in a new collection.
    Implement a method to list all movies by a given director.
    Implement a method to calculate the average rating of all movies by a specific director.
    Implement a method to allow users to add new movies interactively.

Step 4: Aggregation Queries

We will create specific aggregation queries to perform the following:

    List the top 5 highest-rated directors.
    List the 5 directors whose movies have the longest average runtime.
    List the 5 directors with the most movies.
    List the top 15 most frequent actors, including the number of movies they have appeared in and the titles of these movies.

Bonus Features

    Prevent movie duplication in the database.
    Create a shared class for Director and Movie to manage the _id property and implement a generic get_by_id method.
    Externalize the database connection using a singleton pattern.

```bash
cinema_project/
│
├── main.py                          # Le fichier principal où tu exécutes le script
│
├── utils/                           # Utilitaires pour le projet
│   ├── __init__.py
│   ├── csv_loader.py                # Le fichier qui chargera les données CSV
│   ├── mongo_utils.py               # Des fonctions utilitaires pour MongoDB
│   └── config.py                    # Configurations et constantes
│
├── models/                          # Modèles pour les entités
│   ├── __init__.py
│   ├── director.py                  # Modèle pour les réalisateurs
│   └── movie.py                     # Modèle pour les films
│
├── aggregation/                     # Fichiers d'agrégation
│   ├── __init__.py
│   └── movie_aggregation.py         # Agrégations liées aux films
│
└── data/                            # Dossier contenant les données
    └── movies.csv                  # Fichier CSV contenant les données des films
```

# MongoDB Aggregation Class for Movie Dataset

## Overview
This class is part of a larger project and focuses on MongoDB aggregation for analyzing a movie dataset. It provides methods to fetch insights such as the top-rated directors, directors with the longest average movie duration, and the top 15 actors with the most films. The class is designed to interact with MongoDB and perform complex aggregation queries.

## Features
- **Top 5 Rated Directors**: Aggregates and retrieves directors based on the highest average movie ratings.
- **Directors with Longest Average Movie Duration**: Finds directors whose movies have the longest average runtime.
- **Directors with Most Movies**: Lists directors who have directed the most films in the dataset.
- **Top 15 Actors**: Displays the top 15 actors, ranked by the number of films they've appeared in, with a numbered list of their movies.

## Class Details

### Aggregation Methods
- `top_rated_directors(db)`: Retrieves the top 5 directors based on their average movie ratings.
- `longest_average_duration_directors(db)`: Finds directors with the longest average movie runtime.
- `most_movies_directors(db)`: Fetches directors who have directed the most movies.
- `top_15_actors(db)`: Lists the top 15 actors based on the number of movies they appear in and displays a numbered list of the movies.

### Example Output
Top 5 Rated Directors: Christopher Nolan with average rating: 8.7

Directors with Longest Average Movie Duration: Quentin Tarantino with average duration: 142.6 minutes

Directors with Most Movies: Martin Scorsese with number of movies: 20

Top 15 Actors: Nicolas Cage with 34 films:

    Movie 1
    Movie 2 ...