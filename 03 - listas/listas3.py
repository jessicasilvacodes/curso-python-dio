#interar listas

carros = ["Gol", "Celta", "Palio"]

for carro in carros:
    print(carro)


#função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
