def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserUnterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действия с фильмами:")
        print("1 - Добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Добавление фильма")
    def add_user_movies(self):
        dict_movies = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None,
        }
        # print("Добавление фильма".center(50, "="))
        for key in dict_movies:
            dict_movies[key] = input(f"Введите {key} фильма: ")
        # print("=" * 50)
        return dict_movies

    @add_title("Просмотр каталога фильмов")
    def show_all_movies(self, movies):
        # print(" Список фильмов ".center(50, "="))
        for ind, movies in enumerate(movies, 1):
            print(f"{ind}. {movies}")
        # print("=" * 50)

    @add_title("Ввод названия фильма")
    def get_user_movies(self):
        user_movies = input("Введите название фильма: ")
        return user_movies

    @add_title("Просмотр определенного фильма")
    def show_single_movies(self, movies):
        for key in movies:
            print(f"{key} фильма - {movies[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_movies(self, movies):
        print(f" Фильм {movies} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
