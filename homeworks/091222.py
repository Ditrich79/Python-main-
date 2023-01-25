money = int(input("Введите число от 1 до 99 копеек: "))
if 0 < money <= 99:
    print(money, end=" ")
    if money == 1 or money == 21 or money == 31 or money == 41 or money == 51 or money == 61 or money == 71 or \
            money == 81 or money == 91:
        print("копейка")
    elif 2 <= money <= 4 or 22 <= money <= 24 or 32 <= money <= 34 or 42 <= money <= 44 or 52 <= money <= 54 or \
            62 <= money <= 64 or 72 <= money <= 74 or 82 <= money <= 84 or 92 <= money <= 94:
        print("копейки")
    else:
        print("копеек")
else:
    print("Ошибка ввода")
