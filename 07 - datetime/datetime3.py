from datetime import datetime

#convertendo a data para o formato brasileiro

data_hora_atual = datetime.now()
data_hora_nasc_str = "1993-11-25 22:30"
mascara_ptbr = "%d/%m/%Y %a %H:%M"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual)
print(data_hora_atual.strftime(mascara_ptbr))

print("-"*25)

data_str_convertida = datetime.strptime(data_hora_nasc_str, mascara_en)
print(data_hora_nasc_str)
print(data_str_convertida.strftime("%d/%m/%Y %a %H:%M"))

#obs: os dias da semana continuam em inglês
