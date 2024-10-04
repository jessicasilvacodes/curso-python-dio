# 

def exibir_poema(data_extenso, *args, **kwargs): #data, lista de versos, informaçoes de autor etc
    texto = "\n".join(args) #valores de args concatenados com \n = um valor em cada linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) #adicionando um dicionário chave x valor e colocando pra cada chave, um valor = .items pq é um dicionário
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-feira, 26 de agosto de 2022", "Zen of Python", "Beautiful os better than ugly.", "...", autor = "Tim Peters", ano = 1999) #valores separados por vírgula = tupla = entra em valores de args // quando começa chave x valor = kwargs

