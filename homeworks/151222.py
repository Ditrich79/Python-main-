# Задание №1

# import random
#
# r_number = random.randrange(1, 101)
# tries = 0
# num = 0
#
# while r_number != num:
#     num = int(input("Угадайте число от 1 до 100: "))
#     if num == 0 or num > 100 or num < 0:
#         print('Вы вышли из диапазона угадываемых чисел')
#         break
#     elif num > r_number:
#         print('Загаданное число меньше')
#         tries += 1
#     elif num < r_number:
#         print('Загаданное число больше')
#         tries += 1
#     elif num == r_number:
#         tries += 1
#         print('Вы угадали загаданное число с', tries, 'раза')


# Задание №2

# a = [int(input("-> ")) for i in range(int(input('Введите количество элементов в списке: ')))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


# Задание №3

# a = [int(input("-> ")) for i in range(int(input('Введите количество элементов в списке: ')))]
# print(a)
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')


# Задание №4

# n = 8
# for i in range(n, 0, -1):
#     print('*' * i, end='')
#     print()








