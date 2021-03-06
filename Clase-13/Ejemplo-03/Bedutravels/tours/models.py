from django.db import models

# Create your models here.
class User(models.Model):
    """ Define la tabla User """
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    clave = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)

class Zona(models.Model):
    """ Define la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nombre)

class Tour(models.Model):
    """ Define la tabla Tour """
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.nombre)

class Opinion(models.Model):
    """ Define la tabla Opinion """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.texto)

class Salida(models.Model):
    """ Define la tabla Salida """
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    asientos = models.PositiveSmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tour = models.ForeignKey(Tour, related_name="salidas", on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}, {})".format(self.tour, self.fechaInicio, self.fechaFin)
