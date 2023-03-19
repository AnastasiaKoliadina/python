#Задача №39.Даны два массива чисел. Требуется вывести те элементы
#первого массива (в том порядке, в каком они идут в первом
#массиве), которых нет во втором массиве. Пользователь вводит
#число N - количество элементов в первом массиве, затем N
#чисел - элементы массива. Затем число M - количество
#элементов во втором массиве. Затем элементы второго массива
#Ввод: Вывод:
#7 3 3 2 12
#3 1 3 4 2 4 12
#6
#4 15 43 1 15 1 (каждое число вводится с новой строки)
import random
length_mass_1 = int(input("Введите длину первого массива"))
random_mass_1 = [random.randint(1,10) for _ in range(length_mass_1)]
length_mass_2 =int(input("Введите длину второго массива"))
random_mass_2 = [random.randint(1,10) for _ in range(length_mass_2)]
temp_list = []
print(random_mass_1)
print(random_mass_2)
for i in random_mass_1:
    if i not in random_mass_2:
        temp_list.append(i)
print(temp_list)