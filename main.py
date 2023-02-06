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

s = "yandex.com and yandex.ru"  # http://yandex.ru and http://yandex.com
reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
print(re.sub(reg, r'http://\1', s))
