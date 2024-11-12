# decorador retorna função decorada 

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("...faz algo antes de executar")
        funcao(*args, **kwargs)
        print("...faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Hellow World, {nome}!")


ola_mundo("Jessica", 1000)
