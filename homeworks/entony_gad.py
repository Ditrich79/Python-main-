# number = 123456789.12345
# print(f'{number:,.2f}')
# print(f'{number:,.3F}')

# discount = 0.5
# print(f'{discount:.0%}')  # символ % умножает число на 100 и выводит его со знаком %

# number = 123456
# print(f'{number:,d}')  # 123,456

# number = 12345.6789
# print(f'Ширина поля равна {number:15,.2f}')  # Ширина поля равна       12,345.68

# number = 236589
# print(f'{number:^15,d}')  # выравнивание по центру поля
# print(f'{number:<15,d}')  # выравнивание по левому краю поля
# print(f'{number:>15,d}')  # выравнивание по правому краю поля

# def main():
#     show_interest(rate=0.01, periods=10, principal=10000.0)
#
#
# def show_interest(principal, rate, periods):
#     interest = principal*rate*periods
#     print(f'Простой процентный доход составит ${interest:,.2f}')
#
#
# main()


# import time
#
# print(time.strftime('Сегодня: ''%d.%m.%Y, %H:%M:%S'))

# def convert(kiloms):
#     miles = kiloms * 0.6214
#     return miles
#
#
# print(convert(100))

# # Получить требуемое будущее значение
# future_value = float(input("Введите требуемое будущее значение: "))
#
# # Получить годовую процентную ставку
# rate = float(input("Введите годовую процентную ставку: "))
#
# # Получить количество лет хранения денег на счёте
# years = int(input("Введите количество лет хранения денег на счёте: "))
#
# # Рассчитать сумму, необходимую для внесения на счёт
# present_value = future_value / (1 + rate) ** years
#
# # Показать сумму, необходимую для внесения на счёт
# print("Вам потребуется внести сумму: ", round(present_value, 2))


# # Эта программа вычисляет отпускную цену розничного товара.
#
# # DISCOUNT_PERCENTAGE - процент скидки
# DISCOUNT_PERCENTAGE = 0.2
#
#
# # Главная функция.
# def main():
#     #  Получить обычную цену товара.
#     reg_price = get_regular_price()
#
#     #  Рассчитать отпускную цену.
#     sale_price = reg_price - discount(reg_price)
#
#     #  Показать отпускную цену.
#     print(f"Отпускная цена составляет ${sale_price:,.2f}.")
#
#
# # Функция get_regular_price предлагает пользователю ввести обычную цену
# # товара и возвращает это значение.
#
#
# def get_regular_price():
#     price = float(input('Введите обычную цену товара: '))
#     return price
#
#
# # Функция discount принимает цену товара в качестве аргумента и возвращает
# # сумму скидки, указанную в DISCOUNT_PERCENTAGE.
# def discount(price):
#     return price * DISCOUNT_PERCENTAGE
#
#
# # Вызвать главную функцию.
# main()


# def spend_on_car():
#     credit = int(input('Укажите сколько Вы платите в месяц за кредит на машину: '))
#     insur = int(input('Укажите сколько Вы платите в месяц за страховку автомобиля: '))
#     bensin = int(input("Укажите сколько Вы тратите в месяц на бензин: "))
#     tech = int(input('Укажите сколько Вы тратите в месяц на техобслуживание автомобиля: '))
#     month_spend = credit + insur + bensin + tech
#     year_spend = month_spend * 12
#     print(f"Расходы в месяц на автомобиль составляют {month_spend}")
#     print(f"Расходы в год на автомобиль составляют {year_spend}")
#
#
# spend_on_car()

# def main():
#     value = 5
#     show_double(value)
#
#
# def show_double(num):
#     result = num * 2
#     print(result)
#
#
# main()

# def main():
#     show_interest(principal=10000.0, periods=10, rate=0.01)
#
#
# def show_interest(principal, rate, periods):
#     interest = principal * rate * periods
#     print(f'Простой процентный доход составит ${interest:,.2f}')
#
#
# main()


# MAIN_TAX = 0.0072
#
#
# def main():
#     osnov = float(input('Введите фактическую стоимость Вашего имущества: '))
#     tax_new = ozen_cost(osnov)
#     print(f'Оценочная стоимость Вашего имущества составит ${ozen_cost(osnov):,.2f}.\n'
#           f'Налог на имущество будет ${tax(tax_new):,.2f}.')
#
#
# def ozen_cost(num):
#     return num * 0.6
#
#
# def tax(a):
#     return a * MAIN_TAX
#
#
# main()


# with open('F:/R57553.txt', 'r') as f:
#     print(f.read())


# Эта программа предлагает пользователю ввести суммы
# продаж и записывает эти суммы в файл sales.txt.

def main():
    # Получить количество дней.
    num_days = int(input('За какое количество дней ' +
                         'Вы располагаете продажами? '))

    # Открыть новый файл с именем sales.txt.
    sales_file = open('sales.txt', 'w')

    # Получить суммы продаж за каждый день
    # и записать их в файл.
    for count in range(1, num_days + 1):
        # Получить продажи за день.
        sales = float(input(
            f'Введите продажи за день № {count}: '))
        # Записать сумму продаж в файл.
        sales_file.write(f'{sales}\n')

    # Закрыть файл.
    sales_file.close()
    print('Данные записаны в sales.txt.')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()
