class Point3D:
    count = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Point3D.count += 1
        self.info()

    def info(self):
        return f'Координаты {Point3D.count}-й точки: {self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд должен быть типом данных Point3D')
        return f"Сложение координат: {(self.x + other.x, self.y + other.y, self.z + other.z)}"

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд должен быть типом данных Point3D')
        return f"Вычитание координат: {(self.x - other.x, self.y - other.y, self.z - other.z)}"

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд должен быть типом данных Point3D')
        return f"Умножение: {(self.x * other.x, self.y * other.y, self.z * other.z)}"

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд должен быть типом данных Point3D')
        return f"Деление: {(self.x / other.x, self.y / other.y, self.z / other.z)}"

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд должен быть типом данных Point3D')
        elif self.x == other.x and self.y == other.y and self.z == other.z:
            return f"Равенство координат: {True}"
        else:
            return f"Равенство координат: {False}"

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        elif item == "z":
            return self.z

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должен быть целым числом")

        if key == "x":
            self.x = value
            print(f'Запись значения в координату x: {value}')
        elif key == "y":
            self.y = value
            print(f'Запись значения в координату y: {value}')
        elif key == "z":
            self.z = value
            print(f'Запись значения в координату z: {value}')


a1 = Point3D(12, 15, 18)
print(a1.info())
a2 = Point3D(6, 3, 9)
print(a2.info())
a3 = a1 + a2
print(a3)
a4 = a1 - a2
print(a4)
a5 = a1 * a2
print(a5)
a6 = a1 / a2
print(a6)
print(a1 == a2)
print(f'x = {a1["x"]} x1 = {a2["x"]}')
print(f'y = {a1["y"]} y1 = {a2["y"]}')
print(f'z = {a1["z"]} z1 = {a2["z"]}')
a1["x"] = 20

