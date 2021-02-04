names = dict(name="Jhon", age=10)
print(names.keys())
print(names.values())



my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}
print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

print(my_dict.get(2))
print(my_dict.popitem())
print(my_dict.popitem())
print(my_dict.popitem())
print(my_dict.popitem())


my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# setdefault
print(my_dict.setdefault(5))
print(my_dict.items())

print(my_dict.pop(2))
print(my_dict.items())


my_dict.update({8: 8, 9: 9, 10: 10})
print(my_dict.items())