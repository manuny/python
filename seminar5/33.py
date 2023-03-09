""" Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, 
но наоборот: все максимальные – на минимальные. 

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1 """

import random
namber = [random.randint (1, 5) for _ in range(5)]
print(namber)
for i in range (len(namber)):
	if namber[i] == 5:
		namber[i] = 1
	elif namber[i] == 4:
		namber[i] = 2
print(namber)