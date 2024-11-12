'''
Treinando Orientação a Objetos com Python

3 / 3 - Conversor de Temperatura com POO

Descrição:
Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. A fórmula para converter de Celsius para Fahrenheit é:

Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32

Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/classes.html
https://docs.python.org/pt-br/3/library/stdtypes.html#methods

Entrada:
O programa deverá receber como entrada uma temperatura em graus Celsius fornecida pelo usuário.

Saída:
O programa deverá exibir a temperatura convertida para Fahrenheit.

'''

#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
    # Método para converter de Celsius para Fahrenheit
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Entrada do usuário
celsius = float(input("Informe a temperatura em Celsius (°C): "))

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(f"{fahrenheit:.2f} °F")
