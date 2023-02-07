import re


def valid_number(number):
    reg = r'(\+?[7]\s?\(?\d{3}\)?\s?\d{3}-?\s?\d{2}-?\s?\d{2})'
    return re.findall(reg, number)


print(valid_number('+7 499 456-45-78'))
print(valid_number('+74994564578'))
print(valid_number('7 (499) 456 45 78'))
print(valid_number('7 (499) 456-45-78'))
