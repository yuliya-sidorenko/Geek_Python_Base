# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# Вариант 1
def int_func(*args):
    string = input("Введите слово или предложение ")
    print(string.title())
    return
int_func()



# Вариант 2
def int_func(Str):
  return chr(ord(Str[0])-32)+Str[1:]

Input = input('Enter word(s), only lowercase latin allowed:')
if not Input.islower() or not Input.replace(' ','').isalpha():
  print ('only lowercase latin chars allowed')
else:
  for Word in Input.split():
    print (int_func(Word), end = ' ')
  print ()
  print ('Or... ')
  print (' '.join([int_func(x) for x in Input.split()]))