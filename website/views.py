from django.shortcuts import render, get_object_or_404
from .models import Livro, Categoria
from django.core.paginator import Paginator

# Create your views here.


def index(request):
	# 'livros=' recebe os objetos da classe Livro ordenados pelo id de mode decrescente
	livros = Livro.objects.order_by('-id')
	# os objetos visualizados em quantidade de 5 por pagina
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
	livros = Livro.objects.order_by('-id').filter(
		# __icontains facilita a busca tornando dispensável a digitação do termo completo
		titulo__icontains=term,
	)
	paginator = Paginator(livros, 5)
	page = request.GET.get('page')
	livros = paginator.get_page(page)
	return render(request, 'website/search.html', {
		'livros': livros
		})