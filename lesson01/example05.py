max_count = int(input("Максимальное число --"))
delimeter = int(input("Число для деления --"))
current_count = 0
while True:
    if current_count == max_count:
        break

    # current_count = current_count + 1
    current_count += 1

    if current_count % delimeter == 0:
        continue
    print(current_count)
