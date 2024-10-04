#pop = remove uma CHAVE do dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos)

resultado = contatos.pop("guilherme@gmail.com") 
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  #se não existir, retorna um valor padrão = vazio = {}
print(resultado)



#popitem = não informa a chave e retira os itens na sequencia

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos)

resultado = contatos.popitem() 
print(resultado)




#setdefault = se o atributo nao estiver no dicionario, ele adiciona com o valor que eu coloquei; se existir, ele retorna o valor que já existe e não altera

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna") 
print(contato)  

contato.setdefault("idade", 28)  
print(contato)  



#update = atualiza o dicionário com outro dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos)

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})     #nova chave  que não existia antes, então vai incorporar
print(contatos)



#values = retorna todos os valores sem saber as chaves

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (contatos.values())
print(resultado)



#in = verificar se uma chave existe ou não dentro do dicionario

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)



#del = vou passar o objeto que eu quero remover

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)
