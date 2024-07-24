from django.db import models

# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    conteudo = models.TextField()

    class Meta:
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.titulo
    