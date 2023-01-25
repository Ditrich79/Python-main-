# Задание №1

# import math
#
# print('Площадь окружности радиуса 2:', (lambda r: math.pi * r ** 2)(2))
# print('Площадь прямоугольника размером 10*13:', (lambda x, y: x * y)(10, 13))
# print('Площадь трапеции для a=7, b=5, h=3:', (lambda a, b, h: ((a + b) * h) / 2)(7, 5, 3))


# Задание №2

# Вариант №1

# x = lambda a, b, c: a * b * c
# print(x(2, 5, 5))

# Вариант №2

# res = (lambda a: lambda b: lambda c: a * b * c)
# print(res(2)(5)(5))


# Задание №3

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# func1 = sorted(students, key=lambda item: item['final'])
# print(func1)
# func2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(func2)


# Задание №4

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# digit_max = max(students, key=lambda item: item['final'])
# print(digit_max)
# digit_min = min(students, key=lambda item: item['final'])
# print(digit_min)


# Задание №5

# lst = [3, 6, 8, 9, 1, 2]
# lst2 = []
# index = 0
# for i in lst:
#     lst2.append(index)
#     index += 1
#
# res = list(map(lambda x, y: x * y ** 3, lst, lst2))
# print(res)


# Задание №6

# lst = [3, 5, 7, 3, 9, 5, 7, 2]
# res1 = list(map(lambda x: x ** 2, lst))
# res2 = list(map(lambda x: x ** 3, lst))
# print(res1)
# print(res2)


# def get_factors(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     return count
#
#
# n = int(input())
#
#
# print(get_factors(n))


# def merge(list1, list2):
#     list1.extend(list2)
#     list1.sort()
#     return list1
#
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
#
# print(merge(numbers1, numbers2))

# for i in range(26):
#     print(chr(ord('A') + i), end=' ')

# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# while 'Рис' in food:
#     food.remove('Рис')
# print(food)


# def quick_merge(a):
#     return sorted([int(i) for i in range(a) for i in input().split()])
#
#
# a = int(input())
# print(*quick_merge(a))


lst = [3, 6, 8, 9, 1, 2]
print(list(map(lambda elem: elem * lst.index(elem) ** 3, lst)))
