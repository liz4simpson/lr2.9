# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задан список положительных чисел, признаком конца которых служит отрицательное
число. Используя рекурсию, подсчитать количество чисел и их сумму.
"""


def negative_num(s, sm, cnt):
    if not s:
        return sm, cnt
    if s[0] >= 0:
        sm += s[0]
        cnt += 1
    return negative_num(s[1:], sm, cnt)


if __name__ == '__main__':
    count = 0
    summ = 0
    A = list(map(int, input(">> ").split()))
    a = negative_num(A, summ,  count)
    print("Сумма положительных элементов: ", a[0], "\nКоличество положительных элементов: ", a[1])