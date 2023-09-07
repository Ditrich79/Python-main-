# def do_something():
#   a = 1
#   print(a)
#
# a = 0
# do_something()
# print(a)

# a = 1
#
# def do_something():
#   print(a)
#
# do_something()

# def draw_triangle():
#     for i in range(8):
#         print(' ' * (15 - 1 - i) + '*' * (1 + i * 2))
#
#
# draw_triangle()

# def get_shipping_cost(quantity):
#     cost = 1000
#     for i in range(1, quantity):
#         cost += 120
#     return cost
#
#
# n = int(input())
#
#
# print(get_shipping_cost(n))

# from math import factorial
#
# def compute_binom(n, k):
#     bnom = factorial(n) / (factorial(k) * factorial(n - k))
#     return bnom
#
#
# n = int(input())
# k = int(input())
#
#
# print(compute_binom(n, k))

# def number_to_words(num):
#     zero_to_ninety_nine = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
#                            'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
#                            'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', ' ']
#     zero_to_ninety_nine2 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
#                             'девяносто']
#     if num <= 20:
#         return zero_to_ninety_nine[num - 1]
#     else:
#         return zero_to_ninety_nine2[num // 10 - 2] + ' ' + zero_to_ninety_nine[num % 10 - 1]
#
#
# n = int(input())
#
#
# print(number_to_words(n))

# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#               'декабрь']
#
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#               'november', 'december']
#     if language == 'en':
#         return lng_en[num - 1]
#     else:
#         return lng_ru[num - 1]
#
#
# lan = input()
# num = int(input())
#
#
# print(get_month(lan, num))


# def is_magic(date):
#     s = date.split('.')
#     for i in range(len(s)):
#         s[i] = int(s[i])
#     md1 = s[2] % 100
#     md2 = s[0] * s[1]
#     if md1 == md2:
#         return True
#     else:
#         return False
#
#
# date = input()
#
#
# print(is_magic(date))

# def is_pangram(text):
#     lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#            'v', 'w', 'x', 'y', 'z']
#     text = text.replace(' ', '')
#     text = text.lower()
#     for i in lst:
#         if i not in text:
#             return False
#         return True
#
#
# text = input()
#
#
# print(is_pangram(text))

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
#
# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
#
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
# print(total / counter)

# n, m = int(input()), int(input())
#
# my_list = [[0]*m for _ in range(n)]
# print(my_list)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
#
# print(maximum + minimum)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)

# n = int(input())
# list1 = [[j for j in range(1, n + 1)] for i in range(n)]
# for row in list1:
#     print(row)

# n = int(input())
# list1 = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# for row in list1:
#     print(row)

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
#
# non_empty_tuples = [i for i in tuples if len(i) > 0]
#
# print(non_empty_tuples)

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)

# poets = [
#     ('Есенин', 13),
#     ('Тургенев', 14),
#     ('Маяковский', 28),
#     ('Лермонтов', 20),
#     ('Фет', 15)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# a = 1
# for i in numbers:
#     a *= i
# print(a)

# data = 'Python для продвинутых!'
# data_list = data.split()
# a = ''.join(data_list)
# data_tuple = tuple(a)
# print(data_tuple)

# data = 'Python для продвинутых!'
# data_tuple = tuple(data)
# print(data_tuple)

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_list = list(poet_data)
# a = poet_list.insert(2, 'Москва')
# del poet_list[3]
# poet_data = tuple(poet_list)
# print(poet_data)

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# lst = [sum(i) / len(i) for i in numbers]
# print(lst)

# a, b, c = int(input()), int(input()), int(input())
# print((-(b / (2 * a)), (((4 * a * c) - b ** 2)) / 4 / a))

# lst = [(input('name:'), int(input('score:'))) for i in range(int(input()))]
# lst2 = []
# for i in lst:
#     if i[1] > 3:
#         lst2.append(i)
#     print(*i, end='\n')
# print()
# for i in lst2:
#     print(*i, end='\n')

# lst = [tuple(input('name:').split()) for i in range(int(input()))]
# lst2 = []
# for i in lst:
#     if i[1] == '5':
#         lst2.append(i)
#     elif i[1] == '4':
#         lst2.append(i)
#     print(*i, end='\n')
# print()
# for i in lst2:
#     print(*i, end='\n')

# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3

# dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
# for item in dict1:
#     print(item, ':', dict1[item])

# a, b = float(input()), float(input())
# imt = a / (b * b)
# if imt < 18.5:
#     print('Недостаточная масса')
# elif imt > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# st = input()
# cost2 = (len(st) * 60) % 100
# cost1 = (len(st) * 60) // 100
# print(f'{cost1} р. {cost2} коп.')

# print(len(input().split()))

# year = int(input())
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь",
# "Овца"]
# ind = year % 12
# for i in range(len(animals)):
#     if i == ind:
#         print(animals[i])

# int_rever = input()
# if len(int_rever) == 5:
#     print(int(int_rever[::-1]))
# else:
#     print(int(int_rever[0] + int_rever[:-6:-1]))

# int1 = input()
# int1 = list(int1)
# for i in range(len(int1) - 3, 0, -3):
#     int1.insert(i, ',')
# print(''.join(int1))

# n, k = int(input()), int(input())  # задача Иосифа Флавия
# lst = [i for i in range(1, n + 1)]
# while len(lst) > 1:
#     for j in range(0, k - 1):
#         lst.append(lst[j])
#     del lst[:k]
# print(*lst)

# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)

# def func(num1, num2):
#     return num1 % num2 == 0
#
#
# num1, num2 = int(input()), int(input())
#
#
# if func(num1, num2):
#     print("делится")
# else:
#     print("не делится")

# rows = int(input('Введите количество колонок: '))
# cols = int(input('Введите количество столбцов: '))
# matrix = []
# for _ in range(rows):
#     lst = []
#     for _ in range(cols):
#         lst.append(input('Слово: '))
#     matrix.append(lst)
#
# for i in range(rows):
#     for y in range(cols):
#         print(matrix[i][y], end=' ')
#     print()
# print()
#
# for i in range(cols):
#     for y in range(rows):
#         print(matrix[y][i], end=' ')
#     print()

# n = int(input('Введите количество колонок: '))
# m = int(input('Введите количество столбцов: '))
#
# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i * j).ljust(3))
#     print(*mult)

# mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
# print(mult)

