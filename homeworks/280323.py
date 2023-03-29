import json

data = {}


def load_data(func):
    def wrap(filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = {}
        func(filename)
        print("Файл сохранён")

    return wrap


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @staticmethod
    @load_data
    def add_country(file_name):
        new_country = input('Введите название страны: ').capitalize()
        new_capital = input('Введите название столицы: ').capitalize()

        data[new_country] = new_capital

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    @load_data
    def delete_country(file_name):
        del_country = input('Введите название страны: ').capitalize()

        if del_country in data:
            del data[del_country]

            with open(file_name, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print('Такой страны в базе нет.')

    @staticmethod
    @load_data
    def search_data(file_name):
        country = input('Введите название страны: ').capitalize()

        if country in data:
            print(f"Страна {country}, столица {data[country]} есть в словаре")
        else:
            print(f'Страна {country} нет в словаре')

    @staticmethod
    @load_data
    def edit_data(file_name):
        country = input('Введите страну для корректировки: ').capitalize()
        new_capital = input("Введите новое название столицы: ").capitalize()

        if country in data:
            data[country] = new_capital
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as f:
            print(json.load(f))


def interactive():
    file = 'list_capital.json'
    index = ''
    while True:
        print('*' * 30)
        index = input('Выбор действия:\n1 - добавление данных\n'
                      '2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n'
                      '5 - просмотр данных\n6 - завершение работы\nВвод: ')
        print('*' * 30)

        if index == '1':
            CountryCapital.add_country(file)
        elif index == '2':
            CountryCapital.delete_country(file)
        elif index == '3':
            CountryCapital.search_data(file)
        elif index == '4':
            CountryCapital.edit_data(file)
        elif index == '5':
            CountryCapital.load_from_file(file)
        elif index == '6':
            break
        else:
            print("Введён некорректный номер")


if __name__ == '__main__':
    interactive()
