from datetime import datetime, timedelta, timezone

import pytz     #fuso horários do mundo

data_ES = datetime.now(pytz.timezone("Europe/Madrid"))   #+2
data_BR = datetime.now(pytz.timezone("America/Sao_Paulo"))    #-3

print(data_ES)
print(data_BR)

print("-"*32)

data_madrid = datetime.now(timezone(timedelta(hours=2), 'ESPANHA'))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), 'BRASIL'))

print(data_madrid)
print(data_sao_paulo)
