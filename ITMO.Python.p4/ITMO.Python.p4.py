# coding=windows-1251
from random import randint
import time

#���� ���� ��������
print ('���� ���� ��������')
igrok1 = input('������� ��� 1-�� ��������� ')
igrok2 = input('������� ��� 2-�� ��������� ')

#������ ��������
win_player1=0
win_player2=0

for i in range(5):

 #������������� �������� ������ ������ ��������
 print('������������� �������� ������ ������ ��������')
 print('����� �������', igrok1)
 time.sleep(2)
 n1 = randint(1, 6)
 print('������:', n1)

 #������������� �������� ������ ������ ��������
 print ('������������� �������� ������ ������ ��������')
 print('����� �������', igrok2)
 time.sleep(2)
 n2 = randint(1, 6)
 print('������:', n2)

#����������� ���������� (3 ��������� ��������)
 print ('����������� ����������')
 if n1 > n2:
  win_player1+=1
  print('�������', igrok1, '���������:',win_player1)
 elif n1 < n2:
  win_player2+=1
  print('�������', igrok2, '���������:',win_player2)
 else:
  print('�����')

if win_player1>win_player2:
    print("�������",igrok1)
elif win_player1<win_player2:
    print("�������",igrok2)
else:
    print("������ �����")