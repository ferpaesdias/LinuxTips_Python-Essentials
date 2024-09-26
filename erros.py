#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e: 
    print(f"{str(e)}.")
    sys.exit(1)

# EAFP - Easy to Ask Forgiveness than permission

try:
    print(names[5])
except IndexError as e:
    print(f"{str(e)}.")
    sys.exit(1)