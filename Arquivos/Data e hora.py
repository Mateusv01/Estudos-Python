""" Python possui os tipos datetime e time no módulo também chamado datetime
    Esse módulo define uma série de operações para auxiliar a manipulação de
    datas e horas. O tipo datetime representa uma data e uma hora, o tipo date
    apenas uma data e time apenas a hora"""


import datetime

print(datetime.date.today())

print(datetime.datetime.now())

print(datetime.datetime.now().time())

""" Podemos acessar o dia, o mês e o ano como propriedades da data:"""


data = datetime.datetime.today()

print(data.day)
print(data.month)
print(data.year)

""" O tipo datetime, além das propriedades da data(date), permite acessar a hora, os minutos
    e os segundos idependentemente """

momento = datetime.datetime.now()
print(momento.date())
print(momento.time())
print(momento.hour)
print(momento.minute)
print(momento.second)
print(momento.microsecond)
print(momento.weekday()) # No caso 3 representa quinta e começamos a contar 0 apartir de segunda
print(momento.isoweekday()) # quinta é 4 e começamos a contar a partir do 0

""" Uma conversão muito usada na web e principalmente para converter data e hora
    em sring é o formato ISO 8601:"""

print(momento.isoformat())

""" Podemos calcular valores futuros ou passados usando timedelta"""

daqui_a_90_dias = momento + datetime.timedelta(days=90)
print(daqui_a_90_dias)


""" Para evitar repetir o nome datetime, você também pode importar apenas o
    tipo que for usar"""

from datetime import datetime
print(datetime.now())