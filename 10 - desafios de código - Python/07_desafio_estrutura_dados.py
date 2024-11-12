'''

DESAFIO DIO - Estrutura de Dados com Python

Descrição:
Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

Detalhamento:

Função elementos_comuns:
1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/introduction.html#lists

Entrada:
Duas listas de inteiros separados apenas por espaço, por exemplo: 1 2 3 4 e 3 4 5 6.

Saída:
Uma lista com os elementos comuns, por exemplo: [3, 4]. Caso a entrada seja diferente do esperado, retorne: "Entrada inválida."

'''

def elementos_comuns(lista1, lista2):
    try:
        lista1 = list(map(int, lista1.split()))
        lista2 = list(map(int, lista2.split()))
        
        comuns = list(set(lista1) & set(lista2))
        
        return comuns if comuns else []
    
    except ValueError:
        return "Entrada inválida."


entrada1 = input("Digite os números inteiros da primeira lista separados por espaço: ")
entrada2 = input("Digite os números inteiros da segunda lista separados por espaço: ")

resultado = elementos_comuns(entrada1, entrada2)


if resultado == "Entrada inválida.":
    print(resultado)
elif not resultado:
    print("Não há elementos comuns.")
else:
    print(f"Elementos comuns às duas listas: {resultado}")

