from django.shortcuts import render
from produtos.models.product import Product
from produtos.models.image import Image
from produtos.models.specifications import Specification
from produtos.models.rate import Rate
from produtos.models.content import Content

produtos = [
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'precoAnterior': '376,46',
        'preco': '229,99',
        'pix': '270,58',
        'maxVezes': '10',
        'maxVezesPreco': '27,05',
        'qtdEstoque': '20'
    },
    {
        'id': 2,
        'nome': 'Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI',
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg',
        'precoAnterior': '135,28',
        'preco': '89,99',
        'pix': '105,87',
        'maxVezes': '4',
        'maxVezesPreco': '26,46',
        'qtdEstoque': '60'
    },
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'precoAnterior': '376,46',
        'preco': '229,99',
        'pix': '270,58',
        'maxVezes': '10',
        'maxVezesPreco': '27,05',
        'qtdEstoque': '20'
    },
    {
        'id': 2,
        'nome': 'Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI',
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg',
        'precoAnterior': '135,28',
        'preco': '89,99',
        'pix': '105,87',
        'maxVezes': '4',
        'maxVezesPreco': '26,46',
        'qtdEstoque': '60'
    },
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'precoAnterior': '376,46',
        'preco': '229,99',
        'pix': '270,58',
        'maxVezes': '10',
        'maxVezesPreco': '27,05',
        'qtdEstoque': '20'
    },
    {
        'id': 2,
        'nome': 'Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI',
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg',
        'precoAnterior': '135,28',
        'preco': '89,99',
        'pix': '105,87',
        'maxVezes': '4',
        'maxVezesPreco': '26,46',
        'qtdEstoque': '60'
    },
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'precoAnterior': '376,46',
        'preco': '229,99',
        'pix': '270,58',
        'maxVezes': '10',
        'maxVezesPreco': '27,05',
        'qtdEstoque': '20'
    },
    {
        'id': 2,
        'nome': 'Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI',
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg',
        'precoAnterior': '135,28',
        'preco': '89,99',
        'pix': '105,87',
        'maxVezes': '4',
        'maxVezesPreco': '26,46',
        'qtdEstoque': '60'
    }
]

imagens = [
    {
        'id': 1,
        'idProduto': 1,
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg'
    },
    {
        'id': 2,
        'idProduto': 1,
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 2.jpg'
    },
    {
        'id': 3,
        'idProduto': 1,
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 3.jpg'
    },
    {
        'id': 4,
        'idProduto': 1,
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 4.jpg'
    },
    {
        'id': 5,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg'
    },
    {
        'id': 6,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 2.jpg'
    },
    {
        'id': 7,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 3.jpg'
    },
    {
        'id': 8,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 4.jpg'
    }
]

caracteristicas = [
    {
        'id': 1,
        'idProduto': 1,
        'caracteristica': '- Marca: HyperX'
    },
    {
        'id': 2,
        'idProduto': 1,
        'caracteristica': '- Modelo: 4P5E1AA#ABA'
    },
    {
        'id': 3,
        'idProduto': 2,
        'caracteristica': '- Marca: Redragon',
    },
    {
        'id': 4,
        'idProduto': 2,
        'caracteristica': '- Modelo: M711W',
    }
]

especificacoes = [
    {
        'id': 1,
        'idProduto': 1,
        'especificacoes': '- Iluminação RGB dinâmica por tecla'
    },
    {
        'id': 2,
        'idProduto': 1,
        'especificacoes': '- Estrutura durável em alumínio'
    },
    {
        'id': 3,
        'idProduto': 1,
        'especificacoes': '- Descanso para pulso removível'
    },
    {
        'id': 4,
        'idProduto': 1,
        'especificacoes': '- Switches mecânicos confiáveis à prova de poeira[2]'
    },
    {
        'id': 5,
        'idProduto': 1,
        'especificacoes': '- Conector USB em metal dourado com cabo trançado resistente'
    },
    {
        'id': 6,
        'idProduto': 1,
        'especificacoes': '- Personalização avançada com o software HyperX NGENUITY'
    },
    {
        'id': 7,
        'idProduto': 2,
        'especificacoes': '- Exclusiva e linda pintura branca com acabamento Matte.'
    },
    {
        'id': 8,
        'idProduto': 2,
        'especificacoes': '- Sensor PIXART PMW3325 para Alta Performance (10000DPI/20G/100ips)'
    },
    {
        'id': 9,
        'idProduto': 2,
        'especificacoes': '- Iluminação RGB Ajustável'
    },
    {
        'id': 10,
        'idProduto': 2,
        'especificacoes': '- Nova versão com sistema de Iluminação Chroma RGB! (7 Diferentes Modos de Iluminação)'
    }
]

conteudos = [
    {
        'id': 1,
        'idProduto': 1,
        'conteudo': '- Teclado HyperX Alloy MKW100'
    },
    {
        'id': 2,
        'idProduto': 2,
        'conteudo': '- Mouse Gamer Redragon Cobra'
    }
]

garantias = [
    {
        'id': 1,
        'idProduto': 1,
        'garantia': '24 meses de garantia'
    },
    {
        'id': 2,
        'idProduto': 2,
        'garantia': '12 meses de garantia'
    }
]

pesos = [
    {
        'id': 1,
        'idProduto': 1,
        'peso': '1250 gramas (bruto com embalagem)'
    },
    {
        'id': 2,
        'idProduto': 2,
        'peso': '210 gramas (bruto com embalagem)'
    }
]

avaliacoes = [
    {
        'id': 1,
        'idProduto': 1,
        'nome': 'Heitor',
        'titulo': 'Muito Bom',
        'data': '04/08/2023',
        'avaliacao': 'Muito bom, só não gostei porque não tem Ç, mas acredito que deva te sido um erro meu na hora de ver os detalhes. Mas no geral muito bom.'
    },
    {
        'id': 2,
        'idProduto': 1,
        'nome': 'Anônimo',
        'titulo': 'Ótimo',
        'data': '10/04/2023',
        'avaliacao': 'muito bom, produto ótimo, 0 defeitos até hoje, difícil visualizar se o caps está ligado'
    },
    {
        'id': 3,
        'idProduto': 2,
        'nome': 'Andre',
        'titulo': 'Muito bom',
        'data': '04/08/2023',
        'avaliacao': 'Muito bom'
    },
    {
        'id': 4,
        'idProduto': 2,
        'nome': 'Anônimo',
        'titulo': 'Aquisição',
        'data': '19/08/2023',
        'avaliacao': 'Excelente custo benefício, detalhes impecáveis, Nenhum'
    },
    {
        'id': 5,
        'idProduto': 2,
        'nome': 'Pablo',
        'titulo': 'Brabo',
        'data': '02/08/2023',
        'avaliacao': 'Lindo bom acabamento é bem pensado, Todos, Nenhum'
    }
]

def listar_produtos(request):
    context = {
        'produtos': Product.objects.all()
    }
    return render(request, 'index.html', context)

def detalhar_produto(request, id):
    produto = Product.objects.get(pk=id)
    imagens = Image.objects.filter(product__pk=id)
    avaliacoes = Rate.objects.filter(product__pk=id)

    context = {
        'produto': produto,
        'imgs': imagens,
        'especificacoes': Specification.objects.filter(product__pk=id),
        'conteudos': Content.objects.filter(product__pk=id),
        'avaliacoes': avaliacoes
    }

    return render(request, 'detalhar_produto.html', context)
