from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__ (self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    autor = models.CharField(max_length=200, null=False, blank=False)
    ano_pub = models.DateField(default=0, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    isbn = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo