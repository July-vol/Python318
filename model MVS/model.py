import pickle
import os.path


class Movies:
    def __init__(self, title, genre, regisseur, year_of_issue, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.regisseur = regisseur
        self.year_of_issue = year_of_issue
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.regisseur})"


class MoviesModel:
    def __init__(self):
        self.mov_name = "mov.txt"
        self.movies = self.load_data()

    def add_movies(self, dict_movies):
        movies = Movies(*dict_movies.values())
        self.movies[movies.title] = movies

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movies(self, user_title):
        movies = self.movies[user_title]
        dict_movies = {
            "название фильма": movies.title,
            "жанр": movies.genre,
            "режиссер": movies.regisseur,
            "год выпуска": movies.year_of_issue,
            "длительность": movies.duration,
            "студия": movies.studio,
            "актеры": movies.actors
        }
        return dict_movies

    def remove_movies(self, user_title):
        return self.movies.pop(user_title)

    def save_data(self):
        with open(self.mov_name, "wb") as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.mov_name):
            with open(self.mov_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
