# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2, 5]
# N = 30 -> [2, 3, 5]


def check_num():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print('Error')
        return check_num()


def mult(num: int) -> list:
    list = [i for i in range(2, num + 1) if num % i == 0]
    print (list)


number = abs(check_num())


def simple_num(n):
    list = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            list.append(i)
        i += 1
    if n > 1:
        list.append(n)
    return list


mult(number)
print(simple_num(number))
