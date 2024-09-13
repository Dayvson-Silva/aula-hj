produtos = [
    {
        'nome': 'Produto A',
        'preco_original': 100.0,
        'preco_usuario': 80.0,
        'quantidade_vendida': 10
    },
    {
        'nome': 'Produto B',
        'preco_original': 150.0,
        'preco_usuario': 120.0,
        'quantidade_vendida': 5
    },
    {
        'nome': 'Produto C',
        'preco_original': 200.0,
        'preco_usuario': 180.0,
        'quantidade_vendida': 8
    }
]

def analise_vendas(produtos):
    total_quantidade_vendida = 0
    total_vendas = 0
    receita_total = 0
    lucro_total = 0
    num_produtos = len(produtos)
    
    for produto in produtos:
        nome = produto['nome']
        preco_original = produto['preco_original']
        preco_usuario = produto['preco_usuario']
        quantidade_vendida = produto['quantidade_vendida']
        
        receita = preco_usuario * quantidade_vendida
        lucro = (preco_usuario - preco_original) * quantidade_vendida
        
        total_quantidade_vendida += quantidade_vendida
        total_vendas += receita
        receita_total += receita
        lucro_total += lucro
        
        print(f"Produto: {nome}")
        print(f"  Preço Original: R${preco_original:.2f}")
        print(f"  Preço para o Usuário: R${preco_usuario:.2f}")
        print(f"  Quantidade Vendida: {quantidade_vendida}")
        print(f"  Receita: R${receita:.2f}")
        print(f"  Lucro: R${lucro:.2f}")
        print()
    
    media_quantidade_vendida = total_quantidade_vendida / num_produtos if num_produtos > 0 else 0
    
    print(f"Total de Produtos Vendidos: {total_quantidade_vendida}")
    print(f"Média de Quantidade Vendida por Produto: {media_quantidade_vendida:.2f}")
    print(f"Valor Total de Venda de Todos os Produtos: R${total_vendas:.2f}")
    print(f"Receita Total: R${receita_total:.2f}")
    print(f"Lucro Total: R${lucro_total:.2f}")

analise_vendas(produtos)


def identificar_produtos_vendidos(produtos):
    if not produtos:
        print("Nenhum produto disponível para análise.")
        return

    # Identificar o produto mais vendido e o menos vendido
    produto_mais_vendido = max(produtos, key=lambda p: p['quantidade_vendida'])
    produto_menos_vendido = min(produtos, key=lambda p: p['quantidade_vendida'])

    # Exibir informações do produto mais vendido
    print(f"Produto Mais Vendido:")
    print(f"  Nome: {produto_mais_vendido['nome']}")
    print(f"  Quantidade Vendida: {produto_mais_vendido['quantidade_vendida']}")
    print(f"  Preço para o Usuário: R${produto_mais_vendido['preco_usuario']:.2f}")
    print(f"  Receita: R${produto_mais_vendido['preco_usuario'] * produto_mais_vendido['quantidade_vendida']:.2f}")
    print()

    # Exibir informações do produto menos vendido
    print(f"Produto Menos Vendido:")
    print(f"  Nome: {produto_menos_vendido['nome']}")
    print(f"  Quantidade Vendida: {produto_menos_vendido['quantidade_vendida']}")
    print(f"  Preço para o Usuário: R${produto_menos_vendido['preco_usuario']:.2f}")
    print(f"  Receita: R${produto_menos_vendido['preco_usuario'] * produto_menos_vendido['quantidade_vendida']:.2f}")

# Exemplo de uso
produtos = [
    {
        'nome': 'Produto A',
        'preco_original': 100.0,
        'preco_usuario': 80.0,
        'quantidade_vendida': 10
    },
    {
        'nome': 'Produto B',
        'preco_original': 150.0,
        'preco_usuario': 120.0,
        'quantidade_vendida': 5
    },
    {
        'nome': 'Produto C',
        'preco_original': 200.0,
        'preco_usuario': 180.0,
        'quantidade_vendida': 8
    }
]

# Chamar a função para identificar produtos mais e menos vendidos
identificar_produtos_vendidos(produtos)