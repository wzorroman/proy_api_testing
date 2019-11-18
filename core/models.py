from django.db import models


class Author(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField('email', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Article(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField('Descripcion', blank=True, null=True)
    cuerpo = models.TextField('Cuerpo', blank=True, null=True)
    autor = models.ForeignKey('Author', related_name='articulos', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
