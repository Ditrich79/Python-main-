# number = 123456789.12345
# print(f'{number:,.2f}')
# print(f'{number:,.3F}')

# discount = 0.5
# print(f'{discount:.0%}')  # символ % умножает число на 100 и выводит его со знаком %

# number = 123456
# print(f'{number:,d}')  # 123,456

# number = 12345.6789
# print(f'Ширина поля равна {number:15,.2f}')  # Ширина поля равна       12,345.68

# number = 236589
# print(f'{number:^15,d}')  # выравнивание по центру поля
# print(f'{number:<15,d}')  # выравнивание по левому краю поля
# print(f'{number:>15,d}')  # выравнивание по правому краю поля

# def main():
#     show_interest(rate=0.01, periods=10, principal=10000.0)
#
#
# def show_interest(principal, rate, periods):
#     interest = principal*rate*periods
#     print(f'Простой процентный доход составит ${interest:,.2f}')
#
#
# main()


# import time
#
# print(time.strftime('Сегодня: ''%d.%m.%Y, %H:%M:%S'))

# def convert(kiloms):
#     miles = kiloms * 0.6214
#     return miles
#
#
# print(convert(100))

# # Получить требуемое будущее значение
# future_value = float(input("Введите требуемое будущее значение: "))
#
# # Получить годовую процентную ставку
# rate = float(input("Введите годовую процентную ставку: "))
#
# # Получить количество лет хранения денег на счёте
# years = int(input("Введите количество лет хранения денег на счёте: "))
#
# # Рассчитать сумму, необходимую для внесения на счёт
# present_value = future_value / (1 + rate) ** years
#
# # Показать сумму, необходимую для внесения на счёт
# print("Вам потребуется внести сумму: ", round(present_value, 2))


# # Эта программа вычисляет отпускную цену розничного товара.
#
# # DISCOUNT_PERCENTAGE - процент скидки
# DISCOUNT_PERCENTAGE = 0.2
#
#
# # Главная функция.
# def main():
#     #  Получить обычную цену товара.
#     reg_price = get_regular_price()
#
#     #  Рассчитать отпускную цену.
#     sale_price = reg_price - discount(reg_price)
#
#     #  Показать отпускную цену.
#     print(f"Отпускная цена составляет ${sale_price:,.2f}.")
#
#
# # Функция get_regular_price предлагает пользователю ввести обычную цену
# # товара и возвращает это значение.
#
#
# def get_regular_price():
#     price = float(input('Введите обычную цену товара: '))
#     return price
#
#
# # Функция discount принимает цену товара в качестве аргумента и возвращает
# # сумму скидки, указанную в DISCOUNT_PERCENTAGE.
# def discount(price):
#     return price * DISCOUNT_PERCENTAGE
#
#
# # Вызвать главную функцию.
# main()


# def spend_on_car():
#     credit = int(input('Укажите сколько Вы платите в месяц за кредит на машину: '))
#     insur = int(input('Укажите сколько Вы платите в месяц за страховку автомобиля: '))
#     bensin = int(input("Укажите сколько Вы тратите в месяц на бензин: "))
#     tech = int(input('Укажите сколько Вы тратите в месяц на техобслуживание автомобиля: '))
#     month_spend = credit + insur + bensin + tech
#     year_spend = month_spend * 12
#     print(f"Расходы в месяц на автомобиль составляют {month_spend}")
#     print(f"Расходы в год на автомобиль составляют {year_spend}")
#
#
# spend_on_car()

# def main():
#     value = 5
#     show_double(value)
#
#
# def show_double(num):
#     result = num * 2
#     print(result)
#
#
# main()

# def main():
#     show_interest(principal=10000.0, periods=10, rate=0.01)
#
#
# def show_interest(principal, rate, periods):
#     interest = principal * rate * periods
#     print(f'Простой процентный доход составит ${interest:,.2f}')
#
#
# main()


# MAIN_TAX = 0.0072
#
#
# def main():
#     osnov = float(input('Введите фактическую стоимость Вашего имущества: '))
#     tax_new = ozen_cost(osnov)
#     print(f'Оценочная стоимость Вашего имущества составит ${ozen_cost(osnov):,.2f}.\n'
#           f'Налог на имущество будет ${tax(tax_new):,.2f}.')
#
#
# def ozen_cost(num):
#     return num * 0.6
#
#
# def tax(a):
#     return a * MAIN_TAX
#
#
# main()


# with open('F:/R57553.txt', 'r') as f:
#     print(f.read())


# Эта программа предлагает пользователю ввести суммы
# продаж и записывает эти суммы в файл sales.txt.

