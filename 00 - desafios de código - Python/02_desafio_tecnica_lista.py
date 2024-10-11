'''
DESAFIO DIO - Aplicando Técnicas de Listas em Python

Identificando os Produtos Mais Vendidos

Descrição:

Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido, que será usado para destacar produtos populares no relatório do Power BI.

Detalhamento:

Encontre o produto com a maior contagem:

Itere sobre o dicionário contagem, que contém a contagem de cada produto.

Compare a contagem atual com a contagem máxima armazenada em max_count.

Se a contagem atual for maior que max_count, atualize max_count e defina max_produto como o produto atual.

Converter a entrada em uma lista de strings, removendo espaços extras:

Use o método split(',') para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.

Utilize uma list comprehension para remover espaços em branco extras ao redor de cada string, usando o método strip().

Entrada
Uma lista de strings onde cada string representa o nome de um produto vendido.

Saída
A string com o nome do produto mais vendido. Se houver empate, retorne qualquer um dos produtos mais vendidos.
'''


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
    entrada = input("Insira os produtos vendidos (separados por vírgula): ")
    # Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = [produto.strip() for produto in entrada.split(',')]
    return produtos


# Executando a função:
produtos = obter_entrada_produtos()

print(produto_mais_vendido(produtos))
