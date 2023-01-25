# def average(func):
#     def wrap(*args):
#         print("Сумма чисел", str(args)[1:-1], "=", func(*args))
#         print("Среднее арифметическое чисел", str(args)[1:-1], "=", func(*args) / len(args))
#
#     return wrap
#
#
# @average
# def sum_digits(*args):
#     return sum(args)
#
#
# sum_digits(2, 5, 6, 9, 7, 4)
# print()
# sum_digits(10, 9, 8)


# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#         return True
#     else:
#         return False
#
#
# a, b, c = int(input()), int(input()), int(input())
#
#
# print(is_valid_triangle(a, b, c))


# def is_password_good(password):
#     dig = 0
#     big = 0
#     small = 0
#     if len(password) >= 8:
#         for i in password:
#             if i.isdigit():
#                 dig += 1
#             if i.isupper():
#                 big += 1
#             if i.islower():
#                 small += 1
#         if dig > 0 and big > 0 and small > 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# txt = input()
#
#
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 count += 1
#         if count == 0 or count >= 2:
#             return False
#         return True
#     return False
#
#
# txt1 = input()
# txt2 = input()
#
#
# print(is_one_away(txt1, txt2))

# a = input()
# b = a[::-1]
# if a == b:
#     print('YES')
# else:
#     print('NO')


# def is_palindrome(text):
#     text = [a.lower() for a in text if a not in (',.!?- ')]
#     return text == text[::-1]
#
#
# txt = input()
#
#
# print(is_palindrome(txt))

# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
#
#
# txt = input()
#
#
# print(is_correct_bracket(txt))

# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
#
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
#
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# from math import pi
#
#
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius ** 2
#     return c, s
#
#
# r = float(input())
#
#
# length, square = get_circle(r)
# print(length, square)

# a, b, c = float(input()), float(input()), float(input())
# d = (b ** 2) - (4 * a * c)
# x1 = (-b + d ** 0.5) / (2 * a)
# x2 = (-b - d ** 0.5) / (2 * a)
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print(-b / (2 * a))
# elif d > 0:
#     print(min(x1, x2))
#     print(max(x1, x2))


# def solve(a, b, c):
#     d = (b ** 2) - (4 * a * c)
#     a1 = (-b + d ** 0.5) / (2 * a)
#     a2 = (-b - d ** 0.5) / (2 * a)
#     if a1 > a2:
#         return a2, a1
#     else:
#         return a1, a2
#
#
# a, b, c = int(input()), int(input()), int(input())
#
#
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# from math import log2, ceil
#
# print(ceil(log2(int(input()))))

# from random import randrange
#
# m = [
#     [randrange(1, 31) for i in range(10)],
#     [randrange(1, 31) for y in range(10)],
#     [randrange(1, 31) for x in range(10)],
# ]
# print([[x for x in row] for row in m])
#
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()


