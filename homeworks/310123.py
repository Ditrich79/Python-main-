# Задание №1

# str_ing = 'I am learning Python. hello, WORLD!'
# first_ap = str_ing.find('h')
# second_ap = str_ing.rfind('h')
# slic = str_ing[first_ap:second_ap + 1]
# change = str_ing.replace(slic, '')
# print(change)


# Задание №2

# str_ing = 'I am learning Python. hello, WORLD!'
# first_ap = str_ing.find('h')
# second_ap = str_ing.rfind('h')
# slic = str_ing[first_ap + 1:second_ap]
# slic2 = slic[::-1]
# change = str_ing.replace(slic, slic2)
# print(change)


# Задание №3

# st = input('Строка: ')
# subst1 = input('Её заменяемая подстрока: ')
# subst2 = input('Новая подстрока: ')
# change = st.replace(subst1, subst2)
# print(change)


# Задание №4

st = """
Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели.
"""
st1 = st.lower()
arr = st1.split()
print('Количество слов:', (sum(map(lambda x: x.startswith('е'), arr))))

