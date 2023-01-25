# Задание №1

# from random import randint
#
# mas = [randint(0, 99) for i in range(10)]
# print(mas)
# a = max(mas)
# print('Max:', a)
# ind = mas.index(a)
# b = mas.pop(ind)
# mas.insert(0, b)
# print(mas)

# Задание №2

# from random import randint
#
# mas = [randint(-30, 30) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# Задание №3

# from random import randint
#
# mas = [randint(0, 99) for i in range(10)]
# print(mas)
# a = min(mas)
# print('Min:', a)
# ind = mas.index(a)
# print('Index min:', ind)
# del mas[0:ind]
# print(mas)

# n = input().lower()
# glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю' 'Ё', 'Е']
# solas = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ч', 'ш', 'щ', 'Б', 'В',
#           'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
# score = 0
# count = 0
# for i in glas:
#     score += n.count(i)
# for j in solas:
#     count += n.count(j)
# print('Количество гласных букв равно', score)
# print('Количество согласных букв равно', count)

a = input('-> ')
print(len(a))
print(a * 3)
print(a[0])
print(a[0:3])
print(a[-3:])
print(a[::-1])
print(a[1:-1])
