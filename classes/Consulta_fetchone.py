import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f"Nome: {resultado[0]}\nTelefone{resultado[1]}")
cursor.close()
conexão.close()


""" Uso de With para fechar conexão, esse programa é equivalente ao de cima"""


from contextlib import closing
with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break 
            print(f"Nome: {resultado[0]}\nTelefone{resultado[1]}")