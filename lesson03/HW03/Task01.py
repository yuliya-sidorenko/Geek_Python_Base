# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def func_del():
    try:
        num1 = int(input("Первое число - >"))
        num2 = int(input("Второе число - >"))
    except ValueError:
        return ("Нужно число!")

    try:
        result = round((num1 / num2), 2)
        return result
    except ZeroDivisionError:
        return ("Делить на 0 нельзя")


val = func_del()
print(val)
