# coding=windows-1251
from random import randint
import time

def input_name(num):
    print('������� ��� {:d}-�� ��������� ' .format(num))
    return input()

def game_core(player1, player2):
    win_player1=0
    win_player2=0
    for i in range(3):
        print('������������� �������� ������')
        print('����� �������', player1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('������:', n1)
        win_player1+=n1
        print('����� �������', player2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('������:', n2)
        win_player2+=n2
    return[win_player1,win_player2]

def winner(player1, player2, win_player1,win_player2):
    print ('����������� ����������')
    if win_player1>win_player2:
     print('�������', player1)
    elif win_player1<win_player2:
     print('�������', player2)
    else:
     print('�����')
