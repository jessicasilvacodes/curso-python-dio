#

def salvar_carro(marca, modelo, ano, placa): # salva o carro no banco de dados
    print(f'Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}')


# passando os valores de forma sequencial
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# conjuntos chave-valor = evita troca de valores
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# forma de dicionário = ** = kwargs = dicionário (quando se coloca somente 1 *, os valores vem em tupla e são chamados de args)
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

