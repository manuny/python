""" Последовательностью Фибоначчи называется последовательность чисел 
a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 21 """

fib = int(input('Введите номер числа фиббоначи: '))

def fibbon (fib):
    if fib == 1:
        return 1
    elif fib == 0:
        return 0
    else:
        return fibbon (fib - 1) + fibbon (fib - 2)
print(fibbon(fib))