#1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
N = input("Ввудите")
def fibbonachi(fib1):
    if fib1 ==1:
        return 1
    elif fib1 == 0:
        return 0
    else:
        return fibbonachi()