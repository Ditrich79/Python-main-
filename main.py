# name = "Ditrich"  # имя
# print("Hello", name)
# age = 20
# print(type(age))
# print(id(age))
# age = "hello"
# print(type(age))
import re

# a = b = c = 1
# print(a, b, c)

# a, b, c, = 5, "Hello", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type(True))

# a = "5"
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
# # c = a
# # a = b
# # b = c
# # a = a + b  # a = 1 + 2 = 3
# # b = a - b  # b = 3 - 2 = 1
# # a = a - b  # a = 3 - 1 = 2
# a, b = b, a
# print("a =", a)
# print("b =", b)

# print("строка символов")
# print('строка \rсимволов')

# print("\tДокумент   \"file.txt\"")

# s1 = "Hello"
# s2 = "Python"
# print(s1 + " " + s2)
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)

# print(56464652132456464646212341484)
# print(5.6464652132456464646212341484)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# um = a * b * c
# sr = sum1 / 3
# print("Сумма:", sum1)
# print("Произведение:", um)
# print("Среднее арифметическое:", sr)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3
# print(num)  # 12

# num = 4321  # 432
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num % 10
# print(d)
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10  # 432
# res += num % 10 * 100
# num //= 10  # 43
# res += num % 10 * 10
# num //= 10  # 4
# res += num % 10
# print(res)

# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# a = (round(3.8))
# print(a)
# print(type(a))
# b = (round(3.8915464, 2))
# print(b)
# print(type(b))

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне" + str(age) + "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end="\n\n")
# print("Я учу Python.")

# name = input("Ваше имя:")
# print(name)

# Число 5 в степени 2 равно 25

# a, b, c = 5, 2, 25
# print(a, b, c)

# num = input("Число: ")
# st = input("Степень: ")
# num = int(num)
# st = int(st)
# res = num ** st
# print("Число", num )

# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))
# print(bool(None))

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 < 7)
# print(8 <= 7)

# print(2 < 10 < 9)  # True && False
# print(3 * 3 <= 7 >= 3)  # False && False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)

# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 45
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
# if a != b != c:
#     print("Треугольник разносторонний")
# elif a == b == c:
#     print("Треугольник равносторонний")
# else:
#     print("Треугольник равнобедренный")

# day = int(input("Введите день недели (цифрой): "))
# if day >= 1 and day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца (цифрой): "))
# if  month <= 2 or month == 12:
#     print("Сейчас зима")
# elif 3 <= month <= 5:
#     print("Сейчас весна")
# elif 6 <= month <= 8:
#     print("Сейчас лето")
# elif 9 <= month <= 11:
#     print("Сейчас осень")
# else:
#     print("Такого месяца не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода")

# n = int(input("Введите число от 1 до 99: "))
# kop = n
# if 11 <= kop <= 14:
#     print(n, "копеек")
# elif 0 < n <= 10 or 15 <= n <= 99:  #89
#     kop = kop % 10
#     if kop == 1:
#         print(n, "копейка")
#     elif 2 <= kop <= 4:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("Ошибка ввода")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = 'вторник'
# time = 10
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует")


# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = int(input()), int(input())
# print(a / b if b != 0 else "На ноль делить нельзя")


# Исключения

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводить строки и делить на ноль")
# else:  # когда в блоке try не возникло исключение
#     print("Всё нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")


# x = input('Введите первое число: ')
# y = input('Введите второе число: ')
#
# try:
#     x = int(x)
#     y = int(y)
# except ValueError:
#     x = str(x)
# finally:
#     print(x + y)


# Циклы
# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# try:
#     x = int(input('Введите количество: '))
#     while x > 0:
#         print('*', end='')
#         x += 1
# except ValueError:
#     print('Введите число')

# x = int(input('Введите количество: '))
# i = 0
# while i < x:
#     print('*', end='')
#     i += 1


# i = 1
# a = 0
# while i <= 5:
#     if i % 2 != 0:
#         a += i
#     i += 1
# print(a)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# m = 1
# while True:
#     n = int(input('Число: '))
#     if n == 0:
#         break
#     m *= n
# print('Произведение равно:', m)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while i <= 9:
#         print(i, '*', j, '=', i * j, '\t\t', end='')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(j, "*", i, "=", j * i, '\t\t', end='')
#         j += 1
#     print()
#     i += 1

# n = int(input('Размер клетки: '))
# m = int(input('Размер поля: '))
# field1 = ('*' * n + ' ' * n) * (m // 2)
# field2 = (' ' * n + '*' * n) * (m // 2)
# if m % 2 == 1:
#     field1 += '*' * n + ' ' * n + '\n'
#     field2 += ' ' * n + '*' * n + '\n'
# else:
#     field1 += '\n'
#     field2 += '\n'
# field = (field1 * n + field2 * n) * (m // 2)
# if m % 2 == 1:
#     field += field1 * n;
# print(field)

# a, b = 4, 2
# print("На ноль делить нельзя" if b == 0 else a / b)

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
#
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = int(input("Введите количество звездочек: "))
# while i > 0:
#     print("*", end="")
#     i -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# total = 0
# while a <= b:
#     if a % 2 != 0:
#         total += a
#     a += 1
# print(total)

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(j, "*", i, "=", j * i, '\t\t', end='')
#         j += 1
#     print()
#     i += 1


# for element in collection:
#   тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

# range(start, stop, step)

# for i in range(10, 0, -1):
#     print(i, end=" ")

# i = 5
# while i < 100:
#     print(i, end=" ")
#     i += 5

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')

# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for i in range(w):
#         print("*", end="")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         print()
#
# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


#  Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums))
# print(id(nums))
# print(nums[0])
# print(nums[-1])
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(id(nums))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5, 2] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)


# n = list(range(2, 10, 2))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i * 3 for i in "Hello"]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
#
# for i in range(len(nums)):  # 0 1 2 3 4
#     print(nums[i] * 2, end=" ")
# print()
# for elem in nums:  # 8 3 9 4 1
#     print(elem * 2, end=" ")


# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# print(a)

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print(summa)

# a = list(range(21, 41))
# print(a)
# print()
# b = [i for i in range(21, 41)]
# print(b)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, '\nНечетных: ', even)


# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
#
# count = sum1 = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum1 += i
# print('Среднее: ', sum1 / count)


# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:  # a[0] = 7 > a[0 - 1] = 2
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


# список[start:stop:step]

# a = [9, 4, 3, 1, 5, 17]
#
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[10:20])

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# a[3:5] = []
# print(a)
# del a[0:3]
# print(a)
# del a[:]
# print(a)

# Методы списков

# a = list(range(1, 8))
# print(a)
# a.append(99)  # добавляет элемент в конец списка
# print(a)
# a.extend([22, 11, 9])  # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)  # добавляет элемент в список. Первый параметр - индекс, второй - добавляемое значение
# print(a)
# a.extend('add')
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = input("-> ")
#     s.append(x)
# print(s)

# s = []
# n = int(input("Введите заданное количество раз число кратное 3: "))
# if n % 3 == 0:
#     s.append(n)
# else:
#     print("Введённое число не делится на 3 без остатка!")
# print()

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 12, 13, 2, 4]
# c = []
#
# if len(b) < len(a):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 12, 13, 2, 4, 13]
# b.remove(13)  # удаляет элемент из списка по значению, если элементов с заданным значением несколько, то удаляется
# # только первый
# print(b)
# a = 12
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # с пустыми скобками удаляет последний элемент из списка, с заданным индексом в скобках - удаление
# # по индексу
# print(b)
# print(last)
#
# b.clear()
# print(b)  # очищает список

# a = [int(input("-> ")) for i in range(int(input('n = ')))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)  # количество заданных значений в списке
# print(num)
# ind = a.index(2, 2, -1)  # возвращает первый индекс искомого значения, также можно указывать значения start и end
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print('a:', a)
# print('b:', b)
# a.append(20)
# print('a:', a)
# print('b:', b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# # a.reverse()  # перестраивает элементы списка в обратном порядке
# # print(a)
# # a.sort(reverse=True)  # сортирует список, по умолчанию - по возрастанию, reverse=True - по убыванию
# # print(a)
# #
# # b = ["Виталий", "Сергей", "Александр", "Анна"]
# # b.sort(key=len, reverse=True)
# # print(b)
#
# c = sorted(a)
# print(c)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # с 2 по 9 (включительно)
# print(random.randrange(2, 9, 2))

# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))


# import random as r
#
# print(r.randint(2, 9))  # с 2 по 9 (включительно)
# print(r.randrange(2, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = ['5, 3, 2, 4, 1', "abc"]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# # print(sum(lst))

# s = [8, 9, 5, 6, 3, 5, 4, 2, 1]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
# print(res)

# x = list('1a2b3c4c')
# print(x)
# # print('a' in x)
# print('w' in x)
# # print('a' not in x)
# print('w' not in x)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# from random import randint
#
# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print('Третий список: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Элементы обоих списков без повторений: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Элементы общие для двух списков: ', c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# from random import randrange
#
# n = int(input("Размер списка: "))
# s = []
# for i in range(n):
#     num = randrange(10)
#     if num not in s:
#         s.append(num)
# print(s)

# from random import randrange
#
# a = []
# b = int(input('Введите размер первого списка: '))
# while len(a) < b:
#     c = randrange(b)
#     if c not in a:
#         a.append(c)
# print(a)


# m = [
#     [1, 2, 3, 4, ],
#     [4, 8, 7, 6],
#     [11, 9, 6, 8]
# ]

# print(m)
# print(m[2][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()

# from random import randint
# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
# matrix = []
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):  # 5
#         new_row.append(0)
#     matrix.append(new_row)

# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# print([[x for x in row] for row in matrix])

# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for x, y in a:
#     print(x, '+', y, '=', x + y)

# from random import randint
#
# w, h = 3, 4
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#         if x < 0:
#             count += 1
#     print()
# print('Количество отрицательных чисел:', count)

# from random import randint

# w, h = 3, 4
# n = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x != 0:
#             n *= x
#         print(x, end='\t\t')
#     print()
# print('n=', n)

# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
#
# s = []
# # m = 101
# for i in range(w):
#     s.append(matrix[i][i])
#     # if m > matrix[i][i]:
#     #     m = matrix[i][i]
# print(s)
# print(min(s))

# import math
# from math import sqrt, ceil, floor, pi

# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(pi)

# a = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * pi * a, 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(2563124656)))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, 'seconds')

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'sec.')

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, 'sec.')


# Функции
# a = 2
#
#
# def hello(name, word):
#     print("Hello, ", name, ". Say ", word, sep='')
#
#
# hello("Dmitriy", "hi")
# hello("Irina", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
# print((a + b) * (count // 2) + a * (count % 2))
# for i in range(count):
#     if i % 2 == 0:
#         print(a, end="")
#     else:
#         print(b, end="")
# print()
# print("".join([a if i % 2 == 0 else b for i in range(count)]))


# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print(a + b)
#     return
#
#
# x = 2
# y = 5
# get_sum(x, y)


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print('Этот пароль надёжный')
# else:
#     print('Этот пароль ненадёжный')


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
# lst[0], lst[-1] = lst[-1], lst[0]
# end = lst.pop()
# start = lst.pop(0)
# lst.insert(0, end)
# lst.append(start)
# return lst
#     return [lst[-1]] + lst[1:-1] + [lst[0]]
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5))

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма чётных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечётных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info('Igor', age=23, name="Ira")

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))


# s = 'Hello'
# print(id(s))
# s += 'World'
# print(s)
# print(id(s))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(type(a))
# b = tuple(a)
# print(type(b))
# print(b)

# t = (2,)
# print(type(t))
# print(t)

# t = tuple('Hello')
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input('-> ')
# print(tuple(s))

# from random import randint
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('Hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
#
# print(t3.index('a'))

# for i in t3:
#     print(i, end="")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if num not in tup:
#         return tuple()
#     first = tup.index(num)
#     if num not in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]

# from random import randint
#
#
# def tpl_sum(a, b):
#     return tuple(randint(a, b) for i in range(12))
#
#
# t1 = tpl_sum(0, 5)
# # t1 = tuple(randint(0, 5) for i in range(12))
# print(t1)
# t2 = tpl_sum(-5, 0)
# # t2 = tuple(randint(-5, 0) for i in range(12))
# t3 = t1 + t2
# print(t3)
# print(t3.count(0))

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# print(id(a))
# a = 6
# # print(a == b)
# # print(a is b)
#
# print(id(a))


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))


# s = True
# print(id(s))
# s = True
# print(s)
# print(id(s))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple([1, 2, 3, 4, 5])
# print(type(b))
# print(b)

# t = (2,)
# print(type(t))
# print(t)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input("-> ")
# print(tuple(s))
# from random import randint
#
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
#
# print(t3.index('l', 4))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if num not in tup:
#         return tuple()
#     first = tup.index(num)
#     if num not in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint


# def tpl_sum(t1, t2):
#     print(t1)
#     print(t2)
#     print(t1 + t2, (t1 + t2).count(0))
#
#
# tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))

# def tpl_sum(a, b):
#     return tuple(randint(a, b) for _ in range(12))
#
#
# t1 = tpl_sum(0, 5)
# t1 = tuple(randint(0, 5) for i in range(12))
# tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
# print(t1)
# t2 = tpl_sum(-5, 0)
# t2 = tuple(randint(-5, 0) for j in range(12))
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3.count(0))

# ======================

# point = (10, 20)
#
# match point:
#     case (0, 0):
#         print('Точка находится в координатах 0:0')
#     case (x, y):
#         print('Точка находится в координате', x, 'по оси Х и в координате', y, 'по оси Y')
#     case (x, 0):
#         print('Точка находится в координате', x, 'по оси Х и в координате 0 по оси Y')
#     case (0, y):
#         print('Точка находится в координате 0 по оси X и в координате', y, 'по оси Y')
#     case _:
#         print('Это не координаты точки')


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print('t = ', t.__sizeof__())
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print('t = ', t.__sizeof__())
# print(t, id(t))


# a = [1, 2]
# print(a.__sizeof__())
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b.__sizeof__())

# Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# name1, age1, married1 = get_user()
# user = get_user()
# name1, age1, married1 = user
# print(name1, age1, married1)
# print(user[0])

# a = (1, 2)
# del a[0]
# print(a)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население:", cityPopulation)


# set() - множество

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = {x for x in numbers if x % 2 == 0}
# print(s)

# def to_set():
#     a = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]

# def to_set(par):
#     return set(par), len(set(par))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# s = {'banana', 'apple', 'orange'}
# print(s)
# # s.add(4)  # добавляет элемент во множество
# # if 44 in s:
# #     s.remove(44)  # удаляется элемент по значению
# # s.discard(4)  # удаляется элемент по значению без генерации исключения
# s.pop()  # удаление первого элемента
# s.clear()  # полная очистка множества
# print(s)


# Операции над множествами
# a = {0, 1, 2, 3, 4}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # a |= b
# # a &= b
# # c = b - a
# # c = a ^ b
# c = a >= b
# print(c)
# # print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = 'Hello'
# s2 = 'How are you'
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=' ')

# s1 = 'Python'
# s2 = 'Programming language'
# print(set(s1).difference(s2))

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# both_hobby = drawing & music
# print(both_hobby)
# one_hobby = drawing ^ music
# print(one_hobby)
# drawing = drawing - both_hobby
# print(drawing)

# ==============================
# frozenset()

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({'hello', 'world'})
# print(s1)


# Словарь (dict)

# a = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a[0])
# print(d['one'])

# d = {'one': 1, 'two': 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))

# a = [
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@mail.com', 'Anna'),
# ]
# b = dict(a)
# print(b)

# d = {i: i ** 2 for i in range(2, 7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)


# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print('one1' in d)
# key = 'one'
# # if key in d:
# #     del d[key]
# # print(d['one1'])
# try:
#     del d[key]
# except KeyError:
#     print('Элемента с ключом' + key + 'нет в словаре')

# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
#
# for key in d:
#     print(key, '-> ', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input('Какой элемент исключить: '))
# del d[dislike]  # d['1']
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по', goods[i][2], 'руб', sep='')

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('f', 'Такого ключа не существует')  # Получить значение по заданному ключу
# print(value)
# n = d.keys()  # список ключей
# print(n)
# n = d.values()  # список значений
# print(n)
# n = d.items()  # список кортежей ключ + значение
# print(n)
#
# for i, j in d.items():
#     print(i, '->', j)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()  # создание копии словаря
# print('D =', d)
# print('D2 =', d)
#
# d['b'] = 5
# d2['e'] = 7
#
# print('D =', d)
# print('D2 =', d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')  # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)
# item = d.setdefault('f', 5)  # добавляет ключ со значением по умолчанию, если ключа не существует
# print(item)
# print(d)

# d.update({'a': 20, 'w': 10})  # обновление словаря
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# # new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# # new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# # print(d)
# # print(new_d)
#
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five',
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4738, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3908, 'S': 3645, 'E': 8821, 'W': 2451},
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# sales[person][region] = new_data
# print(sales[person])

# ========================

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({k: v for k, v in d.items() if v <= 2})

# value = int(input('=> '))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.values())
# print(value)
# value = list(d.keys())
# print(value)
# value = list(d.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['one'] = []
#         s = i  # s = 'one'
#     else:
#         d[s].append(i)  # d['one']
#
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(a, b))
# print(d)

# b = [12, 1, 2]
# d = list(zip(b))
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
#
# d = list(zip(a, b, c))
# print(d)

# one = {'name': 'Igor', 'Last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'Last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# data = ['a', 'b', 'c', 'd']

# for i in data:
#     print(i, end=' ')
# print()
# for i in range(len(data)):
#     print(i, end=' ')
# print()
# j = 0
#
# for i in data:
#     print(j, ':', i)
#     j += 1

# for j, i in enumerate(data, 1):
#     print(j, ':', i)
# for i in enumerate(data, 1):
#     print(i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, i in enumerate(n, 100):
#     print(j, ':', i, '->', n[i])


# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)

# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())

# def to_dict(*lst):
#     print(type(*lst))
#     print(lst)
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ',avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))

# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(2, 3))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print('Student Name:', student, end=', scores: ')
#     a, b = None, ''
#     for score in scores:
#         a = str(score) + ', '
#         b += a
#     print(b[:-2])
#
#
# print_scores('Kate', 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)


# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def funk(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or only_add and i % 2:
#             res.append(reverse_num(i))
#     return res
#
#
# print(funk(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(funk(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def funk(**kwargs):
#     return kwargs
#
#
# print(funk(a=1, b=2, c=3))
# print(funk())
# print(funk(a='python'))

# def funk(**date):
#     for key, value in date.items():
#         print(key, 'is', value)
#     print()
#
#
# funk(name='Irina', surname='Sharma', age=22, phone=9456413146)
# funk(name='Igor', surname='Wood', email='igor@mail.ru', country='Russia', age=25, phone=5465121313146)


# def funk(**kwargs):
# for key, value in kwargs.items():
#     my_dict[key] = value
# return my_dict
#     my_dict.update(**kwargs)
#
#
# my_dict = {'one': "first"}
# funk(k1=22, k2=31, k3=11, k4=91)
# print(my_dict)

# def func(a, *args, b=2, **data):
#     print(a, args, data, b)
#
#
# func(4, 5, 6, 7, b=3, k1=22, k2=31, k3=11, k4=91)


# Область видимости (score)

# name = 'Tom'  # глобальная переменная
# surname = 'Greefin'
#
#
# def hi():
#     global name, surname
#     name = 'Sam'  # локальная переменная
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print("Good bye", name, surname)
#
#
# print(name)
# hi()
# bye()


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 5
#
#
# def add_two(a):
#     # x = 2
#
#     def add_sum():
#         # x = 3
#         return a + x
#
#     return add_sum()
#
#
# print(add_two(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# max = [8, 6, 5, 3, 4, 9, 7]
# print(min(max))
#
# a = [7, 8, 9, 5]
# print(max(a))


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30 = 55
# print(z)  # 25 + 35 = 60


# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()
# print(x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))
# print(add(20))
#
# add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0  # 3  2
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)  # 3
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(90, 100)
# B = classifier(70, 90)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# print(obj1())


# lambda (Анонимные выражения)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
#
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
#
# print(func(1, 2, 3, 4, 5, 6, 7))
# print(func())


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
# inc1 = (lambda n: lambda x: n + x)
#
# f3 = inc1(42)
# print(f3(3))
#
#
# print('!!!', (lambda n: lambda x: n + x)(42)(3))
#
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap
#
#
# f1 = inc2(42)
# print(f(3))

# ===================

# print((lambda a: lambda b: lambda c: a + b + c)(2)(3)(4))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семёнов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[1](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[3]()

# m = lambda a, b: a if a > b else b
# print(m(2, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 8, 5))


# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
#
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), l1, l2))
# print(res)


# GitHub

# filter(func, iterable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 89, 13, 46, 79, 47]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# lst = [randint(1, 50) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)


# lst = [45, 55, 60, 37, 100, 105, 220]
# lst2 = list(filter(lambda x: x % 15 == 0, lst))
# print(lst2)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # [1, 3, 5, 7, 9]
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name('Ирина', 'Назарова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)


# print_full_name('Ирина', 'Назарова')
# print()
# print_full_name_1('Виктор', second='Фёдорович', last='Назаров')


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             print(f_args[2])
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некорректный тип данных!', f_args[i])  # print('Некорректный тип данных!')
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('Некорректный тип данных!', f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def type_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def type_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(type_fn(3, 4, 5))
# # print(type_fn(3, 4, "Doge"))
# print(type_fn2("Hello", 'world', "!"))
# print(type_fn3("Hello", 'world', z=5))


# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world('world!')
# hello_world2('Hi!')

# print('Hi')
# a = 10


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 10))
# print(int('100', 16))

