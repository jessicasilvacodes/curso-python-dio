def analise_vendas(vendas):
    # Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return total_vendas, media_vendas


def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha:
    vendas = input("Digite as vendas mensais separadas por vírgula: ")
    # Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, vendas.split(',')))
    return vendas


# Função principal que chama as outras funções:
def main():
    # Obtém a lista de vendas:
    vendas = obter_entrada_vendas()
    # Calcula o total e a média:
    total_vendas, media_vendas = analise_vendas(vendas)
    
    # Exibe os resultados:
    print(f"Total de vendas: {total_vendas}")
    print(f"Média mensal de vendas: {media_vendas:.2f}")
    return total_vendas, media_vendas


# Chama a função principal:
if __name__ == "__main__":
    main()

