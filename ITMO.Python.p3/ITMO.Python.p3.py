# coding=windows-1251
from statistics import median, stdev, mean
from math import fsum
from random import randint

list1=[randint(0, 100) for i in range(10)]
print(list1)
print("����� ����� ������: ", fsum(list1))
print("������� ��������: ", mean(list1))
print("�������: ", median(list1))
print("����������� ����������: ", stdev(list1))
print("��������� ����� �� 1 �� 100: ", randint(1,100))
