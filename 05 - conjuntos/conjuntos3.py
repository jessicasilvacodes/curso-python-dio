#add

sorteio = {1, 23}

sorteio.add(25)
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25)  #elemento já existe, então foi ignorado
print(sorteio)



#clear = limpar

sorteio = {1, 23}
print(sorteio) 

sorteio.clear()
print(sorteio)



#copy = copiar

sorteio = {1, 23}
print(sorteio) 

sorteio.copy()
print(sorteio)  



# discard = descartar um valor

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  

numeros.discard(1)
numeros.discard(45)   #não existe esse valor, então é ignorado
print(numeros)  



#pop = retira os valores da lista = valores da frente

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) 
print(numeros.pop()) 
print(numeros.pop()) 
print(numeros)



#remove = retira o valor que voce quer (se o elemento não existe, ele da um erro)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  
print(numeros.remove(5)) 
print(numeros) 



#len = verifica o tamanho do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  



#in = verifica se está presente no conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros) 
print(10 in numeros)
