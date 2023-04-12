def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result

        return wrap

    return wrapper


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def wait_for_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма\n"
              "2 - каталог фильмов\n"
              "3 - просмотр определенного фильма\n"
              "4 - удаление фильма\n"
              "q - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Добавление фильма')
    def add_user_movie(self):
        dict_movies = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_movies:
            dict_movies[key] = input(f"Введите {key} фильма: ")
        return dict_movies

    @add_title('Каталог фильмов')
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, start=1):
            print(f"{ind}. {movie}")

    @add_title('Ввод названия фильма')
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_title('Просмотр выбранного фильма')
    def show_selected_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title('Сообщение об ошибке')
    def show_incorrect_title(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title('Удаление фильма')
    def delete_selected_movie(self, movie):
        print(f"Фильм {movie} - был удалён")

    @add_title('Сообщение об ошибке')
    def show_incorrect_answer(self, answer):
        print(f"Варианта {answer} не существует")
