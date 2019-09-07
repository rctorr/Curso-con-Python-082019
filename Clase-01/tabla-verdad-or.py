#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = "-" * 78
v = True
f = False
p = "{:<10} | {:10} | {:10}"

print("Tabla de verdad del OR")
print(l)
print(p.format("Operador 1", "Operador 2", "Resultado"))
print(l)
print(p.format(v, v, v or v))
print(p.format(v, f, v or f))
print(p.format(f, v, f or v))
print(p.format(f, f, f or f))
print(l)