# def main():
#     # Получить количество дней.
#     num_days = int(input('За какое количество дней ' +
#                          'Вы располагаете продажами? '))
#
#     # Открыть новый файл с именем sales.txt.
#     sales_file = open('sales.txt', 'w')
#
#     # Получить суммы продаж за каждый день
#     # и записать их в файл.
#     for count in range(1, num_days + 1):
#         # Получить продажи за день.
#         sales = float(input(
#             f'Введите продажи за день № {count}: '))
#         # Записать сумму продаж в файл.
#         sales_file.write(f'{sales}\n')
#
#     # Закрыть файл.
#     sales_file.close()
#     print('Данные записаны в sales.txt.')
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# # Программа расчёта налога с продаж
# FED_TAX = 0.05
# MUN_TAX = 0.025
#
#
# def main():
#     sales = float(input("Укажите общий объём продаж за месяц: "))
#     all_taxes = get_fed_tax(sales) + get_mun_tax(sales)
#     print(f"Сумма федерального налога с продаж составляет ${get_fed_tax(sales):,.2f}.")
#     print(f"Сумма муниципального налога с продаж составляет ${get_mun_tax(sales):,.2f}.")
#     print(f"Общий налог с продаж составляет ${all_taxes:,.2f}.")
#
#
# def get_fed_tax(num):
#     return num * FED_TAX
#
#
# def get_mun_tax(num):
#     return num * MUN_TAX
#
#
# if __name__ == '__main__':
#     main()


# Эта программа сохраняет последовательность, состоящую из
# длительностей видеоклипов, в файле video_times.txt.

# def main():
#     # Получить количество видеоклипов в проекте.
#     num_videos = int(input('Cкoлькo видеоклипов в проекте? '))
#
#     # Открыть файл для записи длительностей видеоклипов.
#     video_file = open('video_times.txt', 'w')
#
#     # Получить длительность каждого видеоклипа
#     # и записать е г о в файл.
#     print('Введите длительность каждого видеоклипа.')
#     for count in range(1, num_videos + 1):
#         run_time = float(input(f'Bидeoклип № {count}: '))
#         video_file.write(f'{run_time}\n')
#
#     # Закрыть файл.
#     video_file.close()
#     print('Времена сохранены в video_times. txt. ')
#
#
# # Вызвать главную функцию .
# if __name__ == '__main__':
#     main()


# Эта программа добавляет записи о запасах кофе
# в файл coffee.txt.

# def main():
#     # Создать переменную для управления циклом.
#     another = 'д'
#
#     # Открыть файл coffee.txt file в режиме дозаписи.
#     coffee_file = open('coffee.txt', 'a')
#
#     # Добавить запись в файл.
#     while another == 'д' or another == 'Д':
#         # Получить данные с записью о кофе.
#         print('Введите следующие данные о кофе:')
#         descr = input('Описание: ')
#         qty = int(input('Количество (в фунтах): '))
#
#         # Добавить данные в файл.
#         coffee_file.write(f'{descr}\n')
#         coffee_file.write(f'{qty}\n')
#
#         # Определить, желает ли пользователь добавить
#         # в файл ещё одну запись.
#         print('Желаете ли Вы добавить ешё одну запись?')
#         another = input('Д = да, всё остальное = нет: ')
#
#     # Закрыть файл.
#     coffee_file.close()
#     print('Данные добавлены в coffee.txt.')
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# Эта программа показывает записи
# из файла coffee.txt.

# def main():
#     # Открыть файл coffee.txt.
#     coffee_file = open('coffee.txt', 'r')
#
#     # Прочитать поле с описанием первой записи.
#     descr = coffee_file.readline()
#
#     # Прочитать остаток файла.
#     while descr != '':
#         # Прочитать поле с количеством.
#         qty = float(coffee_file.readline())
#
#         # Удалить \n из описания.
#         descr = descr.rstrip('\n')
#
#         # Показать запись.
#         print(f'Описание: {descr}')
#         print(f'Количество: {qty}')
#
#         # Прочитать следующее описание.
#         descr = coffee_file.readline()
#
#     # Закрыть файл.
#     coffee_file.close()
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# Эта программа позволяет пользователю производить поиск
# в файле coffee.txt записей, которые соответствуют
# описанию.

