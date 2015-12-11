from django.db import models

# Create your models here.

class persona(models.Model):
    idPersona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class cliente(models.Model):
    clave = models.IntegerField(primary_key=True)
    idPersona = models.ForeignKey(persona)
    ncompras = models.IntegerField()
