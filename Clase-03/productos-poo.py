#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imprimir lista de productos con subtotales usando POO 

# from csv import writer
import csv


class Producto:
    """ Define la clase para el objeto Producto """
    def __init__(self, nombre, precio, cantidad):
        """ Es el constructor de la clase """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def subtotal(self):
        """ Calcula el subtotal del producto """
        return self.precio * self.cantidad

    def tupla(self):
        """ Regresa el objeto en tipo tupla """
        return (self.nombre, self.precio, self.cantidad, self.subtotal)


# Obtener lista de productos (Modelo)
def obtener_productos():
    """ 
        Obtiene la lista de productos y la regresa una lista de 
        objetos de tipo Producto.
    """
    productos = {
            "001":Producto("Chocolates dulces", 5.50, 20),
            "002":Producto("Chocolates semiamargo", 7.50, 15),
            "003":Producto("Chocolates amargo", 15.0, 5)
        }

    return productos

def ordena_productos(producs):
    """ Ordena producs en orden alfabéticos en base al nombre """
    llaves_ordenadas = sorted(producs, key=lambda k: producs[k].nombre)

    return llaves_ordenadas

def imprime_productos(producs, total, ordena=False):
    """ Imprime la lista de productos en la salida estándar """
    if ordena:
        llaves = ordena_productos(producs)

    # Imprimir lista de productos (vista)
    for k in llaves:
        print("{:3} {:25} {:5} {:3} {:5}".format(k, *producs[k].tupla()))
    print(" "*30, "Total:", total)

def guarda_productos(producs, nomarch, ordena=False):
    """ Guarda la lista de productos en el archivo nomarch en CSV """
    if ordena:
        llaves = ordena_productos(producs)

    # Guarda lista de productos (vista)
    da = open(nomarch, "w")
    da_csv = csv.writer(da)
    for k in llaves:
        da_csv.writerow(producs[k].tupla())

    da.close()


# Controlador
def main():
    """ Función principal """
    productos = obtener_productos()
    total = 0
    for k in productos:
        total += productos[k].subtotal

    imprime_productos(productos, total, ordena=True)
    guarda_productos(productos, "productos.csv", ordena=True)

if __name__ == "__main__":
    main()


