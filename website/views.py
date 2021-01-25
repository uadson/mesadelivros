from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Livro, Categoria
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.


def index(request):
	livros = Livro.objects.order_by('-id')
	paginator = Paginator(livros, 5)
	page = request.GET.get('page')
	livros = paginator.get_page(page)
	return render(request, 'website/index.html', {
		'livros': livros
	})

def detail(request, livro_id):
	# em caso de id inválido retorna erro 404
	livro = get_object_or_404(Livro, id=livro_id)
	return render(request, 'website/detail.html', {
		'livro': livro
		})

def search(request):
	term = request.GET.get('term')
	# objetos ordenados em modo decrescente filtrados pelo temo digitado	
	
	if term is None or not term:
		messages.add_message(
			request, 
			messages.ERROR, 
			'Campo não pode ficar vazio.'
		)
		return redirect('website:index')

	campos = Concat('nome', Value(' '), 'sobrenome')
	
	livros = Livro.objects.annotate(
		nome_completo=campos
		).filter(
			Q(nome_completo__icontains=term) | Q(titulo__icontains=term) 
		)

	paginator = Paginator(livros, 5)
	page = request.GET.get('page')
	livros = paginator.get_page(page)
	return render(request, 'website/search.html', {
		'livros': livros
		})