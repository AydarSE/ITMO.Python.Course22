# coding=windows-1251
from random import randint
import time

#Ввод имен играющих
print ('Ввод имен играющих')
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')

#Вводим счетчики
win_player1=0
win_player2=0

for i in range(5):

 #Моделирование бросания кубика первым играющим
 print('Моделирование бросания кубика первым играющим')
 print('Кубик бросает', igrok1)
 time.sleep(2)
 n1 = randint(1, 6)
 print('Выпало:', n1)

 #Моделирование бросания кубика вторым играющим
 print ('Моделирование бросания кубика вторым играющим')
 print('Кубик бросает', igrok2)
 time.sleep(2)
 n2 = randint(1, 6)
 print('Выпало:', n2)

#Определение результата (3 возможных варианта)
 print ('Определение результата')
 if n1 > n2:
  win_player1+=1
  print('Выиграл', igrok1, 'выиграшей:',win_player1)
 elif n1 < n2:
  win_player2+=1
  print('Выиграл', igrok2, 'выиграшей:',win_player2)
 else:
  print('Ничья')

if win_player1>win_player2:
    print("Чемпион",igrok1)
elif win_player1<win_player2:
    print("Чемпион",igrok2)
else:
    print("Боевая ничья")