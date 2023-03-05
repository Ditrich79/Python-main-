from math import sqrt


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.val_a(a)
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.val_b(b)
        self.__b = b

    @staticmethod
    def val_a(a):
        if not isinstance(a, (int, float)):
            raise TypeError("А должно быть числом")

    @staticmethod
    def val_b(b):
        if not isinstance(b, (int, float)):
            raise TypeError("В должно быть числом")

    def product(self):
        print(f'Произведение:', end=" ")
        return self.__a * self.__b

    def sum_of_numbers(self):
        print(f'Сумма:', end=" ")
        return self.__a + self.__b


class RightTriangle(Pair):

    def info_hypotenuse(self):
        print(f"Гипотенуза △АВС: {self.hypotenuse()}")

    def hypotenuse(self):
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)

    def area(self):
        print("Площадь △АВС:", end=" ")
        return (self.a * self.b) / 2

    def info_triangle(self):
        print(f"Прямоугольный треугольник △АВС ({self.a}, {self.b}, {self.hypotenuse()})")


triangle = RightTriangle(5, 8)
print(triangle.sum_of_numbers())
print(triangle.product())
triangle.hypotenuse()
triangle.info_hypotenuse()
print(triangle.area())
triangle.info_triangle()
print()
triangle2 = RightTriangle(13, 17)
print(triangle2.sum_of_numbers())
print(triangle2.product())
triangle2.hypotenuse()
triangle2.info_hypotenuse()
print(triangle2.area())
triangle2.info_triangle()

