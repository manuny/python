#Дана последовательность из N целых чисел и числоK. 
#Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
#K – положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]


k = int(input('Введите сдвиг '))

list_1 = [ i for i in range(10) ]
print(list_1)
#print(list_1 [k: ] + list_1 [ : k])

for i in range (k):
    list_1.insert(0, list_1.pop(-1))
    
print(list_1)