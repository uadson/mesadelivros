from django.shortcuts import render, get_object_or_404
from .models import Livro, Categoria
from django.core.paginator import Paginator

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

	livro = get_object_or_404(Livro, id=livro_id)

	context = {
		'livro': livro
	}
	return render(request, 'website/detail.html', context)

def search(request):
	term = request.GET.get('term')	

	livros = Livro.objects.order_by('-id').filter(
		titulo=term,
	)

	context = {
		'livros': livros
	}

	paginator = Paginator(livros, 5)

	page = request.GET.get('page')
	livros = paginator.get_page(page)

	return render(request, 'website/search.html', context)