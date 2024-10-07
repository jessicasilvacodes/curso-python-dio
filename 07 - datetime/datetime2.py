from datetime import date, datetime, timedelta

# timedelta = operações matemáticas com as datas

# exemplo: manipulação de um lavajato 

tipo_carro = "G"  # P, M ou G
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f"O carro chegou às: {data_atual} e ficará pronto às: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f"O carro chegou às: {data_atual} e ficará pronto às: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f"O carro chegou às: {data_atual} e ficará pronto às: {data_estimada}")
