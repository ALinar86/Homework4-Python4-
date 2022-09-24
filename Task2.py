# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список
# исключит повторы элементов исходной последовательности. Не использовать множества.
# [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4] -> [1, 2, 3, 4]


import random


def check_num():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print('Error')
        return check_num()


def get_list():
    num = check_num()
    list = [random.randint(1, 4) for i in range(num)]
    return list


def without_repeating(list_num: list) -> list:
    new_list = []
    for i in list_num:
        if i not in new_list:
            new_list.append(i)
    return new_list


lst = get_list()
print(lst)
print(without_repeating(lst))
