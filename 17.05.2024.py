# Есть некоторый словарь, который хранит название стран и столиц.
# Название стран используется в качестве ключа, название столицы в качестве значения.
# Необходимо реализовать: добавление, удаление, поиск, редактирование и просмотр данных
# (используя упаковку и распаковку данных)


import json

data = {}

print(f"******************************\n")


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def load_data(filename):
        try:
            date = json.load(open(filename))
        except FileNotFoundError:
            date = {}
        finally:
            return date

    @staticmethod
    def add_country(filename):
        country_name = input("Введите название страны(заглавной буквы): ")
        capital_name = input("Введите название столицы(с заглавной буквы): ")
        print("Файл сохранен")
        # try:
        #     date = json.load(open(filename))
        # except FileNotFoundError:
        #     date = {}
        date = CountryCapital.load_data(filename)

        date[country_name] = capital_name
        with open(filename, "w") as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            print(json.load(f))

    @staticmethod
    def delete_country(filename):
        del_country = input("Введите название страны: ")

        # try:
        #     date = json.load(open(filename))
        # except FileNotFoundError:
        #     date = {}
        date = CountryCapital.load_data(filename)

        if del_country in date:
            del date[del_country]

            with open(filename, "w") as f:
                json.dump(date, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_data(filename):
        country = input("Введите название страны: ")

        # try:
        #     date = json.load(open(filename))
        # except FileNotFoundError:
        #     date = {}
        date = CountryCapital.load_data(filename)

        if country in date:
            print(f"Страна {country} столица {date[country]} есть в словаре")
        else:
            print(f"Страны {country} нет в словаре")

    @staticmethod
    def edit_data(filename):
        country = input("Введите страну для корректировки: ")
        new_capital = input("Введите новое название столицы: ")

        # try:
        #     date = json.load(open(filename))
        # except FileNotFoundError:
        #     date = {}
        date = CountryCapital.load_data(filename)

        if country in date:
            date[country] = new_capital
            with open(filename, "w") as f:
                json.dump(date, f, indent=2)
        else:
            print("Такой страны в базе нет")


file = 'list_capital.json'
index = ''
while True:
    index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - "
                  "редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
    if index == "1":
        CountryCapital.add_country(file)
        print(f"******************************\n")
    elif index == "2":
        CountryCapital.delete_country(file)
        print(f"******************************\n")
    elif index == "3":
        CountryCapital.search_data(file)
        print(f"******************************\n")
    elif index == "4":
        CountryCapital.edit_data(file)
        print(f"******************************\n")
    elif index == "5":
        CountryCapital.load_from_file(file)
        print(f"******************************\n")
    elif index == "6":
        print(f"******************************\n")
        break
    else:
        print("Введен некорректный номер")
