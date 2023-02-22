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


