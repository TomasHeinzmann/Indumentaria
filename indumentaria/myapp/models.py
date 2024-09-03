from django.db import models

# Create your models here.
class Remera(models.Model):
    marca = models.CharField("Marca", max_length=30)
    talles = [
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL")
    ]
    talle = models.PositiveSmallIntegerField("Talle", choices=talles)
    color = models.CharField("Color", max_length=20)
    lisa = models.BooleanField("¿Es lisa?")
    generos = [
        (1, "Hombre"),
        (2, "Mujer"),
        (3, "Unisex")
    ]
    genero = models.PositiveSmallIntegerField("genero", choices=generos) 