# n = int(input('Введите количество колонок: '))
# m = int(input('Введите количество столбцов: '))
# matrix = []
# for k in range(n):
#     aver = [int(x) for x in input().split()]
#     matrix.append(aver)
# x = 0
# y = 0
# matrix_max = matrix[0][0]
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix_max:
#             matrix_max = matrix[i][j]
#             x = i
#             y = j
# print(x, y)

# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
#
# print(row, col)

# file = open(input())
#
# print(file.read())


# file = open('lines.txt', 'r', encoding='utf-8')
# print(file.readline())
# file.close()

# file = open('numbers.txt', 'r', encoding='utf-8')
# summa = sum(list(map(int, file.readlines())))
# print(summa)
# file.close()


# file = open('nums.txt', 'r', encoding='utf-8')
# summa = sum(list(map(int, file.read().split())))
# print(summa)
# file.close()

# file = open('prices.txt')
# summa = 0
#
# for line in file.readlines():
#     arr = line.split()
#     summa += int(arr[1]) * int(arr[2])
#
# print(summa)
# file.close()

# with open('text.txt', 'r', encoding='utf-8') as file:
#     string = file.read()[::-1]
#     print(string)

# with open('data.txt') as file:
#     arr = file.readlines()
#     for i in range(len(arr)):
#         print(arr[len(arr) - 1 - i].strip())

# max_len = 0
# max_str = []
#
# with open('lines.txt') as file:
#     for line in file.readlines():
#         if len(line) > max_len:
#             max_len = len(line)
#             max_str = [line]
#         elif len(line) == max_len:
#             max_str.append(line)
#
# for elem in max_str:
#     print(elem, end='')

# n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
# print(roman_numbers[n-1] if 1 <= n <= 10 else 'ошибка')

# s = input("digits: ").split()
# print(s)
# d = list(map(int, s))
# print(d)

# import random
#
# n = int(input())
# for i in range(n):
#     if random.randint(0, i) % 2 == 0:
#         print('Орел')
#     else:
#         print('Решка')

# from random import choice
#
# n = int(input())
#
# for i in range(n):
#     print(choice([i for i in range(1, 7)]))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(fancy(3, '.'))

# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(fancy(char2='$', length=3))

# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     elif n == 1 and m is None:
#         m = 1
#     return [[value] * m for _ in range(n)]

# def f(n=3):
#     return n + 7
#
#
# print(f(f(f())))

# def sq_sum(*args):
#     return sum([i ** 2 for i in args])
#
#
# print(sq_sum(1, 2, 3))


# def mean(*args):
#     lst = [i for i in args if type(i) == int or type(i) == float]
#     return sum(lst) / len(lst)
#
#
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))

# def greet(par, *args):
#     people = ' and '.join((par,) + args)
#     return f"Hello, {people}!"
#
#
# print(greet('Timur', 'Roman', 'Ruslan'))


# def count_sheeps(*sheep):
#     count = 0
#     for i in sheep:
#         if i is True:
#             count += 1
#     return count
#
#
# print(count_sheeps(True, False, True, None, True, None, True, False, None, None, False))

# def summation(num):
#     count = 0
#     for i in range(0, num + 1):
#         count += i
#     return count
#
#
# print(summation(8))


# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a*x**2 + b*x + c
#     return square_polynom
#
#
# f = generator_square_polynom(a=1, b=2, c=1)
# print(f(2))

# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
#
# print(var1 + var2)

# def func_apply(func, args):
#     return [func(item) for item in args]
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))


# from functools import reduce
#
# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
# result = reduce(lambda x, y: x + y, obj, 0)
#
# print(result)

# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# print(list(obj))


# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
#
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# print(map_result)

# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
#
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# print(filter_result)

# from functools import reduce
# numbers = [4, 6, 9, 23, 5]
#
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
# print(reduce_result)


# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# print(func(20))

# func = lambda x: True if x[0] in 'Aa' and x[-1] in 'Aa' else False
# print(func('abcd'))

# is_non_negative_num = lambda x: set(x.replace('.', '', 1)) <= set('0123456789')
# print(is_non_negative_num('10.34ab'))

# is_num = lambda x: "-" not in x[1:] and x.replace('.', '', 1).replace("-", "").isdigit()
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# filter_words = sorted(filter(lambda word: len(word) == 6, words))
# print(*filter_words)

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
#            53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88,
#            94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x % 2 == 0 or (x % 2 != 0 and x < 47), numbers)))
# print(*res)

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# lst = []
# for num in numbers:
#     lst.append(num ** 2)
# print(sum(lst))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# new_list = sorted(fruits, reverse=True)
# print(*new_list, sep='\n')

# print(len(set(input())))

# stin = input()
# loh = set(stin)
# if len(stin) == len(loh):
#     print('YES')
# else:
#     print('NO')

# a = input()
# b = input()
# c = set(a + b)
# if len(c) == 10:
#     print('YES')
# else:
#     print('NO')

# a = set(input())
# b = set(input())
# if a == b:
#     print('YES')
# else:
#     print('NO')

# a = input().split()
# if set(a[0]) == set(a[1]) == set(a[2]):
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# for i in range(n):
#     a = set(input().lower())
#     b = len(a)
#     print(b)

# n = int(input())
# c = 0
# for i in range(n):
#     a = set(input().lower())
#     c += len(a)
# print(c)

# a = set()
# for i in range(int(input())):
#     b = input().lower()
#     for j in b:
#         a.add(j)
# print(len(a))

# import re
#
# words = re.sub(r'[.,;:-?-!]', '', input().lower())
# lst = words.split()
# s = set(lst)
# print(len(s))

# st1 = input().split()
# st2 = input().split()
# a1 = set(st1)
# a2 = set(st2)
# a3 = a1.intersection(a2)
# print(len(a3))

# st1 = set(map(int, input().split()))
# st2 = set(map(int, input().split()))
# st3 = st1 & st2
# print(*sorted(st3))

# st1 = set(map(int, input().split()))
# st2 = set(map(int, input().split()))
# st3 = st1 - st2
# print(*sorted(st3))

# list1 = [{int(dig) for dig in input()} for _ in range(int(input()))]
# set1 = set.intersection(*list1)
# print(*sorted(set1))

# st1 = {int(dig) for dig in input()}
# st2 = {int(dig) for dig in input()}
# if not st1.isdisjoint(st2):
#     print("YES")
# else:
#     print("NO")

# st1 = {int(dig) for dig in input()}
# st2 = {int(dig) for dig in input()}
# if st2.issubset(st1):
#     print("YES")
# else:
#     print("NO")

