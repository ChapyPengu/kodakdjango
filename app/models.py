from django.db import models

# Create your models here.

class Cuenta(models.Model):

    usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    rol = models.CharField(max_length=40)

class FodaPersonal(models.Model):

    miembro = models.CharField(max_length=60)
    fortaleza = models.CharField(max_length=60)
    oportunidad = models.CharField(max_length=60)
    debilidad = models.CharField(max_length=60)
    amenaza = models.CharField(max_length=60)

class Mensaje(models.Model):

    miembro = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=240)

