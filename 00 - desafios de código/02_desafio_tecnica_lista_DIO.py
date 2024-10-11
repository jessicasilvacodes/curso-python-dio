def produto_mais_vendido(produtos):
    # Cria um dicionário para armazenar a contagem de cada produto:
    contagem = {}
    
    for produto in produtos:
        # Verifica se o produto já está no dicionário de contagem:
        if produto in contagem:
            # Se o produto já existe, incrementa a contagem em 1:
            contagem[produto] = contagem[produto] + 1
        else:
            # Se o produto não existe, inicializa a contagem em 1:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # Encontre o produto com a maior contagem:
    for produto, count in contagem.items():
        # Compara a contagem atual com a contagem máxima armazenada:
        if count > max_count:
            max_count = count
            max_produto = produto
    return max_produto


def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = [produto.strip() for produto in entrada.split(',')]
    return produtos


# Executando a função:
produtos = obter_entrada_produtos()

print(produto_mais_vendido(produtos))
