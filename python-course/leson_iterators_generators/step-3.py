"""
Генераторы списков/множеств/словарей.

[expression for item1 in iterable1 if condition
             for item2 in iterable2 if condition
             ...
             for itemN in iterableN if condition]
"""

numbers = [1, 2, 3, 3, 2, 1]

"""
squares = []
for i in numbers:
    squares.append(i * i)
"""
squares = [i * i for i in numbers]
odd = [i for i in numbers if i%2]

"""
points = []
for x in range(3):
    for y in range(2):
        points.append((x,y))
"""
points = [(x, y) for x in range(3) for y in range(2)]

print(squares, odd, points)

#todo: Генераторы множеств

s = {i for i in numbers} # сложно!!! set(numbers)
print(s)

text = 'Python is programming language!'

words_lengths = {len(word) for word in text.split()}
print(f"""
Уникальные длины слов: {words_lengths}
Минимальная длина слова: {min(words_lengths)}
Самое длинное слово: {max(words_lengths)}
""")


# todo: Генераторы словарей

keys = ['id', 'original_url', 'short_url']
values = [1, 'http://python.org', '/1']
# так делать нельзя!!!
# data = {k: v for i, k in enumerate(keys) for j, v in enumerate(values) if i == j}
data = dict(zip(keys, values))
print(data)


users = [
    {
        'id':1,
        'name': 'Linux Torvalds',
        'skills': ('C++', 'Linux'),
        'is developer': True,
    },
    {
        'id':2,
        'name': 'Richard Stallman',
        'skills': ('C', 'GNU'),
        'is developer': True,
    },
    {
        'id':1,
        'name': 'Linux Torvalds',
        'skills': ('C++', 'Linux'),
        'is developer': True,
    },
]

users = {user['id']: user for user in users}
print('\n', users)


# todo: Выражения-генераторы или генераторные выражения

squares_generator = (i * i for i in numbers)
print(squares_generator, tuple(squares_generator), set(squares_generator))

with open(__file__) as f:
    print(type(f))
    lines = (line.strip() for line in f)
    todo = (s for s in lines if s.startswith('# todo:'))
    print('Todos:', todo, list(todo))


# todo: Примеры

print('; '.join(str(i) for i in numbers))

squares = list(map(lambda i: i * i, numbers))
odd = list(filter(lambda i: i % 2, numbers))
print(squares, odd)

squares_sum = sum(i * i for i in numbers)
print(squares_sum)

















