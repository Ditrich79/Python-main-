# Вариант №1

class Car:
    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year_of_issue = year
        self.manufacturer = manufacturer
        self.engine_power = engine
        self.color = color
        self.price = price

    def print_info(self):
        print(' Данные автомобиля '.center(40, '*'))
        print(f'Название модели: {self.model}\nГод выпуска: {self.year_of_issue}\nПроизводитель: {self.manufacturer}'
              f'\nМощность двигателя: {self.engine_power}\nЦвет машины: {self.color}\nЦена: {self.price}')
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year_of_issue = year

    def get_year(self):
        return self.year_of_issue

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine(self, engine):
        self.engine_power = engine

    def get_engine(self):
        return self.engine_power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


c1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
c1.print_info()

c1.set_model("Portofino")
print(c1.get_model())
c1.set_year("2017")
print(c1.get_year())
c1.set_manufacturer("Ferrari")
print(c1.get_manufacturer())
c1.set_engine("600 л.с.")
print(c1.get_engine())
c1.set_color("red")
print(c1.get_color())
c1.set_price("16960000")
print(c1.get_price())

c1.print_info()


# Вариант №2

# class Car:
#     model = 'model'
#     year_of_issue = 'year'
#     manufacturer = 'manufacturer'
#     engine_power = 'engine_power'
#     color = 'color'
#     price = 'price'
#
#     def print_info(self):
#         print(' Данные автомобиля '.center(40, '*'))
#         print(f'Название модели: {self.model}\nГод выпуска: {self.year_of_issue}\nПроизводитель: {self.manufacturer}'
#               f'\nМощность двигателя: {self.engine_power}\nЦвет машины: {self.color}\nЦена: {self.price}')
#         print("=" * 40)
#
#     def input_info(self, model, year, manufacturer, engine, color, price):
#         self.model = model
#         self.year_of_issue = year
#         self.manufacturer = manufacturer
#         self.engine_power = engine
#         self.color = color
#         self.price = price
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_year(self, year):
#         self.year_of_issue = year
#
#     def get_year(self):
#         return self.year_of_issue
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_engine(self, engine):
#         self.engine_power = engine
#
#     def get_engine(self):
#         return self.engine_power
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# c1 = Car()
# c1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# c1.print_info()
#
# c1.set_model("Portofino")
# print(c1.get_model())
# c1.set_year("2017")
# print(c1.get_year())
# c1.set_manufacturer("Ferrari")
# print(c1.get_manufacturer())
# c1.set_engine("600 л.с.")
# print(c1.get_engine())
# c1.set_color("red")
# print(c1.get_color())
# c1.set_price("16960000")
# print(c1.get_price())
#
# c1.print_info()