# print(bin(18))
# print(oct(18))
# print(hex(18))

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print('y' in e)

# s = 'Python'
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_char_to_str(s, c_old, c_new):
#     s2 = ''
#     for i in range(len(s)):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#     return s2
#
#
# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, 'N', 'P')
# print(str1)
# print(str2)

# print(u'Привет')
# print('Привет')

# print(r'C:\folder\file.txt')
# print(r'C:\folder\\'[:-1])

# from math import pi
#
# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}. Мне {age} лет.')
# print(f'Значение числа pi: {round(pi, 2)}')
# print(f'Значение числа pi: {pi:.2f}')
#
# x = 5
# y = 10
# print(f"{x} * {y} / 2 = {x * y / 2}")
# print(f'{x = }, {y = }')

# a = 74
# print(f'{{{{{a}}}}}')


# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr'home\{dir_name}\{file_name}')

# s = """<div>
#     <p>Текст</p>
# </div>
# """
# print(s)
#
# a = "Hello"
# print(a)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
#
# print(square.__doc__)
# print(sum.__doc__)
# print(list.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))  # 97

# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print('ASCII коды', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# # if arr[-1] in arr[:-1]:
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(33))
# print(chr(8364))

# a = 122
# b = 97
# if a > b:
#     a, b = b, a
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))
# print(ord('A'))

# arr = ['red', 'blue', 'yellow']
# arr.sort()
# print(arr)

# from random import randint
#
#
# def random_password():
#     rand_len = randint(6, 16)
#     res = ''
#
#     for i in range(rand_len):
#         rand_char = chr(randint(33, 126))
#         res += rand_char
#     return res
#
#
# print('Ваш случайный пароль:', random_password())


# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())

# print(s.count("h", 0, -4))
#
# print(s.find('e1'))  # ищет в строке заданную подстроку (возвращает '-1' - если подстрока не найдена)
#
# print(s.rfind('e'))
# print(s.index('e1'))  # ищет в строке заданную подстроку
# print(s.rindex('e'))

# s = 'один два'
# s = s[s.find(' ') + 1:] + ' ' + s[:s.find(' ')]
# print(s)

# s = 'ab12c59p7dq'
# d = list(filter(lambda x: '0' <= x <= '9', s))
# print(d)

# s = 'ab12c59p7dq'
# digits = []
# for ch in s:
#     if '0123456789'.find(ch) != -1:
#         digits.append(int(ch))
# print(digits)

# print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# print('abc123!'.isalnum())
#
# print('ABCcbf'.isalpha())
# print('ABCcbf1'.isalpha())
#
# print('123'.isdigit())
# print('123#a'.isdigit())

# print('py'.center(10, "-"))
# print('py'.center(2))
# print("     py".lstrip())
# print("py     ".rstrip())
# print("     py     ".strip())

# print('http://www.python.org'.lstrip('/:pths'))
# print("py.$$$".rstrip(";$."))
# print('https://www.python.orgw'.strip('/:pthsorg.w'))
# print('https://www.python.orgw'.lstrip('/:pths').rstrip('org.w'))

# s = 'hello, WORLD! I am learning Python.'
#
# print(s.startswith("I am", 14))
# print(s.endswith("on."))

# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", 'Python', 2))

# st = r"Замените в этой строке все пОявления буквы 'О', крОме первого и пОследнегО вхождения."
# a = st[:st.find('о') + 1]
# b = st[st.find('о') + 1: st.rfind('о')]
# c = st[st.rfind('о'):]
# print(a + b.replace("о", "О") + c)
# print(st.replace("о", "О"))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
# print("..".join(['1', '99']))
# print(":".join("Hello"))

# print("Строка разделённая пробелами".split())
# print("www.python.org.ru".split(".", 2))
# print("www.python.org.ru".rsplit(".", 2))

# a = input("-> ").split()
# a = list(map(int, a))
# print(a)

# a = input("Введите ФИО: ").split()
# print(f'{a[0]} {a[1][0]}.{a[2][0]}.')


# Регулярные выражения

import re

# print(dir(re))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'Я ищу'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # возвращает первый найденный элемент по шаблону
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # возвращает первый найденный элемент по шаблону с начала строки
#
# reg = r'\.'
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = "Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта. [98_75] Hello"
# reg = r'[А-яЁё.\[\]-]'
# reg = r'.[^2]'
# print(re.findall(reg, s))
# print(ord('Е'))
# print(ord('Ё'))

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# rg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(rg, s1))

# reg = r'20*'
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0012, 0.3"
# print(re.findall(r'[+-]?[\d.]+', d))

# d = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"#.*", "", d))
# print('Дата рождения:', re.sub('-', '.', re.sub(r'\s#.*', '', d)))

# d = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r'\w+\s*=\s*\w+\s*[\w.]+'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, d))

# s1 = "12 сентября 2023 года 235682"
# reg = r'\d{2,4}'
# print(re.findall(reg, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# print(re.findall(r'\+?7\d{10}', s))

# reg = r'^\w+\s\w+'
# reg = r'\w+$'
# print(re.findall(reg, s))

