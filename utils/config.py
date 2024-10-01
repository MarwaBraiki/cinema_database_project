# utils/config.py

# Configuration MongoDB
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = 'cinema_benyahia'

# Noms des colonnes pour le fichier CSV dans l'ordre spécifié
CSV_COLUMNS = [
    "Title",              # Titre
    "Year",               # Année
    "Summary",            # Résumé
    "Short Summary",      # Court résumé
    "IMDB ID",           # ID IMDB
    "Runtime",            # Durée
    "YouTube Trailer",    # Bande-annonce YouTube
    "Rating",             # Note
    "Movie Poster",       # Affiche du film
    "Director",           # Réalisateur
    "Writers",            # Scénaristes
    "Cast"                # Distribution
]
