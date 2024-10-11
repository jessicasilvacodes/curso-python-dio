'''
DESAFIO DIO - Aplicando Técnicas de Listas em Python

Análise de Vendas com Listas

Descrição:

Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.

Detalhamento:

Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.

Entrada
Uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano.

Saída
Um único número inteiro representando o total de vendas e um número decimal representando a média mensal de vendas, separados por um espaço.
'''


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

