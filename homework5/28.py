""" Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы. """

def input_a():
	while True:
		number_a = input('Введите число: ')
		try:
			if 0 <  int (number_a):
				return int(number_a)
		except:
         		print ('Это не целое положительное число. Повторите ввод: ')
			
def input_b():
	while True:
		number_b = input('Введите число: ')
		try:
			if 0 <  int (number_b):
				return int(number_b)
		except:
         		print ('Это не целое положительное число. Повторите ввод: ')

def sum(num_1, num_2):
	if (num_2 != 0):
		return  sum (num_1 + 1, num_2 - 1)
	if (num_2 == 0):
		return (num_1)

num_1 = input_a()  
num_2 = input_b() 

print(sum(num_1, num_2))