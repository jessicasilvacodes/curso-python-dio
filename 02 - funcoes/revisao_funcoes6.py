#

def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def test(a, b):
    return a*2 + b*3

# ... outras operações

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação = {resultado}")



exibir_resultado(2, 7, somar)
exibir_resultado(2, 7, multiplicar)
exibir_resultado(2, 7, test)
