#!/usr/bin/env python3
"""Bloco de Notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")


arguments = sys.argv[1:]
if not arguments:
    print("invald usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    try:
        arg_tag = arguments[1].lower()
    except IndexError:
        arg_tag = input("Qual a tag? ").strip().lower()

    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arg_tag:
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    try:
        title = arguments[1]  
    except IndexError:
        title = input("Qual é o titulo? ").strip().title()

    # criação da nota
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")