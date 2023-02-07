""" Vejamos agora como ler os dados que gravamos no banco de dados, vamos fazer
    uma consulta (query) """


import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda") # 1
resultado = cursor.fetchone() # 2 
print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}") # 3
cursor.close()
conexão.close()

""" 
O comando SQL realiza uma consulta com o select

select * from agenda

O comando select em sua forma mais simples, ultiliza a lista de campos e uma lista de tabelas. No exemplo
a lista de campos foi substituída por * que significa todos os campos da tabela.
A palavra from é ultilizada para separar a lista de campos da lista de tabelas, no exemplo apenas com 
a tabela agenda 

Para acessa os resultados do comando select, devemos ultilizar o método fetchone de nosso cursor
Esse método retorna uma tupla com os resultados de nossa consulta, ou None caso a tabela esteja vazia

A tupla retornada posui a mesma ordem dos campos de nossa consulta. Assim o resultado[0] é o primeiro campo
no caso nome.




"""


