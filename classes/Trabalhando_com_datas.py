""" Embora o SQLite trabalhe com datas, o tipo DATE não é suportado diretamente, gerando uma certa confusão entre datas e
strings.

Criando uma tabela com um campo tipo data no brasil.db

"""
import sqlite3
from contextlib import closing
#feriados = [["2023-01-01", "Confraternização Universal"], ["2023-04-21", "Tiradentes"], ["2023-05-01", "Dia do trabalhador"], ["2023-09-07", "Independência"], ["2023-10-12", "Padroeira do Brasil"], ["2023-11-02", "Finados"], ["2023-11-15", "Proclamação da República"], ["2023-12-25", "Natal"] ]
#with sqlite3.connect("brasil.db") as conexão:
#    conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
#    conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)

""" Observe que o formato está escrito no formato ISO (ANO-MES-DIA)

    Acessando os valores no programa:
"""


with sqlite3.connect("brasil.db") as conexão:
    for feriado in conexão.execute("select * from feriados"):
        print(feriado)
    print(" " * 40)


""" Acessamos o campo data como fazemos até então. Veja uqe ao imprimir a tupla feriado o campo data foi impresso
como uma string qualquer 

Vamos modificar nossa conexão de forma a solicitar o processamento dos tipos de campo em nossas consultas:
"""

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    for feriado in conexão.execute("select * from feriados"):
        print(feriado)
print("=" *40)
""" Veja que os campos de data agora são objetos de classe datetime.date 
Agora vamos usar o strftime para exibir apenas o mes e a data, sem o ano
"""

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    conexão.row_factory = sqlite3.Row
    for feriado in conexão.execute("select * from feriados"):
        print("{0} {1}".format(feriado["data"].strftime("%d/%Y"), feriado["descrição"]))

 
""" O programa a seguir usa o módulo datetime"""
print("=" *40)
import datetime

hoje = datetime.date.today()
hoje60dias = hoje + datetime.timedelta(days=60)

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    conexão.row_factory = sqlite3.Row
    for feriado in conexão.execute("select * from feriados where data >= ? and data <= ?", (hoje, hoje60dias)):
        print("{0} {1}".format(feriado["data"].strftime("%d/%m"), feriado["descrição"]))





# Alterando as datas 
with sqlite3.connect("brasil.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""update feriados
                            set data = '2023-12-25'
                            where data = '2014-12-25' """)
        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexão.commit()
            print("Alterações gravadas")
        else:
            conexão.rollback()
            print("Alterações abortadas")