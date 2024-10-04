#interar tuplas =listas

carros = (
    "Gol",
    "Celta",
    "Palio",
)

#modo 1
for carro in carros:
    print(carro)

#modo 2
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



#count

cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho")) 
print(cores.count("azul")) 
print(cores.count("verde")) 



#index

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))
print(linguagens.index("python"))



#len

linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens))  # 5
