#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
N = int(input('Введите количество элементов в массиве: '))
my_number = int(input('Введите число:'))
list = []
for i in range(N):
    list.append(random.randint(1,N))
print(f'{list}')
print(f'Число {my_number} встречается в массиве = {list.count(my_number)} раза')
