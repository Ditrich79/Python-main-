# Задание №1

# d = {
#     'emp1': {'name': 'John', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500},
# }
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
# for i in d:
#     print(i + '\n' + 'name :', d[i]['name'] + '\n' + 'salary :', d[i]['salary'])


# Задание №2

# studs = {}
# n = int(input('Количество студентов: '))
# summa = 0
# for i in range(n):
#     names = input(str(i + 1) + "-й студент: ")
#     points = int(input("Балл: "))
#     studs[names] = points
#     summa += points
# average = summa / n
# print("\nСредний балл:", round(average), ". Студенты с баллом выше среднего:")
# for i in studs:
#     if studs[i] > average:
#         print(i)
