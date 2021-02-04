# # Списки
#
# str = (list('обфчная строка'))
# print(str)
#
# # добавление новго элемента
# str.append('new')
# print(str)
#
# # расширить список
# str.extend('add list')
# print(str)
#
# str.insert(10, 'new_el')
# print(str)
#
# str.remove("о")
# print(str)
#
# str.pop(3)
# print(str)
#
#
# print(str.index('new'))
#
# print(str.count('d'))
#
# str.reverse()
# print(str)
#
copy_str = (list('1232343554'))
print(copy_str)
#
# str.clear()
# print(str)
var = [12, 43, 575, 332]
var.extend(copy_str)
print(var)
# [12, 43, 575, 332]


var.sort()
print(var)