# Задание №1

# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#008000', '#0000FF']
# d = dict(zip(a, b))
# print(d)


# Задание №2

# d = {i: i ** 3 for i in range(1, 11)}
# print(d)


# Задание №3

# lst1 = ['color', 'fruit', 'pet']
# lst2 = ['blue', 'apple', 'dog']
# d = {k: v for k, v in zip(lst1, lst2)}
# print(d)


# Задание №4

# Вариант №1

# def found_min(*args):
#     print(min(args))
#
#
# found_min(10, 9)
# found_min(2, 3, 4)
# found_min(3, 5, 10, 6)

# Вариант №2

# def found_min(*args):
#     return min(args)
#
#
# print(found_min(10, 9))
# print(found_min(2, 3, 4))
# print(found_min(3, 5, 10, 6))


# Задание №5

# def count_args(*args):
#     c = 0
#     for i in range(len(args)):
#         c += args[i]
#         print(c, end=' ')
#     print()
#
#
# count_args(3, 9, 1)
# count_args(2, 5, 4, 2)
# count_args(3, 5, 10, 6, 3)


# n = int(input())
# a = [i ** 2 for i in range(1, n + 1)]
# print(*a, sep='\n')
# print([i ** 2 for i in range(1, n + 1)])

# n = input()
# lst = n.split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
#     print(int(lst[i]) ** 3, end=' ')

# print(*input().split(), sep='\n')

# n = int(input())
# lst = list()
# for i in range(2, n + 1, 2):
#     lst.append(i)
# print(lst)

# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# c = list()
# for i in range(len(a)):
#     c.append(a[i] + b[i])
# print(*c)

# a = [int(i) for i in input().split()]
# print(*a, sep='+', end='=')
# print(sum(a))

# n = input().split("-")
# lst = [len(i) for i in n]
# if lst == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif lst == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")


# lst = [len(i) for i in input().split(' ')]
# print(max(lst))


# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(i * fill, end='')
#         print()
#     for i in range(base // 2, 0, -1):
#         print(i * fill, end='')
#         print()
#
#
# fill = input()
# base = int(input())
#
#
# draw_triangle(fill, base)


# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
#
#
# name, surname, patronymic = input(), input(), input()
#
#
# print_fio(name, surname, patronymic)

# def convert_to_miles(km):
#     result = km * 0.6214
#     return result
#
#
# num = int(input())
#
#
# print(convert_to_miles(num))


# def area_parallelepiped(a, b, c, s1):
#     s2 = 2 * (s1 + a * c + b * c)
#
#     def area_rectangle():
#         nonlocal a, b, s1
#         s1 = a * b
#         return s1
#
#     print(s2)
#     return area_rectangle()
#
#
# res = area_parallelepiped(2, 4, 6, 8)
# print(res)

# def area_parallelepiped(a, b, c):
#     s2 = a * b
#     s1 = 2 * (s2 + a * c + b * c)
#
#     def area_rectangle():
#         print(s1)
#
#     return area_rectangle()
#
#
# area_parallelepiped(2, 4, 6)
# area_parallelepiped(5, 8, 2)
# area_parallelepiped(1, 6, 8)
