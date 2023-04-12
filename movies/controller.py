from view import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.movie_model = MovieModel()
        self.user_interface = UserInterface()

    def run_program(self):
        answer_user = None
        while answer_user != 'q':
            answer_user = self.user_interface.wait_for_user_answer()
            self.check_user_answer(answer_user)

    def check_user_answer(self, answer_user):
        if answer_user == '1':
            movie = self.user_interface.add_user_movie()
            self.movie_model.add_movie(movie)
        elif answer_user == '2':
            movies = self.movie_model.view_all_movies()
            self.user_interface.show_all_movies(movies)
        elif answer_user == '3':
            movie_title = self.user_interface.get_user_movie()
            try:
                movie = self.movie_model.get_selected_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title(movie_title)
            else:
                self.user_interface.show_selected_movie(movie)
        elif answer_user == '4':
            movie_title = self.user_interface.get_user_movie()
            try:
                title = self.movie_model.delete_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_title(movie_title)
            else:
                self.user_interface.delete_selected_movie(title)
        elif answer_user == 'q':
            self.movie_model.save_database()
        else:
            self.user_interface.show_incorrect_answer(answer_user)
