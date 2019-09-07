#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imprimir lista de productos con subtotales usando funciones 

# Obtener lista de productos (Modelo)
def obtener_productos():
    """ Obtiene la lista de productos y la regresa como lista """
    productos = {
            "001":["Chocolates dulces", 5.50, 20],
            "002":["Chocolates semiamargo", 7.50, 15],
            "003":["Chocolates amargo", 15.0, 5]
        }

    return productos

def ordena_productos(producs):
    """ Ordena producs en orden alfabéticos en base al nombre """
    producs_ordenados = sorted(producs, key=lambda k: producs[k][0])

    return producs_ordenados

def imprime_productos(producs, total, ordena=False):
    """ Imprime la lista de productos en la salida estándar """
    if ordena:
        llaves = ordena_productos(producs)

    # Imprimir lista de productos (vista)
    for k in llaves:
        print("{:3} {:25} {:5} {:3} {:5}".format(k, *producs[k]))
    print(" "*30, "Total:", total)


# Controlador
def main():
    """ Función principal """
    productos = obtener_productos()
    total = 0
    for k in productos:
        subtotal = productos[k][1] * productos[k][2]
        productos[k].append(subtotal)
        total += subtotal

    imprime_productos(productos, total, ordena=True)

if __name__ == "__main__":
    main()


