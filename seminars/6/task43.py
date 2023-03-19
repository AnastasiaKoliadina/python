#Задача №43.
#Дан список чисел. Посчитайте, сколько в нем пар
#элементов, равных друг другу. Считается, что любые
#два элемента, равные друг другу образуют одну пару,
#которую необходимо посчитать. Вводится список
#чисел. Все числа списка находятся на разных
#строках.
#Ввод: 
#1 2 3 2 3 
#Вывод:2
import random
length_mass_1 = int(input("Введите длину первого массива: "))
random_mass_1 = [random.randint(1,10) for _ in range(length_mass_1)]
count = 0
for i in random_mass_1:
    if random_mass_1.count(i) > 1:
        count += 1
print(count // 2)
print(random_mass_1)

# Второй вариант
list_1 = [random.randint(0,20) for _ in range(int(input('Введите размер списка: ')))]
print(list_1)

count = 0
pairs_list = []
for item in set(list_1):
    pairs = list_1.count(item)//2
    count += pairs
    if pairs:
        [pairs_list.append(item) for _ in range(pairs*2)]
    [list_1.remove(item) for _ in range(pairs*2)]

print(pairs_list)
print(list_1)
print(count)
