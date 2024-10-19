class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return self.cor
    
    def __str__(self):
        return f"Veículo: {self.__class__.__name__} = cor: {self.cor}, placa: {self.placa}, num_rodas: {self.num_rodas}"
    

class Motocicleta(Veiculo):      
    pass

class Carro(Veiculo):       
    pass 

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não estou carregado."}")


moto = Motocicleta("prata", "ABC-1234", 2)

carro = Carro("vermelho", "DEF-5678", 4)

caminhao = Caminhao("verde", 
"HIG-8585", 8, carregado=False)

print(moto)
print(carro)
print(caminhao)

