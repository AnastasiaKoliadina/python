#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
list_len = int(input('Введите количество элементов в массиве: '))
my_number = int(input('Введите число:'))
list_random = []
for i in range(list_len):
    list_random.append(random.randint(1,list_len))
min_diff = max(list_random)
for i in range(list_len):
    if abs(my_number - list_random[i]) < min_diff:
        min_diff = abs(my_number - list_random[i])
        near_number = list_random[i]
print(f'{list_random}')
print(f'Близкий элемент {near_number} к заданному числу {my_number}')

        


#a=[int(i) for i in input().split()]
#b=int(input())
#number=0
#for i in range(len(a)):
#    if (b-a[i])<b-number and b-a[i]>0:
#        number=i
#print(a[number])