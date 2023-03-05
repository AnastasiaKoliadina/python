#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8
num = int(input("Введите число A: "))
num_degree = int(input("Введите степень числа B: "))
def deg(a, n):
 if (n == 1):
  return a
 else:
  return a * pow(num, n - 1)
print(deg(num, num_degree))