# st1 = set(map(int, input().split()))
# st2 = set(map(int, input().split()))
# st3 = set(map(int, input().split()))
# st4 = st1 & st2 - st3
# print(*sorted(st4, reverse=True))

# st1 = set(map(int, input().split()))
# st2 = set(map(int, input().split()))
# st3 = set(map(int, input().split()))
# union_set = st1 | st2 | st3
# intersection_set = st1 & st2 & st3
# haupt = union_set.difference(intersection_set)
# print(*sorted(haupt))

# s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3)))

# marks1, marks2, marks3 = [set(int(i) for i in input().split()) for _ in range(3)]
# print(*sorted(marks3 - (marks1 | marks2), reverse=True))

# marks1, marks2, marks3 = [set(int(i) for i in input().split()) for _ in range(3)]
# marks4 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(*sorted(marks4 - (marks1 | marks2 | marks3)))

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# my_set = {int(i) for i in items}
# print(*sorted(my_set))

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# my_set = {i[0].lower() for i in words}
# print(*sorted(my_set))

# from re import sub
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#     traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# stroka = sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
# spisok = stroka.lower().split()
# myset = set(spisok)
# print(*sorted(myset))

# from re import sub
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#     traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# stroka = sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
# spisok = stroka.lower().split()
# my_set = {i for i in spisok if len(i) < 4}
# print(*sorted(my_set))

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
# my_set = {i.lower() for i in files if '.png' in i.lower()}
# print(*sorted(my_set))


# def factorial(x: int) -> int:
#     count: int = 1
#     for i in range(2, x + 1):
#         count *= i
#     return count
#
#
# print(factorial(5))


# n, m, k, p = [int(input()) for i in range(4)]
# c = n - ((m + k) - p)
# print(c)


# d = input()
# a = list(d.split())
# b = set(map(int, d.split()))
# c = len(a) - len(b)
# print(c)


# cities = set(input() for _ in range(int(input())))
# new_city = input()
# if new_city not in cities:
#     print('OK')
# else:
#     print('REPEAT')

# m, n = int(input()), int(input())
# home_lib = {input() for _ in range(m)}
# for i in range(n):
#     if input() in home_lib:
#         print('YES')
#     else:
#         print('NO')

# sheet1 = set(map(int, input().split()))
# sheet2 = set(map(int, input().split()))
# sheet3 = sheet1 & sheet2
# if len(sheet3) > 0:
#     print(*sorted(sheet3, reverse=True))
# else:
#     print('BAD DAY')

# proof1 = set(map(int, input().split()))
# proof2 = set(map(int, input().split()))
# if proof1 == proof2:
#     print('YES')
# else:
#     print('NO')

# m, n = int(input()), int(input())
# students_math = {input() for _ in range(m)}
# students_inf = {input() for _ in range(n)}
# total = students_math - students_inf
# print(len(total))

# m, n = int(input()), int(input())
# students_math = {input() for _ in range(m)}
# students_inf = {input() for _ in range(n)}
# total = students_math ^ students_inf
# print('NO' if len(total) == 0 else len(total))

# list_of_dir = set(i for i in input().split())
# list_of_helper = set(i for i in input().split())
# list_of_main = list_of_dir | list_of_helper
# print(*sorted(list_of_main))

# m, n = int(input()), int(input())
# list_of_students = [input() for _ in range(m+n)]
# set_of_students = set(list_of_students)
# total = len(list_of_students) - len(set_of_students)
# if len(set_of_students) - total == 0:
#     print('NO')
# else:
#     print(len(set_of_students) - total)

# n = int(input())
# total = {input() for _ in range(int(input()))}
#
# for _ in range(n - 1):
#     total &= {input() for _ in range(int(input()))}
#
# print(*sorted(total), sep='\n')

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# users2 = []
# for i in users:
#     if i['phone'][-1] == '8':
#         users2.append(i['name'])
# print(*sorted(users2))
#
# print(*sorted([x['name'] for x in users if x['phone'][-1] == '8']))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# users2 = []
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         users2.append(i['name'])
# print(*sorted(users2))

# di_ct = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# for i in input():
#     print(di_ct[i], end=' ')

# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
#
# a = input()
# if a in d:
#     print(f'{a}: {d[a]}')

# d = {
#     "1": [".", ",", "?", "!", ":"],
#     "2": ["A", "B", "C"],
#     "3": ["D", "E", "F"],
#     "4": ["G", "H", "I"],
#     "5": ["J", "K", "L"],
#     "6": ["M", "N", "O"],
#     "7": ["P", "Q", "R", "S"],
#     "8": ["T", "U", "V"],
#     "9": ["W", "X", "Y", "Z"],
#     "0": [" "]
# }
# string = input().upper().replace('"', '')
# for char in string:
#     for key, value in d.items():
#         if char in value:
#             print(key * (value.index(char) + 1), end='')

# def morse_dictionary():
#     letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
#     morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#              '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#              '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
#     dictionary = dict(zip(letters, morse))
#     word = input('Введите строку: ').upper()
#     for char in word:
#         for key, value in dictionary.items():
#             if char == key:
#                 print(value, end=' ')
#
#
# morse_dictionary()

# result = {}
# a = [i for i in range(1, 16)]
# b = [i ** 2 for i in range(1, 16)]
# c = dict(zip(a, b))
# result.update(c)
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
# result.update(dict1)
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for char in text:
#     result[char] = result.get(char, 0) + 1
# print(result)


# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
#     'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
#     'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana ' \
#     'melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry ' \
#     'apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana ' \
#     'grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit ' \
#     'pomegranate barley'
# lst = s.split()
# result = dict()
# result2 = dict()
# for word in lst:
#     result[word] = result.get(word, 0) + 1
# biggest_num = max(result.values())
# for key, value in result.items():
#     if value == biggest_num:
#         result2[key] = result2.get(key, value)
# print(min(result2))

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
#
# for p, *name in pets:
#     result.setdefault(tuple(name), []).append(p)
# print(result)

# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = dict()
# result2 = dict()
# for word in lst:
#     result[word] = result.get(word, 0) + 1
# min_num = min(result.values())
# for key, value in result.items():
#     if value == min_num:
#         result2[key] = result2.get(key, value)
# print(min(result2))

# lst = [w for w in input().split()]
# result = {}
# for w in lst:
#     result[w] = result.get(w, 0) + 1
# print(result)

