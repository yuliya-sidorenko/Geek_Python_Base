# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

a = (int(input("Первое число - >")))
b = (int(input("Второе число - >")))
c = (int(input("Второе число - >")))


def my_func(a, b, c):
    max_sum = (max(a + b, b + c, c + a))
    print(a + b, b + c, c + a)
    return max_sum


print(my_func(a, b, c))
