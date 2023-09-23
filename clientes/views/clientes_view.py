from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if get_user_model().objects.filter(email=email).first():
            context = {
                'status': 'Já existe um usuário com esse E-mail'
            }
        else:
            novoUsuario = get_user_model().objects.create(
                username=nome, email=email
            )
            novoUsuario.set_password(senha)
            novoUsuario.save()
            context = {
                'status': 'Cadastrado com sucesso!'
            }
    else:
        context = {
            'status': ''
        }

    return render(request, "cadastrar_cliente.html", context)

def loginUsuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = authenticate(
            username=nome,
            password=senha
        )

        if usuario:
            login(request, usuario)
            return redirect('produtos:listar_produtos')
        else:
            context = {
                'status': 'E-mail ou senha incorretos' 
            }
    else:
        context = {
            'status': ''
        }
    
    return render(request, 'login.html', context)

def logoutUsuario(request):
    logout(request)
    return redirect(reverse('produtos:listar_produtos'))