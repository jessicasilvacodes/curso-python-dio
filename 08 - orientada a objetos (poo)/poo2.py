'''
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João informe a cor, modelo, ano e valor da bicicleta vendida. 
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
'''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Bi bi")

    def parar(self):
        print("Stop")

    def correr(Self):
        print("Go")

    def __str__(self):
        return f"Bicicleta = cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor:.2f}, aro: {self.aro}"

    
bike1 = Bicicleta("azul", "Caloi", "2005", 3500, "16")
bike2 = Bicicleta("vermelha", "Monark", "2008", 2520)

#função buzinar
bike1.buzinar()

#função parar
bike2.parar()

#função correr
bike2.correr()

print(bike1)
print(bike2)
