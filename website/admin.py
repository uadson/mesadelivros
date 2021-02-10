from django.contrib import admin
from .models import Categoria, Livro

# Register your models here.


class LivroAdmin(admin.ModelAdmin):
    list_per_page = 10

    list_display = (
        'titulo',
        #'nome',
        #'sobrenome',
        #'ano_pub',
        #'idioma',
        #'categoria',
        #'isbn',
    )

    list_display_links = (
        'titulo',
    )

    
admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria)