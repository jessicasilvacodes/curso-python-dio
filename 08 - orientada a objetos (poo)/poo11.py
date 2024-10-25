#interfaces e classes abstratas

from abc import ABC, abstractmethod, abstractproperty     #importar modulo pois python não fornece classe abstrata por padrão


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("ON!")

    def desligar(self):
        print("Desligando a TV...")
        print("OFF!")

    @property
    def marca(self):
        return "// Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("ON!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("OFF!")

    @property
    def marca(self):
        return "// LG"


controle = ControleTV()

controle.ligar()
print(controle.marca)
controle.desligar()

#---

controle = ControleArCondicionado()

controle.ligar()
print(controle.marca)
controle.desligar()
