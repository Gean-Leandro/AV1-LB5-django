from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda req: redirect('/produtos/'), name="listar_produtos"),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
