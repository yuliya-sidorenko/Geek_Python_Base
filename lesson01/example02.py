# password = input("Введите пароль -->")
# original_password = "pass"
# if original_password == password:
#     print("Correct")
# else:
#     print("Incorrect")

age = int(input("Введите возраст --->"))

if age >= 14:
    # print('паспорт уже должен быть')
    if (age == 45 or age == 20):
        print('Паспорт необходимо поменять')
    if age != 14:
        print('Паспорт уже должен быть')
    else:
        print('Пасспорт нужно получить')
else:
    print('Пасспорт рано получать') 
