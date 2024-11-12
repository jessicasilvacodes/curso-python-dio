'''

Explorando Técnicas de POO com Python

1 / 2 - Criando Classes para Dados de Vendas

Descrição:
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

Classe Venda:
Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

Classe Relatorio:
Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.

Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

Função main:
Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.

Entrada:
A entrada consiste em dados de vendas com as seguintes colunas:

Produto (string)
Quantidade (inteiro)
Valor (decimal)

Saída:
A saída é o total de vendas calculado pela classe Relatorio.
'''

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        if isinstance(venda, Venda):
          self.vendas.append(venda)
        else:
          print('Erro: o objeto não é uma instância de venda.')
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
            # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
          total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade: "))
        valor = float(input("Informe o valor unitário: "))
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: R$ {total_vendas:.1f}")


if __name__ == "__main__":
    main()

