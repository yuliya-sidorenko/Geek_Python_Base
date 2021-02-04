profit = int(input("Укажите выручку ---> "))
lesion = int(input("Укажите издержки ---> "))

if profit <= lesion:
    print("Фирма в убытке")
else:
    print("Фирма получила прибыль - ", (profit-lesion))
    rentability= profit/(profit-lesion)
    empl=int(input("Укажите количество сотрудников ---> "))
    prof_empl=(profit-lesion)/empl
    print("Рентабельность фирмы - ",rentability)
    print("Прибыль в расчете на одного сотрудника  - ", prof_empl)

