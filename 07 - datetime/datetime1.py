from datetime import date, datetime, time

# https://docs.python.org/3/library/datetime.html

data_nascimento = date(1993, 11, 25)     # ano, mês e dia
print(data_nascimento)

data_hora_nascimento = datetime(1993, 11, 25, 22, 30, 00)
print(data_hora_nascimento)

hora_nascimento = time(22, 30, 00)
print(hora_nascimento)

data_hoje = date.today()
print(data_hoje)

data_hora_hoje = datetime.today()
print(data_hora_hoje)