# word = input().split()
# lst = []
# result = {}
#
# for i in word:
#     if i not in lst:
#         lst.append(i)
#     else:
#         result[i] = result.get(i, 0) + 1
#         lst.append(i + '_' + str(result[i]))
# print(*lst)

# result = {}
# for i in range(int(input())):
#     key, value = input().split(': ')
#     result[key.lower()] = value
# for j in range(int(input())):
#     word = input().lower()
#     print(result.get(word, 'Не найдено'))

# result1 = {}
# for char in input():
#     result1[char] = result1.get(char, 0) + 1
#
# result2 = {}
# for char in input():
#     result2[char] = result2.get(char, 0) + 1
#
# if result1 == result2:
#     print('YES')
# else:
#     print('NO')

# lst1 = sorted([i for i in input().lower() if i.isalpha()])
# lst2 = sorted([i for i in input().lower() if i.isalpha()])
#
# result = dict(zip(range(len(lst1)), lst1))
# result2 = dict(zip(range(len(lst2)), lst2))
#
# if result == result2:
#     print('YES')
# else:
#     print('NO')


# result = {}
# for i in range(int(input())):
#     key, value = input().split(' ')
#     result[key] = value
#
# word = input()
#
# for key, value in result.items():
#     if key == word:
#         print(value)
#     elif value == word:
#         print(key)

# result = {}
# for i in range(int(input())):
#     key, *value = input().split()
#     result[key] = value
#
# for i in range(int(input())):
#     city = input()
#     for key, value in result.items():
#         if city in value:
#             print(key)

# result = {}
# for i in range(int(input())):
#     phone, name = input().lower().split()
#     result[name] = result.get(name, []) + [phone]
#
# for i in range(int(input())):
#     names = input().lower()
#     print(*result.get(names, ['абонент не найден']))

# word = input()
# result = {}
#
# for i in range(int(input())):
#     key, value = input().split(': ')
#     result[int(value)] = key
#
# for s in word:
#     print(result[word.count(s)], end='')

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
#           'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None,
#           'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac',
#           'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {i: colors[i] for i in colors if colors[i]}
# print(result)

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {i: favorite_numbers[i] for i in favorite_numbers if 100 > favorite_numbers[i] > 10}
# print(result)

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
#           9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {key: value for value, key in months.items()}
# print(result)

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(k): v for k, v in [i.split(':') for i in s.split()]}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {i: sorted([y for y in range(1, i + 1) if i % y == 0]) for i in numbers}
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {word: [ord(i) for i in word] for word in words}
# print(result)

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
#            13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
#            24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# # result = {key: letters[key] for key in remove_keys}
# result = {key: values for key, values in letters.items() if key not in remove_keys}
# print(result)

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}
# print(result)

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {i[0]: (i[1], i[2]) for i in tuples}
# print(result)

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
#                  'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
#                  'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# # result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]
# result = [{a: {b: c}} for a, b, c in zip(student_ids, student_names, student_grades)]
# print(result)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# my_dict2 = {key: [i for i in value if i <= 20] for key, value in my_dict.items()}
# print(my_dict2)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# lst = sorted([j + "@" + key for key, value in emails.items() for j in value])
# print(*lst, sep="\n")

# DNA_RNA = {"G": "C", "C": "G", "T": "A", "A": "U"}
# result = [DNA_RNA[i] for i in input()]
# print(*result, sep="")

# st = input().split()
# result = {}
#
# for i in st:
#     result[i] = result.get(i, 0) + 1
#     print(result[i], end=' ')

# scrabble = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# word = input().upper()
# result = [key for letter in word for key, value in scrabble.items() if letter in value]
# print(sum(result))

# def build_query_string(params):
#     return '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
#
#
# print(build_query_string({'name': 'timur', 'age': 28}))

# def merge(values):      # values - это список словарей
#     solve = {}
#     for i in values:
#         for key in i:
#             solve.setdefault(key, set()).add(i[key])
#     return solve

# result = {}
# dict_operations = {'W': 'write', 'R': 'read', 'X': 'execute'}
#
# for _ in range(int(input())):
#     x = input().split()
#     result[x[0]] = [dict_operations[i] for i in x[1:]]
#
# for _ in range(int(input())):
#     x = input().split()
#     if x[0] in result[x[1]]:
#         print("OK")
#     else:
#         print("Access denied")

# result = {}
#
# for _ in range(int(input())):
#     name, product, count = input().split()
#     result.setdefault(name, {})
#     result[name][product] = result[name].get(product, 0) + int(count)
#
# for key, value in sorted(result.items()):
#     print(f"{key}:")
#     for i in sorted(value):
#         print(i, value[i])


# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get("https://avidreaders.ru/books/")
# print(res)


# import requests
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ""
#     result = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         base = self.html.find_all("div", class_="card_info")
#         for plugin in base:
#             names = plugin.find("div", class_="book_name").text
#             description = plugin.find("div", class_="dscr").text
#             author = plugin.find("a", class_="genre").text
#             rating = plugin.find("div", class_="rating_count").text
#             self.result.append({
#                 'names': names,
#                 'description': description,
#                 'author': author,
#                 'rating': rating
#             })
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()
#
#     def save(self):
#         with open(self.path, 'w') as f:
#             i = 1
#             for item in self.result:
#                 f.write(f"Книга № {i}\n\nНазвание: {item['names']}\n{'-' * 70}\nАвтор: {item['author']}\n{'-' * 70}\n"
#                         f"Описание: {item['description']}\n{'-' * 70}\nРейтинг: {item['rating']}\n\n{'*' * 70}\n")
#                 i += 1
#
#
# def main():
#     for i in range(0, 3):
#         pars = Parser(f'https://avidreaders.ru/books/{i}', 'books2.txt')
#         pars.run()
#
#
# if __name__ == '__main__':
#     main()

# p = Parser('https://avidreaders.ru/books/', 'books2.txt')
# p.parsing()


