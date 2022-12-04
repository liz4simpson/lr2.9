#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


time_fact_rec = '''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


time_fib_rec = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


time_fact_itr = '''
def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
'''


time_fib_itr = '''
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
'''


time_fact_lru = '''
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


time_fib_lru = '''
from functools import lru_cache
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


if __name__ == '__main__':
    print('Результат рекурсивного факториала:', timeit.timeit(setup=time_fact_rec, number=1000))
    print('Результат рекурсивного числа Фибоначи:', timeit.timeit(setup=time_fib_rec, number=1000))
    print('Результат итеративного факториала:', timeit.timeit(setup=time_fact_itr, number=1000))
    print('Результат итеративного числа Фибоначи:', timeit.timeit(setup=time_fib_itr, number=1000))
    print('Результат факториала с декоратором:', timeit.timeit(setup=time_fact_lru, number=1000))
    print('Результат числа Фибоначи с декоратором:', timeit.timeit(setup=time_fib_lru, number=1000))