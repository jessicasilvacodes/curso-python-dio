#declarando

#objeto tipo set (ou não) = elimina elementos duplicados na lista
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros) 

letras = set("abacaxi")
print(letras) 

carros = set(("palio", "gol", "celta", "palio"))
print(carros) 

linguagens = {"python", "javascript", "python"}
print(linguagens)



#precisa converter em lista para acessar os índices
numeros = {1, 2, 3, 2}
numeros = list(numeros)

print(numeros)
print(numeros[0])



#interando conjuntos

carros = {"Gol", "Celta", "Palio"}

for carro in carros:     #posso percorrer um set interando ele em um for
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

