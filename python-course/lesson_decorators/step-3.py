"""
Декораторы

Декоратор - это функция, основное назначение которой состоит в том, 
чтобы служить оберткой для других функций или класса.

Главная цель такого обертывания 
    - изменить или расширить возможности обертываемого объекта.

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
"""

from functools import wraps
import pickle
import time


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        worked = time.time() - started
        template = 'Функция "{}" выполнилась за {:f} микросекунд.'  
        print(template.format(func.__name__, worked * 1e6))
        return result
    return wrapper


def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]

    return wrapper


@cache #применяется снизу вверх, вызываетс сверху вниз
@benchmark
def factorial(n):
    f = 1

    for i in range(1, n+1):
        f *= i
    
    return f


print(f'Факториал числа 25!: {factorial(25)}')
print(f'Факториал числа 25!: {factorial(25)}')
print(f'Факториал числа 50!: {factorial(50)}')

