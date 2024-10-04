
#declarando listas

frutas = ["laranja", "maca", "uva"]
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])   #ultimo elemento
print(frutas[-3])   #primeiro elemento


verduras = []
print(verduras)


letras = list("python")
print(letras)


numeros = list(range(10))
print(numeros)


carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


#matrizes

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])    # 1, "a", 2]
print(matriz[0][0])    #1
print(matriz[0][-1])    #2
print(matriz[-1][-1])    #"c"
print(matriz[2][0])   #6
