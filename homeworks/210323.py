class ValidInteger:
    @classmethod
    def verify_side(cls, side):
        if not isinstance(side, int):
            raise TypeError(f'Значение {side} должно быть числом.')
        elif side <= 0:
            raise ValueError(f'Значение {side} должно быть положительным и не равно 0.')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_side(value)
        instance.__dict__[self.name] = value


class Triangle:
    a = ValidInteger()
    b = ValidInteger()
    c = ValidInteger()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def proof(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            print(f'Треугольник со сторонами {(self.a, self.b, self.c)} существует.')
        else:
            print(f'Треугольник со сторонами {(self.a, self.b, self.c)} не существует.')


p1 = Triangle(2, 5, 6)
p1.proof()
p2 = Triangle(5, 2, 8)
p2.proof()
p3 = Triangle(7, 3, 6)
p3.proof()