# import requests
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ""
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         p1 = self.html.find_all("div", class_="item-title 21")
#         for plugin in p1:
#             name = plugin.find("span").text
#         p2 = self.html.find_all("div", class_="item_info main_item_wrapper TYPE_1")
#         for plugin in p2:
#             price = plugin.find("button")["data-price"]
#             description = plugin.find("button")["data-text"].strip()
#         p3 = self.html.find_all("div", class_="brand")
#         for plugin in p3:
#             manuf = plugin.text.strip()
#             self.res.append({
#                 'name': name,
#                 'price': price,
#                 'description': description,
#                 'manuf': manuf
#             })
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()
#
#     def save(self):
#         with open(self.path, 'w') as f:
#             i = 1
#             for item in self.res:
#                 f.write(f"Товар № {i}\n\nНазвание: {item['name']}\nЦена: {item['price']}"
#                         f"\nОписание: {item['description']}\nПроизводитель: {item['manuf']}"
#                         f"\n\n{'*' * 40}\n")
#                 i += 1
#
#
# def main():
#     for i in range(0, 3):
#         pars = Parser(f'https://svet161.ru/catalog/svetilniki/podvesnye/?PAGEN_1={i}/', 'news2.txt')
#         pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# class Parser:
#     html = ""
#     result = {}
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def get_data(self):
#         base = self.html.find_all("div", class_="card_info")
#         for plugin in base:
#             names = plugin.find("div", class_="book_name").text
#             description = plugin.find("div", class_="dscr").text
#             author = plugin.find("a", class_="genre").text
#             rating = plugin.find("div", class_="rating_count").text
#
#             self.result = ({
#                 'names': names,
#                 'description': description,
#                 'author': author,
#                 'rating': rating
#             })
#
#     def write_csv(self):
#         with open('books.csv', 'a') as file:
#             write = csv.writer(file, delimiter=";", lineterminator="\r")
#             write.writerow((self.result['names'], self.result['author'], self.result['description'],
#                             self.result['rating']))
#
#     def run(self):
#         self.get_html()
#         self.get_data()
#         self.write_csv()
#
#
# def main():
#     pars = Parser('https://avidreaders.ru/books/', 'books2.csv')
#     pars.get_data()
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
#
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))
# print(res)


# Генератор случайного пароля
# import random
#
# length = int(input())    # длина пароля
#
# for i in range(length):
#     val = random.randint(0, 1)
#     if val == 0:
#         dig = random.randint(65, 90)
#     elif val == 1:
#         dig = random.randint(97, 122)
#     ch = chr(dig)
#     print(ch, end='')


# import random
#
# s = set()
# for i in range(7):
#     val = random.randint(1, 49)
#     s.add(val)
# print(*sorted(s))

# s = set()
#
# while len(s) < 7:
#     s.add(random.randint(1, 49))
#
# print(*sorted(s))


# import random
#
#
# def generate_ip():
#     return f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'

# import random
# import string
#
#
# def generate_index():
#     a = string.ascii_uppercase
#     st = ''.join(random.sample(a, 2))
#     st2 = ''.join(random.sample(a, 2))
#     dig = random.randint(0, 99)
#     dig2 = random.randint(0, 99)
#     return f'{st}{dig}_{dig2}{st2}'
#
#
# print(generate_index())


# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for row in matrix:
#     random.shuffle(row)


# my_cards = set()
# while len(my_cards) != 100:
#     my_cards.add(random.randint(1000000, 9999999))
#
# print(*my_cards, sep='\n')

# import random
#
# word = input()
# lst = list(word)
# random.shuffle(lst)
# lst2 = ''.join(lst)
# print(lst2)

# import random
# from string import *
#
#
# def generate_password(length):
#     letters = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
#     return ''.join(random.sample(letters, length))
#
#
# def generate_passwords(count, length):
#     return [generate_password(length) for i in range(count)]
#
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')


# import random
# import string
#
#
# def generate_password(length):
#     upper_case = [i for i in string.ascii_uppercase if i not in 'IO']
#     lower_case = [i for i in string.ascii_lowercase if i not in 'lo']
#     digits = list(string.digits[2:])
#     chars = upper_case + lower_case + digits
#
#     res = [random.choice(i) for i in (upper_case, lower_case, digits)]
#     res += [random.choice(chars) for i in range(length - 3)]
#     return ''.join(res)
#
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

# from decimal import *
# # Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он
# # вывел сумму наибольшего и наименьшего Decimal числа.
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 ' \
#     '1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 ' \
#     '0.03 9.60 8.86 2.73 5.83 6.50'
# numbers = [Decimal(i) for i in s.split()]
#
# maximum = max(numbers)
# minimum = min(numbers)
# print(minimum + maximum)

# import os
#
# os.mkdir(r"F:\python projects\movies")

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
#            (90, 1, -45, -21)]
#
#
# def compare_avg(a):
#     return sum(a) / len(a)
#
#
# print(min(numbers, key=compare_avg))
# print(max(numbers, key=compare_avg))


# def print_products(*args):
#     args = [i for i in args if type(i) is str and i != '']
#     if args:
#         for num, value in enumerate(args):
#             print(f'{num+1}) {value}')
#         return ''
#     print("Нет продуктов")
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')


# def print_products(*args):
#     counter = 0
#     for i in args:
#         if type(i) is str and i:
#             counter += 1
#             print(f'{counter}) {i}')
#     if counter == 0:
#         print("Нет продуктов")
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')


# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f'{key}: {value}')
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
#
# def get_points(x):
#     return (x[0] ** 2 + x[1] ** 2) ** 0.5
#
#
# print(sorted(points, key=get_points))


# a, b = int(input()), int(input())
# print(fr'{a}\n + \n{b}\n = \n{a + b}')

# import re

# match = re.match(input(), input())
# print(match.group(0))
# print(match.start(0))
# print(match.end(0))
# print(match.pos)
# print(match.endpos)
# print(match.re)
# print(match.string)

# words = input()
# regex = r"#[a-z]*"
# result = re.search(regex, words)
# if result:
#     print(result.group(0))


# pattern = r'[Кк]од'
#
# found = False
# for i in range(4):
#     word = re.search(pattern, input())
#     if word is not None:
#         print(f'{i + 1} {word.start()}')
#         found = True
# if not found:
#     print('код не найден')

# pattern = r'(?<=Activation.key:.)[\w]{5}-[\w]{5}-[\w]{5}-[\w]{5}-[\w]{5}'
#
# for i in range(5):
#     password = re.search(pattern, input())
#     if password:
#         print(password.group())

# pattern = r't\=[0-9\.\+]+'
# key = re.search(pattern, input())
# if key:
#     print(key.group())

# pattern = r'[A-Za-z]{1,}'
# word = re.match(pattern, input())
# if word:
#     print(f"Первое слово в предложении: {word.group()}")

# pattern = r'^([a-z]+.){12,24}'
# word = re.match(pattern, input())
# if word:
#     print("возможно, это seed-фраза")

