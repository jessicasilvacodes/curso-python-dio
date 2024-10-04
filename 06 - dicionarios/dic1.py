
#declarando dicionarios

pessoa = {"nome": "Guilherme", "idade": 28}     #forma 1
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)     #forma 2
print(pessoa)

pessoa["telefone"] = "3333-1234"     #adicionar informações a 'pessoa'
print(pessoa)



#acessando dados

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(dados)

print(dados["nome"]) 
print(dados["idade"]) 
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}



#dicionarios alinhados = um dicionario dentro do outro

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)



#interando dicionarios

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

'''
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)
'''


for chave, valor in contatos.items():     #melhor forma 
    print(chave, valor)

