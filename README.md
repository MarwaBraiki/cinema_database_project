## Project Overview

The Movie Database Project utilizes MongoDB and Python concepts to manage and manipulate a dataset of movies. It involves:

- Importing movie data from a CSV file.
- Managing directors and films using Python classes.
- Executing MongoDB aggregation queries to extract valuable information from the dataset.

### Key Features

- **Data Import**: Import movie data from a CSV file into MongoDB using Python's built-in CSV module.
- **Data Management**: Manage directors and films with Python classes to ensure data integrity.
- **Aggregation Queries**: Execute queries to retrieve top-rated directors, directors with the most films, and more.
- **Duplication Prevention**: Prevent movie duplication and externalize the database connection for better scalability.

## Prerequisites

To run this project, ensure you have the following installed on your machine:

- Python 
- MongoDB
- `pymongo` library

Make sure MongoDB is running locally or remotely and is accessible from your Python script.

## Project Structure

```bash
cinema_project/
│
├── .venv/                           # Virtual environment for project dependencies
│
├── main.py                          # Main file where the script is executed
│
├── utils/                           # Utilities for the project
│   ├── __init__.py
│   ├── csv_loader.py                # Loads CSV data into MongoDB using the CSV module
│   ├── mongo_connection.py          # MongoDB connection functions
│   └── config.py                    # Configuration and constants
│
├── models/                          # Models for entities
│   ├── __init__.py
│   ├── director.py                  # Model for the Director entity
│   └── movie.py                     # Model for the Movie entity
│
├── aggregations/                    # Aggregation queries
│   ├── __init__.py
│   └── movie_aggregation.py         # Aggregation queries related to movies
│
├── data/                            # Data folder
│   └── movies.csv                   # CSV file containing the movie dataset
│
├── requirements.txt                 # File for Python dependencies                  
└── .gitignore                       # Git ignore file
```

## .gitignore File

Include a .gitignore file to prevent committing sensitive information and unnecessary files. Example:

```bash
# Python
*.pyc
__pycache__/
.venv/

# PyCharm
.idea/
```

## Project Installation
1. Clone the project:

```bash
git clone <repository_url>
cd <repo_name>
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run the Project
Step 1: Start MongoDB

Ensure that MongoDB is running on your local machine or a remote server. Start MongoDB with the following command:

```bashbash
mongod
```

Step 2: Run the Main Script

Execute the main.py script to load the data and perform operations on the database:

```bash
python main.py
```

The script will:

    Connect to MongoDB, creating the cinema database and movie collection.
    Load movie data from the movies.csv file into MongoDB using Python's built-in CSV module.
    Display aggregation results, such as top-rated directors, actors, and more.

Aggregation Queries

The project supports several aggregation queries that can be executed directly from the main.py script.
Available Aggregations

    Top 5 Rated Directors: Displays directors with the highest average movie ratings.
    Top 5 Directors with Longest Average Movie Duration: Lists directors whose films have the longest average duration.
    Top 5 Directors with Most Films: Shows directors who have made the most movies.
    Top 15 Most Frequent Actors: Lists actors who have appeared in the most films along with their respective movie titles.

Executing Aggregations

Once the main.py script is executed, the aggregation queries will run automatically, and their results will be displayed in the terminal.

Example output for top 5 rated directors:

Top 5 Rated Directors:
1. Alper Caglar, Average Rating: 9.50
2. Yann Arthus-Bertrand, Average Rating: 8.70
3. ...

Code Structure
main.py

This file orchestrates the project by:

    Connecting to MongoDB using the connect_mongo function from utils/mongo_connection.py.
    Loading movie data from data/movies.csv using Python's built-in CSV module.
    Importing aggregation functions (e.g., top_rated_directors) from aggregations/movie_aggregation.py and executing them to retrieve information.

Example Usage

To load movie data and execute aggregation queries:

    Ensure that MongoDB is running.
    Run the main.py script:

```bash
python main.py
```

The output will include:

    Information about the number of movies and directors inserted.
    Results of aggregation queries (e.g., top-rated directors, actors, etc.).


Conclusion

This project demonstrates the use of MongoDB and Python to manage a movie database, ensuring data integrity and extracting valuable information through aggregation queries. It can be easily extended to include more advanced features such as movie recommendations or user ratings.