#import sqlite3
#conexão = sqlite3.connect("preço.db")
#cursor = conexão.cursor()
#cursor.execute('''
#        create table preço(
#            nome text,
#            preço numeric)
 #       ''')
#cursor.execute('''
#        insert into preço (nome, preço)
#            values(?, ?)
#            ''',("Batata", "4.20"))
#cursor.execute('''
#        insert into preço (nome, preço)
#            values(?, ?)
#            ''',("Maça", "2.70"))
#cursor.execute('''
 #       insert into preço (nome, preço)
#            values(?, ?)
#            ''',("Abóbora", "8.90"))
#conexão.commit()
#cursor.close()
#conexão.close()
import sqlite3
from contextlib import closing
with sqlite3.connect("preço.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from preço")
        for resultado in cursor.fetchall():
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))