import re

# Задание №1

pass_word = input("Введите пароль: ")
patt_pas = r'[a-zA-z\d_@-]{6,18}'
print(re.findall(patt_pas, pass_word))


# Задание №2

# Вариант №1
# text_test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# patt_date = r'[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]'
# print(re.findall(patt_date, text_test))

# Вариант №2
# text_test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# patt_date = r'[\d]+/[\d]+/[\d]+'
# print(re.findall(patt_date, text_test))
