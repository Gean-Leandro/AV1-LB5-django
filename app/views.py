from django.shortcuts import render

# Create your views here.

def paginaInicial(request):
    return render(request, 'index.html')