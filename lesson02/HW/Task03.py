# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# 1 List

mounth = int(input('Введите номер месяца --->'))
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(seasons[mounth - 1])

# Dict

d_mounth = int(input('Введите номер месяца --->'))
d_season = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
            9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
print(d_season.get(d_mounth))
