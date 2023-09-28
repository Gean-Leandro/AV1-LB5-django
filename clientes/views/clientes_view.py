from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if get_user_model().objects.filter(email=email).first():
            messages.warning(request, "E-mail já foi cadastrado")
        else:
            novoUsuario = get_user_model().objects.create(
                username=nome, email=email
            )
            novoUsuario.set_password(senha)
            novoUsuario.save()
            messages.success(request, "Usuário cadastrado com sucesso")

    return render(request, "cadastrar_cliente.html")

def loginUsuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(
            username=email,
            password=senha
        )

        if usuario:
            login(request, usuario)
            messages.success(request, "Seja bem vindo {}".format(usuario.username))
            return redirect('produtos:listar_produtos')
        else:
            messages.warning(request, 'E-mail ou senha incorretos')

    
    return render(request, 'login.html', context)

def logoutUsuario(request):
    logout(request)
    return redirect(reverse('produtos:listar_produtos'))