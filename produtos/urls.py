from django.urls import path

from produtos.views.produtos_views import listar_produtos, detalhar_produto

app_name = 'produtos'

urlpatterns = [
    path('', listar_produtos, name="listar_produtos"),
    path('<int:id>/', detalhar_produto, name="produto_detail")
]