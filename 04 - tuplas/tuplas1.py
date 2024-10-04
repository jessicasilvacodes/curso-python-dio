#declarando tuplas

frutas = ("maçã", "laranja", "uva", "pera",)      #a vírgula no final difere listas de tuplas (quando se usa parentese)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])     #tupla de lista de números
print(numeros)

pais = ("Brasil",)
print(pais)



#acessando valores

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas)
print(frutas[0]) 
print(frutas[2]) 
print(frutas[-1])



#matriz =igual listas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0]) 
print(matriz[0][-1])  
print(matriz[-1][-1])  



#fatiamento =igual listas

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:]) 
print(tupla[:2])  
print(tupla[1:3]) 
print(tupla[0:3:2])
print(tupla[::])  
print(tupla[::-1]) 
