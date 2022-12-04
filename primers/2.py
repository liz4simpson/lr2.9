#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Любое вычисление, которое может быть выполнено с использованием итерации, также может
быть выполнено с использованием рекурсии. Вот версия find_max (поиск максимального
значения в последовательном контейнере, например списке или кортеже), написанная с
использованием хвостовой рекурсии:
"""


def find_max(seq, max_so_far):
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:
        return find_max(seq[1:], seq[0])
    else:
        return find_max(seq[1:], max_so_far)