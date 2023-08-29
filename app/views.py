from django.shortcuts import render

produtos = [
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 2,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 3,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 4,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 5,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 6,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 7,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    },
    {
        'id': 8,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'preco': '199,99'
    }
]

def listar_produtos(request):
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)