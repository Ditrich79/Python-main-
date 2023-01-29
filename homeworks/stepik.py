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

n, k = int(input()), int(input())  # задача Иосифа Флавия
lst = [i for i in range(1, n + 1)]
while len(lst) > 1:
    for j in range(0, k - 1):
        lst.append(lst[j])
    del lst[:k]
print(*lst)
