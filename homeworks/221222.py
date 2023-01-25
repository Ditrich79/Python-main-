# Задание №1

# from math import pi, sqrt
# n = int(input('Вычисление площади фигур \nВыберите фигуру=> \n1 - треугольник \n2 - прямоугольник \n3 - круг \n'
#         'Введите цифру: '))
# if n == 1:
#     a = int(input('Введите сторону a = ', ))
#     b = int(input('Введите сторону b = ', ))
#     c = int(input('Введите сторону c = ', ))
#     d = (a + b + c) / 2
#     s = sqrt(d * (d - a) * (d - b) * (d - c))
#     print('Площадь треугольника равна: ', round(s, 2))
# elif n == 2:
#     a = int(input('Введите сторону a = ', ))
#     b = int(input('Введите сторону b = ', ))
#     print('Площадь прямоугольника равна: ', round(a * b, 2))
# elif n == 3:
#     a = int(input('Введите радиус круга R = ', ))
#     print('Площадь круга равна: ', round(pi * a ** 2, 2))
# elif n <= 0 or n > 3:
#     print('Введено неверное значение')


# Задание №2

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print('\n')
# t_matrix = [[0 for x in range(len(matrix))]for y in range(len(matrix[0]))]
#
# for y in range(len(matrix)):
#     for x in range(len(matrix[0])):
#         t_matrix[x][y] = matrix[y][x]
#
# for row in t_matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# Задание №3

# from random import randint
#
# w = h = 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
# lst = [randint(0, 10) for i in range(6)]
# lst1 = lst
# lst2 = lst
# print('\n')
# print(lst)
# print('\n')
#
# matrix[0] = lst
# matrix[2] = lst1
# matrix[4] = lst2
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()


# Задание №4

from random import randint

new = []
w = h = 6
matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
for row in matrix:
    for x in row:
        print(x, end="\t")
    print()
print('\n')
matrix[0], matrix[1] = matrix[1], matrix[0]
matrix[2], matrix[3] = matrix[3], matrix[2]
matrix[4], matrix[5] = matrix[5], matrix[4]

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()
