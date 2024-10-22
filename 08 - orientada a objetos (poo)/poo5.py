#encapsulamento, variavel publica e privada (_ na frente)

class Conta:
    def __init__(self, num_agencia, saldo=0):
        self._saldo = saldo 
        self.num_agencia = num_agencia

    def depositar(self, valor):
        self._saldo += valor
        pass

    def sacar(self, valor):
        self._saldo -= valor
        pass

    def mostrar_saldo(self):      #função para acessar variavel privada
        return self._saldo

conta = Conta("0001", 100)    #num agencia e saldo

conta.depositar(150)
conta.sacar(20)

print(conta.num_agencia)
print(conta.mostrar_saldo())
