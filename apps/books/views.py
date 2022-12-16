from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Livro
from .forms import FormCategoria, FormLivro, FormAlteraLivro
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
	livros = Livro.objects.order_by('-id')
	paginator = Paginator(livros, 5)
	page = request.GET.get('page')
	livros = paginator.get_page(page)
	return render(request, 'apps/books/index.html', {
		'livros': livros
	})


def detail(request, livro_id):
	# em caso de id inválido retorna erro 404
	livro = get_object_or_404(Livro, id=livro_id)
	return render(request, 'apps/books/detail.html', {
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
		return redirect('index')

	campos = Concat('nome', Value(' '), 'sobrenome')
	
	livros = Livro.objects.annotate(
		nome_completo=campos
		).filter(
			Q(nome_completo__icontains=term) | Q(titulo__icontains=term) 
		)

	paginator = Paginator(livros, 5)
	page = request.GET.get('page')
	livros = paginator.get_page(page)
	return render(request, 'apps/books/search.html', {
		'livros': livros
		})
 
 
@login_required(login_url='/login/')
def cadlivro(request):
    if request.method != 'POST':
        form = FormLivro()
        return render(request, 'apps/books/cadlivro.html', {
            'form': form
        })

    form = FormLivro(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormLivro(request.POST)
        return render(request, 'apps/books/cadlivro.html', {
            'form': form
        })

    form.save()
    messages.success(
        request, f'Livro {request.POST.get("titulo")} foi cadastrado com sucesso.'
    )
    return redirect('cadlivro')


@login_required(login_url='/login/')
def altlivro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if request.method == 'POST':
        form = FormAlteraLivro(request.POST, instance=livro)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso.')
            return redirect('index')
    else:
        form = FormAlteraLivro(instance=livro)
        
    context={'form':form}
        
    return render(request, 'apps/books/altlivro.html', context)


@login_required(login_url='/login/')
def del_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if livro:
        obj = Livro.objects.get(pk=pk)
        obj.delete()
        messages.success(request, f'Livro: {livro.titulo} - excluído com sucesso!')
    
    return redirect('index')


@login_required(login_url='/login/')
def cadcateg(request):
    if request.method != 'POST':
        form = FormCategoria()
        return render(request, 'apps/books/cadcateg.html', {
            'form': form
        })

    form = FormCategoria(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao cadastrar categoria.')
        form = FormCategoria(request.POST)
        return render(request, 'apps/books/cadcateg.html', {
            'form': form
        })

    form.save()
    messages.success(
        request, f'Categoria {request.POST.get("nome")} foi cadastrada com sucesso.'
    )
    return redirect('cadcateg')
