'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

a = input('Введите несколько слов через пробел: ')
a = list(a.split(' '))
for i, item in enumerate(a):
    print(i+1, item[0:10])
