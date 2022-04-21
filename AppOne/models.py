from django.db import models

# Create your models here.
class Integrantes(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaDnacimiento = models.CharField(max_length=30)
class Empleo(models.Model):
    Ocupacion = models.CharField(max_length=40)
    Salario = models.IntegerField()
class Entretenimiento(models.Model):
    Pasatiempos = models.CharField(max_length=40)
    
