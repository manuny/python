#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
sum=int(number % 10)  + (number % 100//10) + (number //100)

print(f'Сумма цифр: {sum}')