#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
---------
Tabuado do 2
2
4
...
---------
"""
__version__ = "0.1.0"
__author__ = "Fernando"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero, "x", outro_numero,"=", numero * outro_numero)
    print("-" * 12, "\n")
