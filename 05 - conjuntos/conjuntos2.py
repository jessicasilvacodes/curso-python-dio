#union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)



#intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)



#difference = tudo que tem em um conjunto e não tem no outro

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)



#symmetric difference = todos os elementos que não estão na intersecção

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)



#issubset = um conjunto é subconjunto de outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  #todos os elementos da a estão em b? True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  #todos os elementos de b estão em a? False
print(resultado)



#issuperset = ao contrário

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  #todos os elementos de b estão em a? False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  #todos os elementos de a estão em b? True
print(resultado)



#isdisjoint = operação de conjunto disjunto = conjuntos que não tem intersecção

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
