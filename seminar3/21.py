import random
list_1 = [random.randint (0, 10) for _ in range(10)]
print (list_1) 
list_2 = []
for item in list_1:
    if list_1.count(item) == 1:
    	list_2.append(item)
    
print(list_2)
    
