""" Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8  """
    
def input_a():
	while True:
		number_a = input('Введите число: ')
		try:
			return int(number_a)
		except:
         		print ('Это не число. Повторите ввод: ')
			
def input_b():
	while True:
		number_b = input('Введите степень: ')
		try:
			if 0 <  int (number_b) < 100:
				return int(number_b)
			else:
				print ('Число должно быть от 1 до 99')
		except:
         		print ('Это не число. Повторите ввод: ')

def result(num_1, num_2):
	if (num_2 == 1):
		return (num_1)
	if (num_2 != 1):
		return (num_1 * result (num_1, num_2 - 1))

num_1 = input_a()  
num_2 = input_b() 

print(result(num_1, num_2))

