# Задача с рекурсией

# Вариант №1

digits = [-2, 3, 8, -11, -4, 6]


def look_digits(nums):
    if not nums:
        return 0
    else:
        count = look_digits(nums[1:])
        if nums[0] < 0:
            count += 1
        return count


minus = look_digits(digits)
print(f'n = {minus}')


# Вариант №2

# digits = [-2, 3, 8, -11, -4, 6]
#
#
# def look_digits(num):
#     if not num:
#         return num
#     if num[0] > 0:
#         return look_digits(num[1:])
#     else:
#         return num[:1] + look_digits(num[1:])
#
#
# print(f'n = {len(look_digits(digits))}')




