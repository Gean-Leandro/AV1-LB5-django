from django.shortcuts import render

produtos = [
    {
        'id': 1,
        'nome': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB...',
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 1.jpg',
        'precoAnterior': '376,46',
        'preco': '229,99',
        'pix': '270,58',
        'maxVezes': '10',
        'maxVezesPreco': '27,05'
    },
    {
        'id': 2,
        'nome': 'Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI',
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg',
        'precoAnterior': '135,28',
        'preco': '89,99',
        'pix': '105,87',
        'maxVezes': '4',
        'maxVezesPreco': '26,46'
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
        'idProduto': 1,
        'img': 'img/produtos/teclados/Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto/img 5.jpg'
    },
    {
        'id': 6,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 1.jpg'
    },
    {
        'id': 7,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 2.jpg'
    },
    {
        'id': 8,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 3.jpg'
    },
    {
        'id': 9,
        'idProduto': 2,
        'img': 'img/produtos/mouses/Mouse Gamer Redragon Cobra, RGB, 7 Botões, 10000DPI, Lunar White - M711W/img 4.jpg'
    }
]

descricoes = [
    {
        'id': 1,
        'idProduto': 1,
        'caracteristica': '- Marca: HyperX<br>- Modelo: 4P5E1AA#ABA',
        'especificacoes': '- Iluminação RGB dinâmica por tecla<br>- Estrutura durável em alumínio<br>- Descanso para pulso removível<br>- Switches mecânicos confiáveis à prova de poeira[2]<br>- Conector USB em metal dourado com cabo trançado resistente<br>- Personalização avançada com o software HyperX NGENUITY',
        'conteudo da embalagem': '- Teclado HyperX Alloy MKW100',
        'garantia': '24 meses de garantia',
        'peso': '1250 gramas (bruto com embalagem)'
    },
    {
        'id': 2,
        'idProduto': 2,
        'caracteristica': '- Marca: Redragon<br>- Modelo: M711W',
        'especificacoes': '- Exclusiva e linda pintura branca com acabamento Matte.<br>- Sensor PIXART PMW3325 para Alta Performance (10000DPI/20G/100ips)<br>- Iluminação RGB Ajustável<br>- Nova versão com sistema de Iluminação Chroma RGB! (7 Diferentes Modos de Iluminação)',
        'conteudo da embalagem': '- Mouse Gamer Redragon Cobra',
        'garantia': '12 meses de garantia',
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
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def detalhar_produto(request, id):
    for p in produtos:
        if p['id'] == id:
            produto = p
            break

    imgs = []
    for i in imagens:
        if i['idProduto'] == id:
            imgs.append(i['img'])

    for d in descricoes:
        if d['idProduto'] == id:
            descr = d
            break

    av = []
    for a in avaliacoes:
        if a['idProduto'] == id:
            av.append(a)


    context = {
        'produto': produto,
        'imgs': imgs,
        'descricao': descr,
        'avaliacoes': av
    }

    return render(request, 'detalhar_produto.html', context)