# s = 'Hello, Привет^'
# reg = r'[A-zА-я]'
# print(re.findall(reg, s))
# print(ord('Я'))
# print(ord('а'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '12 + й', re.A))

# text = 'hello world'
# print(re.findall(r'\w+', text, re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта."
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one$', text, flags=re.MULTILINE))

# print(re.findall("""
# [a-z.-]+
# @
# [a-z.-]+
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# def valid_name(name):
#     return re.findall('^[a-z0-9_-]{3,16}$', name, re.I)
#
#
# print(valid_name("Python_master"))
# print(valid_name("Pyt"))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))

# *, +, ?, {,} - greedy - жадные квантификаторы
# *?, +?, ??, {m,n}?, {,n}?, {m,}? - lazy - ленивые квантификаторы

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = '<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий'
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r"\w+\s*=\s*\d+[.\w]*"
# # reg = r"(?:int|double)\s*=\s*\d+[.\w]*"
# # reg = r"(int|double)\s*=\s*(\d+[.\w]*)"
# reg = r"((int|double)\s*=\s*(\d+[.\w]*))"
# print(re.findall(reg, s))

# () - сохраняющие скобки
# (?:) - несохраняющие скобки

# s = '127.0.0.1'
# s = '192.168.255.255'
# # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# reg = r'(?:\d{1,3}\.){3}\d{1,3}'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())

# s = "Word2016, PS6, AI5"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = input('Введите дату: ')
# reg = r'([0-3][0-9])-([0-1][0-9])-([1-2][0-9][0-9][0-9])'
# print(re.findall(reg, s))

# s = input('Введите дату в формате dd-mm-YYYY: ')
# print(s)
# reg = r'(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20\d{2})'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображение <img alt='картинка' src =\'bg.jpg\'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))


# (?P<name>...)  (?P=name)

# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022."  # 24.10.2022
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"  # http://yandex.ru and http://yandex.com
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))


# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=> ", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9 +
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 3 5 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):  # 254
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(18, 16))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(names)
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# count = 0
# for i in range(len(names)):
#     count += i
# print(count)

# count = 0
# for i in names:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 # for k in j:
#                 #     count += 1
#                 count += len(j)
#             else:
#                 count += 1
#     else:
#         count += 1
# print(count)

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def union(s):
#     if not s:  # len(s) == 0 s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])  # 'Adam'
#
#
# print(union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # HelloWorld! + ""
#
#
# print(remove(" Hello\tWorld! "))


# Линейный (последовательный) поиск
from random import randint
import time

#
#
# def seq_search(s, item):
#     found = False
#     pos = 0
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# print(seq_search(lst, 0))
# res = time.monotonic() - start
# print(round(res, 3), 'sec')
# # lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# # print(seq_search(lst, 32))
# # print(seq_search(lst, 3))
#
#
# def seq_search(s, item):
#     found = False
#     pos = 0
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# # lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst = [randint(1, 99) for y in range(10000)]
# lst.sort()
# start = time.monotonic()
# # print(lst)
# # print(seq_search(lst, 32))
# # print(seq_search(lst, 3))
# print(seq_search(lst, 0))
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# Бинарный поиск

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1  # 3
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 4  # 1
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:  # 1 < 13
#                 last = midpoint - 1  # 3
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst.sort()
# print(binary_search(lst, 17))
# print(binary_search(lst, 3))


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         #     print(*array)
#         # print('=' * 50)
#
#
# lst = [randint(1, 99) for y in range(10000)]
# start = time.monotonic()
# # print(lst)
# bubble(lst)
# # print(lst)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# def merge_sort(a):
#     n = len(a)  # 5
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])  # [8, 2]
#     right = merge_sort(a[n // 2: n])  # [6, 4, 5]
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# # array = [8, 2, 6, 4, 5]
# array = [randint(1, 99) for y in range(10000)]
# start = time.monotonic()
# # print(array)
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# Сортировка Шелла

# def shell_sort(s):  # [10, 21, 9, 14, 67, 44, 26, 87]
#     gap = len(a)  # 4
#
#     while gap > 0:
#         for val in range(gap, len(s)):  # range(4, 8)
#             cur_val = s[val]  # s[4] = 67
#             pos = val  # 4
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2  # 4
#     return s
#
#
# a = [10, 21, 9, 14, 67, 44, 26, 87]
# print(a)
# shell_sort(a)
# print(a)


# Быстрая сортировка

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]  # a[(7 - 1) // 2] = 3 = a[3] = 4
#
#         low = [i for i in a if i < x]  # [-3, -8]
#         eq = [i for i in a if i == x]  # [4]
#         hi = [i for i in a if i > x]  # [9, 5, 7, 8]
#         a = quick_sort(low) + eq + quick_sort(hi)
#
#     return a
#
#
# lst = [9, 5, -3, 4, 7, 8, -8]
# print(lst)
# lst = quick_sort(lst)
# print(lst)


# Файлы

# f = open('Text13.txt')  # mode='r'
# print(*f)
# print(f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)

# f = open('Text13.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('new13.txt')
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# print(f.readlines(16))
# print(f.readlines())
# f.close()


# f = open('new13.txt')
# for line in f:
#     print(line)
# f.close()

# f = open('new13.txt')
# print(len(f.readlines()))
# f.close()

# f = open('new13.txt', 'a')
# f.write('New text.')
# f.close()

