from View import UserUnterface
from model import MoviesModel


class Controller:
    def __init__(self):
        self.movies_model = MoviesModel()
        self.user_interface = UserUnterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            movies = self.user_interface.add_user_movies()
            self.movies_model.add_movies(movies)
        elif answer == "2":
            movies = self.movies_model.get_all_movies()
            self.user_interface.show_all_movies(movies)
        elif answer == "3":
            movies_title = self.user_interface.get_user_movies()
            try:
                movies = self.movies_model.get_single_movies(movies_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movies_title)
            else:
                self.user_interface.show_single_movies(movies)
        elif answer == "4":
            movies_title = self.user_interface.get_user_movies()
            try:
                title = self.movies_model.remove_movies(movies_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(movies_title)
            else:
                self.user_interface.remove_single_movies(title)
        elif answer == 'q':
            self.movies_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
