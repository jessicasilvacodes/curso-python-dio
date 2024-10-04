#métodos - classe list

#append -adiciona itens
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)


#clear -limpar lista
lista = [1, "Python", [40, 30, 20]]
print(lista)

lista.clear()
print(lista)


#copy -copia a lista
lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)
print(lista2)


#count -quantas vezes o objeto aparece
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  
print(cores.count("azul")) 
print(cores.count("verde")) 


#extend -juntar listas (vários valores)
linguagens = ["python", "js", "c"]
print(linguagens) 

linguagens.extend(["java", "csharp"])
print(linguagens) 


#index -qual index está o objeto (primeira ocorrencia)
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java")) 
print(linguagens.index("python")) 


#pop -retirar os ultimos itens
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens) 
print(linguagens.pop()) 
print(linguagens) 
print(linguagens.pop()) 
print(linguagens) 
print(linguagens.pop()) 
print(linguagens) 
print(linguagens.pop(0))
print(linguagens) 


#remove -retirar o objeto específico
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens) 

linguagens.remove("c")
print(linguagens)


#reverse -espelhar a lista
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)

linguagens.reverse()
print(linguagens)


#sort -ordem alfabetica
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #espelhamento da ordem
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  #ordem de tamanho da palavra
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  #espelhamento da ordem de tamanho da palavra
print(linguagens)


#len -quantos caracters(itens) tem
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5


#sorted
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

