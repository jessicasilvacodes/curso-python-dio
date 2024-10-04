#

def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


# ... outras operações

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação = {resultado}")



sum = somar
mult = multiplicar

print(sum(3, 6))
print(mult(3, 6))

