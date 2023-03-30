import csv


def main():
    with open('data2.csv', 'r') as file:
        f_reader = csv.reader(file, delimiter=';')
        for row in f_reader:
            print(row)
    print()

    with open('data2.csv', 'r') as file:
        f_reader = csv.reader(file, delimiter=';')
        counter = 0
        for row in f_reader:
            if counter == 0:
                print(f"Файл содержит следующие столбцы: {', '.join(row).upper()}")
            else:
                print(f"Имя хоста: {row[0]}, продавец: {row[1]}, модель: {row[2]}, местонахождение: {row[3]}")
            counter += 1
            print(f"Всего в файле data2.csv содержится следующее количество строк - {counter}")
            print('*' * 70)


if __name__ == '__main__':
    main()
