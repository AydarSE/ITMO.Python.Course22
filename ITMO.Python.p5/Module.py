# coding=windows-1251
from random import randint
import time

def input_name(num):
    print('Введите имя {:d}-го играющего ' .format(num))
    return input()

def game_core(player1, player2):
    win_player1=0
    win_player2=0
    for i in range(3):
        print('Моделирование бросания кубика')
        print('Кубик бросает', player1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        win_player1+=n1
        print('Кубик бросает', player2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        win_player2+=n2
    return[win_player1,win_player2]

def winner(player1, player2, win_player1,win_player2):
    print ('Определение результата')
    if win_player1>win_player2:
     print('Выиграл', player1)
    elif win_player1<win_player2:
     print('Выиграл', player2)
    else:
     print('Ничья')