# def main():
#     # Создать булеву переменную для использования её в качестве флага.
#     found = False
#
#     # Получить искомое значение.
#     search = input('Введите искомое описание: ')
#
#     # Открыть файл coffee.txt.
#     coffee_file = open('coffee.txt', 'r')
#
#     # Прочитать поле с описанием кофе первой записи.
#     descr = coffee_file.readline()
#
#     # Прочитать остаток файла.
#     while descr != '':
#         # Прочитать поле с количеством.
#         qty = float(coffee_file.readline())
#
#         # Удалить \n из описания.
#         descr = descr.rstrip('\n')
#
#         # Определить, соответствует ли эта запись
#         # поисковому значению.
#         if descr == search:
#             # Показать запись.
#             print(f'Описание: {descr}')
#             print(f'Количество: {qty}')
#             print()
#             # Назначить флагу found значение True.
#             found = True
#
#         # Прочитать следующее описание.
#         descr = coffee_file.readline()
#
#     # Закрыть файл.
#     coffee_file.close()
#
#     # Если поисковое значение в файле не найдено,
#     # то показать сообщение.
#     if not found:
#         print('Это значение в файле не найдено.')
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# # Эта программа показывает содержимое файла
# def main():
#     # Получить имя файла
#     filename = input("Введите имя файла: ")
#
#     try:
#         # Открыть файл
#         infile = open(filename, "r")
#
#         # Прочитать содержимое файла
#         contents = infile.read()
#
#         # Показать содержимое файла
#         print(contents)
#
#         # Закрыть файл
#         infile.close()
#     except IOError:
#         print('Произошла ошибка при попытке прочитать')
#         print('файл', filename)
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         hours = int(input('Введите сколько часов Вы отработали: '))
#         pay_rate = float(input("Введите почасовую ставку: "))
#         gross_pay = hours * pay_rate
#         print(f"Заработная плата: ${gross_pay:,.2f}")
#     except ValueError as err:
#         print(err)
#
#
# if __name__ == "__main__":
#     main()


# Эта программа демонстрирует консервацию объектов
import pickle


#
#
# # Главная функция.
# def main():
#     again = 'д'  # Для управления повторением цикла
#
#     # Открыть файл для двоичной записи.
#     output_file = open('info.dat', 'wb')
#
#     # Получать данные, пока пользователь не решит прекратить.
#     while again.lower() == 'д':
#         # Получить данные о человеке и сохранить их.
#         save_data(output_file)
#
#         # Пользователь желает ввести еще данные?
#         again = input('Желаете ввести еще данные? (д/н) : ')
#
#     # Закрыть файл.
#     output_file.close()
#
#
# # Функция save_data получает данные о человеке,
# # сохраняет их в словаре и затем консервирует
# # словарь в указанном файле.
# def save_data(file):
#     # Создать пустой словарь.
#     person = {}
#
#     # Получить данные о человеке и сохранить
#     # их в словаре.
#     person['имя'] = input('Имя: ')
#     person['возраст'] = int(input('Возраст: '))
#     person['масса'] = float(input('Масса: '))
#
#     # Законсервировать словарь.
#     pickle.dump(person, file)
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# # Эта программа демонстрирует расконсервацию объектов.
# # Главная функция.
# def main():
#     end_of_file = False  # Для обозначения конца файла.
#
#     # Открыть файл для двоичного чтения.
#     input_file = open('info.dat', 'rb')
#
#     # Прочитать файл до конца.
#     while not end_of_file:
#         try:
#             # Расконсервировать следующий объект.
#             person = pickle.load(input_file)
#
#             # Показать объект.
#             display_data(person)
#         except EOFError:
#             # Установить флаг, чтобы обозначить, что
#             # был достигнут конец файла.
#             end_of_file = True
#
#     # Закрыть файл.
#     input_file.close()
#
#
# # Функция display_data показывает данные о человеке
# # в словаре, который передан в качестве аргумента.
# def display_data(person):
#     print('Имя: ', person['имя'])
#     print('Возраст: ', person['возраст'])
#     print('Масса: ', person['масса'])
#     print()
#
#
# # Вызвать главную функцию.
# if __name__ == '__main__':
#     main()


# class Pet:
#     def __init__(self, name, animal_type, age):
#         self.__name = name
#         self.__animal_type = animal_type
#         self.__age = age
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def set_animal_type(self, new_animal_type):
#         self.__animal_type = new_animal_type
#
#     def set_age(self, new_age):
#         self.__age = new_age
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
#     def __str__(self):
#         return f'Имя животного: {self.__name}; тип: {self.__animal_type}; возраст: {self.__age} лет'
#
#
# a1 = Pet('Гриша', 'попугай', 5)
# print(a1)
# a2 = Pet('Фиса', 'кошка', 3)
# print(a2)
# a2.set_name('Маруся')
# print(a2)
# print(a1.get_animal_type())


