'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них
'''

rating = [98, 76, 54, 32, 10]
print(f'начальный список {rating}')
number = input('Добавьте новое значение рейтига: ')
number = int(number)
rating.append(number)
print(f'новый список:    {sorted(rating, reverse=True)}')