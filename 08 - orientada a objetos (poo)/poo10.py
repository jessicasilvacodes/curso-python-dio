#metodos de classe e metodos estaticos
#são ligado a classe e não ao objeto


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod       #metodo de classe = recebe primeiro parametro que aponta para a classe
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod     #não recebe um primeiro argumento explicito, e não pode acessar e nem modificar 
    def e_maior_idade(idade):
        return idade >= 18

p1 = Pessoa("Jessica", 30)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_data_nascimento(1993, 11, 25, "Jessica")
print(p2.nome, p2.idade)

p3 = Pessoa.e_maior_idade(30)
print(p3)

#---
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

