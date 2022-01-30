#!/usr/bin/python
# -*- coding: latin-1 -*-

'''Функции'''

# todo: Как объявить функцию

def print_hello():
	print('Hello, Python!')

# todo: Как выполнить вызов функции?

print_hello()
print_hello()

# todo:Как вернуть значение из функции?

def return_hello():
	return 'Hello, Batya!' # После return блок кода не работает. С помощью return можно просто выходить из функции

result = return_hello()
print(result)

# todo: Зачем функции аргумент? 

def print_greeting(username):
	print('Hello, ', username, "!", sep='')

#todo: Как передавать аргументы?
print_greeting('Linus')

def sqrt(x):
	return x** .5

print(sqrt(9))


def multi(a, b):
	return (a * b)

print(multi(5, 6))

# todo: Как задать значение аргумента по умолчанию?

def my_pow(x, n=2):
	return x ** n

print(
	my_pow(8),
	my_pow(2, 5)
)

# Аргументы по умолчанию строго идут после заданных аргументов

# todo: Позиционные и именованные аргументы
# - любой аргумент можно передать как именованный

my_pow(2, n=5)
my_pow(x=2, n=5)
#my_pow(x=2, 5) # позиционные аргументы идут после именованных
my_pow(n=5, x=2)

# todo: Переменное количество аргументов

def super_multi(a, b, *args):
	r = a * b
	
	for i in args:
		r *= i

	return r

print(super_multi(1, 2))
print(super_multi(1, 2, 3))
print(super_multi(1, 2, 3, 4))
print(super_multi('a', 5, 3))


def db_connect(provider, **kwargs): # **name позволяет принять в функцию любое количество именованных аргументов
	print('Connecting to database', provider)
	print('==>', kwargs)

db_connect("sqlite", filename='/tmp/db.sqlite3')
db_connect(provider='mysql', user='root', host='localhost')

def f(*args, **kwargs):
	pass # пустой блок кода


# todo: Как развернуть кортеж/список в значения позиционных аргументов?

numbers = [8, 20]
print(multi(*numbers))

numbers = tuple(range(10, 20, 2))
print(super_multi(*numbers))

# todo: Как развернуть словарь в значения именованных аргументов?

options = {
	'provider': 'pgsql',
	'user': 'root',
	'host': '127.0.0.1',
}

db_connect(**options)

d = {
	'x': 2,
	'n': 9,
}

print(my_pow(**d))


# todo: Передача значений аргумента по ссылке

def parse(src, output):
	src = src.strip('.')

	for word in src.split():
		output.append(word)

src = 'Python is a programming language.'
lst = []
parse(src, lst)
print(lst)


def slpit_pieces(s, size, output=None):
	if output is None:
		output = []

	#output = output or [] 

	start = 0
	end = len(s)

	while start < end:
		output.append(s[start:start+size])
		start += size

	return output

print(slpit_pieces(src, 5))
print(slpit_pieces(src, 2))

# todo: Анонимная функция

sqrt = lambda x: x ** .5 

print(sqrt(16))

lst = [1, 2, 3, 4, 5]
#print(', '.join(map(lambda i: str(i), lst)))
print(', '.join(map(str, lst)))

# todo: Рекурсивная функция

def factorial(n):
	return 1 if n == 0 else n ( factorial(n - 1))

'''
Косвенная рекурсия
def a():
	b()

def b():
	a()

a()
'''

g = 666

def wrapper():
	external = 777

	def func():
		global g # !!!!! ЗЛО
		nonlocal external

		g += 1
		external += 1

	func()
	print(g, external)

wrapper()



# todo: Замыкания

def trim(chars=None):
	def f(s):
		return s.strip(chars)
	return f

spaces_trim = trim()

print(spaces_trim)

slashes_trim = trim('/|\\')
print(slashes_trim)

print(slashes_trim('//// post ////'))


















