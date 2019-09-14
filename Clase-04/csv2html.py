#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script se encarga de convertir arhchivos CSV en HTML
"""

import click
import csv

def print_html(lista):
    """ Imprime en formato html el contenido de lista """
    
    plantilla = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h2>Lista de personas</h2>
        <hr />
        <table>
        <tr>
            <th>Nombre</th>
            <th>Lugar nacimiento</th>
            <th>Actividad</th>
            <th>Edad</th>
        </tr>
        {}
        </table>
    </body>
    </html>
    """
    html_lista = ""
    for linea in lista:
        linea_html = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n"
        linea_html = linea_html.format(*linea)
        html_lista += linea_html

    plantilla = plantilla.format(html_lista)

    print(plantilla)


@click.command()
@click.argument("nomarch", type=click.File())
def csv2html(nomarch):
    """
    Este script se encarga de convertir arhchivos CSV en HTML
    """
    csv_reader = csv.reader(nomarch)
    personas = []
    for row in csv_reader:
        personas.append(row)

    print_html(personas)


if __name__ == "__main__":
    csv2html()
