#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imprimir lista de productos con subtotales 

# Obtener lista de productos
productos = {
        "001":["Chocolates dulces", 5.50, 20],
        "002":["Chocolates semiamargo", 7.50, 15],
        "003":["Chocolates amargo", 15.0, 5]
    }

# Imprimir lista de productos
total = 0
for k in productos:
    subtotal =  productos[k][1] * productos[k][2]
    total += subtotal  # total = total + subtotal
    print("{:3} {:25} {:5} {:3} {:5}".format(k, *productos[k],
        subtotal)
print(" "*30, "Total:", total)
