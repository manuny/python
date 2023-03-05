#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
n = int(input('Введите длинну списка '))
my_list = [random.randint (0, 10) for _ in range(n)]

print (my_list)

number = int(input('Введите искомое число '))
num = 0
num_3 = 0


for i in range (n):
   if my_list[i] == number:
    num += 1 
print(f'{num} раз встречается число {number}')

for i in set(my_list):
    num_2 = i - number 
    if num_2 < num_3:
        num_3 = i
print(f'максимально близкое число {num_3}')