# class Car:
#     def __init__(self, year_model, make):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         return self.__speed + 5
#
#     def break_(self):
#         return self.__speed - 5
#
#     def get_speed(self):
#         return self.__speed
#
#     def range(self):
#         return self.accelerate() * 5
#
#     def stop(self):
#         return self.accelerate() / 5
#
#     def __str__(self):
#         return f'Год выпуска автомобиля: {self.__year_model}, марка: {self.__make}, скорость: {self.__speed}'
#
#
# # def main():
# #     y_model = int(input('Введите год выпуска автомобиля: '))
# #     make = input('Введите марку автомобиля: ')
# #     speed = input('Укажите скорость автомобиля: ')
# #     car = Car(y_model, make)
#
# c1 = Car(1997, "Шевроле Камаро")
# print(c1)
# print(c1.accelerate())
# print(c1.range())
# print(c1.stop())


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def write_csv(data):
#     with open('books.csv', 'a') as file:
#         write = csv.writer(file, delimiter=";", lineterminator="\r")
#         write.writerow((data['names'], data['author'], data['description'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("div", class_="item_block item full_block")
#     for plugin in p1:
#         try:
#             names = plugin.find("div", class_="book_name").text
#         except ValueError:
#             names = ''
#
#         try:
#             description = plugin.find("div", class_="dscr").text
#         except ValueError:
#             description = ''
#
#         try:
#             author = plugin.find("a", class_="genre").text
#         except ValueError:
#             author = ''
#
#         try:
#             rating = plugin.find("div", class_="rating_count").text
#         except ValueError:
#             rating = ''
#
#         data_base = {
#             'names': names,
#             'description': description,
#             'author': author,
#             'rating': rating
#         }
#         write_csv(data_base)
#
#
# def main():
#     for i in range(0, 3):
#         url = f"https://avidreaders.ru/books/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# class Mammal:
#     def __init__(self, species):
#         self.__species = species
#
#     def show_species(self):
#         print('Я -', self.__species)
#
#     def make_sound(self):
#         print('Гррррррр')
#
#
# class Dog(Mammal):
#     def __init__(self):
#         Mammal.__init__(self, 'собака')
#
#     def make_sound(self):
#         print('Гав-гав')
#
#
# class Cat(Mammal):
#     def __init__(self):
#         Mammal.__init__(self, 'кот')
#
#     def make_sound(self):
#         print('Мяу!')
#
#
# m = Mammal('млекопитающее')
# m.show_species()
# m.make_sound()
# d = Dog()
# d.show_species()
# d.make_sound()
# c = Cat()
# c.show_species()
# c.make_sound()


# def main():
#     message(5)
#
#
# def message(times):
#     if times > 0:
#         print('Это - рекурсивная функция.')
#         message(times - 1)
#
#
# if __name__ == '__main__':
#     main()
#

# def main():
#     num = int(input('Введите неотрицательное число: '))
#     fac = factorial(num)
#     print(f'Факториал числа {num} равняется {fac}.')
#
#
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
#
# if __name__ == '__main__':
#     main()

# Ханойские башни
# def main():
#     num_disks = 3
#     from_peg = 1
#     to_peg = 3
#     temp_peg = 2
#
#     move_discs(num_disks, from_peg, to_peg, temp_peg)
#     print('Все кольца перемещены.')
#
#
# def move_discs(num, from_peg, to_peg, temp_peg):
#     if num > 0:
#         move_discs(num - 1, from_peg, temp_peg, to_peg)
#         print(f'Переместить кольцо со стержня {from_peg} на стержень {to_peg}')
#         move_discs(num - 1, temp_peg, to_peg, from_peg)
#
#
# if __name__ == '__main__':
#     main()

# def main(n):
#     if n > 0:
#         print('*' * n)
#         main(n - 1)
#
#
# main(10)

# print(format(0.5, '.0%'))


# class Employer:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.check_age(age)
#         self.show_info()
#
#     @staticmethod
#     def show_info():
#         print('This is Employer class')
#
#     def __str__(self):
#         return f'Name: {self.__name}, age: {self.__age}.'
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     @staticmethod
#     def check_age(age):
#         if not isinstance(age, int):
#             raise TypeError(f'The value must be integer.')
#
#
# e = Employer("Vasja", 35)
# print(e)
# e2 = Employer('Petya', 40)
# print(e2)
#
#
# class President(Employer):
#     def __init__(self, name, age, car):
#         super().__init__(name, age)
#         super().check_age(age)
#         self.__car = car
#
#     def show_info(self):
#         print('This is President class.')
#
#     def __str__(self):
#         return f'Name: {self.name}, Age: {self.age}, Car: {self.__car}'
#
#     @property
#     def car(self):
#         return self.__car
#
#     @car.setter
#     def car(self, new_car):
#         self.__car = new_car
#
#
# p = President('Dima', 43, 'Mercedes')
# print(p)
# p.car = "Audi"
# print(p)


# class MathCalculations:
#     count = 0
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     def __str__(self):
#         print(f'Сторона А: {self.__a}, сторона B: {self.__b}, сторона С: {self.__c}.')
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         self.__b = b
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         self.__c = c
#
#     @staticmethod
#     def get_square_area(a):
#         return a * a
#
#     @staticmethod
#     def get_rectangle_area(a, b):
#         return a * b
#
#
# m = MathCalculations(4, 5, 3)
# print(m.get_square_area(5))
# print(m.get_rectangle_area(8, 7))


