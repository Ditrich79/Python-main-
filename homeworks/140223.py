# Решение задачи с использованием линейного поиска и пузырьковой сортировки.

lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
main_list = []
main_list.extend(lst1)
main_list.extend(lst2)
main_list.extend(lst3)
main_list.extend(lst4)

choose = int(input(f'Выберите вид сортировки: \n1 - сортировка по убыванию \n2 - сортировка по возрастанию \n-> '))

if choose == 1:
    for i in range(len(main_list) - 1):
        for j in range(len(main_list) - 1 - i):
            if main_list[j] < main_list[j + 1]:
                main_list[j], main_list[j + 1] = main_list[j + 1], main_list[j]
    print(main_list)
elif choose == 2:
    for i in range(len(main_list) - 1):
        for j in range(len(main_list) - i - 1):
            if main_list[j] > main_list[j + 1]:
                main_list[j], main_list[j + 1] = main_list[j + 1], main_list[j]
    print(main_list)

search_digit = int(input('Введите значение для поиска: '))

count = 0
flag = False

for i in range(len(main_list)):
    if main_list[i] == search_digit:
        flag = True
        break

if flag == 1:
    print(f'Значение {search_digit} найдено.')
else:
    print('Значение не найдено.')