# f = open('new13.txt', 'w')
# f.write('Hello\nWorld!\n')
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i ** 5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# my_file = open('text23.txt', 'w')
# my_file.writelines('Заменить строку в текстовом файле;\nизменить строку в списке;\nзаписать список в файл')
# my_file.close()
#
# my_file = open('text23.txt', 'r')
# read_file = my_file.readlines()
# print(read_file)
# read_file[1] = "Hello World!\n"
# print(read_file)
# my_file.close()
#
# my_file = open('text23.txt', 'w')
# my_file.writelines(read_file)
# my_file.close()

# my_file = open('text23.txt', 'w')
# my_file.writelines('Заменить строку в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# my_file.close()
#
# my_file = open('text23.txt', 'r')
# read_file = my_file.readlines()
# my_file.close()
#
# request = int(input('Укажите индекс строки, которую нужно удалить: '))
# read_file.pop(request - 1)
#
# my_file = open('text2.txt', 'w')
# my_file.write('\n'.join([*read_file]))
# my_file.close()

# my_file = open('text2.txt', 'w')
# my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# my_file.close()
#
# my_file = open('text2.txt', 'r')
# lst = my_file.readlines()
# my_file.close()
#
# print(lst)
# num = int(input('Номер строки для удаления: '))
# lst.pop(num - 1)
# print(lst)
#
# my_file = open('text2.txt', 'w')
# my_file.write(''.join([*lst]))
# my_file.close()

# f = open('text13.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text13.txt', 'w+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('text13.txt', 'w+') as f:
#     print(f.write('12345\n67890'))
#
# with open('text13.txt', 'r') as f:
#     for line in f:
#         print(line)


# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
# print(list(map(str, lst)))
#
# with open(file_name, 'w+') as my_file:
#     my_file.write('\t'.join(map(str, lst)))

# with open(file_name, 'r+') as my_file:
#     new_lst = my_file.read().split('\t')
#
# print(len(new_lst))
# print(list(map(float, new_lst)))
# print(f'Sum = {sum(map(float, new_lst))}')


# def longest_word(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         print(w)
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_word('text23.txt'))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


# Модуль OS или OS.PATH

import os
import os.path


# print(os.getcwd())  # текущая директория

# print(os.listdir())  # список директорий и файлов по указанному пути
# print(os.listdir('../..'))

# os.mkdir("folder/new")  # создать папку

# os.makedirs("nested1/nested2/nested3")  # создает не только конечную директорию, но и промежуточные папки

# os.remove('xyz.txt')  # удаление файла

# os.rmdir("folder")  # удаление пустой папки

# os.rename('nested1', 'test')  # переименование папки и файлов
# os.rename('two.txt', 'test/test1.txt')
# os.renames('text2.txt', 'text/test3.txt')  # переименовывает папки и файлы, создавая промежуточные траектории

# for root, dirs, files in os.walk('test', topdown=False):
#     print("Root:", root)
#     print("Sub_dirs:", dirs)
#     print("Files:", files)


# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#     print('-' * 50)
#
#
# remove_empty_dirs('test')

# print(os.path.split(r'F:\python projects\test\nested2\nested3'))  # разбивает путь на кортеж (head, tail)
#
# print(os.path.dirname(r'F:\python projects\test\nested2\nested3'))
# print(os.path.basename(r'F:\python projects\test\nested2\nested3'))

# print(os.path.join(r'F:\python projects', 'test', 'nested2', 'text1.txt'))  # соединяет один или несколько компонентов
# # пути с учётом особенности OS

# print(os.path.exists(r'F:\python projects\test\nested2\nested3'))  # возвращает True, если указанный путь существует

# import time
#
# path = r'F:\python projects\text'
# print(os.path.getsize(path) // 1024)
# print(os.path.getmtime(path))  # последнее изменение файла
# print(os.path.getatime(path))  # последний доступ файла
# print(os.path.getctime(path))  # создание файла
#
# t = time.strftime('%d.%m.%Y, %H:%M:%S')
# print(t)


# read1_file = 'one.txt'
# read2_file = 'two.txt'
# write_file = 'three.txt'
#
# with open(read1_file, 'r') as fr, open(read2_file, 'r') as fw, open(write_file, 'w') as f:
#     l1 = fr.readlines()
#     l2 = fw.readlines()
#     print(l1 + l2)
#
#     f.writelines(l1 + l2)


# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вниз"}')
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print("-" * 50)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)

# import time
# file_path = r'Work\F2\F21\f212.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dirs}) - время последнего доступа к файлу: {time.strftime("%d.%m.%Y, %H:%M:%S")}')
# else:
#     print(f'Файл {file_path} не существует!')

# print(os.path.isfile(r'D:\Python214\214\test\nested12\text.txt'))
# print(os.path.isdir(r'D:\Python214\214\test\nested12\text.txt'))

# dir_name = 'Work'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(type(p1))
# print(dir(Point))
# print(Point.__doc__)

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# Point.x = 100
# p1.x = 20
# p1.y = 30
# print(p1.x, p1.y)
#
# p2 = Point()
# print(p2.x, p2.y)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)

# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
# p2 = Point()
# # p2.x = 100
# # p2.y = 200
# p2.set_coord(100, 200)


