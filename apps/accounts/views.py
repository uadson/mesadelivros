from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from .models import User
from django.contrib.auth.decorators import login_required


# 1. Tela de Login
def login(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        senha = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=senha)

        if not user:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'apps/accounts/login.html')
        else:
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso.')
            return redirect('dashboard')
    else:
        return render(request, 'apps/accounts/login.html')


# 2. Desconectando Usuário do Sistema
def logout(request):
    auth.logout(request)
    return redirect('login')


# 3. Tela de Redefinição de Senha
def pwreset(request):
    """Função com objetivo de verificar dados e realizar ou 
    não a redefinição de senha conforme solicitação do usuário."""

    if request.method != 'POST':
        return render(request, 'apps/accounts/password_reset.html')

    # variáveis que receberam os dados informados
    email = request.POST.get('email')
    senha = request.POST.get('password')
    senha2 = request.POST.get('senha2')

    # a) se nenhum dado for informado, retorna mensagem de erro.
    if not email or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos.')
        return render(request, 'apps/accounts/password_reset.html')

    # b) verificando o formato do email ex.: email@email.com, etc
    # se por exemplo email@b ou email@email, retorna mensagem de erro
    try:
        validate_email(email)
    except:
        messages.error(request, 'Formato do email é inválido.')
        return render(request, 'apps/accounts/password_reset.html')

    # c) verifica se senhas possuem no mínimo 6 caracteres,
    # caso contrário retorna mensagem de erro.
    if len(senha) < 6:
        messages.error(request, 'Senha deve ter no mínimo 6 caracteres.')
        return render(request, 'apps/accounts/password_reset.html')

    # d) verifica se as senhas informadas são iguais, caso contrário,
    # retorna mensagem de erro.
    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'apps/accounts/password_reset.html')

    # e) verifica se o email informado já está cadastrado na base de dados.
    # se sim, redefine a senha
    # se não retorna mensagem de erro.
    if not User.objects.filter(email=email).exists():
        messages.error(
            request, 'Email não cadastrado, clique em Registrar-se.')
        return render(request, 'apps/accounts/password_reset.html')
    else:
        # obtendo nomes de usuário que não são super usuários
        user = User.objects.filter(is_superuser=False)

        # para cada usuario em user
        for usuario_email in user:
            # se algum possuir o email informado
            if usuario_email.email == email:
                # variavel usr recebe o valor do email
                usr = User.objects.get(email=email)
                # atualiza a senha
                usr.set_password(senha)
                # salva os dados
                usr.save()
                # retorna mensagem de redefinição de senha
                messages.success(request, 'Nova senha cadastrada com sucesso.')
                # redireciona para página de login
                return redirect('login')

    return render(request, 'apps/accounts/password_reset.html')


# 4 . Formulário para Cadastro de Novos Usuários
def register(request):
    # se não houver nenhuma tentativa de cadastro retorne o formulário em branco
    if request.method != 'POST':
        return render(request, 'apps/accounts/register.html')

    # coleta de dados
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    senha2 = request.POST.get('senha2')

    # se todos ou algum campo não for preenchido, retorne a mensagem de erro
    # e em seguida o formulário em branco
    if not nome or not sobrenome or not email \
            or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos.')
        return render(request, 'apps/accounts/register.html')

    # validação do email
    # em caso de email inválido retorne mensagem de erro
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'apps/accounts/register.html')

    # validacao de senha
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'apps/accounts/register.html')

    # validacao de senha2
    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'apps/accounts/register.html')

    # checando cadastro de email
    # se o email estiver cadastrado anteriormente retorna mensagem de erro
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'apps/accounts/register.html')

    # mensage de confirmação de registro/cadastro de usuário
    messages.success(request, 'Usuário cadastrado com sucesso!')

    # salvando os dados
    user = User.objects.create_user(
        first_name=nome,
        last_name=sobrenome,
        email=email,
        password=senha
    )
    user.save()
    # redirecionando para tela de login
    return redirect('apps/accounts:login')


@login_required(redirect_field_name='apps/accounts:login')
def dashboard(request):
    return render(request, 'apps/accounts/dashboard.html')


def user(request):
    if request.method != 'PUT':
        return render(request, 'apps/accounts/userform.html')

    return render(request, 'apps/accounts/userform.html')
