""" Напишите программу, которая принимает на вход строку, и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n. """

import random
list_1 = [random.randint (0, 5) for _ in range(15)]
print (list_1) 
dict = {}

for i in list_1:
    dict[i] = dict.get(i, 0) + 1
    print (i if dict.get(i) == 1 else f' {i} _ {dict.get(i) - 1}', end = '  ')