a = int(input("Км в первый день ---> "))
b = int(input("Желаемый результат в км  ---> "))
d = 1
print("{0}-й день: {1:9.1f} км".format(d,a))

while a <= b:
    a = (a * 0.1) + a
    d = d + 1
    print("{0}-й день: {1:9.1f} км".format(d,a))

print(f"на {d}-й день спортсмен достиг результата — не менее {b} км")
