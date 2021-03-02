from django.db import models
import datetime

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__ (self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=False, blank=False)
    ano_pub = models.DateField(
        default=datetime.date.today, null=False, blank=False
        )
    idioma = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(blank=True)
    capa = models.ImageField(blank=True, upload_to="")

    def __str__(self):
        return self.titulo