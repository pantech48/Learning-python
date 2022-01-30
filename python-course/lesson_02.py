#!/usr/bin/python
# -*- coding: latin-1 -*-
"""
todo: Какие операторы существуют в Python?
Арифметические 		+ - / % // **
Сравнения : 		== != > < >= <= (в результате возвращают boolean)
Логические : 		and or not (boolean)
Побитовые: 			& | ~ ^ << >>
Присваивания:		= += -+ *= /= %= //= **= &= |= ^= <<= >>= 
Принадлежности:		in, not in
Тождественности: 	is, is not
"""
i = 1
i += 1
lst = [1, 2, 3,]

# todo: Ветвление
a = 1
b = 2
if a > b:
	print('a > b')
elif a == b:
	print('a = b')
else: 
	# pass
	print('a < b') 

# todo: Тернарный оператор

#number = input()
#number = int(number) if number.isdigit() else 0

#print(number)

# todo: Циклы

'''
i = 1

while i:
	if  not i % 2:
		print(i)

	if i == 10:
		break

	i += 1
'''

lst = [x for x in range(0,10)]

for j in lst:
	print(j)

for i in range(11, 1, -2):
	print('=>', i)

s = 'Hello'

for i, c in enumerate(s):
	print(i, c)

person = {
    'name': 'Vasya',
    'age': 45,
    'is_developer': True,
}

for key, value in person.items():
	print(key, "=>", value)


lst = [(1,2,3), (4, 5, 6)]

for a, b, c in lst:
	print(a, b, c)

# todo: Срезы
