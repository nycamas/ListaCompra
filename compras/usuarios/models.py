from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    STATUS_CHOICES = [
        ('admin', 'Administrador'),
        ('comprador', 'Comprador'),
        ('tecnico', 'Técnico'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.usuario.username
