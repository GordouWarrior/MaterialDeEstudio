from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    clave = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    sede = models.CharField(max_length=30)


class MaterialDeEstudio(models.Model):
    materia = models.CharField(max_length=30)
    profesor = models.CharField(max_length=15)
    semestre = models.CharField(max_length=15)
    fecha = models.DateTimeField(max_length=15)
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.materia
