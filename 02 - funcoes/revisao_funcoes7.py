#

salario = 3500

def salario_bonus(bonus):
    global salario    # variavel local na função é inexistente = pegar variavel no global (fora da função)
    salario += bonus
    return salario


salario_com_bonus = (salario_bonus(500))
print(salario_com_bonus)                     
