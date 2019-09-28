#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file, request

HOST = "localhost"
PORT = 8000

# Agregar ruta y vista para atender peticiones de archivos estáticos
@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

def leer_html(nomarch):

    with open(nomarch) as da:
        contenido = da.read()

    return contenido

# Agregar ruta y vista para atender petición raíz /
@route("/")
def index():
    plantilla = leer_html("formulario.html")
    return plantilla

# Agregar ruta y vista para atender petición raíz / con datos POST
@route("/post")
def post():
    pass

if __name__ == "__main__":
    # Inicializa el servidor de la aplicación web
    run(host=HOST, port=PORT, debug=True, reloader=True)

