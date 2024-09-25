#!/usr/bin/env python3
"""Calculadora prefix

Funcionamento

[Operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operaçao: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Fernando Dias"

import sys
arguments = sys.argv[1:]

# TODO: Exceptions
if not arguments:
    operation =input("operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("Ex.: 'sum 5 5'")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição com While + tratamento com exceptions
    if not num.replace(".","").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2  

print(f"O resultado é {result}")          