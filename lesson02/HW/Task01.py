# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.

first_list = [7, 'example', 127, 45.3, None]
print(first_list)

for node in first_list:
    print(type(node))