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

def main():
    show_interest(rate=0.01, periods=10, principal=10000.0)


def show_interest(principal, rate, periods):
    interest = principal*rate*periods
    print(f'Простой процентный доход составит ${interest:,.2f}')


main()



