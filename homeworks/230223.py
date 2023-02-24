from math import pi


class Sphere:
    __slots__ = ["__r", "__x", "__y", "__z"]

    def __init__(self, r, x, y, z):
        self.__x = self.__y = self.__z = self.__r = 0
        if Sphere.__check_value(r) and Sphere.__check_value(x) and Sphere.__check_value(y) and Sphere.__check_value(z):
            self.__r = r
            self.__x = x
            self.__y = y
            self.__z = z

    def __check_value(self):
        if isinstance(self, (int, float)):
            return True
        return False

    def get_volume(self):
        return round((self.__r ** 3) * pi * 4 / 3, 4)

    def get_square(self):
        return round((self.__r ** 2) * pi * 4, 4)

    def get_radius(self):
        return self.__r

    def get_center(self):
        return self.__x, self.__y, self.__z

    def set_radius(self, r):
        if Sphere.__check_value(r):
            self.__r = r
        else:
            print("Радиус должен быть числом.")

    def set_center(self, x, y, z):
        if Sphere.__check_value(x) and Sphere.__check_value(y) and Sphere.__check_value(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print("Координаты должны быть числами.")

    def is_point_inside(self, x, y, z):
        return (self.__x - x) ** 2 + (self.__y - y) ** 2 + (self.__z - z) ** 2 < self.__r ** 2


s1 = Sphere(0.6, 0, 0, 0)
print(s1.get_volume())
print(s1.get_square())
print(s1.get_center())
print(s1.is_point_inside(0, -1.5, 0))
s1.set_radius(1.6)
print(s1.is_point_inside(0, -1.5, 0))
s1.set_radius("two")
s1.set_center("one", 0, "zero")


