#polimorfismo = mesmo método com comportamento diferente, NÃO é possível sem herança

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


#recebo o objeto, mas tem que ter o 'voar' implementado, ou seja, nesse caso, todo objeto é um filho de passaro
def plano_voo(obj):
    obj.voar()

'''
p0 = Passaro()
p1 = Pardal()
p2 = Avestruz()

plano_voo(p0)
plano_voo(p1)
plano_voo(p2)
'''

#exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

plano_voo(Passaro())
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())

