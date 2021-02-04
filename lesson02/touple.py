# print(tuple('обфчна строка'))
#
#
# t_list=(4,4,67,89,3,23)
# print(t_list.__sizeof__())
#
# l_list=[4,4,67,89,3,23]
# print(l_list.__sizeof__())
#
# perem_1 = set('abrakadabra')
# perem_2 = frozenset('abrakadabra')
# print(perem_1)
# print(perem_2)
# perem_1.add('!')
# print(perem_1)
# perem_2.add('!')add
# print(perem_2)


my_set = {400, None, "text", True}
print(my_set)

my_set.add("another_el")
print(my_set)

my_set.remove("text")
print(my_set)

my_set.discard(400)
print(my_set)

my_set.pop()
print(my_set)


my_s = set('abrakadabra')
my_fs = frozenset('abrakadabra')
print(my_s == my_fs)

my_s = set('kadabra')
print(my_s)
my_fs = frozenset('abra')
print(my_fs)
print(my_s - my_fs)