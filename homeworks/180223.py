# Задание №1

# Вариант 1

# my_new_file = open("new_text_18.txt", "w")
# my_new_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# my_new_file.close()
#
# my_new_file = open("new_text_18.txt", "r")
# lst_file = my_new_file.readlines()
# print(lst_file)
# pos1 = int(input("Введите номер первой строки: "))
# pos2 = int(input("Введите номер второй строки: "))
# lst_file[pos1 - 1], lst_file[pos2 - 1] = lst_file[pos2 - 1], lst_file[pos1 - 1]
# print(lst_file)
# my_new_file.close()
#
# my_new_file = open("new_text_18.txt", "w")
# my_new_file.writelines(lst_file)
# my_new_file.close()

# Вариант 2

# my_new_file = open("new_text_18.txt", "w")
# my_new_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# my_new_file.close()
#
# my_new_file = open("new_text_18.txt", "r")
# lst_file = my_new_file.readlines()
# print(lst_file)
# lst_file[1], lst_file[2] = lst_file[2], lst_file[1]
# print(lst_file)
# my_new_file.close()
#
# my_new_file = open("new_text_18.txt", "w")
# my_new_file.writelines(lst_file)
# my_new_file.close()


# Задание №2

# second_file = open("new_text2_18.txt", "w")
# second_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# second_file.close()
#
# second_file = open("new_text2_18.txt", "r")
# lst_file2 = second_file.readlines()
# print(lst_file2)
# lst = lst_file2[::-1]
# print(lst)
# second_file.close()
#
# second_file = open("new_text2_18.txt", "w")
# second_file.writelines(lst)
# second_file.close()


# Задание №3

with open('third_file.txt', 'w') as tf:
    with open('new_text_18.txt', 'r') as text:
        tf.write(text.read())
    with open('new_text2_18.txt', 'r') as text:
        tf.write(text.read())

# print(tf.closed)
# print(text.closed)
