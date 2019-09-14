#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument("nombre")
@click.argument("n", type=int, default=1)
def hola(nombre, n):
    """ función principal """
    for i in range(n):
        print("Hola", nombre)

if __name__ == "__main__":
    hola()

