'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

a = input('Введите сюда произвольное количество символов, слово или фразу:')
a = list(a)
print('Вы ввели:',a)
j = 0
for i in range(int(len(a) / 2)):
  a[j], a[j + 1] = a[j + 1], a[j]
  j += 2
print('А стало: ',a)