#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#не превосходящие числа N.
#10 -> 1 2 4 8
N = int(input('Введите число N: '))
k = 0
n = str(2**k)
while 2**(k+1) <= N:
    n = n+' ' + str(2**(k+1))
    k = k+1
print(f'{N} --> {n}')
