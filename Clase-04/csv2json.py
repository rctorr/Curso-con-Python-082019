#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script se encarga de convertir arhchivos CSV en JSON
"""

import click
import csv
import json

def print_json(lista):
    """ Imprime en formato json el contenido de lista """
    # personasDictionary = {}
    # for id, element in enumerate(lista):
    #     personasDictionary.update({id: element})

    personasDictionary = {id:element for id, element in enumerate(lista)}
    
    print(json.dumps(personasDictionary, indent=4))


@click.command()
@click.argument("nomarch", type=click.File())
def csv2json(nomarch):
    """
    Este script se encarga de convertir arhchivos CSV en JSON
    """
    csv_reader = csv.reader(nomarch)
    personas = []
    for row in csv_reader:
        personas.append(row)

    print_json(personas)


if __name__ == "__main__":
    csv2json()
