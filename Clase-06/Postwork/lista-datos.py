#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import obtiene_viajes
from stdout import imprime_registros, imprime_registros_html

@click.command()
@click.option("--html", is_flag=True, help="Imprime la lista en formato HTML")
def lista_datos(html):
    """
    Imprime la lista de registros de un reporte generado a partir de dos
    o más tablas en la salida estándar.
    """
    # Se obtiene la lista de registros para el reporte fulanito
    fulanitos = obtiene_filanitos()
    if html:
        # Se imprimen los fulanitos en formato html en la salida estándar
        imprime_fulanitos_html(fulanitos, "Lista de fulanitos")
    else:
        # Se imprimen los fulanitos en formato texto en la salida estándar
        imprime_fulanitos(fulanitos, "Lista de fulanitos")

if __name__ == '__main__':
    lista_datos()
