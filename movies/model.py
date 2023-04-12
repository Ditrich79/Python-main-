import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class MovieModel:
    def __init__(self):
        self.database_name = 'database.txt'
        self.movies = self.load_database()

    def add_movie(self, dict_movies):
        movie = Movie(*dict_movies.values())
        self.movies[movie.title] = movie

    def view_all_movies(self):
        return self.movies.values()

    def get_selected_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movies = {
            "название": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actors
        }
        return dict_movies

    def delete_movie(self, user_title):
        return self.movies.pop(user_title)

    def load_database(self):
        if os.path.exists(self.database_name):
            with open(self.database_name, 'rb') as file:
                return pickle.load(file)
        else:
            return dict()

    def save_database(self):
        with open(self.database_name, 'wb') as file:
            pickle.dump(self.movies, file)
