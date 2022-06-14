# coding=windows-1251
from statistics import median, stdev, mean
from math import fsum
from random import randint

list1=[randint(0, 100) for i in range(10)]
print(list1)
print("Сумма чисел списка: ", fsum(list1))
print("Среднее значение: ", mean(list1))
print("Медиана: ", median(list1))
print("Стандартное отклонение: ", stdev(list1))
print("Случайное число от 1 до 100: ", randint(1,100))
