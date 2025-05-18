from django.db import models

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    web = models.URLField(max_length=200, blank=True, null=True)
    tlf = models.CharField(max_length=15, blank=True, null=True)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 11)], blank=True, null=True)

    def __str__(self):
        return self.nombre
