""" Álem de inserir consultar e alterar registros podemos também apagá-los. O comando 
delete apaga registros com base em um critério de seleção especificando na cláusula where

Sintaxe do comando delete:
    delete from agenda where nome = 'Maria' """

import sqlite3
from contextlib import closing

#with sqlite3.connect("agenda.db") as conexão:
#    with closing(conexão.cursor()) as cursor:
#        cursor.execute("""delete from agenda
 #                                   where nome = 'Maria'""")
  #      print("Registros apagados: ", cursor.rowcount)
   #        print("Alterações salvas")
   #     else:
     #       conexão.rollback()
      #      print("Alterações abortadas")



""" ============================ Simplificando o acesso sem cursores ============================="""


''' A interface de banco de dados do Python permite executar comandos ultilizando o objeto diretamente da conexão sem um cursor'''

with sqlite3.connect("agenda.db") as conexão: 
    for registro in conexão.execute("select * from agenda"):
        print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")


""" Usamos a estrutura with para facilitar o fechamento da conexão. Em conexão.execute retorna um cursor que pode ser
usado com for. Você pode também usar o método executemany diretamente com o objeto conexão.

Mas essa ultilização simplificada pode atrapalhar quando migramos para outro banco de dados, sendo assim é importante
usar cursores


"""

"""=================================== Acessando os campos como em um dicionário ================================"""

''' Acessar campos por posição nem smpre é fácil. Em Python, usando SQLite, podemos acessá-los pelo nome, adicionando uma linha

    conexão.row_factory = sqlite3.Row'''

with sqlite3.connect("agenda.db") as conexão:
    conexão.row_factory = sqlite3.Row
    with closing(conexão.cursor()) as cursor:
        for registro in cursor.execute("select * from agenda"):
            print(f"Nome: {registro['nome']}\nTelefone: {registro['telefone']}")


""" Dessa forma o registro pode ser acessado como se fosse um dicionário, no qual o nome do campo é usado
como uma chave. Outra facilidade que essa linha traz é que as chaves são aceitas independentemente se escrevemos
o nome dos campos em maiúsculas ou minúsculas"""

