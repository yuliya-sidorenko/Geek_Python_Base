user_number = int(input ("Введите число ----->"))
user=user_number
max_number = -1
while user_number > 10:
    delim = user_number % 10
    print(delim)
    user_number //= 10
    print(user_number)
    if delim > max_number:
        max_number = delim
print(f" Самая большая цифра в числе {user} -  {max_number}")