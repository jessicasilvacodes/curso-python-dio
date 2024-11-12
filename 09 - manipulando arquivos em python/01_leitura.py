arquivo = open(
    "09 - manipulando arquivos em python\lorem.txt", "r")

# print(arquivo.read())
# print(arquivo.readline())

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