# pattern = r'[\w]+(?=\@)'
# sentence = re.match(pattern, input())
# if sentence:
#     print(sentence.group())

# pattern = r'[\d]{13,}'
# account = re.fullmatch(pattern, input())
# if account:
#     print("True")
# else:
#     print("False")
#
# print(bool(re.fullmatch(r'\d{13,}', input())))

# print(bool(re.fullmatch(r'[A-Za-z0-9@#$%^&*()_+!?-]{8,}', input())))

# print(bool(re.fullmatch(r'\+?[0-9]+[ ]?(\()?[0-9]{3}(?(1)\)|)[ ]?[0-9]{3}(?: |-)?[0-9]{2}(?: |-)?[0-9]{2}', input())))
# print(bool(re.fullmatch(r'\+?(\d[( )-]{0,2}){11,}', input())))

# print(bool(re.fullmatch(r'(-?\d*(?:x\^\d+|x)?\+?\b)+', input())))

# pattern = r'\w+'
# word = re.finditer(pattern, input())
# for i in word:
#     print(i.group())

# pattern = r'\b\w{5}\b'
# word = re.finditer(pattern, input())
# for i in word:
#     print(i.group())

# [print(i.group()) for i in re.finditer(r'\d+\,\d+\s₽', input())]

# pattern = r'https://imgur.com/[0-9A-Za-z]{7}'
# word = re.findall(pattern, input())
# for i in word:
#     print(i)
#
# for i in re.findall(r'https://imgur.com/[a-zA-Z0-9]{7}', input()):
#     print(i)

# for res in re.findall(r'\b[a-zA-Z0-9_-]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,3}\b', input()):
#     print(res)

# for res in re.findall(r'((\d{2}(?P<n>[\./])\d{2}(?P=n)\d{4})|(\d{4}(?P<m>[\./])\d{2}(?P=m)\d{2}))', input()):
#     print(res[0])

# for i in re.findall(r'[0-1]\d\:[0-5]\d|2[0-3]\:[0-5]\d', input()):
#     print(i)

# import re

# res = re.findall(r'(?<=\<a class=\"link\" href=\")(.*?)(?=\")|(?<=\<a target=\"_blank\" href=\")(.*?)(?=\")', input())
# lst = list(map(lambda x: x[0] if len(x[0]) > 3 else x[1], res))
#
# for i in lst:
#     print(i)

# pattern = r'[.?!]'
# result = re.split(pattern, input())
# print(result)

# pattern = r'[.?!, ]'
# result = re.split(pattern, input())
# print(result)

# pattern = r'(?:Категория:\s[А-Яа-яЁё\s]+\\n)'
# result = re.split(pattern, input())
# print(result)

# pattern = r'[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]'
# replace = '!'
# result = re.sub(pattern, replace, input())
# print(result)

# pattern = r'(?:<.+?>)'
# print(re.sub(pattern, '', input()))

# sname, name, pname = input().split()
# sentence = input()
# pattern = fr'({sname}[а-яё]*\s{name[0]}\.\s{pname[0]}\.)|({sname}[а-яё]*\s{name[0:3]}[^\s]*\s{pname}[^\s]*)'
# print(re.sub(pattern, 'ФИО', sentence))
#
# f, i, o = input().split()
# print(re.sub(fr'{f}\w*\s{i[0]}.\s{o[0]}.|{f}\w*\s{i[:-1]}\w*\s{o}\w*', 'ФИО', input()))

# pattern = r'[.?!,:]'
# result = re.subn(pattern, '', input())
# print(result[1])

# pattern = r'\d'
# print(re.subn(pattern, 'X', input()))

# pattern = r'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕ' \
#           r'ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;'
# print(re.escape(pattern))

# pattern = input()
# print(re.escape(pattern))

# pattern = r'(?P<Протокол>http[s]?)+:\/\/(?P<Домен>[a-z.\d]*?)\/[a-z\/\d_-]*(?P<Параметры>\?[^# ]*)?' \
#           r'(?P<Якорь>[#][a-z]*)?'
# match = re.match(pattern, input())
# print(match.groupdict())

# regex = r'(<|</)([a-z0-9]+?.+?)>'
# result = re.findall(regex, input())
# print(result)

# lst = str(input())
# res = re.findall(r'\d([A-z\d])([A-z\d_]*)', lst)
# print(res)

# regex = r'(?i)привет'
# res = re.findall(regex, input())
# print(res)

# import re


# with open(r'F:\python projects\numbers.txt', 'r', encoding='utf-8') as file:
#     print(*map(lambda st_ng: sum(map(int, st_ng.strip().split())), file.readlines()), sep='\n')

# with open(r'F:\python projects\nums.txt', 'r', encoding='utf-8') as file:
#     count = 0
#     for line in file:
#         line.rstrip()
#         num = re.findall(r'\d+', line)
#         dig = sum(list(map(int, num)))
#         count += dig
#     print(count)

# with open('nums.txt') as f:
#     print(sum(map(int, re.findall(r'\d+', f.read()))))

# dig = [int(n) for n in input().split()]
# count = 0
# for i in range(1, len(dig)):
#     if dig[i] > dig[i - 1]:
#         count += 1
# print(count)

# dig = [int(n) for n in input().split()]
# for i in range(0, len(dig) - 1, 2):
#     dig[i], dig[i+1] = dig[i+1], dig[i]
# print(*dig)

# dig = [int(n) for n in input().split()]
# dig1 = dig[-1:] + dig[:-1]
# print(*dig1)

# dig = [int(n) for n in input().split()]
# count = 0
# for i in range(len(dig)):
#     if dig[i] != dig[i - 1]:
#         count += 1
# print(count)

# dig = [int(n) for n in input().split()]
# arr = []
# for i in range(len(dig)):
#     if dig[i] not in arr:
#         arr.append(dig[i])
# print(len(arr))


# st = input().split('О')
# count = max(map(len, st))
# print(count)


# tim_item = input()
# rus_item = input()
# if tim_item == "камень" and rus_item == "ножницы":
#     print("Тимур")
# elif tim_item == "ножницы" and rus_item == "бумага":
#     print("Тимур")
# elif tim_item == "бумага" and rus_item == "камень":
#     print("Тимур")
# elif tim_item == rus_item:
#     print("ничья")
# else:
#     print("Руслан")

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
#
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
#
# print_matrix(matrix, n, width=1)

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# count = 0
# for i in range(n):
#     matrix[i] = int(matrix[i])
#     matrix[i][i] += count
#     print(count)


