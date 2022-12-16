from django.db import models
from stdimage.models import StdImageField, JPEGField
import datetime
import uuid


def get_file_path(_instance, filename):
    # separando nome do arquivo e extensão
    ext = filename.split('.')[-1]
    # criando um novo nome para arquivo em formato de hash
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'categoria'

    def __str__ (self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    autor = models.CharField(max_length=150, null=False, blank=False)
    ano_pub = models.DateField(
        default=datetime.date.today, null=False, blank=False
        )
    idioma = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(blank=True)
    # capa = StdImageField(upload_to=get_file_path,
    #                             variations={
    #                                 'thumbnail': {'with': 100, 
    #                                               'height': 75, 
    #                                               'crop': True}
    #                             })
    capa = JPEGField(
        upload_to=get_file_path,
        variations={'full': (None, None), 'thumbnail': (100, 75)},
    )
    
    class Meta:
        db_table = 'livro'

    def __str__(self):
        return self.titulo
