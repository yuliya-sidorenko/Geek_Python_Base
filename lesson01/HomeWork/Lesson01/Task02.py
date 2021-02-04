user_sec = int(input("Введите время в секундах "))

time_min = (user_sec // 60)
time_sec = (user_sec % 60)
time_hour = (time_min // 60)

if time_min >= 60:
    time_min_add = time_min // 60
    print(f"Ваше время -  {time_hour} ч : {time_min_add} м : {time_sec} с")
else:
    # time_min = (time_min % 60)

    # time_hour = time_min // 60
    # time_hour_min = time_min % 60
    # time_hour_min_sec = time_hour_min /
    print(f"Ваше время - {time_hour} ч : {time_min} м : {time_sec} с")

# if time_sec >=60:
# time_min=(time_sec/60)
