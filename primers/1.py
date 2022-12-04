#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Пример обратного отсчета, написанного с использованием хвостовой рекурсии:


def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)