from django.contrib import admin
from .models import Usuario, Libro

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "apellidos", "edad", "genero")

admin.site.register(Usuario, UsuarioAdmin)


class LibroAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "titulo", "editorial", "numPag", "autores")

admin.site.register(Libro, LibroAdmin)
