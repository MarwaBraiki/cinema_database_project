from typing import Optional
from models.director import Director


class Movie:
    def __init__(self, title: str, year: int, summary: Optional[str] = None,
                 short_summary: Optional[str] = None, imdb_id: str = "",
                 runtime: Optional[int] = None, rating: Optional[float] = None,
                 youtube_trailer: Optional[str] = None, movie_poster: Optional[str] = None,
                 director: Optional[Director] = None, writers: Optional[str] = None,
                 cast: Optional[str] = None):
        """Initializes an instance of Movie with relevant details."""
        self.title = title
        self.year = year
        self.summary = summary
        self.short_summary = short_summary
        self.imdb_id = imdb_id
        self.runtime = runtime
        self.rating = rating
        self.youtube_trailer = youtube_trailer
        self.movie_poster = movie_poster
        self.director = director
        self.writers = writers
        self.cast = cast

        # Validate the data after initialization
        if not self.is_valid():
            raise ValueError("Movie data is not valid.")

    def __str__(self) -> str:
        """String representation of the Movie object."""
        director_name = self.director.name if self.director else "Unknown"
        return (f"{self.title} ({self.year}) - Rating: {self.rating if self.rating is not None else 'N/A'}, "
                f"Directed by: {director_name}, "
                f"Runtime: {self.runtime if self.runtime is not None else 'N/A'}, "
                f"Summary: {self.short_summary if self.short_summary is not None else 'N/A'}")

    def is_valid(self) -> bool:
        """Checks if the movie data is valid."""
        # Validate title
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Invalid title: Must be a non-empty string.")

        # Validate year
        if not isinstance(self.year, int) or self.year < 1888:  # 1888 is the year of the first film
            raise ValueError("Invalid year: Must be an integer greater than or equal to 1888.")

        # Validate summary
        if self.summary is not None and not isinstance(self.summary, str):
            raise ValueError("Invalid summary: Must be a string.")

        # Validate short summary
        if self.short_summary is not None and not isinstance(self.short_summary, str):
            raise ValueError("Invalid short summary: Must be a string.")

        # Validate IMDb ID
        if not isinstance(self.imdb_id, str):
            raise ValueError("Invalid IMDb ID: Must be a string.")

        # Validate runtime
        if self.runtime is not None and (not isinstance(self.runtime, int) or self.runtime < 0):
            raise ValueError("Invalid runtime: Must be a non-negative integer.")

        # Validate rating
        if self.rating is not None and not (isinstance(self.rating, (float, int)) and 0 <= self.rating <= 10):
            raise ValueError("Invalid rating: Must be a number between 0 and 10.")

        # Validate YouTube trailer
        if self.youtube_trailer is not None and not isinstance(self.youtube_trailer, str):
            raise ValueError("Invalid YouTube Trailer: Must be a string.")

        # Validate movie poster
        if self.movie_poster is not None and not isinstance(self.movie_poster, str):
            raise ValueError("Invalid movie poster: Must be a string.")

        # Validate writers
        if self.writers is not None and not isinstance(self.writers, str):
            raise ValueError("Invalid writers: Must be a string.")

        # Validate cast
        if self.cast is not None and not isinstance(self.cast, str):
            raise ValueError("Invalid cast: Must be a string.")

        # Validate director
        if self.director is not None and not isinstance(self.director, Director):
            raise ValueError("Invalid director: Must be an instance of Director.")

        return True
