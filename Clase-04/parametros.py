#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Leer el tercer valor de sys.argv y guardarlo en una variable n
try:
    n = int(sys.argv[2]) if sys.argv[2].isdigit() else 1
except IndexError:
    n = 1

# Repetir las siguiente líneas de código n veces
try:
    for i in range(n):
        print("Hola", sys.argv[1])
except IndexError:
    print("Hola Fulanit@")

a3 = sys.argv[3]
print([int(i) if i.isdigit() else 1 for i in a3.split(",")])




