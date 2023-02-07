"""     Vejamos agora como incluir os outros telefones de nossa agenda. O programa seguinte apresenta o método
    executemany. A principal diferença entre o executemany e o execute é que o executemany trabalha com varios
    valores.  """


#import sqlite3
#dados = [("João" ,"9999-9999"),
#        ("André", "0009-9980"),
#       ("Maria", "8981-8393")]
#conexão = sqlite3.connect("agenda.db")
#cursor = conexão.cursor()
#cursor.executemany('''
#            insert into agenda (nome, telefone)
#            values(?, ?)
#            ''', dados)
#conexão.commit()
#cursor.close()
#conexão.close()

""" Com os dados inseridos no programa vamos imprimir o conteúdo de nossa tabela"""

import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall() #1
for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}") #2

cursor.close()
conexão.close()


"""
    Em (1) ultilizamos o método fetchall de nosso cursor para retornar uma lista com resultados de nossa
    consulta. 
    
    Em (2) ultilizamos a variável registro para exibir os dados. Assim como no método executemany, que
    aceita uma lista de tuplas como parâmetro, fetchall retorna uma lista de tuplas. 

    Para consultas pequenas, contendo poucos registros como resultado, o método fetchall é muito interessante
    e fácil de ultilizar. Para consultas maiores, em que mais de 100 registros são retornados, outros métodos
    de obter os resultados da consulta podem ser mais interessantes

    O programa seguinte mostra o método fetchone sendo usado dentro de um while. Como não sabemos quantos
    registros vão ser retornados vamos usar while True


    Podemos ler fetch como Obter: logo fetchone é obter um resultado e fatchall obter todos os resultados
"""

