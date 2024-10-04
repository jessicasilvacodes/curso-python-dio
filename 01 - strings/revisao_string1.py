# aula de strings

curso = "     Python "

print(curso.strip()) # remove espaços em branco

print(curso.lstrip()) # left

print(curso.rstrip()) # right

curso2 = "Python"

print(curso2.center(10, "#")) # centralizado e com caracters 

print(".".join(curso2)) # juntar na string. comum em listas

# 

nome = "Jessica Silva"

print(nome.upper())
print(nome.lower())
print(nome.title())

for letra in nome:
    print(letra, end="-")

print("-".join(nome))
