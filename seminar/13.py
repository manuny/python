#Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
#В следующих строках располагается N целых чисел.
#Каждое число – среднесуточная температура в соответствующий день. 
#Температуры – целые числа и лежат в диапазоне от –50 до 50
#Input: 6 -> -20 30 -40 50 10 -10
#Output: 2

N = int(input('Введите количество рассматриваемых дней:'))

import random
temp = 0
count = 0
count_max = 0

for i in range (N):
    temp += random.randint(-4, 4)
    print (temp, end= ", ")
    if temp > 0:
        count += 1
    else:
        count = 0
    if count > count_max:
            count_max = count
    
print (f'Максимальное количество теплых дней: {count_max}')

