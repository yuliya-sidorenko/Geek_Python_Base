# named_lambda = lambda name: f"Hello, {name}!!!!"
#
#
# print(named_lambda("Peter"))

print((lambda name: f"Hello, {name}!!!!")
      ("Sam")
      )

print((lambda x: x ** 2)
      (4)
      )
print((lambda *numbers: numbers)
      (1,3,6,7,9)
      )


#print(ord(input("-> ")))

print(len(input("-> ")))

round()