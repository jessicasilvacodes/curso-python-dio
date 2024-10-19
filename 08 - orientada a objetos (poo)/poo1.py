
class Cachorro:
    def __init__(self, nome, cor, acordado=True):           #metodo construtor
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

#   def __del__(self):     #metodo destrutor
#       print("Removendo a instância da classe.")

    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado = False
        print('Zzzz...')

cao1 = Cachorro("Zé", "amarelo", False)
cao2 = Cachorro("Bob", "branco e preto")


#função latir:
cao1.latir()
cao2.latir()


#função dormir:
print(cao2.acordado)
cao2.dormir()
print(cao2.acordado)
