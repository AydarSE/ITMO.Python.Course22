# coding=windows-1251
from os import name
from turtle import title

print("Работа со строками")
string1 = "This is a string."
string2 = " This is another string."
print("#2","\n", string1+string2)
print('#3')
print(len(string1))
print(string1.title())
print(string2.lower())
print(string1.upper())
print(string2.rstrip('.gn'))
print(string1.lstrip('Th'))
print(string2.strip())
print(string2.strip(' .Tghn'))
#4
print('#4')
d="abcdefg"
print(d[5])
#5
print('#5')
print (d[1:3])
#6
print('#6')
print(d[1:])
print(d[:3])
print(d[:])
print(d[1:5:2])
#7
print('#7')
#d[2]='o'
#print(d)

print('-------Работа с числами------')
a=3
b=7
print(b//a,b%a,a**3)
param='string'+str(15)
print(param)

print('-------Преобразование данных------')
print('#2')
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
print('{:7.3f}  plus  {:7.3f} =  {:7.3f}'.format(float(n1), float(n2), n3))

print('-------Форматирвоание строк------')
print('#2')
a = 1/3
print("{:7.3f}".format(a))
print('#3')
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
print('#4 - Cм. выше')

print('-------Списки------')
print('#1')
list1 = [82,8,23,97,92,44,17,39,11,12]
print(list1)
print('#2')
print(dir(list))
print('#3')
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)
print('#4')
list1[2]=777
print(list1)
print('#5-8')
list1.append(333)
print(list1)
list1.insert(5, 55)
list1.pop(3)
list1.pop()
print(list1)

print('-------Сортировка элементов списка------')
print('#1-2')
print(list1)
list1.sort(reverse=True)
print(list1)
print('#3-5')
list2 = [3,5,6,2,33,6,11]
print(list2)
lis = sorted(list2)
print(lis)

print('-------Кортежи------')
print('#1-2')
print(dir(tuple))
help(tuple.index)
help(tuple.count)
print('#3')
seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(listseq)
print(type(listseq))
listseq.append(123)
listseq.pop(5)
print(listseq)

print('-------Словари------')
print('#1-2')
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D)
print(D['food'])
D['quantity'] += 10
print(D['quantity'])
print('#3-4')
dp = {}
dp['name'] = input('Введите имя:')
dp['age'] = input('Введите возраст:')
print(dp)

print('-------Вложенность хранения данных------')
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
   'job': ['dev', 'mgr'],
   'age': 25}
print(rec)
print(rec['name']['firstname'], '', rec['name']['lastname'])
print(rec['name']['lastname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)