from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    establecimiento = models.ForeignKey('establecimientos.Establecimiento', on_delete=models.CASCADE)

    def __str__(self):
        return self.producto
