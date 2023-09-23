from django.urls import path
from clientes.views.clientes_view import cadastrar, loginUsuario, logoutUsuario

app_name = 'clientes'

urlpatterns = [
    path('cadastrar/', cadastrar, name="cadastrar_usuario"),
    path('login/', loginUsuario, name="login"),
    path('logout/', logoutUsuario, name="logout")
]