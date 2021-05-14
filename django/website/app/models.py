from django.db import models

# Create your models here.
class Estanteria(models.Model):
    venta = models.CharField(max_length=50)
    peso = models.CharField(max_length=10)
    pintura = models.CharField(max_length=10)
    estatura = models.CharField(max_length=10)

    def __str__(self):
        return self.venta

class Locker(models.Model):
    venta = models.CharField(max_length=50)
    puertas = models.CharField(max_length=1)
    material = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.venta

class Mueble(models.Model):
    venta = models.CharField(max_length=50)
    nombre = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.venta

class Caja(models.Model):
    venta = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)

    def __str__(self):
        return self.venta