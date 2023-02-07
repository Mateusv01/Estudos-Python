"""         SQL - Structured Query Language (Linguagem de consulta estruturada)

        É a linguagem usada para criar bancos de dados, gerar consultas, manipular (inserir, atualizar, alterar e apagar)
        registros e, principalmente, realizar consultas. É uma linguagem de programação especializada na manipulação de dados,
        baseada na álgebra relacional e no modelo relacional criado por Edgar F.Codd


        Nesse capítulo veremos como escrever os comandos SQL para banco SQLite que vem pré-instalado com o interpretador e
        que é facilmente acessível, a linguagem SQL é definida por vários padrões veremos exclusivamente o SQLlite





        ==================================================== SQLite ================================================


        O SQLite é um gerenciador de banco de dados leve e completo, muito ultilizado e presente mesmo em telefones celulares.
        Uma de suas principais características é não precisar de um servidor dedicado, sendo capaz de iniciar a partir de seu
        programa
"""

import sqlite3 # Importando o SQLite (1)
conexão = sqlite3.connect("agenda.db") # Criando um banco de dados (2)
cursor = conexão.cursor() #(3)
cursor.execute('''
        create table agenda(
                nome text,
                telefone text)
                ''') #(4)
cursor.execute('''
        insert into agenda (nome, telefone)
                values(?, ?)
                ''', ("Mateus", "7770-9999")) #(5)
conexão.commit()#(4)
cursor.close()#(5)
conexão.close()#(6)

"""
        (2): geranndo um arquivo .db (O recomendado é diferenciar o nome do arquivo de um arquivo normal)
        porque todos os seus dados serão guardados nesse arquivo

        (3): Criamos um cursor, cursores são objetos usados para enviar comandos e receber resultados do banco
        de dados. Um cursor é criado para uma conexão chamando-se o método cursor().
        Uma vez que obtivemos um cursor, nós podemos enviar comandos ao banco de dados. O primeiro deles é
        criar uma tabela para guardar nomes e telefones. 

        create table agenda(nome, text, telefone, text)

        O comando SQL usado para cirar uma tabela é create table. Esse comando precisa do nome da tabela a criar, 
        nesse exemplo, agenda é uma lista de campos entre parênteses. Nome e telefone são nossos campos e text é o
        tipo
        Um campo tipo text pode armazenar informações como uma string do Python 

        (4): Usamos o método execute de nosso cursor para enviar o comando ao banco de dados. Observe que escrevemos o 
        comando em várias linhas usando apóstrofos triplos do Python. A linguagem SQL não exige essa formatação
        embora deixe o comando mais claro, é melhor escrever tudo em uma única linha

        Como a tabela criada vejamos o comando SQL para inserir um registro

                insert into agenda (nome, telefone) values (?, ?)

        O comando insert precisa do nome da tabela, na qual vamos inserir os dados, e também do nome dos campos e seus
        respectivos valores. into faz parte do comando insert 
        Em nosso exemplo, a posição de cada valor foi marcada com interrogação, uma para cada campo
        as interrogações equivalem como máscaras de string do Python

        (5): Ultilizamos o método execute para executar o comando insert, mas desta vez passamos os dados logo após o comando
        importante notar que as informações foram passadas com uma tupla

        Uma vez que o comando é executado, os dados são enviados para o banco de dados, mas ainda não estão gravados definitivamente
        Isso acontece pois estamos usando uma transação

        Transações serão apresentadas com mais detalhes em outra seção; mas por enquanto, considere o comando commit em (6)
        como parte das operações necessárias para modificar o banco de dados

        Antes de terminar o programa fechamos (close) o cursor e a conexão com o banco de dados respectivamente em 7 e 8
        mais adiante vamos usar o with para facilitar essas operações

        
"""