'''

DESAFIO DIO - Fundamentos - Python

Descrição:
Neste desafio, você deve escreva uma solução que receba um número inteiro como entrada e determine se ele é par ou ímpar. Dessa forma, a solução deve retornar uma string indicando Par se o número for par e Ímpar se o número for ímpar.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada:
A entrada do programa é um único número inteiro.

Saída:
A saída do programa é uma string que será Par se o número for par e Ímpar se o número for ímpar.
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
      return "Par"
    else:
      return "Ímpar"

numero = int(input("Digite um número: "))

print(par_ou_impar(numero))
