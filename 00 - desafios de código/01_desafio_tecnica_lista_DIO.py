def analise_vendas(vendas):
    # Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return total_vendas, media_vendas


def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha:
    vendas = input()
    # Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, vendas.split(',')))
    return vendas


# Função principal que chama as outras funções:
def main():
    # Obtém a lista de vendas:
    vendas = obter_entrada_vendas()
    # Calcula o total e a média:
    total_vendas, media_vendas = analise_vendas(vendas)
    print(f'{total_vendas}, {media_vendas:.2f}')
    

# Chama a função principal:
if __name__ == "__main__":
    main()
