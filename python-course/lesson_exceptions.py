#!/usr/bin/python
# -*- coding: latin-1 -*-

""""Исключения"""
try:
	# код, в котором потенциально может появиться исключение 
	a = input()

	if a.isdigit():
		a = int(a)
	else:
		print("Vi vveli ne 4islo")

	b = int(input())
	print(a + b)
except ValueError:
	# обработка исключения
	print('Vi vveli ne 4islo')
except TypeError as err:
	print(err)
except:
	('All errors')
else:
	print('Выполняется, если не было ошибок')
finally:
	print('Always')

# 