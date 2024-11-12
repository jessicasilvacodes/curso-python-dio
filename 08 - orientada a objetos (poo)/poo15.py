#primeiro decorador 

'''
def meu_decorador(funcao):
    def envelope():
        print("...faz algo antes de executar")
        funcao()
        print("...faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo():
    print("Hello World!")


ola_mundo()
'''

def meu_decorador(funcao):
    def envelope():
        print("...faz algo antes de executar")
        funcao()
        print("...faz algo depois de executar")

    return envelope


def ola_mundo():
    print("Hellow World!")


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

