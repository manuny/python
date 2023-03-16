"""  Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) """

min_number = int(input('Введите минимум: '))
max_number = int(input('Введите максимум: '))

import random

list_1 = [random.randint (-100, 100) for _ in range(30)]
print (list_1)

list_2 = []

for i in range(len(list_1)):
	if min_number <= list_1[i] <= max_number:
		list_2.append (i)
print(list_2)
		