# def map1(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def make_round(x):
#     return round(x, 2)
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45,
#            314.1528, 2.71828, 1.41546]
#
# print(*map1(make_round, numbers), sep='\n')


# def map1(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter1(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95,
#            1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027,
#            257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127,
#            928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496,
#            370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268,
#            1018, 1274, 387, 120, 340, 963, 832, 1127]
#
#
# def formula1(x):
#     return len(str(x)) == 3 and x % 5 == 2
#
#
# def cube(x):
#     return x ** 3
#
#
# print(*map1(cube, filter1(formula1, numbers)), sep='\n')


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23,
#            35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67,
#            62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29,
#            84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
#
# def formula(x, y):
#     return x + y ** 2
#
#
# print(reduce(formula, numbers, 0))


# def map1(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter1(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99,
#            270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201,
#            260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229,
#            60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135,
#            29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54,
#            278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263,
#            219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
#
# def formula1(x):
#     return len(str(abs(x))) == 2 and x % 7 == 0
#
#
# def formula2(x):
#     return x ** 2
#
#
# print(sum(map1(formula2, filter1(formula1, numbers))))


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
#            (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
#
# def compare_by_sum(number):
#     return number[0] + number[1] + number[2]
#
#
# print(sorted(numbers, key=compare_by_sum))


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
#            (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
#
# def sum_dig(number):
#     return max(number) + min(number)
#
#
# numbers.sort(key=sum_dig)
#
# print(numbers)


# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for i in numbers:
#     f = Fraction(i)
#     print(f"{i} = {f}")

# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 ' \
#     '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 ' \
#     '0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# s1 = s.split()
#
#
# m1 = Fraction(min(s1))
# m2 = Fraction(max(s1))
# print(m1 + m2)

# a, b = int(input()), int(input())
# print(Fraction(a, b))

# a, b = input(), input()
# print(f'{Fraction(a)} + {Fraction(b)} = {Fraction(a) + Fraction(b)}')
# print(f'{Fraction(a)} - {Fraction(b)} = {Fraction(a) - Fraction(b)}')
# print(f'{Fraction(a)} * {Fraction(b)} = {Fraction(a) * Fraction(b)}')
# print(f'{Fraction(a)} / {Fraction(b)} = {Fraction(a) / Fraction(b)}')

# word = input() + ' запретил букву'
# abv = [chr(i) for i in range(1072, 1104)]
# for char in abv:
#     if char in word:
#         print(word, char)
#         word = word.replace(char, '').replace('  ', ' ').strip()


# lst = []
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         lst.append(i)
# print(lst)

# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# for i in range(26):
#     print(chr(ord('A') + i), end=' ')

# def print_text(txt: str, n: int) -> None:
#     print(txt * n)
#
#
# print_text('Hello', 5)


# with open('words.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

# from random import randint
# dig = [str(randint(111, 777)) + '\n' for _ in range(25)]
# with open('random.txt', 'w', encoding='utf-8') as file:
#     file.writelines(dig)

# with open('input.txt', 'r') as out:
#     lst = out.readlines()
#
# with open('output.txt', 'w') as file:
#     for count, line in enumerate(lst, start=1):
#         print(count, line, sep=') ', end='', file=file)

# with open('class_scores.txt', 'r', encoding='utf-8') as file, open('new_scores.txt', 'w', encoding='utf-8') as new:
#     for line in file:
#         name, score = line.split()
#         score = int(score) + 5
#         if score > 100:
#             score = 100
#         print(name, score, file=new)


# first_quarter = 0
# second_quarter = 0
# third_quarter = 0
# fourth_quarter = 0
#
# for i in range(int(input())):
#     x, y = list(map(int, input().split()))
#     if x > 0 and y > 0:
#         first_quarter += 1
#     elif x < 0 < y:
#         second_quarter += 1
#     elif x < 0 and y < 0:
#         third_quarter += 1
#     elif y < 0 < x:
#         fourth_quarter += 1
#     elif x == 0 or y == 0:
#         continue
# print(f'Первая четверть: {first_quarter}\nВторая четверть: {second_quarter}\nТретья четверть: {third_quarter}\n'
#       f'Четвертая четверть: {fourth_quarter}')


# import re
#
# regex = r'\w*a\w*n\w*t\w*o\w*n\w*'
# lst = []
#
# for i in range(int(input())):
#     s = re.findall(regex, input())
#     if s:
#         lst.append(i + 1)
# print(*lst)


# itr = int(input())
# lst = []
# flag = "НЕТ"
# for i in range(itr):
#     lst.append(int(input()))
# num = int(input())
#
# for j in range(0, itr):
#     for k in range(0, itr):
#         if j != k:
#             if lst[k] * lst[j] == num:
#                 flag = "ДА"
#                 break
# print(flag)

# tim_item = input()
# rus_item = input()
# if tim_item == "камень" and (rus_item == "ножницы" or rus_item == "ящерица"):
#     print("Тимур")
# elif tim_item == "ножницы" and (rus_item == "бумага" or rus_item == "ящерица"):
#     print("Тимур")
# elif tim_item == "бумага" and (rus_item == "камень" or rus_item == "Спок"):
#     print("Тимур")
# elif tim_item == "ящерица" and (rus_item == "бумага" or rus_item == "Спок"):
#     print("Тимур")
# elif tim_item == "Спок" and (rus_item == "камень" or rus_item == "ножницы"):
#     print("Тимур")
# elif tim_item == rus_item:
#     print("ничья")
# else:
#     print("Руслан")


# word = input().split()
# lst = [[word[0]]]
# for i in range(1, len(word)):
#     if word[i] == word[i - 1]:
#         lst[-1].append(word[i])
#     else:
#         lst.append([word[i]])
# print(lst)


# num = int(input())
# description = {1: 'One', 2: 'Two', 3: 'Three'}
# print(description.get(num, 'Unknown'))

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for char in text:
#     result[char] = result.get(char, 0) + 1
# print(result)

# iterable = [[1], [2], [3]]
# result = list(map(len, iterable))
# print(result)

# listA = [2, 3, 4]
# listB = [3, 2, 1]
#
# result = sum(map(pow, listA, listB))
# print(result)


# words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
# words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
# words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']
#
# print(len(list(zip(words1, words2, words3))))


