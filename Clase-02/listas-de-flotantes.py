#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imprimir listas de números flotantes 

# Metodología de desarrollo llamada MVC (Modelo, Vista, Controlador)
# 1. Generar la lista de flotantes (Modelo)
N = 1000000
enteros = range(N)  # Genera el rango de enteros del 0 al N-1
flotantes = []
for i in enteros:
    f = float(i)  # i * 1.0
    flotantes.append(f)

# 2. Imprimirla (Vista)
print(flotantes)

