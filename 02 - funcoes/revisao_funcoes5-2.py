# positional and keyword only

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel): # valor de MARCA está hibrido, pode ser por posição ou por nome
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # valido


criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") # valido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # invalido

