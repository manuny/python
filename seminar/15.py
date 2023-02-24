#Пользователь вводит одно число N – количество арбузов. 
#Вторая строка содержит N чисел, записанных на новой строчке каждое. 
#Здесь каждое число – это масса соответствующего арбуза
#Input: 5 -> 5 1 6 5 9
#Output: 1 9

num = int(input('Введите количество арбузов:'))

number = 10
max_num = number
min_num = number

from random import randint as RI
for i in range (num):
    number = RI(1,30)
    print (number)
   
    if number > max_num:
                max_num = number
    elif number < min_num:
            min_num = number

print (f'Масса максимальная арбуза: {max_num}')
print (f'Масса минимального арбуза: {min_num}')



