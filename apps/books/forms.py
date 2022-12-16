from .models import Livro, Categoria
from django import forms


class FormLivro(forms.ModelForm):
	class Meta:
		model = Livro
		exclude = ()


class FormCategoria(forms.ModelForm):
	class Meta:
		model = Categoria
		exclude = ()
  

class FormAlteraLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
			'titulo',
			'autor',
			'ano_pub',
			'idioma',
			'categoria',
			'descricao',
   			'capa',
		]
