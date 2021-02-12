from django.db import models
from website.models import Livro, Categoria
from django import forms

# Create your models here.


class FormLivro(forms.ModelForm):
	class Meta:
		model = Livro
		exclude = ()

class FormCategoria(forms.ModelForm):
	class Meta:
		model = Categoria
		exclude = ()