# class Human:
#     name = "name"
#     birth = "00.00.0000"
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f'Имя: {self.name}\nДата рождения: {self.birth}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print("=" * 40)
#
#     def input_info(self, first, birthday, phone, country, city, address):
#         self.name = first
#         self.birth = birthday
#         self.country = country
#         self.phone = phone
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, val):
#         self.birth = val
#
#     def get_birthday(self):
#         return self.birth
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
#
# h1.set_name("Оля")
# print(h1.get_name())
# h1.set_birthday("26.03.1989")
# print(h1.get_birthday())
# h1.set_country("Германия")
# print(h1.get_country())
# h1.set_phone("11-22-33")
# print(h1.get_phone())
# h1.set_city("Гессен")
# print(h1.get_city())
# h1.set_address("Липпенштрассе, 5")
# print(h1.get_address())


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p1.add_skill(2)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print("Экземпляр класса создан!")
#
#     def __del__(self):
#         print("Экземпляр класса удалён!")
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# # del p1
# p1 = 5
# print(p1.__dict__)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(20, 40)
# print(Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота: {self.name}')
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print(f"Работающих роботов осталось {Robot.k}")
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# droid3 = Robot("TP-4PO")
# droid3.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n\n"
#       "Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
# del droid3
# print(f'Численность роботов: {Robot.k}')


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата должна быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(12, 30.8)
# p1.set_x(15)
# p1.set_y(56.4)
# print(p1.get_x(), p1.get_y())
# print(p1.get_coord())
# p1._Point__x = 30
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.y = "abc"
# print(p1.__dict__)
#
# p2 = Point(3, 7)
# print(p2.__dict__)

# import math


# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = self.__width = 0
#         if Rectangle.__check_value(length) and Rectangle.__check_value(width):
#             self.__length = length
#             self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_width(9)
# a.set_length(3)
# print("Длина прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimeter())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.get_draw()


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# # print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __get_x(self):
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# # p1.set_x(15)
# # print(p1.get_x())
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# del p1.old
# print(p1.__dict__)
# p1.new_name = "Vasya"
# print(p1.new_name)
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")


# class Count:
#     def __init__(self, x, y, z, c):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.c = c
#
#     @staticmethod
#     def minimum(x, y, z, c):
#         return min(x, y, z, c)
#
#     @staticmethod
#     def maximum(x, y, z, c):
#         return max(x, y, z, c)
#
#     @staticmethod
#     def factorial(x):
#         count = 1
#         for i in range(2, x + 1):
#             count *= i
#         return count
#
#     @staticmethod
#     def summa(*args):
#         return sum(args) / len(args)
#
#
# print(Count.minimum(3, 5, 7, 9))
# print(Count.factorial(5))

# import math
#
#
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         Area.count += 1
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print(f'Площадь треугольника по формуле Герона: {Area.triangle_area(3, 4, 5)}')
# print(f'Площадь треугольника через основание и высоту: {Area.triangle_area2(3, 5)}')
# print(f'Площадь квадрата: {Area.square_area(3)}')
# print(f'Площадь прямоугольника: {Area.rect_area(3, 4)}')
# print(Area.get_count())


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '40.01.2021',
#     '12.31.2022'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print(f'Неправильная дата или формат строки с датой.')
#
# # string_date = '23.10.2022'
# # date = Date(23, 10, 2022)
#
# date = Date.from_string('23.10.2022')
# print(date.string_to_db())
# date2 = Date.from_string('14.12.2022')
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} ,был открыт.")
#         print("*" * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}.")
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}.')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению, у Вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счёте")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_usd_rate(2)
# acc.convert_to_usd()
# acc.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# acc.withdraw_money(5000)
# print()
# acc.add_money(5000)

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[А-яё-]", fio))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 килограммов и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# # p1.fio = "Соболев Игорь Николаевич"
# print(p1.__dict__)


# Наследование

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self.sp = sp
#         self.ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор класса Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределённый инициализатор Line")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # print(line._width)
# # print(line.__dict__)
# # rect = Rect(Point(30, 40), Point(70, 90))
# # rect.draw_rect()
# line.draw_line()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float))
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int)
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self.sp = sp
#         self.ep = ep
#         self._color = color
#         self.__width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_init() and ep.is_init():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3.5, 40), Point(100.8, 200))


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.border = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.border)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.fon = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid bold")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector((1, 2, 3))
# print(v)
# print(type(v))


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата должна быть целым числом")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3, 40), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()

# Перегрузка методов


# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print("Нарисовать шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещён на е2е4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print()
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class Grandchild(Child):
#     def display2(self):
#         print("Grandchild")
#
#
# gc = Grandchild()
# gc.display2()
# gc.display1()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('outer_obj_method')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я метод вложенного класса', MyOuter.age)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name", self.name, self.lg.code)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#             self.code = "024avc"
#
#         def display(self):
#             print("Name:", self.name)
#             print("Code:", self.code)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Intern"
#
#         def display(self):
#             print("Name", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Head"
#
#         def display(self):
#             print("Name", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()


# class Out:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Out')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Inner')
#
#         class InnerClass:
#             def show(self):
#                 print('InnerClass')
#
#
# outer = Out()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# print(comp.name)
# my_os = comp.os
# my_cpu = comp.cpu
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner Of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("Инициализатор А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print("Инициализатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print("Инициализатор Pos")
#         self._ep = ep
#         self._sp = sp
#         # Style.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color, width):
#     #     Style.__init__(self, color, width)
#     #     Pos.__init__(self, sp, ep)
#
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())


# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет напечатана и сохранена в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.save_log()


# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть целым числом')
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# c3 = c1 + c2 + c4  # c3 = Clock(100 + 200)  # c3 = Clock(300) + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
# c2 += c1
# print(c2.get_format_time())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")


s1 = Student("Сергей", [5, 5, 3, 4, 5])
print(s1[3])
# print(s1.marks[2])

