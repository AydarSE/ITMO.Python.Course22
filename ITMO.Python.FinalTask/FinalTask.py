# coding=windows-1251
from random import randint

a=[]
Finish=int(input("Финальный размер:"))
T=int(input("Ведите длину:"))
for i in range(T):
    a.append(randint(1,100))
    print(a)
print (len(a))
y=len(a)
if Finish==y:
 print('True')
else:
 print('False')
