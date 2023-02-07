""" Até agora trabalhamos com apenas campos normais, ou seja, campos que contém dados. Confome a nossa tabela
crescem, trabalhar com os dados pode não ser a melhor solução, e precisamos acrescentar campos para manter o banco
de dados. Uma dessas necessidades é indentificar cada registro de maneira única

Uma alternativa do SQLite é a geração automática de chaves. Nesse caso o banco se encarrega de criar números únicos 
para cada registro 

Sintaxe da criação da chave primária:
        create table estados(id integer primary key autoincrement,
                             nome text, população integer)
                             
                             
Ao criarmos a tabela estados, estamos especificando três campos: id, nome e população
Id e população são do tipo integer ou seja números inteiros (int)
id é o campo que escolhemos para ser a chave primária dessa tabela 
escrevemos primary key autoincrement para que o SQLite gere esses números 

O programa a seguir cria o banco de dados brasil.db, a tabela estados e também inclui o nome da população
"""

import sqlite3
from contextlib import closing
#dados = [["São Paulo",43663672],["Minas Gerais",20593366],["Rio de Janeiro",16369178],["Bahia",15044127],["Rio Grande do Sul",11164050],["Paraná",10997462],["Pernambuco",9208511],["Ceará",8778575],["Pará",7969655],["Maranhão",6794298],["Santa Catarina",6634250],["Goiás",6434052],["Paraíba",3914418],["Espírito Santo",3838363],["Amazonas",3807923],["Rio Grande do Norte",3373960],["Alagoas",3300938],["Piauí",3184165],["Mato Grosso",3182114],["Distrito Federal",2789761],["Mato Grosso do Sul",2587267],["Sergipe",2195662],["Rondônia",1728214],["Tocantins",1478163],["Acre",776463],["Amapá",734995],["Roraima",488072]]

#with sqlite3.connect("brasil.db") as conexão:
#    conexão.row_factory = sqlite3.Row
 #   with closing(conexão.cursor()) as cursor:
 #       cursor.execute("""create table estados(
  #                              id integer primary key autoincrement,
 #                               nome text,
  #                              população integer
  #                       )""")
 #   cursor.executemany("insert into estados(nome, população) values(?, ?)", dados)
#conexão.commit()
#cursor.close()
#conexão.close()


""" O valor do campo id será gerado automaticamente. Uma vez que temos a população dos estados, vamos fazer uma consulta"""


conexão = sqlite3.connect("brasil.db")
conexão.row_factory = sqlite3.Row
print("%3s %-20s %12s %12s %12s" % ("Id","Estado","População","Sigla","Região"))
print("="*67)
for estado in conexão.execute("select * from estados order by população desc"):
    print( "%3s %-20s %12s %12s %12s" %
          (estado["id"],
           estado["nome"],
           estado["população"],
           estado["sigla"],
           estado["região"]))
conexão.close()


""" Modifiquei a tabela para os estados sejam impressos pela população usando no select
    e colocando em ordem descrescente (desc) logo após o nome do campo """


"""================================= ALTERANDO TABELA ===================================


Vamos acrescentar mais alguns campos a nossa tabela de estados. Um campo para região do Brasil e outro para sigla do estado
em SQL o comando usado para alterar os campos de uma tabela é o alter table

    alter table estados add sigla text
    alter table estados add região text

Os comandos alter table do SQLite é limitado se comparado a outros bancos de dados, assim sendo obrigados a alterar os campos
um por um. Por isso é importante pensar muito bem as tabelas em SQLite para não precisar adicionar tudo

"""

#with sqlite3.connect("brasil.db") as conexão:
 #   conexão.execute("""alter table estados
#                       add sigla text""")
#    conexão.execute("""alter table estados
#                       add região text""")
#
dados = [["SP", "SE", "São Paulo"], ["MG", "SE", "Minas Gerais"], ["RJ", "SE", "Rio de Janeiro"], ["BA", "NE", "Bahia"], ["RS", "S", "Rio Grande do Sul"], ["PR", "S", "Paraná"], ["PE", "NE", "Pernambuco"], ["CE", "NE", "Ceará"], ["PA", "N", "Pará"], ["MA", "NE", "Maranhão"], ["SC", "S", "Santa Catarina"], ["GO", "CO", "Goiás"], ["PB", "NE", "Paraíba"], ["ES", "SE", "Espírito Santo"], ["AM", "N", "Amazonas"], ["RN", "NE", "Rio Grande do Norte"], ["AL", "NE", "Alagoas"], ["PI", "NE", "Piauí"], ["MT", "CO", "Mato Grosso"], ["DF", "CO", "Distrito Federal"], ["MS", "CO", "Mato Grosso do Sul"], ["SE", "NE", "Sergipe"], ["RO", "N", "Rondônia"], ["TO", "N", "Tocantins"], ["AC", "N", "Acre"], ["AP", "N", "Amapá"], ["RR", "N", "Roraima"] ]

with sqlite3.connect("brasil.db") as conexão:
    conexão.executemany("""update estados
                           set sigla = ?,
                           região = ?
                           where nome = ?""", dados)