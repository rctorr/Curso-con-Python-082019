#!/usr/bin/env python
# -*- coding: utf-8 -*-

productos = [
        ["Automóvil", 800000.00, 1],
        ["Bici", 4500.00, 8],
        ["Thinkpad", 16000, 3]
    ]

# Imprimir los elemtos de la lista
total = 0
for p in productos:
    st = p[1] * p[2]
    total += st  # total = total + st
    print("{:10} {:10.2f} {:1} {:10.2f}".format(p[0], p[1], p[2], st))

print("{:10} {:5} {:6} {:10.2f}".format("", "", "Total:",total))

