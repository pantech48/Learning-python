"""
Генераторы

"""

from urllib.request import urlopen

def generator():
    print('Шаг №1')
    yield 1
    print('Шаг №2')
    yield 2
    print('Шаг №3')

g = generator()
print(g, type(g))
print(next(g))
print(next(g))
#print(next(g))


def countdown(n, step=1):
    print('Генератор стартовал!')
    while n > 0:
        yield n
        n -= step


for i in countdown(5):
    print(i)


def iter_page(urls):
    for ulr in urls:
        yield urlopen(ulr).read

pages = iter_page(['http://python.org', 'https://ya.ru'])
for source in pages:
    print(source)


