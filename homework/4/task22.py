#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств.
#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18
#6 12
import random
n = int(input('Number of elements of the first set '))
m = int(input('Number of elements of the second set '))
list_1 = [random.randint(1,10) for i in range(n)]
list_2 = [random.randint(1,10) for i in range(m)]
print(list_1)
print(list_2)
print(f'{sorted(set(list_1).intersection(set(list_2)))}')
