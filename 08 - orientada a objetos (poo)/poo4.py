
class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"ANIMAL - {self.__class__.__name__}: {' | '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_pena, cor_bico, **kw):
        self.cor_pena = cor_pena
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Arara(Ave):
     def __init__(self, num_patas, cor_pena, cor_bico):
        super().__init__(num_patas=num_patas, cor_pena=cor_pena, cor_bico=cor_bico)


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, num_patas, cor_pena, cor_bico, cor_pelo):
        super().__init__(num_patas=num_patas, cor_pena=cor_pena, cor_pelo=cor_pelo, cor_bico=cor_bico)


cao = Cachorro(num_patas=4, cor_pelo="preto")
print(cao)

gato = Gato(num_patas=4, cor_pelo="laranja")
print(gato)

leao = Leao(num_patas=4, cor_pelo="amarelo")
print(leao)

arara = Arara(num_patas=2, cor_pena="azul e amarelo", cor_bico="preto")
print(arara)

ornito = Ornitorrinco(num_patas=2, cor_pelo="marrom", cor_pena="n/a", cor_bico="amarelo")
print(ornito)

