#clear = limpar

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
print(contatos)



#copy = copiar = manipular sem alterar os dados do original

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia_contatos = contatos.copy()
copia_contatos["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  
print(copia_contatos["guilherme@gmail.com"]) 



#fromkeys = cria chaves 

resultado = dict.fromkeys(["nome", "telefone"])     #vazias, sem atribuir valor
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")     #com valores padrão
print(resultado)



#get = verificar se uma chave existe ou não no dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.get("chave")  #não encontra = None
print(resultado)

resultado = contatos.get("chave", {})  #não encontra = devolve vazio = {}
print(resultado)

resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)



#items = retorna lista de tuplas = útil p/ usar no comando for

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items() 
print(resultado)



#keys = retorna somente as chaves

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()
print(resultado)
