arquivo = open("09 - manipulando arquivos em python/teste.txt", "w")


arquivo.write("Escrevendo dados em um novo arquivo...")

arquivo.writelines(['\nEscrevendo ',
                    'um ',
                    'novo ',
                    'texto.'])

arquivo.close()
