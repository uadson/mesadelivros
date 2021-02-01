from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.


def login(request):
	return render(request, 'accounts/login.html')

def logout(request):
	return render(request, 'accounts/logout.html')

# registro/cadastro de usuário/senha
def register(request):
	# se não houver nenhuma tentativa de cadastro retorne o formulário em branco
	if request.method != 'POST':
		return render(request, 'accounts/register.html')

	# coleta de dados
	nome = request.POST.get('nome')
	sobrenome = request.POST.get('sobrenome')
	email = request.POST.get('email')
	usuario = request.POST.get('usuario')
	senha = request.POST.get('senha')
	senha2 = request.POST.get('senha2')

	# se todos ou algum campos não for preenchido, retorne a mensagem de erro
	# e em seguida o formulário em branco
	if not nome or not sobrenome or not email or not usuario \
			or not senha or not senha2:
		messages.error(request, 'Todos os campos devem ser preenchidos.')	
		return render(request, 'accounts/register.html')

	# validação do email
	# em caso de email inválido retorne mensagem de erro
	try:
		validate_email(email)
	except:
		messages.error(request, 'Email inválido.')
		return render(request, 'accounts/register.html')

	# validacao de nome de usuário
	if len(usuario) < 6:
		messages.error(request,'Nome de usuário precisa ter 6 caracteres ou mais.')
		return render(request, 'accounts/register.html')

	# validacao de senha
	if len(senha) < 6:
		messages.error(request,'Senha precisa ter 6 caracteres ou mais.')
		return render(request, 'accounts/register.html')

	# validacao de senha2
	if senha != senha2:
		messages.error(request,'Senhas não conferem.')
		return render(request, 'accounts/register.html')

	# checando cadastro de email
	# se o email estiver cadastrado anteriormente retorna mensagem de erro
	if User.objects.filter(email=email).exists():
		messages.error(request, 'Email já existe.')
		return render(request, 'accounts/register.html')

	# checando cadastro de usuário
	# se o nome de usuário estiver cadastrado anteriormente retorna mensagem de erro
	if User.objects.filter(username=usuario).exists():
		messages.error(request, 'Usuário já existe.')
		return render(request, 'accounts/register.html')

	# mensage de confirmação de registro/cadastro de usuário
	messages.success(request, 'Usuário cadastrado com sucesso!')

	# salvando os dados
	user = User.objects.create_user(
		first_name=nome,
		last_name=sobrenome,
		email=email,
		username=usuario,
		password=senha
		)
	user.save()
	# redirecionando para tela de login
	return redirect('accounts:login')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')


385685	