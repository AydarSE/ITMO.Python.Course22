# coding=windows-1251

from Module import input_name, game_core, winner

player1 = input_name(1)
print('Игрок #1 ' + player1)
player2 = input_name(2)
print('Игрок #2' + player2)

playersWins=game_core(player1, player2)

winner(player1, player2, playersWins[0], playersWins[1])