# from math import *
#
#
# def get_res(n, f):
#     funcs = {'квадрат': n ** 2,
#              'куб': n ** 3,
#              'корень': n ** 0.5,
#              'модуль': abs(n),
#              'синус': sin(n)}
#     return funcs[f]
#
#
# a, b = int(input()), input().lower()
# print(get_res(a, b))


# numbers = [10, 30, 20, 50, 40, 60, 70, 80]
#
# total = 0
# for index, number in enumerate(numbers, 1):
#     if index % 2 == 0:
#         total += number
# print(total)

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# result = 0
# for x, y in zip(list1, list2):
#     result += x*y
# print(result)

# num = int('100', 8)
# print(num)

# def high_order_func(func):
#     return func(5)
#
#
# def add_two(x):
#     return x + 2
#
#
# print(high_order_func(add_two))

# from random import randint
#
#
# numbers = [randint(-20, 50) for i in range(10)]
#
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
# print(result)

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# prim = list(filter(lambda x: 'primary' in x[2] and x[1] > 10000000, data))
# lst = []
# for city in prim:
#     lst.append(city[0])
# sorted_city = list(sorted(lst))
# result = ', '.join(sorted_city)
# print(f'Cities: {result}')


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
#
# data2 = list(sorted(data, key=lambda x: x[1][-1], reverse=True))
# print(*list(map(lambda x: f'{x[1]}: {x[0]}', data2)), sep='\n')


# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# data2 = list(sorted(data))
# data3 = list(sorted(data2, key=lambda x: len(x)))
#
# print(' '.join(data3))


# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
#               'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491,
#               'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643,
#               'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113,
#               1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603,
#               'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday',
#               2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159,
#               605320, 2347441]
#
# number_list = list(filter(lambda x: x if isinstance(x, int) else 0, mixed_list))
# result = max(number_list)
# print(result)


# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday',
#               76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41,
#               'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78,
#               10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14,
#               'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday',
#               'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47,
#               'able', 11]
#
# number_list = list(filter(lambda x: x if isinstance(x, int) else 0, mixed_list))
# number_list2 = sorted(number_list)
# word_list = list(filter(lambda x: x if isinstance(x, str) else 0, mixed_list))
# word_list2 = sorted(word_list)
# result = number_list2 + word_list2
# print(*result)


# print(*map(lambda x: 255 - int(x), input().split()))


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for capital, country, population in zip(capitals, countries, population):
#     print(f'{capital} is the capital of {country}, population equal {population} people.')


# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
#
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))


# print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split('.'))))


# result = [x for x in range(int(input()), int(input()))]
# print(all(map(lambda a: a != 0 and a % a == 0, result)))

# a, b = int(input()), int(input())
#
# for i in range(a, b+1):
#     digits = [int(d) for d in str(i)]
#     if all(map(lambda x: x != 0 and i % x == 0, digits)):
#         print(i, end=' ')


# word = input()
#
# print('YES' if all((any(x.isdigit() for x in word),
#                     any(x.islower() for x in word),
#                     any(x.isupper() for x in word),
#                     len(word) >= 7)) else 'NO')


# from functools import reduce
#
#
# result = lambda k, x: reduce(lambda s, a: s * x + a, k)
#
# print(result(map(int, input().split()), int(input())))


# students = []
#
# for i in range(int(input())):
#     students.append(any(['5' in input() for y in range(int(input()))]))
# print('YES' if all(students) else 'NO')


# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f"""To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!"""
#
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))


# def pretty_print(data, side='-', delimiter='|'):
#     main = delimiter + " " + f' {delimiter} '.join(map(str, data)) + " " + delimiter
#     secondary = " " + (len(main) - 2) * side + " "
#     print(secondary)
#     print(main)
#     print(secondary)
#
#
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))
#
# print(result)

# print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))


# from functools import reduce
#
# numbers = [1, 2, 3]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)


# from functools import reduce
#
# numbers = [1, 2, 3]
# result = reduce(lambda a, b: a * b, numbers, 10)
# print(result)


# def concat(*args, sep=' '):
#     return sep.join(map(str, args))
#
#
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))


# from functools import reduce
#
#
# def product_of_odds(data):
#     return reduce(lambda x, s: x * s, filter(lambda x: x % 2 == 1, data), 1)


# words = 'the world is mine take a look what you have started'.split()
#
# print(*list(map(lambda x: f'"{x}"', words)))


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
#            (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)


# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# def call(funk, *args):
#     return funk(*args)
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def compose(f, g):
#     return lambda x: f(g(x))
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# from operator import *
#
#
# def arithmetic_operation(operation):
#     result = {'+': add, '-': sub, '*': mul, '/': truediv}
#     return result[operation]
#
#
# print(add(10, 20))
# print(div(20, 5))


# print(*sorted(input().split(), key=lambda x: x.lower()))


# def gematria(word):
#     return sum(map(lambda x: ord(x.upper()) - ord('A'), word)), word
#
#
# words = [input() for i in range(int(input()))]
#
# print(*sorted(words, key=gematria), sep='\n')


# def funk(ip):
#     lst_ip = [int(i) for i in ip.split('.')]
#     return lst_ip[0] * 256 ** 3 + lst_ip[1] * 256 ** 2 + lst_ip[2] * 256 + lst_ip[3]
#
#
# print(*sorted([input() for i in range(int(input()))], key=funk), sep="\n")

# s = input().upper()
# for c in ('Аденин:', 'Гуанин:', 'Цитозин:', 'Тимин:'):
#     print(c, s.count(c[0]))

# for i in range(26):
#     print(chr(ord('A') + i), end='')

# o = {'a': 10, 'b': 10}
# n = {}
#
# for i, j in o.items():
#     n[j] = i
#
# print(n)

# d = [1, 1, 2]
# print(len(set(d)))

# dict = {{{'Socrat': 'Empty'}: {'Plato': 'A lot of material'}}: 'again'}
# key = {'Socrat': 'Empty'}
# print(dict[key]['Plato'])

# for i in 'str':
#     print(i.upper(), end='.')

# c = 'some str'
# print(c[-3:9] + " " + c[0:5])

# t_1 = (1,2,3)
# t_2 = (4,5,6)
# t_3 = t_1 + t_2
# print(t_1 < t_2)
# print(t_2 < t_3)
# print(t_1 < t_3)

# p = True
#
#
# def fun_1():
#     p = None
#
#     def fun_2():
#         global p
#         p = 'py'
#
#     fun_2()
#
# fun_1()
# print(p)

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end='')

a = 'str'
print(len(a))
