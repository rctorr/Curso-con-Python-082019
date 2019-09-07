#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imprimir listas de números enteros

# Metodología de desarrollo llamada MVC (Modelo, Vista, Controlador)
# 1. Generar la lista de enteros (Modelo)
N = 100000000
enteros = range(N)  # Genera el rango de enteros del 0 al N-1
enteros = list(enteros)  # Convierte a una lista

# 2. Imprimirla (Vista)
print(enteros)

