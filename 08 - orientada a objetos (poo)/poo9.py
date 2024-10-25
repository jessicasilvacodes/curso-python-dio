#interfaces e classes abstratas
#variaveis de classe e instacia

class Estudante:
    escola = "DIO"     #variaveis de classe = sao unicas pra todos os ojetos

    def __init__(self, nome, matricula):     #variaveis de instancia = cada objeto tem uma copia
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} | {self.matricula} | {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Jessica", 12345)
aluno_2 = Estudante("Gabriela", 23785)

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "PUC"     #classe = altera pra todos
aluno_3 = Estudante("Carolina", 84693)

mostrar_valores(aluno_1, aluno_2, aluno_3)

#também troca os valores da 'escola' dos outros objetos, pois trocou a variável de classe, e não de instancia

aluno_2.escola = "Python"     #objeto = troca somente esse objeto 
mostrar_valores(aluno_1, aluno_2, aluno_3)

Estudante.nome = "Maria"     #não altera pois o nome não é variavel de classe
mostrar_valores(aluno_1, aluno_2, aluno_3)

# SELF = instancia !!!
